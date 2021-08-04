from tkinter import *
from PIL import ImageTk, Image
import sys
root = Tk()
top = Toplevel()
top.geometry("600x400")
top.title("Клавиатурный тренажер")
var = IntVar()
Radiobutton(top, text='Легкая', variable=var, value=0).pack()
Radiobutton(top, text='Нормальная', variable=var, value=1).pack()
Radiobutton(top, text='Сложная', variable=var, value=2).pack()
button1 = Button(top, text="Играть").pack()
button2 = Button(top, text="Выйти", command=lambda: command2()).pack()
img = ImageTk.PhotoImage(Image.open("images.jpg"))
panel = Label(top, image=img)
panel.pack(side="bottom", fill="both", expand="yes")
label5 = Label(top, text="Топ времени игроков:", justify=LEFT, font='Times 10')
label5.place(relx=.1, rely=.1)


def start_app():
    root.withdraw()
    return root


def command2():
    top.destroy()
    root.destroy()
    sys.exit()


if __name__ == '__main__':
    app = start_app()
    app.mainloop()
