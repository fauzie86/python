from tkinter import *
from tkinter import ttk

#pip install googletrans==4.0.0-rc1
from googletrans import Translator, LANGUAGES

def change(text="type" , src="English" ,dest = "french"):
    text1 = text
    src1 = src
    dest1 = dest
    trans =Translator()
    trans1 = trans.translate(text,src=src1,dest=dest1)
    return trans1.text

def data():
    s = comb_src.get()
    d = comb_dest.get()
    msg = sor_txt.get(1.0 , END)

    extget = change(text=msg, src=s, dest = d)
    dest_txt.delete(1.0, END)
    dest_txt.insert(END, textget)




 # first part
root = Tk()
root.title("translator")
root.geometry("500x700")
root.config(bg='Red')

lab_txt = Label(root , text="Translator" , font=("Time New Roman" , 40, "bold"),bg="Red")
lab_txt.place(x=100 , y=40, height=50, width=300)

frame = Frame(root).pack(side=BOTTOM) #for placement

#another box text

lab_txt = lab_txt(root, text="Source Text" , font=("Time New Roman" , 40, "bold"),fg="black" , bg="Red")
lab_txt.place(x=100 , y = 100 , height=200, width=300)
sor_txt = Text(frame,font=("Time New Roman" , 40, "bold"), wrap=WORD)
sor_txt.place(x=10, y=130, height=50, width=400)

#combo list
list_text = list(1,2,3,4,5) #temporary

comb_src = ttk.Combobox(frame, value=list_text)
comb_src.place(x=10 , y=250, height=40, width=150)
comb_src.set("English")

Button_change = Button(frame,text="Translate" , relief=RAISED , command= data)
Button_change.place(x=170 , y=250 , height=40, width=150)

comb_dest = ttk.Combobox(frame,value=list_text)
comb_dest.place(x=330 , y=250 , height=40 , width=150)
comb_dest.set("english")

lab_txt = Label(root , text="Des Text" , font=("Time New Roman" , 20, "bold") , fg="black" , bg= "Red")
lab_txt.place(x=100, y=350 , height=20, width=300)

dest_txt = Text(frame,font=("Time New Roman" , 20 , "bold"), wrap=WORD)
dest_txt.place(x=10, y=400, height=100,width=480)

root.mainloop()







