import tkinter as tk
from tkinter import ttk
from status_led import StatusLED
from controller import RadiationController
from config import MAX_DURATION

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