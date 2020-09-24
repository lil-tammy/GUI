# WEBSITES
# https://www.tutorialspoint.com/python/tk_button.htm
# https://www.youtube.com/watch?v=D8-snVfekto&list=PLle-B6F23GFjoEsIPFZ6gVledAl7NvUhB&index=1&t=308s

import tkinter as tk

# Variables
WIDTH = 780
HEIGHT = 360

# HEX CODE
FAINT_PINK = '#ffc0cb'
SALMON_PINK = '#f87060'
SKIN_TONE = '#ffb367'
PASTEL_BLUE = '#c0fff4'
PASTEL_PURPLE = '#deaddd'

win = tk.Tk()
win.title("GUI")
win.configure(bg=PASTEL_PURPLE)

canvas = tk.Canvas(win, width=WIDTH, height=HEIGHT, bg=PASTEL_PURPLE)
canvas.pack()

label_1 = tk.Label(win, text="Press one", bg=PASTEL_PURPLE)
label_1.pack()

button_1 = tk.Button(win, text="Press me?", bg=FAINT_PINK, fg=SALMON_PINK)
button_1.pack()
button_2 = tk.Button(win, text="It's okay >.<", bg=SALMON_PINK, fg=FAINT_PINK)
button_2.pack()

frame = tk.Frame(win)


win.mainloop()
