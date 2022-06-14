from tkinter import *
from tkinter import font,messagebox as ms
import tkinter
from PIL import ImageTk, Image 
import random,time
import socket
from matplotlib.pyplot import text
import pandas as pd

app = Tk()
app.title("Generador de ZPL")
app.geometry("600x270")
app.config(bg="#314252")        
app.resizable(0,0)
app.iconbitmap('C:\\Users\\yair.carvajal\\Desktop\\zpl\\coffy.ico')



textConstante = '''
^XA 
^DFR:SAMPLE.GRF^FS
^FS^FO70,100^GB700,5,5 ^FX  - primera linea - ^FS ^FX  - Linea superior - ^FS
^FS^FO70,480^GB700,5,5 ^FX  - segund linea - ^FS ^FX  - Linea inferior - ^FS

^CF0,70^FO50,30^FD LasserEngraving Pack ^FX  - Texto Cabezado - ^FS

^FO30,150^ADN,36,20^FD WorkOrder: ^FS
^FO30,200^ADN,36,20^FD Part number: ^FS
^FO30,250^ADN,36,20^FD Batch: ^FS

^FO380,150^ADN,36,20^FN1^FS (ship to)
^FO380,200^ADN,36,20^FN2^FS(part num)
^FO380,250^ADN,36,20^FN3^FS(batch)

^FO140,300^BY3^B3N,,120^FN4^FS(barcode)

^XZ

^XA
^XFR:SAMPLE.GRF
^FN1^FD {idWO} ^FS
^FN2^FD {idPN} ^FS
^FN3^FD {idBatch} ^FS

^FN4^FD {idBatch} ^FS

^FO800,0^GFA,6525,6525,29,,::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::V08,,:S078M03C,S0F8M03F,R03F8M03F8,R0FF8M01FE,Q01FEO07F8,Q07F8O03FC,Q07FQ0FEK0E01OFEJ03,Q07FP01FEJ01F01J0LFCI0B8,Q07FCO07FEJ02F018007LFEI03C,Q07FFJ0AJ0FFEJ08F01007NF0037C,Q07FF800108003FFEJ02F01QF802FC,Q079F800402003F9EJ0AF01QFC03FC,Q0787801K03E3EJ0AF01QFE03FC,Q0783806I0C0183EJ0FF01QFE03FC,Q078M02I03EJ0FF01FE001FE007FE03FC,Q078002K04003EJ0FF01FE001FE003FE03FC,Q078003J01C003EJ0FF01FE001FE001FE03FC,Q078003CI03C001EJ0FF01FE001FE001FE03FC,Q03I03FI0FCI08J0FF01FE001FE001FE03FC,U03FC03FCN0FF01FE001FE001FE03FC,U03FE0FFCN0FF01FE001FE001FE03FC,U03FFBFFCN0FF01FE001FE001FE03FC,U03KFCN0FF01FE001FE001FE03FC,:::Q07I03KFC001CJ0FF01FE001FE001FE03FC,Q078003KFC003EJ0FF01FE001FE001FE03FC,:Q078003KF8003EJ0FF01FE001FE001FE03FC,Q078I0JFEI03EJ0FF01FE001FE001FE03FC,Q0787803IFC03C3EJ0FF01FE001FE001FE03FC,Q078F800IF003F3EJ0FF01FE001FE001FE03FC,Q07BF8007FC003FFEJ0FF01FE001FE001FE03FC,Q07FFI01FI01FFEJ0FF01FE001FE001FE03FC,Q07FEJ06J0FFEJ0FF01FE001FEI0FE03FC,Q07F8O03FEJ07F01FC001FCI0FE03F8,Q07FQ0FEJ03E00FCI0FCI07C01F8,Q07FP01FEK0C007J07J038006,P0C3FCO07FC7,O01E0FFN01FF078,O01E03F8I06I03FC078,O01C01F8I0FI03F8078,S078I0FI03E,S01J0FI018,X0F,V0E0F07,U01F0F1F,U01FCF7F,U01KF,V07IFE,V01IF8,W0FFE,W03F8,X0F,,:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::^FS

^XZ
'''

idWO = StringVar()
idPN = StringVar()
idBatch = StringVar()
#sidtextConstante = StringVar()


def limpiar():
    idWO.set("")
    idPN.set("")
    idBatch.set("")
    
def limpiarBox():
    pass

