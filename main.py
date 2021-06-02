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

        self.objekt = self.oknoStartowe()

#---------------------------------------------
#--okno startowe do którego podaję parametry--
#---------------------------------------------

    def oknoStartowe(self):

        self.dlugosc = tk.StringVar()
        self.szerokoksc = tk.StringVar()

        self.autor = tk.Label(text = "Autor: Damian Madej",padx=50, pady=10)
        self.autor.pack()

        self.podajN = tk.Label(text = "Podaj długość:")
        self.podajN.pack()
        self.e1 = tk.Entry(self.master, textvariable = self.dlugosc, width = 5, borderwidth=5)
        self.e1.pack()

        self.podajM = tk.Label(text = "Podaj wysokość:")
        self.podajM.pack()
        self.e2 = tk.Entry(self.master,textvariable = self.szerokoksc, width = 5, borderwidth=5)
        self.e2.pack()

        self.przyciskOk = tk.Button(self.master, text = "GRAJ!",command = lambda: self.nacisniecieGraj())
        self.przyciskOk.pack()

        self.bladWartosci1 = tk.Label(pady=10)
        self.bladWartosci1.pack()

        return [self.autor, self.podajN, self.e1, self.podajM, self.e2, self.przyciskOk, self.bladWartosci1]

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
            self.bladWartosci1 = tk.Label(self.master, text = "Prosze podać liczbę!",pady=10)
            self.bladWartosci1.pack()
            return

        test = False
        if self.N < 2 or self.M < 2:
            self.bladWartosci1 = tk.Label(self.master, text = "Podaj wartość większą niż 2",pady=10)
            self.bladWartosci1.pack()
            test = True

        if self.N > 15 or self.M > 15:
            self.bladWartosci2 = tk.Label(self.master, text = "Podaj wartość mniejszą niż 15",pady=10)
            self.bladWartosci2.pack()
            test = True

        if not test:
            self.oknoGry()
#---------------------------------------------
#--------okno tworzące panel górny------------
#---------------------------------------------

    def oknoGry(self):
        for i in self.objekt:
            i.destroy()

        if self.N <5:
            self.licznik_min = tk.Label(self.master,width = 3, bg="black", fg="red", font=("", 20))
            self.licznik_min.grid(row=0, column=self.M//2, columnspan=3)
            self.licznik_min['text'] = '001'

            self.licznik_czasu=tk.Label(self.master,width = 3, bg="black", fg="red", font=("", 20))
            self.licznik_czasu.grid(row=1, column=self.M//2, columnspan=3)
            self.licznik_czasu['text'] = '001'
            self.planszaGry(1)

        else:
            self.licznik_min = tk.Label(self.master, bg="black", fg="red", font=("", 20))
            self.licznik_min.grid(row=0, column=0, columnspan=4)
            self.licznik_min['text'] = '001'

            self.licznik_czasu=tk.Label(self.master,width = 3, bg="black", fg="red", font=("", 20))
            self.licznik_czasu.grid(row=0, column=self.M-4, columnspan=4)
            self.licznik_czasu['text'] = '001'
            self.planszaGry(0)


        return [self.licznik_min, self.licznik_czasu]

#---------------------------------------------
#-------okno tworzace siatke z grą------------
#---------------------------------------------

    def planszaGry(self, przesuniecie):
        self.przyciski = [tk.Button(root, height = 1, width = 2) for i in range(self.N*self.M)]
        for i in range(self.N):
            for j in range(self.M):
                if j == 0:
                    self.przyciski[i*self.M+j].grid(row = i+przesuniecie+1, column = j, padx = (20, 0))
                elif j == self.M-1:
                    self.przyciski[i*self.M+j].grid(row = i+przesuniecie++1, column = j, padx = (0, 20))
                elif i == self.N-1:
                    self.przyciski[i*self.M+j].grid(row = i+przesuniecie++1, column = j, pady = (0, 0)) # tutaj trzeba cos zmienic
                else:
                    self.przyciski[i*self.M+j].grid(row = i+przesuniecie++1, column = j)

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

