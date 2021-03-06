from tkinter import *
from PIL import ImageTk, Image
import sys
import os
if os.environ.get('DISPLAY', '') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')
from src.list_pop import list_pip
import src.difficulty
root = Tk()  
top = Toplevel() 
top.geometry("600x400")
top.title("Клавиатурный тренажер")  
var = IntVar()
Radiobutton(top, text='Легкая', variable=var, value=0).pack()
Radiobutton(top, text='Нормальная', variable=var, value=1).pack()
Radiobutton(top, text='Сложная', variable=var, value=2).pack()
button1 = Button(top, text="Играть", command=lambda: command()).pack()
button2 = Button(top, text="Выйти", command=lambda: command2()).pack()
img = ImageTk.PhotoImage(Image.open("images.jpg"))
panel = Label(top, image=img)
panel.pack(side="bottom", fill="both", expand="yes")
label5 = Label(top, text="Топ времени игроков:", justify=LEFT, font='Times 10')
label5.place(relx=.1, rely=.1)
label2 = Label(top, text=list_pip(1), justify=LEFT, font='Times 10')
label2.place(relx=.1, rely=.2)
label3 = Label(top, text=list_pip(3), justify=LEFT, font='Times 10')
label3.place(relx=.1, rely=.3)
label4 = Label(top, text=list_pip(5), justify=LEFT, font='Times 10')
label4.place(relx=.1, rely=.4)


def start_app():
    root.withdraw() 
    return root


def command2():
    top.destroy() 
    root.destroy()
    sys.exit()
    
    
def command():

    with open("words.txt", "r"):
        test_words1 = src.difficulty.get_words(var.get() + 3)
        app2 = src.difficulty.dif(test_words1)
        app2.mainloop()
    return True


if __name__ == '__main__':
    app = start_app()
    app.mainloop()
