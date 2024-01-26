import tkinter as tk

#window properties
window = tk.Tk()
window.title("Pie Chart")
window.geometry("900x600")

txtNumber1 = tk.Entry(window)
txtNumber2 = tk.Entry(window)
txtNumber3 = tk.Entry(window)
txtNumber4 = tk.Entry(window)
txtNumber5 = tk.Entry(window)
txtNumber6 = tk.Entry(window)
txtNumber7 = tk.Entry(window)
txtNumber8 = tk.Entry(window)
txtNumber9 = tk.Entry(window)
txtNumber10 = tk.Entry(window)

def hide2():
    txtNumber2.grid_forget()
def unhide2():
    txtNumber2.grid(row=2,column=1,padx=10,)

def hide3():
    txtNumber3.grid_forget()
def unhide3():
    txtNumber3.grid(row=3,column=1)

def hide4():
    txtNumber4.grid(row=-1,column=-1)
def unhide4():
    txtNumber4.grid(row=4,column=1)
                    
def hide5():
    txtNumber5.grid(row=-1,column=-1)
def unhide5():
    txtNumber5.grid(row=5,column=1)

def hide6():
    txtNumber6.grid(row=-1,column=-1)
def unhide6():
    txtNumber6.grid(row=6,column=1)

def hide7():
    txtNumber7.grid(row=-1,column=-1)
def unhide7():
    txtNumber7.grid(row=7,column=1)

def hide8():
    txtNumber8.grid(row=-1,column=-1)
def unhide8():
    txtNumber8.grid(row=8,column=1)

def hide9():
    txtNumber9.grid(row=-1,column=-1)
def unhide9():
    txtNumber9.grid(row=9,column=1)

def hide10():
    txtNumber10.grid(row=-1,column=-1)
def unhide10():
    txtNumber10.grid(row=10,column=1)
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
        unhide2()
        hide3()
        hide4()
        hide5()
        hide6()
        hide7()
        hide8()
        hide9()
        hide10()

    if Inputammount == 1:
        hide2()
        hide3()
        hide4()
        hide5()
        hide6()
        hide7()
        hide8()
        hide9()
        hide10()
        

    
    if Inputammount == 2:
        unhide2()
        

    if Inputammount == 3:
        unhide2()
        unhide3()

        hide4()
        hide5()
        hide6()
        hide7()
        hide8()
        hide9()
        hide10()
    if Inputammount == 4:
        unhide2()
        unhide3()
        unhide4()
        
        hide5()
        hide6()
        hide7()
        hide8()
        hide9()
        hide10()
    if Inputammount == 5:
        unhide2()
        unhide3()
        unhide4()
        unhide5()

        hide6()
        hide7()
        hide8()
        hide9()
        hide10()
    if Inputammount == 6:
        unhide2()
        unhide3()
        unhide4()
        unhide5()
        unhide6()

        hide7()
        hide8()
        hide9()
        hide10()
    if Inputammount == 7:
        unhide2()
        unhide3()
        unhide4()
        unhide5()
        unhide6()
        unhide7()
       
        hide8()
        hide9()
        hide10()
    if Inputammount == 8:
        unhide2()
        unhide3()
        unhide4()
        unhide5()
        unhide6()
        unhide7()
        unhide8()
       
        hide9()
        hide10()
    if Inputammount == 9:
        unhide2()
        unhide3()
        unhide4()
        unhide5()
        unhide6()
        unhide7()
        unhide8()
        unhide9()
       
        hide10()
    if Inputammount == 10:
        unhide2()
        unhide3()
        unhide4()
        unhide5()
        unhide6()
        unhide7()
        unhide8()
        unhide9()
        unhide10()
#the struggle is real
#canvas
canvas= tk.Canvas(window, width= 500, height= 400, bg="white")

clicked.set( "Number of Inputs" ) 

#buttons
button1 = tk.Button(window,text="set",command=show)
#labels
label = tk.Label(window,text=" ")



#place gui items
drop.grid(column=1,row=0,padx=10,pady=10)
button1.grid(column=2,row=0)
txtNumber1.grid(row=1,column=1,padx=10)
canvas.place(x=250,y=100)
#build window
window.mainloop()