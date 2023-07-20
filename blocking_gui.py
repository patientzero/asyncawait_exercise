import tkinter as tk
import time
from tkinter import ttk


class App:
    def exec(self):
        self.window = Window()
        self.window.show();
        

class Window(tk.Tk):
    def __init__(self):
        self.root = tk.Tk()
        self.animation = "░▒▒▒▒▒"
        self.label = tk.Label(text="")
        self.label.grid(row=0, columnspan=2, padx=(8, 8), pady=(16, 0))
        self.progressbar = ttk.Progressbar(length=280)
        self.progressbar.grid(row=1, columnspan=2, padx=(8, 8), pady=(16, 0))
        button_block = tk.Button(text="Calculate Sync", width=10, command=self.calculate_sync)
        button_block.grid(row=2, column=0, sticky=tk.W, padx=8, pady=8)

    def show(self):
        while True:
            self.label["text"] = self.animation
            self.animation = self.animation[1:] + self.animation[0]
            self.root.update()

    def calculate_sync(self):
        max = 300
        for i in range(1, max):
            self.progressbar["value"] = i / max * 100
            self.root.update()

App().exec()