def surprise():
    def cambiarColor2():  
        color = "%06x" % random.randint(0, 0xFFFFFF)
        sp.configure({"background": "#" + color})

    def reset():  
        sp.configure({"background": "#314252"})

    sp = Toplevel()
    sp.title("Sorprice")
    sp.geometry("250x150")
    sp.config(background="#314252",cursor="heart")
    sp.resizable(0,0)
    image1 = Image.open("C:\\Users\\yair.carvajal\\Desktop\\zpl\\coffy.png")
    test = ImageTk.PhotoImage(image1)
    label1 = Label(sp,image=test)
    label1.image = test
    label1.place(x=75, y=25)
    Bnsp = Button(sp,text='Clic Me!', command=cambiarColor2)
    Bnsp.place(x=15,y=35)
    Bnsp2 = Button(sp,text='Restart!', command=reset)
    Bnsp2.place(x=15,y=65)
    Bnsp3 = Button(sp,text="Adios!", command= sp.destroy)
    Bnsp3.place(x=200,y=105)

def mostrarInfo():
    lBox.insert(END,textConstante.replace('{idWO}',WO.get()).replace('{idPN}',PN.get()).replace('{idBatch}',BT.get()))
    mostrarInfoConsole()
    limpiar()

def mostrarInfoConsole():
    print(str(textConstante.replace('{idWO}',WO.get()).replace('{idPN}',PN.get()).replace('{idBatch}',BT.get())    ))
    

def cambiarColor():  
    color = "%06x" % random.randint(0, 0xFFFFFF)
    app.configure({"background": "#" + color})
    
def reset():  
    app.configure({"background": "white"})

def times():
    current_time=time.strftime("%H:%M:%S")
    clock.config(text=current_time,bg="#314252",fg="red",font="Helvetica 10 bold")
    clock.after(200,times)

def SendZPLFile():
    mysocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)        
    host = "10.42.1.53"
    port = 9100  

    try:          
        mysocket.connect((host, port)) #connecting to host
        mysocket.send(b"^XA^A0N,50,50^FO50,50^FDSocket Test^FS^XZ")#using bytes
        mysocket.close () #closing connection
        ms.showinfo(title="Send", text="Enviado")
    except:
        print("Error with the connection")
        raise ms.showinfo("Error","ZPL was not send to the printer, please validate the folowing option \n\nValidate the connection printer \nValidate ZPL format \nIf this problem continues please notify the System Department")

def DownLoad():
    try:          
        dt = (str(textConstante.replace('{idWO}',WO.get()).replace('{idPN}',PN.get()).replace('{idBatch}',BT.get())    ))
        fb = [dt]
        lista = [fb]

        lista2 = pd.DataFrame(lista,
                                columns=['Testing1'])
        lista2.to_excel('hellow.xlsx', index=False)
        ms.showinfo("Successfully","Excel is Created")
    except:
        ms.showwarning(title="Error", message="Excel is not Created \n\nPlease validate if you do not have your file open")

    limpiar()

####  Frame  ####

LabelWO =Label(text="WO").place(x=20,y=30)
WO = Entry(text="Introduzca WorkORder", textvariable=idWO)
WO.place(x=100,y=30)
WO.focus_set()

LabelPN =Label(text="PN").place(x=20,y=60)
PN = Entry(text="Introduzca PartNumber", textvariable=idPN)
PN.place(x=100,y=60)

LabelBT =Label(text="Batch").place(x=20,y=90)
BT = Entry(text="Introduzca Batch", textvariable=idBatch)
BT.place(x=100,y=90)


BnStart = Button(text="Start",command=mostrarInfo ).place(x=100,y=120)

BnClear = Button(text="Clear",command=limpiar)
BnClear.place(x=150, y=120) 

BnSorprice = Button(text="ShowSorprice",command= surprise).place(x=200,y=120)

BnExist = Button(text="Exit",command=quit)
BnExist.place(x=550,y=220)
BnExist.config(background="Red")


lBox = Listbox(app,justify= "center")
lBox.config(width=40,height=11)
lBox.place(x=300, y=30)

scrollbarV = Scrollbar(app, orient=VERTICAL,command=lBox.yview)
scrollbarV.place(x=540,y=30)
lBox['yscrollcommand'] = scrollbarV.set

scrollbarH = Scrollbar(app, orient=HORIZONTAL,command=lBox.xview)
scrollbarH.place(x=300,y=210)
lBox['xscrollcommand'] = scrollbarH.set


clock=Label(app,font=("times",10,"bold"))
clock.place(x=20,y=220)
times()




menubar = Menu(app)
app.config(menu=menubar)

filemenu = Menu(menubar, tearoff=0)

filemenu.add_command(label="SendZpl", command=SendZPLFile)
filemenu.add_command(label="DownLoad", command=DownLoad)


menubar.add_cascade(label="Archivo", menu=filemenu)
app.mainloop()
