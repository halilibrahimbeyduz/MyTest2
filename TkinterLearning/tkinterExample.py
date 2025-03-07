from tkinter import *

window = Tk()
window.title("Example")
window.minsize(width=600, height=600)
window.config(padx=20, pady=20)

label = Label(text="this is a label")
label.config(bg="black")
label.config(fg="white")
label.config(padx=10, pady=10)
label.pack()

def button_clicked():
    print(my_text.get(1.0,END))

button = Button(text="button", command=button_clicked)
button.config(padx=10, pady=10)
button.pack()

my_text = Text(width=30, height=5)
my_text.focus()
my_text.pack()

#LİSTBOX

def listbox_selected(event):
    print(my_listbox.get(my_listbox.curselection())) # üstüne tıklandığında seçecek fonksiyon

my_listbox = Listbox()
name_list = ["Atil","ABC","Kjs","SSKDF"]

for i in range(len(name_list)): # index numarasını yazdırmak için kullanırız
    my_listbox.insert(i,name_list[i]) #LİSTEDEKİ İSİMLERİ YAZDIRMAYA YARAR

my_listbox.bind('<<ListboxSelect>>', listbox_selected) # yukarda yazılan fonksiyonu bağlamak için yazdık

my_listbox.pack()


window.mainloop()