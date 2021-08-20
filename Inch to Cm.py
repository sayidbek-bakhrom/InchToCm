from tkinter import *

# setting up screen for project
window = Tk()
window.title("Converter from Inch to Cm")
window.config(padx=40, pady=40)

# making functions for calculations
def change_to_cm():
    inch = float(inch_input.get())
    cm = inch * 2.54
    answer_a.config(text=f"{cm}cm")

def change_to_inch():
    cm = float(cm_input.get())
    inch = round(cm * 0.3937, 4)
    # rounding calculations until 4 decimal digits
    answer_b.config(text=f"{inch}inch")


# some texts that show user which is a cm entry and which is an inch entry below
label_a = Label(text="Inch")
label_a.grid(row=0, column=1)

label_b = Label(text="Cm")
label_b.grid(row=0, column=2)


# inputs by the user
inch_input = Entry(width=10)
inch_input.grid(row=1, column=1)

cm_input = Entry(width=10)
cm_input.grid(row=1, column=2)


# buttons inch/cm
button_a = Button(text="Change to cm", command=change_to_cm)
button_a.grid(row=2, column=1)

button_b = Button(text="Change to inch", command=change_to_inch)
button_b.grid(row=2, column=2)


# results of converting of inches and cms
answer_a = Label(text="0")
answer_a.grid(row=3, column=1)

answer_b = Label(text="0")
answer_b.grid(row=3, column=2)

# TODO give some color to make graphics better. :)
window.mainloop()

