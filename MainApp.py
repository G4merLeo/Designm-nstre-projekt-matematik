import tkinter as tk
from tkinter import StringVar
import random


class Program:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('1000x800')
        self.root.title('Matematik 0. Klasse')
        self.label_0 = tk.Label(self.root, text="Matematik for 0. Klasse", width=70, font=('Arial', 60))
        self.label_0.pack(padx=40, pady=40)

        self.label_1 = tk.Label(self.root, text="Vælg en af følgende muligheder", width=40, font=('Arial', 40))
        self.label_1.pack(padx=40, pady=40)

        self.buttonframe = tk.Frame(self.root)
        self.buttonframe.columnconfigure(0, weight=1)
        self.buttonframe.columnconfigure(1, weight=1)
        self.buttonframe.columnconfigure(2, weight=1)

        self.plusknap = tk.Button(self.buttonframe, text="Plus/Addition", font=('Bold', 30),
         command=lambda: Plus(self.root))
        self.plusknap.grid(row=0, column=0, padx=10)

        self.minusknap = tk.Button(self.buttonframe, text="Minus/Subtraktion", font=('Bold', 30),  
         command=lambda: Minus(self.root))
        self.minusknap.grid(row=0, column=1, padx=10)

        self.buttonframe.pack()

        self.root.mainloop()


label_yes=None
label_no=None

def Plus(root):
    Plusvindue = tk.Toplevel(root)
    Plusvindue.geometry("1000x800")

    Plus_Svar = tk.StringVar()
    plusnummer1 = tk.StringVar()
    plusnummer2 = tk.StringVar()

    label_400 = tk.Label(Plusvindue, text="", width=40, font=('Arial', 50))
    label_400.pack(padx=40, pady=40)

    def TilfældigPlusTal():
        if label_yes is not None:
            label_yes.destroy()
        if label_no is not None:
            label_no.destroy()

        plusnummer1.set(random.randint(1, 20))
        plusnummer2.set(random.randint(1, 20))
        spørgsmål = str(plusnummer1.get()) + "+" + str(plusnummer2.get())
        label_400.config(text=spørgsmål)

        EntrySvar.delete(0,tk.END)

 
        






    def PlusCheck():
        global label_yes, label_no

        if label_yes is not None:
            label_yes.destroy()
        if label_no is not None:
            label_no.destroy()

        print(Plus_Svar.get())
        if int(Plus_Svar.get()) == int(plusnummer1.get()) + int(plusnummer2.get()):
            print("yes")
            if label_no is not None:
                label_no.destroy()
            label_yes = tk.Label(Plusvindue, text="Godt gået, det er rigtigt!", width=40, font=('Arial', 50))
            label_yes.pack(padx=40, pady=40)
        else:
            label_no = tk.Label(Plusvindue, text="Forkert, prøv igen!", width=40, font=('Arial', 50))
            label_no.pack(padx=40, pady=40)

    EntrySvar = tk.Entry(Plusvindue, textvariable=Plus_Svar, font=('Bold', 30))
    EntrySvar.pack(padx=10, pady=10)

    plusknap = tk.Button(Plusvindue, text="Svar", font=('Bold', 30), command=PlusCheck)
    plusknap.pack(pady=10, padx=10)

    næsteknap = tk.Button(Plusvindue, text="Næste", font=('Bold', 30), command=TilfældigPlusTal)
    næsteknap.pack(padx=10, pady=10)
    TilfældigPlusTal()

def Minus(root):
    Minusvindue = tk.Toplevel(root)
    Minusvindue.geometry("1000x800")

    Plus_Svar = tk.StringVar()
    plusnummer1 = tk.StringVar()
    plusnummer2 = tk.StringVar()

    label_400 = tk.Label(Minusvindue, text="", width=40, font=('Arial', 50))
    label_400.pack(padx=40, pady=40)

    def TilfældigPlusTal():
        if label_yes is not None:
            label_yes.destroy()
        if label_no is not None:
            label_no.destroy()

        plusnummer1.set(random.randint(10, 20))
        plusnummer2.set(random.randint(1, 10))
        spørgsmål = str(plusnummer1.get()) + "-" + str(plusnummer2.get())
        label_400.config(text=spørgsmål)

        EntrySvar.delete(0,tk.END)

 
        






    def PlusCheck():
        global label_yes, label_no

        if label_yes is not None:
            label_yes.destroy()
        if label_no is not None:
            label_no.destroy()

        print(Plus_Svar.get())
        if int(Plus_Svar.get()) == int(plusnummer1.get()) - int(plusnummer2.get()):
            print("yes")
            if label_no is not None:
                label_no.destroy()
            label_yes = tk.Label(Minusvindue, text="Godt gået, det er rigtigt!", width=40, font=('Arial', 50))
            label_yes.pack(padx=40, pady=40)
        else:
            label_no = tk.Label(Minusvindue, text="Forkert, prøv igen!", width=40, font=('Arial', 50))
            label_no.pack(padx=40, pady=40)

    EntrySvar = tk.Entry(Minusvindue, textvariable=Plus_Svar, font=('Bold', 30))
    EntrySvar.pack(padx=10, pady=10)

    plusknap = tk.Button(Minusvindue, text="Svar", font=('Bold', 30), command=PlusCheck)
    plusknap.pack(pady=10, padx=10)

    næsteknap = tk.Button(Minusvindue, text="Næste", font=('Bold', 30), command=TilfældigPlusTal)
    næsteknap.pack(padx=10, pady=10)
    TilfældigPlusTal()



Program()
