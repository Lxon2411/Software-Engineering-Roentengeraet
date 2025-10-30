import tkinter as tk
from ui import RadiationUI

def main():
    root = tk.Tk()
    app = RadiationUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()