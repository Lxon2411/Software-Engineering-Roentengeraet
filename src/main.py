import tkinter as tk
from tkinter import ttk, messagebox
import time
import platform

if platform.system() == "Windows":
    import winsound

MAX_DURATION = 120  # Maximal erlaubte Dauer in Sekunden


class StatusLED(tk.Canvas):
    def __init__(self, master, diameter=20, bg_color="#f0f0f0"):
        super().__init__(master, width=diameter, height=diameter, highlightthickness=0, bg=bg_color)
        self.oval = self.create_oval(2, 2, diameter-2, diameter-2, fill="red", outline="#ccc")

    def set_on(self):
        self.itemconfig(self.oval, fill="green")

    def set_off(self):
        self.itemconfig(self.oval, fill="red")


class RadiationController:
    def __init__(self, ui):
        self.ui = ui
        self.is_radiating = False
        self.elapsed_time = 0
        self.max_duration = 0
        self.update_interval = 100
        self.start_time = None

    def start_radiation(self):
        try:
            self.max_duration = int(self.ui.duration_entry.get())
            if not (0 < self.max_duration <= MAX_DURATION):
                raise ValueError
        except ValueError:
            messagebox.showerror("Fehler", f"Bitte eine Zahl zwischen 1 und {MAX_DURATION} eingeben.")
            return

        if not self.is_radiating:
            self.is_radiating = True
            self.elapsed_time = 0
            self.start_time = time.time()
            self.ui.status_led.set_on()
            self.ui.start_stop_button.config(text="🛑 Strahlung stoppen", bg="#cc3333")
            self.ui.log_message(f"✅ Strahlung gestartet ({self.max_duration}s)")
            self.update_timer()

    def stop_radiation(self, user_stopped=True):
        if self.is_radiating:
            self.is_radiating = False
            self.ui.status_led.set_off()
            self.ui.start_stop_button.config(text="▶ Strahlung starten", bg="#4caf50")
            self.ui.progress['value'] = 0
            self.ui.timer_label.config(text="Strahlungsdauer: 0.0 s")
            actual_duration = time.time() - self.start_time if self.start_time else self.elapsed_time
            msg = f"⏹️ Strahlung gestoppt nach {actual_duration:.1f}s"
            self.ui.log_message(msg)
            if user_stopped:
                messagebox.showinfo("Strahlung beendet", msg)

    def toggle_radiation(self):
        if self.is_radiating:
            self.stop_radiation(user_stopped=True)
        else:
            self.start_radiation()

    def update_timer(self):
        if self.is_radiating:
            self.elapsed_time += self.update_interval / 1000
            self.ui.timer_label.config(text=f"Strahlungsdauer: {self.elapsed_time:.1f} s")

            progress_percent = (self.elapsed_time / self.max_duration) * 100
            self.ui.progress['value'] = progress_percent

            if self.elapsed_time >= self.max_duration:
                self.stop_radiation(user_stopped=False)
                if platform.system() == "Windows":
                    winsound.Beep(1000, 500)
                messagebox.showwarning("Warnung", "⚠️ Maximale Strahlungsdauer erreicht!")
                return

            self.ui.root.after(self.update_interval, self.update_timer)


class RadiationUI:
    def __init__(self, root):
        self.root = root
        self.is_dark_mode = False

        self.root.title("💡 Röntgengerät Steuerung")
        self.root.geometry("500x550")

        self.build_ui()
        self.controller = RadiationController(self)
        self.start_stop_button.config(command=self.controller.toggle_radiation)

    def build_ui(self):
        title = tk.Label(self.root, text="Röntgengerät Steuerung", font=("Helvetica", 18, "bold"))
        title.pack(pady=10)

        # Einstellungen
        input_frame = tk.LabelFrame(self.root, text="Einstellungen", font=("Helvetica", 10, "bold"))
        input_frame.pack(padx=20, pady=10, fill="x")

        tk.Label(input_frame, text=f"Maximale Strahlungsdauer (1–{MAX_DURATION} Sekunden):").pack(anchor="w", padx=10, pady=5)

        self.duration_entry = tk.Entry(input_frame, font=("Helvetica", 12), justify="center")
        self.duration_entry.pack(padx=10, pady=5, fill="x")
        self.duration_entry.insert(0, "10")

        # Buttons
        self.start_stop_button = tk.Button(self.root, text="▶ Strahlung starten",
                                           font=("Helvetica", 12, "bold"),
                                           bg="#4caf50", fg="white", relief="flat")
        self.start_stop_button.pack(pady=10, ipadx=10, ipady=5)

        # Timer Label
        self.timer_label = tk.Label(self.root, text="Strahlungsdauer: 0.0 s", font=("Helvetica", 12))
        self.timer_label.pack(pady=5)

        # Fortschrittsbalken
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("green.Horizontal.TProgressbar", foreground="#4caf50", background="#4caf50", thickness=20)

        self.progress = ttk.Progressbar(self.root, style="green.Horizontal.TProgressbar",
                                        orient="horizontal", length=400, mode="determinate")
        self.progress.pack(pady=10)

        # Status-LED
        status_frame = tk.LabelFrame(self.root, text="Status", font=("Helvetica", 10, "bold"))
        status_frame.pack(pady=10, padx=20, fill="x")

        inner = tk.Frame(status_frame)
        inner.pack(pady=5)
        tk.Label(inner, text="Strahlung:", font=("Helvetica", 11)).pack(side=tk.LEFT, padx=5)
        self.status_led = StatusLED(inner)
        self.status_led.pack(side=tk.LEFT)

        # Logfeld
        log_frame = tk.LabelFrame(self.root, text="Protokoll")
        log_frame.pack(padx=20, pady=10, fill="both", expand=True)

        self.log_text = tk.Text(log_frame, height=6, state="disabled", bg="#ffffff", wrap="word")
        self.log_text.pack(fill="both", padx=10, pady=5)


    def log_message(self, message):
        self.log_text.configure(state="normal")
        self.log_text.insert(tk.END, f"{message}\n")
        self.log_text.see(tk.END)
        self.log_text.configure(state="disabled")

def main():
    root = tk.Tk()
    app = RadiationUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
