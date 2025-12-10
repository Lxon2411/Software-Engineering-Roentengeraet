import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext, filedialog
import winsound
from datetime import datetime

from src.config import MAX_DURATION
from src.system.status_led import StatusLED

class RadiationUI:
    def __init__(self, root, controller):
        self.controller = controller
        self.root = root

        self.input_frame = tk.LabelFrame(root, text="Einstellungen", font=("Helvetica", 10, "bold"))
        self.input_frame.pack(padx=20, pady=5, fill="x")

        self.duration_label = tk.Label(self.input_frame, text=f"Strahlungsdauer (1-{MAX_DURATION} Sekunden) eingeben:")
        self.duration_label.pack(anchor="w", padx=10)

        self.duration_entry = tk.Entry(self.input_frame, font=("Arial", 12), justify="center")
        self.duration_entry.pack(fill="x", padx=12, pady=(5, 15))

        self.elapsedTime_label = tk.Label(root, font=("Arial", 10), text=f"Vergangene Strahlungsdauer: ")
        self.elapsedTime_label.pack(pady=(2, 0))

        self.progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
        self.progress.pack(pady=5)

        self.progress_label = tk.Label(root, text="Fortschritt: 0 %")
        self.progress_label.pack(pady=5)

        self.startButton = tk.Button(
            root,
            text="Start",
            command=self.start_radiation,
            bg="green",
            fg="white",
            activebackground="#45a049",
            activeforeground="white",
            font=("Arial", 11, "bold"),
            width=15
        )
        self.startButton.pack(padx=20, pady=10)

        self.status_led = StatusLED(root)

        log_frame = tk.LabelFrame(root, text="Logs", font=("Helvetica", 10, "bold"))
        log_frame.pack(padx=20, pady=5, fill="x")

        log_button_frame = tk.Frame(log_frame)
        log_button_frame.pack(fill="x", padx=5, pady=(5, 0))

        self.export_log_button = tk.Button(
            log_button_frame,
            text="Logs exportieren",
            font=("Arial", 9, "bold"),
            command=self.export_logs
        )
        self.export_log_button.pack(side="right")

        self.log_widget = scrolledtext.ScrolledText(
            log_frame,
            height=8,
            state="disabled",
            wrap="word"
        )
        self.log_widget.pack(fill="both", expand=True, padx=5, pady=5)

    def start_radiation(self):
        try:
            duration = int(self.duration_entry.get())
            if not 1 <= duration <= MAX_DURATION:
                raise ValueError
            self.controller.start(duration)
            self.startButton.config(
                text="Stop",
                bg="red",
                command=self.stop_radiation
            )
            self.status_led.set_active()
            self.root.focus_set()
        except ValueError:
            messagebox.showerror("Fehler", f"Bitte eine Zahl zwischen 1 und {MAX_DURATION} eingeben!")

    def update_progress(self, value, max_value):
        self.progress["maximum"] = max_value
        self.progress["value"] = value

        percent = (value / max_value) * 100 if max_value > 0 else 0
        if value / max_value >= 1: percent = 100

        self.elapsedTime_label.config(text=f"Vergangene Strahlungsdauer: {value:.1f} s")
        self.progress_label.config(text=f"Fortschritt: {percent:.0f} %")

        self.root.update_idletasks()

    def reset_ui(self):
        self.startButton.config(
            text="Start",
            bg="green",
            command=self.start_radiation
        )
        self.progress["value"] = 0
        self.duration_entry.delete(0, tk.END)
        self.elapsedTime_label.config(text=f"Vergangene Strahlungsdauer: ")
        self.progress_label.config(text=f"Fortschritt: 0 %")
        self.status_led.set_inactive()

    def show_finished_message(self, duration):
        winsound.Beep(400, 600)
        messagebox.showinfo("Fertig", f"Die Strahlung wurde erfolgreich nach {duration} Sekunden beendet.")

    def show_abort_message(self, elapsed):
        winsound.Beep(250, 300)
        messagebox.showwarning("Abgebrochen", f"Die Strahlung wurde nach {elapsed:.1f} Sekunden abgebrochen!")
    def stop_radiation(self):
        self.controller.stop()

    def log_message(self, msg: str):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        line = f"• [{timestamp}] {msg}"
        self.log_widget.config(state="normal")
        self.log_widget.insert("end", line + "\n")
        self.log_widget.see("end")
        self.log_widget.config(state="disabled")

    def export_logs(self):
        logs = self.log_widget.get("1.0", "end").strip()
        if not logs:
            messagebox.showinfo("Logs exportieren", "Keine Log-Einträge vorhanden.")
            return

        ts = datetime.now().strftime("%Y%m%d-%H%M%S")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        default_name = f"RGS-Logs-{ts}.txt"
        file_path = filedialog.asksaveasfilename(
            title="Logs exportieren",
            initialfile=default_name,
            defaultextension=".txt",
            filetypes=[("Textdateien", "*.txt"), ("Alle Dateien", "*.*")]
        )
        if not file_path:
            return

        try:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(f"Röntgengerät Simulator - Protokoll erstellt am {timestamp}\n\n")
                f.write(logs + "\n")
            messagebox.showinfo("Logs exportieren", f"Logs wurden erfolgreich nach\n{file_path}\nexportiert.")
        except OSError as e:
            messagebox.showerror("Fehler beim Exportieren", f"Die Logs konnten nicht gespeichert werden:\n[{e}")