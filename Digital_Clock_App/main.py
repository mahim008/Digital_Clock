from tkinter import *   # importing modules
from time import strftime

window = Tk()   # creating clock window
window.title("Digital Computer Clock")

# created function to display time
def show_time():
    string = strftime("%H:%M:%S %p")
    lbl.config(text=string)
    lbl.after(1000, show_time)

# styling the UI
lbl = Label(window, font=("times new romans", 150, "bold"), bg="white", fg="red")

# fixing positions
lbl.pack(anchor="center", fill="both", expand=1)

show_time()    # time function calling
mainloop()    # running the main application
