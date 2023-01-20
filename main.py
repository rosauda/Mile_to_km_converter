import tkinter


# Creating window
window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=500, height=500)

# Creating label
my_label = tkinter.Label(text="Hello I am Rodrigo Sauda, how are you?", font=("Arial", 12, "bold"))
my_label.pack()


window.mainloop()

