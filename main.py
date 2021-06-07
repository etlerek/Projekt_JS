import tkinter as tk
import game


def glowneOkno():
    """ustawienia okna głównego"""
    root = tk.Tk()
    root.title('Saper')

    return root

if __name__ == '__main__':
    """funkcja main"""
    root = glowneOkno()
    app = game.Gra(root)
    del app
    root.mainloop()
