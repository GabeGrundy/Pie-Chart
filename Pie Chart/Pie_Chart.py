import tkinter as tk

#window properties
window = tk.Tk()
window.title("Pie Chart")
window.geometry("600x400")

txtNumber1 = tk.Entry(window)
txtNumber2 = tk.Entry(window)


def hide1():
    txtNumber2.grid_remove
def unhide1():
    txtNumber2.grid(row=1,column=1)


#drop down select
numinputs = [
    1,    
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10
]

clicked = tk.IntVar()

drop = tk.OptionMenu(window,clicked,*numinputs)


#funtions
def show():
    label.config(text= clicked.get())
    Inputammount = 0
    Inputammount = (clicked.get())
    if Inputammount == 2:
        unhide1()
    if Inputammount == 1:
        hide1()
#the struggle is real





clicked.set( "Number of Inputs" ) 





#buttons
button1 = tk.Button(window,text="set",command=show)
#labels
label = tk.Label(window,text=" ")



#place gui items
drop.grid(column=0,row=0)
button1.grid(column=1,row=0)
txtNumber1.grid(row=1,column=1)



#build window
window.mainloop()