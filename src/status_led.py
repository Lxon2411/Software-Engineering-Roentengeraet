import tkinter as tk

class StatusLED(tk.Canvas):
    def __init__(self, master, diameter=20, bg_color="#f0f0f0"):
        super().__init__(master, width=diameter, height=diameter, highlightthickness=0, bg=bg_color)
        self.oval = self.create_oval(2, 2, diameter - 2, diameter - 2, fill="red", outline="#ccc")

    def set_on(self):
        self.itemconfig(self.oval, fill="green")

    def set_off(self):
        self.itemconfig(self.oval, fill="red")