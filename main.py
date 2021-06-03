import tkinter as tk
import random

#zmienne globalne
CZAS = 0
MINY = 40

class Ustawienia:

#---------------------------------------------
#-------------konstruktor okna----------------
#---------------------------------------------

    def __init__(self, master):

        self.master = master
        self.N = 12
        self.M = 12

        self.ikonki = self.wczytajPliki()
        self.oknoGry()
#        self.objekt = self.oknoStartowe()



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
            self.bladWartosci1 = tk.Label(self.master, text = "Podaj wartość większą niż 1",pady=10)
            self.bladWartosci1.pack()
            test = True

        if self.N > 15 or self.M > 15:
            self.bladWartosci2 = tk.Label(self.master, text = "Podaj wartość mniejszą niż 16",pady=10)
            self.bladWartosci2.pack()
            test = True

        if not test:
            self.oknoGry()

    def oknoGry(self):
        try:
            for i in self.objekt:
                i.destroy()
        except AttributeError:
            pass

        if self.M < 5:
            self.minyLicznik = tk.Label(self.master, width = 3, bg="black", fg="red", font=("", 20))
            self.minyLicznik.grid(row=0, column=self.M // 2 - 1, columnspan=3, pady=10)
            self.liczMiny(self.minyLicznik)

            self.czasLicznik=tk.Label(self.master, width = 3, bg="black", fg="red", font=("", 20))
            self.czasLicznik.grid(row=1, column=self.M // 2 - 1, columnspan=3, pady=10)
            self.liczCzas(self.czasLicznik)
            self.planszaGry(1)

        else:
            self.minyLicznik = tk.Label(self.master, bg="black", fg="red", font=("", 16))
            self.minyLicznik.grid(row=0, column=0, columnspan=4, pady=15)
            self.liczMiny(self.minyLicznik)

            self.czasLicznik=tk.Label(self.master, width = 3, bg="black", fg="red", font=("", 16))
            self.czasLicznik.grid(row=0, column=self.M - 4, columnspan=4, pady=15)
            self.liczCzas(self.czasLicznik)
            self.planszaGry(0)


        return [self.minyLicznik, self.czasLicznik]

    #---------------------------------------------
    #--------licznik czasu gry oraz min-----------
    #---------------------------------------------

    def liczCzas(self, licznik):
        global CZAS
        CZAS += 1
        licznik["text"] = "0"*(3 - len(str(CZAS))) + str(CZAS)
        self.master.after(1000, self.liczCzas, licznik)

    def liczMiny(self, licznik):
        licznik["text"] = "0"*(3 - len(str(MINY))) + str(MINY)


    #---------------------------------------------
    #-------okno tworzace siatke z grą------------
    #---------------------------------------------

    def planszaGry(self, przesuniecie):
        self.przyciski = [tk.Button(self.master, width = -1, height = -2) for i in range(self.N*self.M)]
        self.planszaGryLogika()
        for i in range(self.N):
            for j in range(self.M):
                if j == 0:
                    self.przyciski[i*self.M+j].grid(row = i+przesuniecie+1, column = j, padx = (20, 0))
                elif j == self.M-1:
                    self.przyciski[i*self.M+j].grid(row = i+przesuniecie++1, column = j, padx = (0, 20))
                else:
                    self.przyciski[i*self.M+j].grid(row = i+przesuniecie++1, column = j)
                    self.przyciski[i*self.M+j].bind('<Button-1>', lambda: self.lpm())
                    self.przyciski[i*self.M+j].bind('<Button-3>', lambda event, p = self.przyciski[i*self.M+j]: self.ppm(p, self.ikonki))

        return self.przyciski

    def lpm(self):
        pass

    def ppm(self, przyciski, ikonki):

        przyciski['image'] = ikonki['flaga']


    def wczytajPliki(self):

        """TODO: resize ikonek"""

        self.ikonki = {}
        self.ikonki['cyfry'] = [tk.PhotoImage(file = 'resources/' + str(i) + '.png') for i in range(1,9)]
        self.ikonki['miny'] = [tk.PhotoImage(file = 'resources/mina' + str(i) + '.png') for i in range(1,3)]
        self.ikonki['flaga'] = [tk.PhotoImage(file = 'resources/flag.png')]

        return self.ikonki

    #---------------------------------------------
    #--------przypisywanie polom min--------------
    #---------------------------------------------

    def planszaGryLogika(self):
        self.tablicaGry = [[0 for j in range(self.M)] for i in range(self.N)]
        self.liczbaMin = MINY


        #wypisuje do konsoli plansze z grą, na której m oznacza minę, natomiast liczba oznaczy ilosc sąsiadujących min
        while self.liczbaMin:
            self.x = random.randint(0, self.M-1)
            self.y = random.randint(0, self.N-1)
            if self.tablicaGry[self.y][self.x] == 0:
                self.tablicaGry[self.y][self.x] = 'm'
                self.liczbaMin -= 1

        for i in range(self.N):
            for j in range(self.M):
                if self.tablicaGry[i][j] == 0:
                    self.sasiedzi = self.sasiadujaceMiny(j, i)
                    self.liczba = 0
                    for self.x, self.y in self.sasiedzi:
                        if self.tablicaGry[self.y][self.x] == 'm':
                            self.liczba += 1

                    self.tablicaGry[i][j] = self.liczba
        print(self.tablicaGry)

        return self.tablicaGry

    def sasiadujaceMiny(self, x, y):

        self.sasiedzi = []
        for i in range(-1, 2):
            for j in range(-1,2):
                if not i == 0 and j == 0:
                    if y + i >= 0 and y+ i < self.N:
                        if x+j >= 0 and x +j < self.M:
                            self.sasiedzi.append((x+j, y+i))

        return self.sasiedzi
#---------------------------------------------
#--------okno tworzące panel górny------------
#---------------------------------------------


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

