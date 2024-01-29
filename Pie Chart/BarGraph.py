from sqlite3 import Row
import tkinter as tk

#window properties
window = tk.Tk()
window.title("Pie Chart")
window.geometry("1300x700")

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

txtLabel1 = tk.Entry(window)
txtLabel2 = tk.Entry(window)
txtLabel3 = tk.Entry(window)
txtLabel4 = tk.Entry(window)
txtLabel5 = tk.Entry(window)
txtLabel6 = tk.Entry(window)
txtLabel7 = tk.Entry(window)
txtLabel8 = tk.Entry(window)
txtLabel9 = tk.Entry(window)
txtLabel10 = tk.Entry(window)


lblNames = tk.Label(window,text="Labels")
lblNumbers = tk.Label(window,text="Numeric Input")








def hide2():
    txtNumber2.grid_remove()
    txtLabel2.grid_remove()
def unhide2():
    txtNumber2.grid(row=4,column=2)
    txtLabel2.grid(row=4,column=1,padx=10)
def hide3():
    txtNumber3.grid_remove()
    txtLabel3.grid_remove()
def unhide3():
    txtNumber3.grid(row=5,column=2)
    txtLabel3.grid(row=5,column=1,padx=10)
def hide4():
    txtNumber4.grid_remove()
    txtLabel4.grid_remove()
def unhide4():
    txtNumber4.grid(row=6,column=2)
    txtLabel4.grid(row=6,column=1,padx=10)
def hide5():
    txtNumber5.grid_remove()
    txtLabel5.grid_remove()
def unhide5():
    txtNumber5.grid(row=7,column=2)
    txtLabel5.grid(row=7,column=1,padx=10)
def hide6():
    txtNumber6.grid_remove()
    txtLabel6.grid_remove()
def unhide6():
    txtNumber6.grid(row=8,column=2)
    txtLabel6.grid(row=8,column=1,padx=10)
def hide7():
    txtNumber7.grid_remove()
    txtLabel7.grid_remove()
def unhide7():
    txtNumber7.grid(row=9,column=2)
    txtLabel7.grid(row=9,column=1,padx=10)
def hide8():
    txtNumber8.grid_remove()
    txtLabel8.grid_remove()
def unhide8():
    txtNumber8.grid(row=10,column=2)
    txtLabel8.grid(row=10,column=1,padx=10)
def hide9():
    txtNumber9.grid_remove()
    txtLabel9.grid_remove()
def unhide9():
    txtNumber9.grid(row=11,column=2)
    txtLabel9.grid(row=11,column=1,padx=10)

def hide10():
    txtNumber10.grid_remove()
    txtLabel10.grid_remove()
def unhide10():
    txtNumber10.grid(row=12,column=2)
    txtLabel10.grid(row=12,column=1,padx=10)
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
def get():
    Label1 = tk.Label(text=txtLabel1.get)
    Label2 = tk.Label(text=txtLabel2.get)
    Label3 = tk.Label(text=txtLabel3.get)  
    Label4 = tk.Label(text=txtLabel4.get)
    Label5 = tk.Label(text=txtLabel5.get)
    Label6 = tk.Label(text=txtLabel6.get)
    Label7 = tk.Label(text=txtLabel7.get)
    Label8 = tk.Label(text=txtLabel8.get)
    Label9 = tk.Label(text=txtLabel9.get)
    Label10 = tk.Label(text=txtLabel10.get)



def show():
    label.config(text= clicked.get())
    Inputammount = 0
    Inputammount = (clicked.get())
   
    
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
        hide3()
        hide4()
        hide5()
        hide6()
        hide7()
        hide8()
        hide9()
        hide10()
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
Number1 = txtNumber1.get
Number2 = txtNumber2.get
Number3 = txtNumber3.get
Number4 = txtNumber4.get
Number5 = txtNumber5.get
Number6 = txtNumber6.get
Number7 = txtNumber7.get
Number8 = txtNumber8.get
Number9 = txtNumber9.get
Number10 = txtNumber10.get


#canvas
canvas= tk.Canvas(window, width= 800, height= 500, bg="white")
clicked.set( "Number of Inputs" ) 
#buttons
button1 = tk.Button(window,text="set",command=show)
button2 = tk.Button(window,text="Graph!",command=get)
#labels
Label1 = tk.Label
Label2 = tk.Label
Label3 = tk.Label
Label4 = tk.Label
Label5 = tk.Label
Label6 = tk.Label
Label7 = tk.Label
Label8 = tk.Label
Label9 = tk.Label
Label10 = tk.Label




#place gui items






lblNames.grid(row=2,column=1)
lblNumbers.grid(row=2,column=2)

txtLabel1.grid(row=3,column=1,padx=10)
txtNumber1.grid(row=3,column=2)




Label1.place(x=350,y=125)


drop.grid(column=1,row=1,padx=10,pady=10)
button1.grid(column=2,row=1)
button2.grid(column=3,row=1)
canvas.place(x=350,y=125,)
#build window
window.mainloop()