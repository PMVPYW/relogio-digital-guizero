from guizero import *
from time import strftime

if __name__ == "__main__":
    a = App(title = "clock", height = 100)
    a.bg = (0,0,0)
    t = Text(a, text = "0", font="ds-digital", size=80, color = (2,246,251))

    def update_clock():
        global t
        t.clear()
        string = strftime("%H:%M:%S")
        t.append(string)
    a.repeat(100, update_clock)
    a.display()
        
