from tkinter import *
from tkinter import messagebox

from linked_list import *

my_list = LinkedList()


def rgb(rgb):
    return "#%02x%02x%02x" % rgb


def add_to_the_list():
    text = entry_to_list.get()
    text = text.split(' ')
    entry_to_list.delete(0, 'end')
    for el in text:
        try:
            my_list.insert(int(el))
        except ValueError:
            messagebox.showerror(title='Error', message='Please enter only numbers')

    label_text_list.set(f"Curr list: {my_list.traverse()}")


def get_element():
    text = entry_m.get()
    entry_m.delete(0, 'end')

    try:
        el = my_list.return_M(int(text))
        label_text_res.set(f"Element value: {el}")
    except ValueError as e:
        if "invalid literal for int()" in str(e):
            messagebox.showerror(title='Error', message='Please enter only numbers')
        else:
            messagebox.showerror(title='Error', message="Please enter a valid M-number. Тhe number cannot be negative or greater than the length of the list - 1 ")


def clear_list():
    global my_list
    my_list = LinkedList()
    label_text_list.set("Curr list: ")



#Create Window:
window = Tk()
window.title("My Application")
window.geometry("600x400")
window.config(bg=rgb((255, 178, 102)))
window.resizable(False, False)
positionRight = int(window.winfo_screenwidth() / 2 - 600 / 2)
positionDown = int(window.winfo_screenheight() / 2 - 400 / 2)

# Positions the window in the center of the page.
window.geometry("+{}+{}".format(positionRight, positionDown))

#adding input fields
entry_to_list = Entry(window)
entry_to_list.pack()
entry_to_list.place(x=230, y=80, width=150, height=20)

entry_m = Entry(window)
entry_m.pack()
entry_m.place(x=230, y=110, width=150, height=20)


#adding buttons
button_add = Button(window,  text="Add to the list", bg=rgb((255, 68, 0)), fg='white', command=add_to_the_list)
button_add.pack()
button_add.place(x=400, y=80, height=20)

button_get_element = Button(window,  text="Get element", bg=rgb((255, 68, 0)), fg='white', command=get_element)
button_get_element.pack()
button_get_element.place(x=400, y=110, height=20)

button_clear = Button(window,  text="Clear list", bg=rgb((255, 68, 0)), fg='white', command=clear_list)
button_clear.pack()
button_clear.place(x=540, y=140, height=20)

#adding labels
label_text_res = StringVar()
label_text_res.set("Element value: ")
result = Label(window, bg=rgb((122,122,122)), fg='white', height=30, width=130, textvariable=label_text_res)
result.pack()
result.place(x=230, y=140, width=150, height=20)

label_text_list = StringVar()
label_text_list.set("Curr list: ")
result = Label(window, bg=rgb((122,122,122)), fg='white', height=30, width=130, textvariable=label_text_list)
result.pack()
result.place(x=0, y=170, width=600, height=20)


window.mainloop()
