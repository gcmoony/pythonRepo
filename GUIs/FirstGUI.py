import tkinter as tk


"""
Some things to look back on:

Labels = lbl_someLabelName
Buttons = btn_someButtonName
Entries = ent_someEntryName
Text = txt_someTextName
Frame = frm_someFrameName
"""


#### This is a single window ####
window = tk.Tk()


#### Making Labels ####
greeting = tk.Label(text = "Hello World!")
# This puts the greeting LABEL in the window
greeting.pack()

greeting2 = tk.Label(
    text = "I am the second label",
    fg = "red",
    bg = "dark grey",
    width = 100,
    height = 2
)
greeting2.pack()

label01 = tk.Label(
    text = "Some funky label",
    foreground = "white",
    background = "black"
).pack() # Here's some chaining


##### Making buttons ####
button01 = tk.Button(
    text = "Button 01",
    width = 15,
    height = 15
)
button01.pack()


#### Making Frames ####
frame01 = tk.Frame(
    master = window,
    relief = tk.RIDGE,
    borderwidth = 3
)

frameLabel = tk.Label(
    master= frame01,
    text = "I'm in Frame 01"
).pack()

frame01.pack()


# This goes last
window.mainloop()