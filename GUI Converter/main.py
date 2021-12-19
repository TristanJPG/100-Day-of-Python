from tkinter import *


def miles_to_km():
    miles = float(milesInput.get())
    km = miles * 1.609
    kiloLabel.config(text=f"{km}")


window = Tk()
window.title("My Program!")
window.config(padx=20, pady=20)
FONT = ("Arial", 24, "bold")

milesInput = Entry()
milesInput.grid(column=1, row=0)

mileLabel = Label(text="Miles", font=FONT)
mileLabel.grid(column=2, row=0)

equalToo = Label(text="Is Equal To:", font=FONT)
equalToo.grid(column=0, row=1)

kiloLabel = Label(text="0", font=FONT)
kiloLabel.grid(column=1, row=1)

kmLabel = Label(text="km", font=FONT)
kmLabel.grid(column=2, row=2)

calc = Button(text="Calculate!", font=FONT, command=miles_to_km)
calc.grid(column=1, row=2)
window.mainloop()
