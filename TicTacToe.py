from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Tic-Tac-Toe')

Clicked = True
count = 0
Winner = True

def b_click(b):
    global Clicked, count
    
    if b["text"] == " " and Clicked == True:
        b["text"] = "X"
        Clicked = False
        count += 1 
        check_ifWon()

    elif b["text"] == " " and Clicked == False:
        b["text"] = "O"
        Clicked = True
        count += 1
        check_ifWon()
    else: 
        messagebox.showerror("Tic Tac Toe", "BOX IS ALREADY BEEN SELECTED")

b1 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b1))
b2 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b2))
b3 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b3))

b4 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b4))
b5 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b5))
b6 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b6))

b7 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b7))
b8 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b8))
b9 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b9))

b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)

b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)

b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)


def disable_all_buttons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

def check_ifWon():
    global Winner
    Winner = False

    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        Winner = True
        messagebox.showinfo("X_WON", "X WINS")
        disable_all_buttons()

    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        Winner = True
        messagebox.showinfo("X_WON", "X WINS")
        disable_all_buttons()

    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        Winner = True
        messagebox.showinfo("X_WON", "X WINS")
        disable_all_buttons()

    elif b1["text"] == "X" and b3["text"] == "X" and b7["text"] == "X":
        b1.config(bg="red")
        b3.config(bg="red")
        b7.config(bg="red")
        Winner = True
        messagebox.showinfo("X_WON", "X WINS")
        disable_all_buttons()

    elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
        Winner = True
        messagebox.showinfo("X_WON", "X WINS")
        disable_all_buttons()

    elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
        b3.config(bg="red")
        b6.config(bg="red")
        b9.config(bg="red")
        Winner = True
        messagebox.showinfo("X_WON", "X WINS")
        disable_all_buttons()

    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        Winner = True
        messagebox.showinfo("X_WON", "X WINS")
        disable_all_buttons()

    elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
        b3.config(bg="red")
        b5.config(bg="red")
        b7.config(bg="red")
        Winner = True
        messagebox.showinfo("X_WON", "X WINS")
        disable_all_buttons()

    #Check for O

    elif b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
        b1.config(bg="green")
        b2.config(bg="green")
        b3.config(bg="green")
        Winner = True
        messagebox.showinfo("O_WON", "O WINS")
        disable_all_buttons()

    elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
        b4.config(bg="green")
        b5.config(bg="green")
        b6.config(bg="green")
        Winner = True
        messagebox.showinfo("O_WON", "O WINS")
        disable_all_buttons()

    elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
        b7.config(bg="green")
        b8.config(bg="green")
        b9.config(bg="green")
        Winner = True
        messagebox.showinfo("O_WON", "O WINS")
        disable_all_buttons()

    elif b1["text"] == "O" and b3["text"] == "O" and b7["text"] == "O":
        b1.config(bg="green")
        b3.config(bg="green")
        b7.config(bg="green")
        Winner = True
        messagebox.showinfo("O_WON", "O WINS")
        disable_all_buttons()

    elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
        b2.config(bg="green")
        b5.config(bg="green")
        b8.config(bg="green")
        Winner = True
        messagebox.showinfo("O_WON", "O WINS")
        disable_all_buttons()

    elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
        b3.config(bg="green")
        b6.config(bg="green")
        b9.config(bg="green")
        Winner = True
        messagebox.showinfo("O_WON", "O WINS")
        disable_all_buttons()

    elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
        b1.config(bg="green")
        b5.config(bg="green")
        b9.config(bg="green")
        Winner = True
        messagebox.showinfo("O_WON", "O WINS")
        disable_all_buttons()

    elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
        b3.config(bg="green")
        b5.config(bg="green")
        b7.config(bg="green")
        Winner = True
        messagebox.showinfo("O_WON", "O WINS")
        disable_all_buttons()
    
    if count == 9 and Winner == False:
        messagebox.showinfo("Tic Tac Toe", "NO ONE WINS")
        disable_all_buttons()

def reset():

    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global Clicked, count
    Clicked = True
    count = 0

    b1 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b1))
    b2 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b2))
    b3 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b3))

    b4 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b4))
    b5 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b5))
    b6 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b6))

    b7 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b7))
    b8 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b8))
    b9 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b9))

    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)

    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)

    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)

my_menu = Menu(root)
root.config(menu=my_menu)

options_menu = Menu(my_menu, tearoff = False)
my_menu.add_cascade(label="Options", menu =options_menu)

options_menu.add_command(label="Reset Game", command=reset)
reset()

root.mainloop()