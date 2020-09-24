import tkinter as tk

# VARIABLES

# HEX CODES
FAINT_PINK = '#ffc0cb'
SALMON_PINK = '#f87060'



# makes window
win = tk.Tk()

# True = Resize, False = not
win.resizable(True, True)

#canvas.tk.Canvas(root)

pwetty_fwame = tk.Frame(win)
pwetty_fwame.pack()

tk.Label(win, text="Label Time BABY").pack()
tk.Button(win, text="Press Me~~", bg=FAINT_PINK, fg=SALMON_PINK).pack()

label2 = tk.Label(win,text="^^^ Press that button")
label2.pack()

button2 = tk.Button(win, text="No press meeee!!!")
button2.pack()

# Starts GUI
win.mainloop()
