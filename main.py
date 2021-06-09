import tkinter as tk
import game


def glowneOkno():
    """ustawienia okna głównego"""

    root = tk.Tk()
    root.title('Saper')
    root.iconphoto(False, tk.PhotoImage(file = 'resources/mina1.png'))
    app = game.Gra(root)
    root.mainloop()

if __name__ == '__main__':
    """funkcja main"""
    glowneOkno()

