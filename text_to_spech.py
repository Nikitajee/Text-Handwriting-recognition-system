#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Text To Speech(6)

from tkinter import *
from tkinter import ttk,filedialog
import random
import pyttsx3
from PIL import Image,ImageTk 
import os

class text_to_spech:
    def __init__(self,root):
        
            e=pyttsx3.init()

            self.root=root
            self.root.geometry("1920x990+0+0")
            self.root.title('textTospeech')
            

            
            
          

            def blind():
                color=['pink','yellow','red','blue','green','indigo','purple','orange']
                a=random.choice(color)
                lbl_title.configure(bg=a)
                lbl_title.after(200,blind)

            def talk():
                def check_voice():
                    if (gender == 'Male'):
                        e.setProperty('voice', v[0].id)
                        e.setProperty('volume', (volume_) / 100)
                        e.say(text)
                        e.runAndWait()
                    else:
                        e.setProperty('voice', v[1].id)
                        e.setProperty('volume', (volume_) / 100)
                        e.say(text)
                        e.runAndWait()

                text = txt_area.get(1.0, END)
                gender = gender_combo.get()
                speed = speed_combo.get()
                volume_ = scale_level.get()
                v = e.getProperty('voices')
                if (text):
                    if (speed == 'Fast'):
                        e.setProperty('rate', 300)
                        check_voice()
                    elif (speed == 'Normal'):
                        e.setProperty('rate', 150)
                        check_voice()
                    else:
                        e.setProperty('rate', 50)
                        check_voice()


            def download():
                def check_voice():
                    if (gender == 'Male'):
                        e.setProperty('voice', v[0].id)
                        e.setProperty('volume', (volumes) / 100)
                        path=filedialog.askdirectory()
                        os.chdir(path)
                        e.save_to_file(text,'music.mp3')
                        e.runAndWait()
                    else:
                        e.setProperty('voice', v[1].id)
                        e.setProperty('volume', (volumes) / 100)
                        path = filedialog.askdirectory()
                        os.chdir(path)
                        e.save_to_file(text, 'music.mp3')
                        e.runAndWait()

                text=txt_area.get(1.0,END)
                gender=gender_combo.get()
                speed=speed_combo.get()
                volumes=scale_level.get()
                v=e.getProperty('voices')
                if(text):
                    if(speed=='Fast'):
                        e.setProperty('rate',300)
                        check_voice()
                    elif(speed=='Normal'):
                        e.setProperty('rate',150)
                        check_voice()
                    else:
                        e.setProperty('rate',50)
                        check_voice()



            #==========================title====================
            lbl_title=Label(self.root,text="Text to Speech",font='arial 50 bold')
            lbl_title.place(x=0,y=0,relwidth=1)

            f1=Frame(self.root,relief=GROOVE,bd=5)
            f1.place(x=10,y=105,width=1000,height=500)

            scrol_bar=Scrollbar(f1,orient=VERTICAL)
            scrol_bar.pack(side=RIGHT,fill=Y)
            txt_area=Text(f1,font=('times new rommon',15,'bold'),bg='grey99',yscrollcommand=scrol_bar.set,wrap=WORD)
            txt_area.pack(fill=BOTH)

            scrol_bar.config(command=txt_area.yview)
            gender_lbl=Label(self.root,text='Gender',font='Impack 20 bold',width=15,bg='yellow',fg='red')
            gender_lbl.place(x=10,y=610)

            speed_lbl=Label(self.root,text='Speed',font='Impack 20 bold',width=15,bg='yellow',fg='red')
            speed_lbl.place(x=333,y=610)

            volume_lbl=Label(self.root,text='Volume',font='Impack 20 bold',width=15,bg='yellow',fg='red')
            volume_lbl.place(x=666,y=610)

            #===================combo box====================
            gender_combo=ttk.Combobox(self.root,values=['Male','Female'],font='arial 12 bold',state='r')
            gender_combo.place(x=10,y=660)
            gender_combo.set('Male')

            speed_combo=ttk.Combobox(self.root,values=['Fast','Normal','slow'],font='arial 12 bold',state='r')
            speed_combo.place(x=350,y=660)
            speed_combo.set('Fast')

            scale_level=Scale(self.root,from_=0,to=100,orient=HORIZONTAL,length=160)
            scale_level.place(x=680,y=660)
            scale_level.set(50)

            #===================buttons======================
            play_btn=Button(self.root,text='Play',font='arial 25 bold',width=10,bg='lime',activebackground='yellow',relief=SUNKEN,bd=10,command=talk)


            play_btn.place(x=100,y=800)
            d_btn=Button(self.root,text='Download',width=10,font='arial 25 bold ',relief=SUNKEN,bg='lime',activebackground='yellow',bd=10,command=download)
            d_btn.place(x=500,y=800)

            #=========================
           
            image3 = Image.open(r"image/1.PNG")
            self.photo3 = ImageTk.PhotoImage(image3)
            bg=Label(self.root,bd=0,image=self.photo3)
            bg.place(x=1200,y=130)

            

            self.root.configure(bg='black')
            blind()
if __name__=="__main__":
    
    root= Tk()
    obj=text_to_spech(root)
    root.mainloop()

