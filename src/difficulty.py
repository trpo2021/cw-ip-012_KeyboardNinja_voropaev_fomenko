import time
from random import choices
from tkinter import *
pos = 0
b = 0
mistakes = 0
correct_presses = 0


def get_words(word_num):
    with open("words.txt", "r") as words:
        return choices(list(words), k=word_num)


def key_type(e):
    if e.keycode != 16:
        global pos, b, mistakes, correct_presses
        if test_text[pos] != e.char:
            text_widget.tag_add("wrong", f"1.{b}")
            mistakes += 1
        if test_text[pos] == e.char:
            text_widget.tag_add("correct", f"1.{b}")
            correct_presses += 1
        b += 1
        pos += 1

        if pos == len(test_text):
            rav = time.time() - start_time
            label1 = Label(root2, text="NICE!", fg="#eee", bg="#957")
            label2 = Label(root2, text="TIME:", fg="#eee", bg="#957")
            label0 = Label(root2, text=rav, fg="#eee", bg="#957")

            label1.pack()
            label2.pack()
            label0.pack()
            with open("LeaderBoard.txt", "a") as board:
                board.writelines(str(rav) + "\n")
            with open("LeaderBoard.txt", "r") as board:
                lines = board.readlines()
                lines.sort()
                open("sort.txt", "w").write("\n".join(lines))
def dif(test_words1):
    global root2
    global start_time
    global test_text
    global text_widget
    root2 = Tk()  
    root2.deiconify()  
    start_time = time.time()
    final_word_list1 = []

   
    for i in range(len(test_words1)):
        final_word_list1.append(test_words1[i].strip())
        test_text = " ".join(final_word_list1)
        

    text_widget = Text(root2, height=10, width=100,
                       padx=20, pady=20, font=("Arial ", 16))
    text_widget.insert(END, test_text)
    text_widget.configure(state="disabled")
    text_widget.tag_config("correct", background="green", foreground="white")
    text_widget.tag_config("wrong", background="red", foreground="white")

    text_widget.bind("<KeyPress>", key_type)
    text_widget.focus()
    text_widget.pack()

    message = Label(root2,
                    text="Start typing",
                    font=("Arial ", 24))
    message.pack()
    return root2
