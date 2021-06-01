import tkinter as tk

#zmienne globalne
CZAS = 0
MINY = 10

class Ustawienia:

#---------------------------------------------
#-------------konstruktor okna----------------
#---------------------------------------------

    def __init__(self, master):

        self.master = master
        self.master.geometry('200x200')

        self.oknoStartowe()

#---------------------------------------------
#--okno startowe do którego podaję parametry--
#---------------------------------------------

    def oknoStartowe(self):

        self.dlugosc = tk.StringVar()
        self.szerokoksc = tk.StringVar()

        self.podajN = tk.Label(text = "Podaj długość:")
        self.podajN.pack()
        self.e1 = tk.Entry(self.master, textvariable = self.dlugosc, width = 5, borderwidth=5)
        self.e1.pack()

        self.podajM = tk.Label(text = "Podaj wysokość:")
        self.podajM.pack()
        self.e2 = tk.Entry(self.master,textvariable = self.szerokoksc, width = 5, borderwidth=5)
        self.e2.pack()

        self.przyciskOk = tk.Button(self.master, text = "GRAJ!", command = lambda: self.nacisniecieGraj())
        self.przyciskOk.pack()

#---------------------------------------------
#-----------obsługa przycisku Graj------------
#---------------------------------------------

    def nacisniecieGraj(self):

        #usuwa komunikat w razie potrzeby ponownego wpisania wartośći dla szerokości i długości
        try:
            self.bladWartosci1.destroy()
            self.bladWartosci2.destroy()
        except:
            pass

        self.N = self.dlugosc.get()
        self.M = self.szerokoksc.get()

        #wyłapuje błąd jeżeli podane N i M nie są liczbami
        try:
            self.N = int(self.N)
            self.M = int(self.M)
        except ValueError:
            self.bladWartosci1 = tk.Label(self.master, text = "Prosze podać liczbę!")
            self.bladWartosci1.pack()
            return

        test = False
        if self.N < 2 or self.M < 2:
            self.bladWartosci1 = tk.Label(self.master, text = "Podaj wartość większą niż 2")
            self.bladWartosci1.pack()
            test = True

        if self.N > 15 or self.M > 15:
            self.bladWartosci2 = tk.Label(self.master, text = "Podaj wartość mniejszą niż 15")
            self.bladWartosci2.pack()
            test = True

        if not test:
            self.oknoGry()
#---------------------------------------------
#-------okno tworzące siatkę z grą------------
#---------------------------------------------

    def oknoGry(self):
        pass


#---------------------------------------------
#-------przypisyawnie tworzenie okna----------
#---------------------------------------------

def glowneOkno():
    root = tk.Tk()
    root.title('Saper')

    return root
#---------------------------------------------
#--------------funkcja main-------------------
#---------------------------------------------
if __name__ == '__main__':

    root = glowneOkno()
    app = Ustawienia(root)
    root.mainloop()

