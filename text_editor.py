# Text Editor(4)

from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter.font import Font
from tkinter.scrolledtext import *

import file_menu
import edit_menu
import format_menu

class text_editor:
    def __init__(self,root):
        self.root = root

        self.root.title("Text Editor-Untiltled")
        self.root.geometry("1920x990+0+0")
       

        text = ScrolledText(self.root, state='normal', height=400, width=400, wrap='word', pady=2, padx=3, undo=True)
        text.pack(fill=Y, expand=1)
        text.focus_set()

        menubar = Menu(self.root)

        file_menu.main(self.root, text, menubar)
        edit_menu.main(self.root, text, menubar)
        format_menu.main(self.root, text, menubar)
        
if __name__=="__main__":
    
    root= Tk()
    obj=text_editor(root)
    root.mainloop()