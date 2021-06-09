import os
import sys
import tkinter as tk
import random

# zmienne globalne
CZAS = 0
MINY = None
TRAFIONE_MINY = 0

class Gra:
    """klasa główna z grą"""

    def __init__(self, master):
        """konstruktor"""
        self.master = master
        self.N = 4
        self.M = 4
        self.master.minsize(150, 100)
        self.game = True
        #self.oknoGry()
        self.ikonki = self.wczytajPliki()
        self.objekt = self.oknoStartowe()

    def oknoStartowe(self):
        """okno startowe do którego podaję parametry"""
        dlugosc = tk.StringVar()
        szerokosc = tk.StringVar()
        liczbamin = tk.StringVar()

        self.autor = tk.Label(text="Autor: Damian Madej", padx=50, pady=10)
        self.autor.pack()

        self.podajN = tk.Label(text="Podaj wysokość:")
        self.podajN.pack()
        self.e1 = tk.Entry(self.master, textvariable=dlugosc, width=5, borderwidth=5)
        self.e1.pack()

        self.podajM = tk.Label(text="Podaj długość:")
        self.podajM.pack()
        self.e2 = tk.Entry(self.master, textvariable=szerokosc, width=5, borderwidth=5)
        self.e2.pack()

        self.podajMiny = tk.Label(text="Podaj liczbę min:")
        self.podajMiny.pack()
        self.e3 = tk.Entry(self.master, textvariable=liczbamin, width=5, borderwidth=5)
        self.e3.pack()

        self.przyciskOk = tk.Button(self.master, text="GRAJ!", command=lambda: self.nacisniecieGraj(dlugosc, szerokosc, liczbamin))
        self.przyciskOk.pack()

        self.bladWartosci1 = tk.Label(pady=10)
        self.bladWartosci1.pack()

        return [self.autor, self.podajN, self.e1, self.podajM, self.e2, self.podajMiny, self.e3, self.przyciskOk, self.bladWartosci1]


    def nacisniecieGraj(self, d, s, lm):
        """obsługa przycisku Graj"""
        try:
            self.bladWartosci1.destroy()
        except:
            pass
        try:
            self.bladWartosci2.destroy()
        except:
            pass
        try:
            self.bladWartosci3.destroy()
        except:
            pass

        global MINY
        global POZOSTALE_FLAGI

        MINY = lm.get()
        self.N = d.get()
        self.M = s.get()
        POZOSTALE_FLAGI = lm.get()

        try:
            self.N = int(self.N)
            self.M = int(self.M)
            MINY = int(MINY)
            POZOSTALE_FLAGI = int(POZOSTALE_FLAGI)

        except ValueError:
            self.bladWartosci1 = tk.Label(self.master, text="Prosze podać liczbę!", pady=10)
            self.bladWartosci1.pack()
            return

        test = False
        if self.N < 2 or self.M < 2:
            self.bladWartosci1 = tk.Label(self.master, text="Podaj wartość większą niż 1", pady=10)
            self.bladWartosci1.pack()
            test = True
            return test

        if self.N > 15 or self.M > 15:
            self.bladWartosci2 = tk.Label(self.master, text="Podaj wartość mniejszą niż 16", pady=10)
            self.bladWartosci2.pack()
            test = True
            return test

        if MINY > self.N*self.M or MINY < 0:
            self.bladWartosci3 = tk.Label(self.master, text="Podałeś błędną liczbę min", pady=10)
            self.bladWartosci3.pack()
            test = True
            return test

        if not test:
            self.goraOkna()


    def goraOkna(self):
        """Tworzy górę okna z licznikami"""
        try:
            for i in self.objekt:
                i.destroy()
        except AttributeError:
            pass

        if self.M < 5:
            self.minyLicznik = tk.Label(self.master, bg="black", fg="red", font=("", 16))
            self.minyLicznik.grid(row=0, column=0, columnspan=4, pady=16)
            self.liczMiny(self.minyLicznik)

            self.czasLicznik = tk.Label(self.master, width=3, bg="black", fg="red", font=("", 16))
            self.czasLicznik.grid(row=0, column=5, columnspan=4, pady=16)
            self.liczCzas(self.czasLicznik)
            self.planszaGry()

        else:
            self.minyLicznik = tk.Label(self.master, bg="black", fg="red", font=("", 16))
            self.minyLicznik.grid(row=0, column=0, columnspan=4, pady=15)
            self.liczMiny(self.minyLicznik)

            if self.M > 7:
                self.nowaGraPrzycisk = tk.Button(self.master, text = "Nowa \nGra", command = lambda : self.nowaGra())
                self.nowaGraPrzycisk.grid(row=0, column=self.M//2-2, columnspan=4, pady=15)

            self.czasLicznik = tk.Label(self.master, bg="black", fg="red", font=("", 16))
            self.czasLicznik.grid(row=0, column=self.M - 4, columnspan=4, pady=15)
            self.liczCzas(self.czasLicznik)
            self.planszaGry()

        return [self.minyLicznik, self.czasLicznik]


    def liczCzas(self, licznik):
        """aktualizuje licznik czasu"""
        global CZAS
        CZAS += 1
        licznik["text"] = "0" * (3 - len(str(CZAS))) + str(CZAS)
        if self.game == True:
            self.master.after(1000, self.liczCzas, licznik)


    def liczMiny(self, licznik):
        """aktualizuje licznik min"""
        licznik["text"] = "0" * (3 - len(str(POZOSTALE_FLAGI))) + str(POZOSTALE_FLAGI)

    def planszaGry(self):
        """tworzy siatkę z grą"""
        self.code = tk.StringVar()
        self.przyciski = [tk.Button(self.master, width=-2, height=-1) for i in range(self.N * self.M)]
        self.planszaGryLogika()
        for i in range(self.N):
            for j in range(self.M):
                if j == 0:
                    self.przyciski[i * self.M + j].grid(row=i + 1, column=j, padx=(20, 0))
                elif j == self.M - 1:
                    self.przyciski[i * self.M + j].grid(row=i + 1, column=j, padx=(0, 20))
                else:
                    self.przyciski[i * self.M + j].grid(row=i + 1, column=j)
                self.przyciski[i * self.M + j].bind('<Button-1>',
                                                    lambda event, p=self.przyciski[i * self.M + j]: self.lpm(p))
                self.przyciski[i * self.M + j].bind('<Button-3>',
                                                    lambda event, p=self.przyciski[i * self.M + j]: self.ppm(p))
        self.e = tk.Entry(self.master, textvariable = self.code, width=self.M*4).grid(row = self.N+3, column = 0, columnspan = self.M)
        self.master.bind('<Return>', lambda event: self.kod())

        return self.przyciski

    def kod(self):
        """po wprowadzeniu kodu xyzzy pola z minami stają się ciemniejsze"""

        tekst = self.code.get()
        if tekst == "xyzzy":
            for i in range(self.N):
                for j in range(self.M):
                    if self.tablicaGry[i][j] == 'm':
                        self.przyciski[i*self.M + j].config(bg='grey30')

        return self.przyciski

    def planszaGryLogika(self):
        """przypisuje miny do poszczególnych min"""
        self.tablicaGry = [[0 for j in range(self.M)] for i in range(self.N)]
        liczbaMin = MINY

        while liczbaMin:
            x = random.randint(0, self.M - 1)
            y = random.randint(0, self.N - 1)

            if self.tablicaGry[y][x] == 0:
                self.tablicaGry[y][x] = 'm'
                liczbaMin -= 1

        for i in range(self.N):
            for j in range(self.M):
                if self.tablicaGry[i][j] == 0:
                    sasiedzi = self.sasiadujacePola(j, i)

                    liczbaMin = 0
                    for x, y in sasiedzi:
                        if self.tablicaGry[y][x] == 'm':
                            liczbaMin += 1

                    self.tablicaGry[i][j] = liczbaMin

        return self.tablicaGry

    def sasiadujacePola(self, x, y):
        """sprawdza co znajduje się na sąsiadujących polach"""

        sasiedzi = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if not (i == 0 and j == 0):
                    if 0 <= y + i < self.N:
                        if 0 <= x + j < self.M:
                            sasiedzi.append((x + j, y + i))

        return sasiedzi

    def lpm(self, przycisk):
        """obsługa lewego przycisu myszy"""
        global POZOSTALE_FLAGI
        global TRAFIONE_MINY
        global MINY
        index = self.przyciski.index(przycisk)
        pole = self.tablicaGry[index // self.M][index % self.M]

        if przycisk.cget('image'):
            przycisk['image'] = ''
            POZOSTALE_FLAGI += 1
            self.liczMiny(self.minyLicznik)

        if pole == 'm':
            self.koniecGry()
        else:
            self.aktualizujPrzycisk(index, pole)

        if TRAFIONE_MINY == MINY and POZOSTALE_FLAGI == 0:
            if self.game == True:
                self.wygranaGra()

        return pole

    def ppm(self, przycisk):
        """obsługa prawego przycisku myszy"""
        index = self.przyciski.index(przycisk)
        pole = self.tablicaGry[index // self.M][index % self.M]

        global POZOSTALE_FLAGI
        global TRAFIONE_MINY
        global MINY
        if przycisk.cget('image'):
            przycisk['image'] = ''
            POZOSTALE_FLAGI += 1
            if pole == 'm':
                TRAFIONE_MINY -= 1

        else:
            przycisk['image'] = self.ikonki['flaga']
            POZOSTALE_FLAGI -= 1
            if pole == 'm':
                TRAFIONE_MINY += 1

        if TRAFIONE_MINY == MINY and POZOSTALE_FLAGI == 0:
            self.wygranaGra()

        self.liczMiny(self.minyLicznik)

    def wygranaGra(self):
        """okno wyświetlane po wygraniu gry"""
        self.game = False
        global CZAS
        info = "Gratulacje! Udało Ci się wygrać w " + str(CZAS+1) +"s"
        for i in range(self.N):
            for j in range(self.M):
                if isinstance(self.przyciski[i * self.M + j], tk.Button) and self.przyciski[i * self.M + j]['state'] != 'disabled':
                    self.przyciski[i*self.M + j].configure(state='disabled')
                    self.przyciski[i*self.M + j].unbind("<Button-1>")
                    self.przyciski[i*self.M + j].unbind("<Button-3>")
        self.noweOkno(info, 0)

    def koniecGry(self):
        """okno wyświetlane po przegraniu gry"""
        self.game = False
        info = "Niestety, tym razem przegrywasz"
        for i in range(self.N):
            for j in range(self.M):
                if isinstance(self.przyciski[i * self.M + j], tk.Button) and self.przyciski[i * self.M + j]['state'] != 'disabled':
                    self.przyciski[i*self.M + j].configure(state='disabled')
                    self.przyciski[i*self.M + j].unbind("<Button-1>")
                    self.przyciski[i*self.M + j].unbind("<Button-3>")
                    if self.tablicaGry[i][j] == 'm':
                        self.przyciski[i*self.M + j] = tk.Label(self.master, image = self.ikonki['miny'][1])
                        if j == 0:
                            self.przyciski[i*self.M + j].grid(row=i+1, column=j, padx=(20, 0))
                        elif j == self.M - 1:
                            self.przyciski[i*self.M + j].grid(row=i+1, column=j, padx=(0, 20))
                        else:
                            self.przyciski[i*self.M + j].grid(row=i+1, column=j)
        self.noweOkno(info, 1)

    def noweOkno(self, info, nrBuzki):
        """tworzy nowe okno informujące o wygranej lub przegranej gracza"""
        newWindow = tk.Toplevel(self.master)
        newWindow.title("Koniec gry")
        tk.Label(newWindow, text = info,padx = 20, pady = 10, font = ("", 15)).pack()
        tk.Label(newWindow, image = self.ikonki['buzia'][nrBuzki]).pack()
        tk.Label(newWindow, pady = 5).pack()
        tk.Button(newWindow, text = "Rozpocznij nową grę", command=lambda: self.nowaGra()).pack()
        tk.Button(newWindow, text = "Wyjdź z gry", command=lambda: exit()).pack()
        tk.Label(newWindow, pady = 5).pack()

    def aktualizujPrzycisk(self, index, pole):
        """aktualizuje wciśnięty przycisk na gridzie planszy z grą"""
        global POZOSTALE_FLAGI

        if self.przyciski[index].cget('image'):
            POZOSTALE_FLAGI += 1
            self.liczMiny(self.minyLicznik)
        self.przyciski[index].configure(state='disabled', border = 2)
        self.przyciski[index].config(bg='grey70')
        self.przyciski[index].unbind("<Button-1>")
        self.przyciski[index].unbind("<Button-3>")

        if pole != 0:
            self.przyciski[index] = tk.Label(self.master, image=self.ikonki['cyfry'][pole - 1])
            if index % self.M == 0:
                self.przyciski[index].grid(row=index // self.M + 1, column=index % self.M, padx=(20, 0))
            elif index % self.M == self.M - 1:
                self.przyciski[index].grid(row=index // self.M + 1, column=index % self.M, padx=(0, 20))
            else:
                self.przyciski[index].grid(row=index // self.M + 1, column=index % self.M)
        else:
            sasiedzi = self.sasiadujacePola(index % self.M, index // self.M)
            for x, y in sasiedzi:
                if isinstance(self.przyciski[y * self.M + x], tk.Button) and self.przyciski[y * self.M + x]['state'] != 'disabled':
                    self.aktualizujPrzycisk(y * self.M + x, self.tablicaGry[y][x])

    def wczytajPliki(self):
        """wczytuje ikonki do gry z folderu resources"""

        self.ikonki = {}
        self.ikonki['cyfry'] = [tk.PhotoImage(file='resources/' + str(i) + '.png') for i in range(1, 9)]
        self.ikonki['miny'] = [tk.PhotoImage(file='resources/mina' + str(i) + '.png') for i in range(1, 3)]
        self.ikonki['flaga'] = [tk.PhotoImage(file='resources/flag.png')]
        self.ikonki['buzia'] = [tk.PhotoImage(file='resources/buzia' + str(i) + '.png') for i in range(1, 3)]

        return self.ikonki

    def nowaGra(self):
        """rozpocznij nową grę"""
        os.execl(sys.executable, sys.executable, *sys.argv)

