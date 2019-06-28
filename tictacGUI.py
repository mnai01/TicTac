from tkinter import *

root = Tk()
root.title("Tic Tac Toe")

button = [' ' for x in range(10)]

click = True


def clearBoard(button):
    for i in range(1, 10):
        button[i]["text"] = " "
        print("cleared", i)


def isFreeSpace(position):
    return button[position]["text"] == ' '


def isBoardFull(button):
    for i in range(1, 10):
        if button[i]["text"].count(' ') == 1:
            print("is full")
            return True
        else:
            print("is not full")
            return False


o = Radiobutton(root, text='O', value=2, command=(lambda: radClkO()))
o.grid(row=0, column=2)

x = Radiobutton(root, text='X', value=1, command=(lambda: radClkX()))
x.grid(row=0, column=1)


def radClkX():
    global click
    click = True
    print(click)


def radClkO():
    global click
    click = False
    print(click)


clearButton = Button(root, text="Clear", font=(
    'Times 12 bold'), height=1, width=4, command=(lambda: clearBoard(button)))
clearButton.grid(row=0, column=3)

button[0] = " "

button[1] = Button(root, text="1", font=('Times 20 bold'),
                   height=4, width=8, command=(lambda: btnClick(1)))
button[1].grid(row=1, column=1)

button[2] = Button(root, text="2", font=('Times 20 bold'),
                   height=4, width=8, command=(lambda: btnClick(2)))
button[2].grid(row=1, column=2)

button[3] = Button(root, text="3", font=('Times 20 bold'),
                   height=4, width=8, command=(lambda: btnClick(3)))
button[3].grid(row=1, column=3)

button[4] = Button(root, text="4", font=('Times 20 bold'),
                   height=4, width=8, command=(lambda: btnClick(4)))
button[4].grid(row=2, column=1)

button[5] = Button(root, text="5", font=('Times 20 bold'),
                   height=4, width=8, command=(lambda: btnClick(5)))
button[5].grid(row=2, column=2)

button[6] = Button(root, text="6", font=('Times 20 bold'),
                   height=4, width=8, command=(lambda: btnClick(6)))
button[6].grid(row=2, column=3)

button[7] = Button(root, text="7", font=('Times 20 bold'),
                   height=4, width=8, command=(lambda: btnClick(7)))
button[7].grid(row=3, column=1)

button[8] = Button(root, text="8", font=('Times 20 bold'),
                   height=4, width=8, command=(lambda: btnClick(8)))
button[8].grid(row=3, column=2)

button[9] = Button(root, text="9", font=('Times 20 bold'),
                   height=4, width=8, command=(lambda: btnClick(9)))
button[9].grid(row=3, column=3)


def btnClick(id):
    global click

    if (button[id]["text"] == ' ' and click == True):
        button[id]["text"] = "x"
        print("clicked")
        checkWinner('x')
        click = False

    elif (button[id]["text"] == ' ' and click == False):
        button[id]["text"] = "o"
        print("clicked")
        checkWinner('o')
        click = True


def checkWinner(letter):
    # checks all 8 possible solutions to see if X or O is the winner
    if ((button[1]['text'] == letter and button[2]['text'] == letter and button[3]['text'] == letter) or
        (button[4]['text'] == letter and button[5]['text'] == letter and button[6]['text'] == letter) or
        (button[7]['text'] == letter and button[8]['text'] == letter and button[9]['text'] == letter) or

        (button[1]['text'] == letter and button[4]['text'] == letter and button[7]['text'] == letter) or
        (button[2]['text'] == letter and button[5]['text'] == letter and button[8]['text'] == letter) or
        (button[3]['text'] == letter and button[6]['text'] == letter and button[9]['text'] == letter) or

        (button[1]['text'] == letter and button[5]['text'] == letter and button[9]['text'] == letter) or
            (button[3]['text'] == letter and button[5]['text'] == letter and button[7]['text'] == letter)):
        print(letter + "is the winner")
        return True
    else:
        return False


root.mainloop()
