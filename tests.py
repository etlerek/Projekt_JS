from game import *
import unittest
import tkinter

class Test(unittest.TestCase):
    def test_sprawdzWielkosc(self):
        gra = Gra(tk.Tk())

        result = gra.nacisniecieGraj(tk.StringVar(value=1), tk.StringVar(value=1), tk.StringVar(value=1))
        self.assertEqual(result, True)

        result = gra.nacisniecieGraj(tk.StringVar(value=5), tk.StringVar(value=1), tk.StringVar(value=1))
        self.assertEqual(result, True)

        result = gra.nacisniecieGraj(tk.StringVar(value=4), tk.StringVar(value=1), tk.StringVar(value=2))
        self.assertEqual(result, True)

        result = gra.nacisniecieGraj(tk.StringVar(value=4), tk.StringVar(value=1), tk.StringVar(value=2))
        self.assertEqual(result, True)

        result = gra.nacisniecieGraj(tk.StringVar(value=20), tk.StringVar(value=500), tk.StringVar(value=12))
        self.assertEqual(result, True)

        result = gra.nacisniecieGraj(tk.StringVar(value=5), tk.StringVar(value=6), tk.StringVar(value=-4))
        self.assertEqual(result, True)

        result = gra.nacisniecieGraj(tk.StringVar(value=3), tk.StringVar(value=3), tk.StringVar(value=10))
        self.assertEqual(result, True)

        result = gra.nacisniecieGraj(tk.StringVar(value=1), tk.StringVar(value=10), tk.StringVar(value=5))
        self.assertEqual(result, True)

