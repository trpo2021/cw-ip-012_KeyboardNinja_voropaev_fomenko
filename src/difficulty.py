from tkinter import *
from random import choices


def dif():
    global root2
    global test_text
    global text_widget
    root2 = Tk()  
    root2.deiconify()  

    text_widget = Text(root2, height=10, width=100,
                       padx=20, pady=20, font=("Arial ", 16))
    text_widget.insert(END, test_text)
    text_widget.configure(state="disabled")
    text_widget.tag_config("correct", background="green", foreground="white")
    text_widget.tag_config("wrong", background="red", foreground="white")


    text_widget.focus()
    text_widget.pack()

    message = Label(root2,
                    text="Start typing",
                    font=("Arial ", 24))
    message.pack()
    return root2
