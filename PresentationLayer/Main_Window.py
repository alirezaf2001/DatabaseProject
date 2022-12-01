import tkinter as tk
import tkinter.ttk as ttk

class Window:
    def __init__(self, master) -> None:
        frame = ttk.Frame(master)

class MainWindow:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.window = Window(self.root)

    def startWindow(self):
        self.root.mainloop()
