import tkinter as tk
import csv

#from tkinter import Tk, Label, Button

class Principal:
    def __init__(self,master,*args, **kwargs):
        # Create labels, entries,buttons
        self.master = master
        self.configure_gui()

        #self.path = PhotoImage(file="card.png")

        self.Frame1 = tk.Frame(self.master)
        self.Frame1.place(relx=1,rely=1)
        self.Frame1.pack()

        #Botones
        self.buttonP = tk.Button(text="Pago", width=15, height=5, command= self.abrir_ventana_pagar )
        self.buttonP.place(relx=0.8, rely=0.05)
        self.buttonP.place()

        self.photo1 = tk.PhotoImage(file="images/audifonos apple.png")
        self.button1 = tk.Button(text="Audifono apple", image=self.photo1)
        self.button1.place(relx=0.05, rely=0.05)
        self.button1.place()

        self.photo2 = tk.PhotoImage(file="images/audifonos_samsung.png")
        self.button2 = tk.Button(text="Audifono sans undertale",image=self.photo2)
        self.button2.place(relx=0.22, rely=0.05)
        self.button2.place()

        self.photo3 = tk.PhotoImage(file="images/Llave maya de 16 gb.png")
        self.button3 = tk.Button(text="llave maya 16",image=self.photo3)
        self.button3.place(relx=0.39, rely=0.05)
        self.button3.place()

        self.photo4 = tk.PhotoImage(file="images/Llave maya 128 G.png")
        self.button4 = tk.Button(text="lave maya 128",image=self.photo4)
        self.button4.place(relx=0.56, rely=0.05)
        self.button4.place() 

        self.photo5 = tk.PhotoImage(file="images/Google chromecast.png")
        self.button5 = tk.Button(text="google chromecast",image=self.photo5)
        self.button5.place(relx=0.05, rely=0.25)
        self.button5.place()

        self.photo6 = tk.PhotoImage(file="images/Amazon fire stickjpg.png")
        self.button6 = tk.Button(text="amazon fire",image=self.photo6)
        self.button6.place(relx=0.22, rely=0.25)
        self.button6.place()

        self.photo7 = tk.PhotoImage(file="images/telefono desechable 1.png")
        self.button7 = tk.Button(text="telefono 1",image=self.photo7)
        self.button7.place(relx=0.39, rely=0.25)
        self.button7.place()       

        self.photo8 = tk.PhotoImage(file="images/telefono desechable 2.png")
        self.button8 = tk.Button(text="telefono 2",image=self.photo8)
        self.button8.place(relx=0.56, rely=0.25)
        self.button8.place()

        self.photo9 = tk.PhotoImage(file="images/Parlante bluetooth JBL.png")
        self.button9 = tk.Button(text="parlante JBL",image=self.photo9)
        self.button9.place(relx=0.05, rely=0.45)
        self.button9.place()

        self.photo10 = tk.PhotoImage(file="images/Parlante bluetooth Sony.png")
        self.button10 = tk.Button(text="Parlante Sonny",image=self.photo10)
        self.button10.place(relx=0.22, rely=0.45)
        self.button10.place()

        self.photo11 = tk.PhotoImage(file="images/adaptador-jack-lightning-audifonos.png")
        self.button11 = tk.Button(text="lighting jack cable",image=self.photo11)
        self.button11.place(relx=0.39, rely=0.45)
        self.button11.place()

        self.photo12 = tk.PhotoImage(file="images/usb tipo C.png")
        self.button12 = tk.Button(text="USB Tipo C",image=self.photo12)
        self.button12.place(relx=0.56, rely=0.45)
        self.button12.place()

        self.photo13 = tk.PhotoImage(file="images/teclado inalambrico.png")
        self.button13 = tk.Button(text="Teclado",image=self.photo13)
        self.button13.place(relx=0.05, rely=0.65)
        self.button13.place()

        self.photo14 = tk.PhotoImage(file="images/mouse inalambrico.png")
        self.button14 = tk.Button(text="Mouse Inalambrico",image=self.photo14)
        self.button14.place(relx=0.22, rely=0.65)
        self.button14.place()

        self.photo15 = tk.PhotoImage(file="images/GO PRO.png")
        self.button15 = tk.Button(text="Go pro",image=self.photo15)
        self.button15.place(relx=0.39, rely=0.65)
        self.button15.place()

        self.photo16 = tk.PhotoImage(file="images/bateria externa.png")
        self.button16 = tk.Button(text="Bateria externa",image=self.photo16)
        self.button16.place(relx=0.56, rely=0.65)
        self.button16.place()
    

    def abrir_ventana_pagar(self):
        # If button is clicked, run this method and open window 2
        self.nuevaVentana = tk.Toplevel(self.master)
        self.app = VentanaPago(self.nuevaVentana)

    def configure_gui(self):
        self.master.title("Maquina Expendedora")
        self.master.geometry("850x500")
        self.master.resizable(False, False)

class VentanaPago:
    def __init__(self, master):
        self.master = master
        self.configure_gui()

        #create buttons,entries,etc
        


    def button_method(self):
        #run this when button click to close window
        self.master.destroy()

    def configure_gui(self):
        self.master.title("Pantalla de pago")
        self.master.geometry("300x400")
        self.master.resizable(False, False)

def main(): #run mainloop 
    root = tk.Tk()
    app = Principal(root)
    root.mainloop()

if __name__ == '__main__':
    main()

