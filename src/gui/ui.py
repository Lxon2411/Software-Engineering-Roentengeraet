import tkinter as tk
from tkinter import ttk, messagebox
import winsound

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

