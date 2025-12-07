import tkinter as tk


class StatusLED:
    def __init__(self, root):
        self.status_frame = tk.LabelFrame(root, text="Status", font=("Helvetica", 10, "bold"))
        self.status_frame.pack(padx=20, pady=5, fill="x")

        self.inner_frame = tk.Frame(self.status_frame)
        self.inner_frame.pack(expand=True)

        self.status_label = tk.Label(self.inner_frame, text="Strahlung: ", font=("Arial", 10))
        self.status_label.pack(side="left", pady=5)

        self.status_canvas = tk.Canvas(self.inner_frame, width=20, height=20, highlightthickness=0)
        self.status_canvas.pack(side="left")
        self.status_circle = self.status_canvas.create_oval(2, 2, 18, 18, fill="red")

    def set_active(self):
        self.status_canvas.itemconfig(self.status_circle, fill="green")

    def set_inactive(self):
        self.status_canvas.itemconfig(self.status_circle, fill="red")
