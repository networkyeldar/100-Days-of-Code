from tkinter import *

window = Tk()
window.title("My app")
window.minsize(300,300)
window.config(padx=20, pady=20)

my_label = Label(text="miles", font=("Arial", 10, "bold"))
my_label.grid(column=2, row = 0)

my_label2 = Label(text="is equal to", font=("Arial", 10, "bold"))
my_label2.grid(column=0, row = 1)

my_label3 = Label(text="0", font=("Arial", 10, "bold"))
my_label3.grid(column=1, row = 1)

my_label4 = Label(text="km", font=("Arial", 10, "bold"))
my_label4.grid(column=2, row = 1)
def button_clicked():
    miles_amount = int(my_input.get())
    km_amount = round(miles_amount *1.6)
    my_label3.config(text=km_amount,font=("Arial", 10, "bold"))

my_button = Button(text="Calculate", command=button_clicked)
my_button.grid(column = 1, row = 2)

my_input = Entry(width=10)
my_input.grid(column = 1, row = 0)


window.mainloop()
