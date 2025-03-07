import tkinter

window = tkinter.Tk()
window.title("Python Tkinter")
window.minsize(width=650, height=300)

#label
my_label = tkinter.Label(text="this is a label", font=('Arial', 10, "bold"))
#my_label.config(bg="black", fg="white")
my_label.pack(side="left")

def click_button():
    user_entry = my_entry.get()
    print(user_entry)

#   button
my_button = tkinter.Button(text="this is a button",command=click_button )
my_button.place(x=100,y=100)

#   entry
my_entry = tkinter.Entry(width=20)
my_entry.pack(side="bottom")

window.mainloop()