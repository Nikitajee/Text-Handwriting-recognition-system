from tkinter import *
from tkinter.messagebox import *
import sys
import tkinter as tk
from tkinter import *

class Help():
        def __init__(self,root):
            def about(root):
                showinfo(title="About", message="Created by Nikita singh",parent=self.root)


def main(root, text, menubar):

    help = Help()

    helpMenu = Menu(menubar)
    helpMenu.add_command(label="About", command=help.about)
    menubar.add_cascade(label="Help", menu=helpMenu)

    root.config(menu=menubar)


if __name__ == "__main__":
    print("Please run 'main.py'")
