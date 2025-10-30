import time
import platform
from tkinter import messagebox
from config import MAX_DURATION

if platform.system() == "Windows":
    import winsound


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