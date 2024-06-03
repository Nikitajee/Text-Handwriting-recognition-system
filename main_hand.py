#!/usr/bin/env python
# coding: utf-8

# In[4]:


import tkinter as tk
from tkinter import *

from tkinter import messagebox as msg
from tkinter import ttk
################################### importing scripts
from Application import Digit_Character
from change_language import all_language_change
from text_editor import  text_editor
from text_to_spech import text_to_spech
from text_to_handwritten import text_to_handwritten
from Im_text_gui import Image_to_text
################################### lib to perform CRUD operations in csv/excel
import cv2
import numpy as np
from keras.models import Sequential
from keras.layers import Conv2D, Activation, MaxPooling2D, Flatten, Dense, Dropout, BatchNormalization
from PIL import Image, ImageTk
from openpyxl import *
import pandas as pd
import numpy as np
import cv2,os
from cv2 import cvtColor
import csv
################################### other dependencies
import datetime
from time import strftime
from datetime import datetime
import os

class main_gui:
    def Digit_and_Character(self):
        self.app=Digit_Character()
    def text_to_myhandwritten(self):
        self.new_window=Toplevel(self.root)
        self.app=text_to_handwritten(self.new_window)
    
    def image_to_text(self):
        self.new_window=Toplevel(self.root)
        self.app=Image_to_text(self.new_window)
    def text_edit(self):
        self.new_window=Toplevel(self.root)
        self.app=text_editor(self.new_window)
    def language_change(self):
        self.new_window=Toplevel(self.root)
        self.app=all_language_change(self.new_window)
    def text_to_spech(self):
        self.new_window=Toplevel(self.root)
        self.app=text_to_spech(self.new_window)
    def __init__(self,root):
        self.root=root
        self.root.title("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@WELCOME TO MY HANDWRITINY@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        self.root.geometry("1920x990+0+0")


        # title
        title=Label(self.root,text="@@@@!!!Handwriting Text Recognition & Text To Handwriting Recognition!!!@@@@",font=("times new roman",30,"bold"),bg="#330000",fg="white")
        title.place(x=0,y=0,width=1920,height=45)

        title=Label(self.root,text="**********************************************************************************************************************************************************",font=("times new roman",15,"bold"),bg="#330000",fg="white")
        title.place(x=0,y=45,width=1920,height=15)

        # bg image
        image3 = Image.open(r"image/image13.jpg")
        image3=image3.resize((1920,690), Image.ANTIALIAS)
        self.photo3 = ImageTk.PhotoImage(image3)
        bg=Label(self.root,image=self.photo3)
        bg.place(x=0,y=53,width=1920,height=690)

        # Digit & Character

        image4 = Image.open(r"image/image17.png")
        image4=image4.resize((250,210), Image.ANTIALIAS)
        self.photo4 = ImageTk.PhotoImage(image4)

        b1=Button(bg,image=self.photo4,cursor="hand2",command=self.Digit_and_Character)
        b1.place(x=240,y=50,width=250,height=210)
        b1_1=Button(bg,text="*Digit & Character*",cursor="hand2",command=self.Digit_and_Character,activebackground="lightpink",font=("times new roman",15,"bold"),bg="#330000",fg="white")
        b1_1.place(x=240,y=260,width=250,height=40)

        # Text to Handwritten

        image5 = Image.open(r"image/image21.png")
        image5=image5.resize((250,210), Image.ANTIALIAS)
        self.photo5 = ImageTk.PhotoImage(image5)

        b1=Button(bg,image=self.photo5,cursor="hand2",command=self.text_to_myhandwritten)
        b1.place(x=640,y=50,width=250,height=210)

        b1_1=Button(bg,text="*Text to Handwritten*",cursor="hand2",command=self.text_to_myhandwritten,activebackground="lightpink",font=("times new roman",15,"bold"),bg="#330000",fg="white")
        b1_1.place(x=640,y=260,width=250,height=40)

        # Image To Text

        image6 = Image.open(r"image/image8.jpg")
        image6=image6.resize((250,210), Image.ANTIALIAS)
        self.photo6= ImageTk.PhotoImage(image6)

        b1=Button(bg,image=self.photo6,cursor="hand2",command=self.image_to_text)
        b1.place(x=1040,y=50,width=250,height=210)

        b1_1=Button(bg,text="*Image To Text*",cursor="hand2",command=self.image_to_text,activebackground="lightpink",font=("times new roman",15,"bold"),bg="#330000",fg="white")
        b1_1.place(x=1040,y=260,width=250,height=40)

        # Text Editor

        image7 = Image.open(r"image/image14.png")
        image7=image7.resize((250,210), Image.ANTIALIAS)
        self.photo7= ImageTk.PhotoImage(image7)

        b1=Button(bg,image=self.photo7,cursor="hand2",command=self.text_edit)
        b1.place(x=1440,y=50,width=250,height=210)

        b1_1=Button(bg,text="*Text Editor*",cursor="hand2",command=self.text_edit,activebackground="lightpink",font=("times new roman",15,"bold"),bg="#330000",fg="white")
        b1_1.place(x=1440,y=260,width=250,height=40)

        # All Language Change

        image8 = Image.open(r"image/image20.png")
        image8=image8.resize((250,210), Image.ANTIALIAS)
        self.photo8= ImageTk.PhotoImage(image8)

        b1=Button(bg,image=self.photo8,cursor="hand2",command=self.language_change)
        b1.place(x=440,y=350,width=250,height=210)

        b1_1=Button(bg,text="*All Language Change*",cursor="hand2",command=self.language_change,activebackground="lightpink",font=("times new roman",14,"bold"),bg="#330000",fg="white")
        b1_1.place(x=440,y=560,width=250,height=40)

        # Text To Speech

        image10 = Image.open(r"image/image25.png")
        image10=image10.resize((250,210), Image.ANTIALIAS)
        self.photo10= ImageTk.PhotoImage(image10)

        b1=Button(bg,image=self.photo10,cursor="hand2",command=self.text_to_spech)
        b1.place(x=840,y=350,width=250,height=210)

        b1_1=Button(bg,text="*Text To Speech*",cursor="hand2",command=self.text_to_spech,activebackground="lightpink",font=("times new roman",15,"bold"),bg="#330000",fg="white")
        b1_1.place(x=840,y=560,width=250,height=40)

        # Exit button

        def close():
            root.destroy()

        image11 = Image.open(r"image/image23.png")
        image11=image11.resize((250,210), Image.ANTIALIAS)
        self.photo11= ImageTk.PhotoImage(image11)

        b1=Button(bg,image=self.photo11,cursor="hand2")
        b1.place(x=1240,y=350,width=250,height=210)

        b1_1=Button(bg,text="*Exit*",cursor="hand2",command=close,activebackground="lightpink",font=("times new roman",15,"bold"),bg="#330000",fg="white")
        b1_1.place(x=1240,y=560,width=250,height=40)

        title=Label(self.root,text="**********************************************************************************************************************************************************",font=("times new roman",15,"bold"),bg="#330000",fg="white")
        title.place(x=0,y=740,width=1920,height=15)

        # down image

        image = Image.open(r"image/image11.jpg")
        image=image.resize((640,245), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(image)
        f1=Label(root,image=self.photo)
        f1.place(x=0,y=750,width=640,height=245)

        image1 = Image.open(r"image/image12.jpg")
        image1=image1.resize((640,245), Image.ANTIALIAS)
        self.photo1 = ImageTk.PhotoImage(image1)
        f1=Label(root,image=self.photo1)
        f1.place(x=640,y=750,width=640,height=245)

        image2 = Image.open(r"image/image11.jpg")
        image2=image2.resize((640,245), Image.ANTIALIAS)
        self.photo2 = ImageTk.PhotoImage(image2)
        f1=Label(root,image=self.photo2)
        f1.place(x=1280,y=750,width=640,height=245)

if __name__=="__main__":
    root=Tk()
    obj=main_gui(root)
    root.mainloop()


# In[ ]:




