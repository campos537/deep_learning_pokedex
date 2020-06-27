from tkinter import *
from windows.main_window import MainWindow

window = Tk()
mywin = MainWindow(window)
window.title('Pokedex Desktop')
window.geometry("960x540+10+10")
window.mainloop()