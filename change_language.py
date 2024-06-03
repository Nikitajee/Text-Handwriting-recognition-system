# All Language Change(5)

from tkinter import *
from tkinter import ttk,messagebox
import googletrans
from PIL import Image, ImageTk
from googletrans import Translator
class all_language_change:
    def __init__(self,root):

        self.root = root
        self.root.title("All type language change")
        self.root.geometry("1920x990+0+0")
        self.root.resizable(False , False)
        self.root.configure(background = "black")

        def label_change():
            c=combo1.get()
            c1=combo2.get()
            label1.configure(text=c)
            label2.configure(text=c1)
            root.after(1000,label_change)

        def translate_now():
            text_=text1.get(1.0,END)
            t1=Translator()
            trans_text=t1.translate(text_,src=combo1.get(),dest=combo2.get())
            trans_text=trans_text.text

            text2.delete(1.0,END)
            text2.insert(END,trans_text)

        #arrow
        

        self.arrow_image=PhotoImage(file ="image/arrow.png")
        image_label = Label(self.root,image=self.arrow_image,width=250)
        image_label.place(x=800,y=400)

        language = googletrans.LANGUAGES
        languageV=list(language.values())
        lang1 = language.keys()

        #first combobox

        combo1=ttk.Combobox(self.root,values=languageV,font="Roboto 20",state="r")
        combo1.place(x=130,y=30)
        combo1.set("ENGLISH")

        label1=Label(self.root,text="ENGLISH", font="segoe 30 bold",bg="pink",width=19,bd=5,relief=RAISED)
        label1.place(x=30,y=80)

        #second combobox

        combo2=ttk.Combobox(self.root,values=languageV,font="Roboto 20",state="r")
        combo2.place(x=1300,y=30)
        combo2.set("SELECT LANGUAGE")

        label2=Label(self.root,text="ENGLISH", font="segoe 30 bold",bg="Turquoise",width=19,bd=5,relief=RAISED)
        label2.place(x=1200,y=80)


        #first frame
        f= Frame(self.root,bg="red",bd=5)
        f.place(x=30,y=150,width=600,height=810)

        text1=Text(f,font="Robote 20",bg="white",relief=RAISED,wrap=WORD)
        text1.place(x=0,y=0,width=570,height=800)

        scrollbar1=Scrollbar(f)
        scrollbar1.pack(side="right",fill='y')

        scrollbar1.configure(command=text1.yview)
        text1.configure(yscrollcommand=scrollbar1.set)


        #second frame
        f1= Frame(self.root,bg="red",bd=5)
        f1.place(x=1200,y=150,width=600,height=810)

        text2=Text(f1,font="Robote 20",bg="white",relief=RAISED,wrap=WORD)
        text2.place(x=0,y=0,width=570,height=800)

        scrollbar2=Scrollbar(f1)
        scrollbar2.pack(side="right",fill='y')

        scrollbar2.configure(command=text2.yview)
        text2.configure(yscrollcommand=scrollbar2.set)

        #translate button
        translate=Button(self.root,text="Change",font=("Roboto",15),activebackground="darkgreen",cursor="hand2",bd=1,width=15,height=4,bg="red",fg="black",command=translate_now)
        translate.place(x=800,y=650)


        label_change
if __name__=="__main__":
    
    root= Tk()
    obj=all_language_change(root)
    root.mainloop()