import tkinter as tk

# VARIABLES
WIDTH = 1080
HEIGHT = 550

# HEX CODES
FAINT_PINK = '#ffc0cb'
SALMON_PINK = '#f87060'
SKIN_TONE = '#ffb367'


# makes window
win = tk.Tk()

# True = Resize, False = not
win.resizable(False, False)

# CONTAINER TO STORE
canvas = tk.Canvas(win, width=WIDTH, height=HEIGHT)
canvas.pack()

pwetty_fwame = tk.Frame(win, bg='blue')
pwetty_fwame.place()

tk.Label(win, text="Label Time BABY").pack()
tk.Button(win, text="Press Me~~", bg=FAINT_PINK, fg=SALMON_PINK).pack()

label2 = tk.Label(win,text="^^^ Press that button")
label2.pack()



button2 = tk.Button(win, text="No press meeee!!!")
button2.pack()

# Starts GUI
win.mainloop()
