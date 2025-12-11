import os
import sys
import tkinter as tk
from tkinter import PhotoImage

from src.gui.ui import RadiationUI
from src.controller.controller import RadiationController


def resource_path(relative_path: str) -> str:
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(os.path.abspath(__file__))

    return os.path.join(base_path, relative_path)


def main():
    PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if PROJECT_ROOT not in sys.path:
        sys.path.insert(0, PROJECT_ROOT)

    root = tk.Tk()
    root.title("Röntgengerät Simulation")
    root.geometry("500x550")
    root.resizable(False, False)

    icon_path = resource_path("icon.png")
    try:
        icon = PhotoImage(file=icon_path)
        root.iconphoto(False, icon)
    except Exception as e:
        print(f"Icon konnte nicht geladen werden: {e}")

    ui = RadiationUI(root, None)
    controller = RadiationController(ui)
    ui.controller = controller
    root.mainloop()


if __name__ == "__main__":
    main()
