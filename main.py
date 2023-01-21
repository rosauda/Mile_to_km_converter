from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=5, pady=5)


def button_clicked():
    miles_input = float(user_input.get())
    km_answer = round((miles_input * 1.609), 2)

    result.config(text=f"{km_answer}")


# Entry
user_input = Entry(width=10)
print(user_input.get())
user_input.grid(column=1, row=0)

# Label
miles_label = Label(text="Miles", font=("Arial", 10, "bold"))
miles_label.grid(column=2, row=0)
miles_label.config(padx=5, pady=5)

# Label
is_equal_to = Label(text="Is equal to:", font=("Arial", 10, "bold"))
is_equal_to.grid(row=2, column=0)
is_equal_to.config(padx=5, pady=5)

# Label
result = Label(text="", font=("Arial", 10, "bold"))
result.grid(row=2, column=1)
result.config(padx=5, pady=5)

# Label
km_label = Label(text="Km", font=("Arial", 10, "bold"))
km_label.grid(row=2, column=2)
km_label.config(padx=5, pady=5)

# Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=3)

window.mainloop()
