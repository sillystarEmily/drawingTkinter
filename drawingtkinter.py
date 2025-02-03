import tkinter as tk 
from tkinter import*

def inputnumbers():
    Num1 = float(txtNum1.get())
    Num2 = float(txtNum2.get())
    Num3 = float(txtNum3.get())
    Num4 = float(txtNum4.get())
    canvas.create_rectangle(10,5,110,Num1, outline = "grey", fill = "#C4D7D1") 
    canvas.create_rectangle(120,5,220,Num2, outline = "grey", fill = "light pink")
    canvas.create_rectangle(230,5,330,Num3, outline = "grey", fill = "light blue")
    canvas.create_rectangle(340,5,440,Num4, outline = "grey", fill = "#CBC3E3")

        
def Clear():
    txtNum1.delete(0,tk.END)
    txtNum2.delete(0,tk.END)
    txtNum3.delete(0,tk.END)
    txtNum4.delete(0,tk.END)
    canvas.delete("all")


##### builds the window ######
window = tk.Tk() #creates the window 
window.title("Bar Graph Data") #the name/title      
window.geometry("600x600")
window.resizable(False,False) #make the window not be able to move
canvas=Canvas(window,width="500",height="500")

##### Adding GUI elements #####
lblparagraph = tk.Label(window, text = "This program will take numbers and make a bar graph")
lblOne = tk.Label(window, text = "Enter 1st number: ")
lblTwo = tk.Label(window, text = "Enter 2nd Number: ")
lblThree = tk.Label(window, text = "Enter 3rd number: ")
lblFour = tk.Label(window, text = "Enter 4th number: ")

txtNum1 = tk.Entry(window)
txtNum2 = tk.Entry(window)
txtNum3 = tk.Entry(window)
txtNum4 = tk.Entry(window)

btnClear = tk.Button(window, text = "Clear", command = Clear) 
btnEnter = tk.Button(window, text = "Enter", command = inputnumbers)


##### building the grid #####

lblparagraph.grid(row=0, column=0,padx=10, pady=10)
lblOne.grid(row=1, column=0,padx=10, pady=10)
lblTwo.grid(row=2, column=0,padx=10, pady=10)
lblThree.grid(row=3, column=0,padx=10, pady=10)
lblFour.grid(row=4, column=0,padx=10, pady=10)

txtNum1.grid(row=1, column=2,padx=10, pady=10)
txtNum2.grid(row=2, column=2,padx=10, pady=10)
txtNum3.grid(row=3, column=2,padx=10, pady=10)
txtNum4.grid(row=4, column=2,padx=10, pady=10)

btnEnter.grid(row=5,column=0,padx=10,pady=10)
btnClear.grid(row=6, column=0,padx=10, pady=10)

canvas.grid(row=10, column=0, columnspan=5, padx=10, pady=10)

#draw2.grid(row=5, column= 0, columnspan=5, padx=10, pady=10)
##### runs the app ######
window.mainloop()

