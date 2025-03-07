from tkinter import *

window = Tk()
window.title("BMI Quiz")
window.minsize(width=300, height=250)

# label

my_label = Label(text="Enter Your Weight (kg)", font=('Arial',10,'normal'))
my_label.config(padx=10,pady=10)
my_label.pack()

# entry

my_entry = Entry(width=20)

my_entry.pack()

# label2

my_label2 = Label(text="Enter Your Height(cm)",font=('Arial',10,'normal'))
my_label2.config(padx=10,pady=10)
my_label2.pack()

# entry

my_entry2 = Entry(width=20)
my_entry2.pack()


# button

def button_selected():
    print(my_entry.get())

    try:
        boy = float(my_entry2.get()) * float(my_entry2.get())
        kilo = int(my_entry.get()) / float(boy)

        #label_value.config(text=kilo)
        if kilo < 18.5:
            print(label_value.config(text="zayıf"))
        elif 18.5 < kilo < 24.9:
            print(label_value.config(text="sağlıklı"))
        elif 25 < kilo < 29.9:
            print(label_value.config(text="şişman"))
        elif 30 < kilo < 39.9:
            print(label_value.config(text="obez"))
        else:
            print(label_value.config(text="şişkosun"))
    except ValueError:
        print(label_value.config(text="please number"))

def delete_select():
    my_entry.delete(0,END)
    my_entry2.delete(0, END)
    my_entry.focus()

my_button = Button(text="Calculate", command=button_selected)
my_button.pack()

my_button2 = Button(text="Delete", command=delete_select)
my_button2.pack()

label_value = Label(text="DEĞER")
label_value.config(pady=20)
label_value.pack()

window.mainloop()