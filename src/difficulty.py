from tkinter import *
<<<<<<< HEAD

def get_words(word_num):
    with open("words.txt", "r") as words:
        return choices(list(words), k=word_num)
        
=======
from random import choices


>>>>>>> d3732648a00aa3ec58676ee672584064606b9e36
def dif():
    global root2
    global test_text
    global text_widget
    root2 = Tk()  
<<<<<<< HEAD
    root2.deiconify() 
=======
    root2.deiconify()  
>>>>>>> d3732648a00aa3ec58676ee672584064606b9e36

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
