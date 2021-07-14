from tkinter import *
from tkinter import messagebox

class ZachowanieError(Exception):
    pass
class ZlaOcenaError(Exception):
    pass
class Program(object):
    def __init__(self):
        self.okno = Tk()
        self.okno.geometry("260x164")
        self.okno.title("Świadectwa")
        self.utworzwidgety()
        self.okno.mainloop()
    def utworzwidgety(self):
        self.przycisk1=Button(self.okno,width = 2,height=2)
        self.przycisk1["text"] = "9"
        self.przycisk1.grid(row=0,column=0,sticky=W)
        self.przycisk1["command"]=self.Zanotuj
        
        self.przycisk2=Button(self.okno,width = 2,height=2)
        self.przycisk2["text"] = "8"
        self.przycisk2.grid(row=0,column=1,sticky=W)
        self.przycisk2["command"]=self.Zanotuj
        
        self.przycisk3=Button(self.okno,width = 2,height=2)
        self.przycisk3["text"] = "7"
        self.przycisk3.grid(row=0,column=2,sticky=W)
        self.przycisk3["command"]=self.Zanotuj
        
        self.przycisk4=Button(self.okno,width = 2,height=2)
        self.przycisk4["text"] = "6"
        self.przycisk4.grid(row=1,column=0,sticky=W)
        self.przycisk4["command"]=self.Zanotuj
        
        self.przycisk5=Button(self.okno,width = 2,height=2)
        self.przycisk5["text"] = "5"
        self.przycisk5.grid(row=1,column=1,sticky=W)
        self.przycisk5["command"]=self.Zanotuj
        
        self.przycisk6=Button(self.okno,width = 2,height=2)
        self.przycisk6["text"] = "4"
        self.przycisk6.grid(row=1,column=2,sticky=W)
        self.przycisk6["command"]=self.Zanotuj
        
        self.przycisk6=Button(self.okno,width = 2,height=2)
        self.przycisk6["text"] = "3"
        self.przycisk6.grid(row=2,column=0,sticky=W)
        self.przycisk6["command"]=self.Zanotuj
        
        self.przycisk7=Button(self.okno,width = 2,height=2)
        self.przycisk7["text"] = "2"
        self.przycisk7.grid(row=2,column=1,sticky=W)
        self.przycisk7["command"]=self.Zanotuj
        
        self.przycisk8=Button(self.okno,width = 2,height=2)
        self.przycisk8["text"] = "1"
        self.przycisk8.grid(row=2,column=2,sticky=W)
        self.przycisk8["command"]=self.Zanotuj
        
        self.przycisk9=Button(self.okno,width = 2,height=2)
        self.przycisk9["text"] = "0"
        self.przycisk9.grid(row=3,column=1,sticky=W)
        self.przycisk9["command"]=self.Zanotuj
        
        self.przyciskprocent=Button(self.okno,width = 2,height=2)
        self.przyciskprocent["text"] = "."
        self.przyciskprocent.grid(row=3,column=0,sticky=W)
        #self.przyciskprocent["command"]=self.Procent
        
        self.przyciskznak=Button(self.okno,width = 2,height=2)
        self.przyciskznak["text"] = "+/-"
        self.przyciskznak.grid(row=3,column=2,sticky=W)
        self.przyciskznak["command"]=self.ZmienZnak

        self.pole1=Entry(self.okno,width=35,font=("Calibri",18))
        self.pole1.grid(row=0,column=3,columnspan=4,ipady=25,rowspan=2)

    def Zanotuj(self):
        liczba=int(self.przycisk1["text"])
        self.pole1.insert(0,liczba)
    def ZmienZnak(self):
        liczba=int(self.pole1.get())
        print(liczba)
        liczba=(-1)*liczba
        print(liczba)
        self.pole1.delete(0,END)
        self.pole1.insert(0,liczba)
        
a=Program()
