import os
import sys
import tkinter as tk
from tkinter import PhotoImage

from src.gui.ui import RadiationUI
from src.controller.controller import RadiationController


def main():
    root = tk.Tk()
    root.title("Röntgengerät Simulation")
    root.geometry("500x550")
    root.resizable(False, False)

    # BASE_DIR = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    # icon_path = os.path.join(BASE_DIR, "icon.png")
    # icon = PhotoImage(file=icon_path)
    # root.iconphoto(False, icon)

    ui = RadiationUI(root, None)
    controller = RadiationController(ui)
    ui.controller = controller
    root.mainloop()


if __name__ == "__main__":
    main()
