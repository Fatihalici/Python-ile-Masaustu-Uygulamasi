import tkinter
import sudokuscreen
import solver
import threading
from threading import Thread
import sys
from tkinter import *

global f
sys.setrecursionlimit(10000)
f = open('steps.txt', 'w')
top = tkinter.Tk()
canvas = tkinter.Canvas(
    top,
    bg="white",
    height=720,
    width=1224
)


# sudoku şeklini çizdirme
def drawlines(x, y):
    for i in range(10):
        color = "blue" if i % 3 == 0 else "gray"
        color1 = "#181D31"
        # satırlar
        x0 = x
        y0 = y + i * 25
        x1 = x + 225
        y1 = y + i * 25

        if i % 3 == 0:
            canvas.create_line(x0, y0, x1, y1, width=2, fill=color)
        canvas.create_line(x0, y0, x1, y1, fill=color)

        # sütunlar

        x0 = x + i * 25
        y0 = y
        x1 = x + i * 25
        y1 = y + 225
        if i % 3 == 0:
            canvas.create_line(x0, y0, x1, y1, width=2, fill=color)
        canvas.create_line(x0, y0, x1, y1, fill=color)


# grafik şeklini cizdirme
def draw_graphic():
    color = "black"
    # yatay
    canvas.create_line(700, 500, 1215, 500, width=1, fill=color)
    # dikey
    canvas.create_line(700, 100, 700, 500, width=1, fill=color)


# grafik cizdirme
drawlines(50, 100)
drawlines(350, 100)
drawlines(50, 400)
drawlines(350, 400)
drawlines(200, 250)
draw_graphic()
print(sudokuscreen.sudoku)


# sudoku txt sayıları ekrana bastırma
def drawsudoku(x, y):
    # 1. 2. 3. sudoku bloğu satırları
    for i in range(len(sudokuscreen.sudoku)):
        x0 = 60
        y0 = y + 92
        x1 = 140
        y1 = y + 92

        y0 += i * 25
        y1 += i * 25

        for j in range(len(sudokuscreen.sudoku[i])):

            if len(sudokuscreen.sudoku[i]) == 18:

                if sudokuscreen.sudoku[i][j] != '*' and j < 9:
                    canvas.create_text(x0 + j * 25, y0, text=sudokuscreen.sudoku[i][j], fill="black",
                                       font=('Helvetica 15 bold', 15))


                elif sudokuscreen.sudoku[i][j] != '*' and j >= 9:
                    canvas.create_text(x1 + 25 * j, y1, text=sudokuscreen.sudoku[i][j], fill="black",
                                       font=('Helvetica 15 bold', 15))

            if len(sudokuscreen.sudoku[i]) == 21:

                if sudokuscreen.sudoku[i][j] != '*':
                    canvas.create_text(x0 + j * 25, y0, text=sudokuscreen.sudoku[i][j], fill="black",
                                       font=('Helvetica 15 bold', 15))

            if len(sudokuscreen.sudoku[i]) == 9:

                if sudokuscreen.sudoku[i][j] != '*':
                    canvas.create_text(x0 + j * 25 + 150, y0, text=sudokuscreen.sudoku[i][j], fill="black",
                                       font=('Helvetica 15 bold', 15))


canvas.pack()

threads5 = [
    Thread(target=solver.solvesudoku_lefttop2, args=(f,)),
    Thread(target=solver.solvesudoku_righttop2, args=(f,)),
    Thread(target=solver.solvesudoku_mid2, args=(f,)),
    Thread(target=solver.solvesudoku_leftbottom2, args=(f,)),
    Thread(target=solver.solvesudoku_rightbottom2, args=(f,))
]
threads10 = [
    Thread(target=solver.solvesudoku_lefttop2, args=(f,)),
    Thread(target=solver.solvesudoku_righttop2, args=(f,)),
    Thread(target=solver.solvesudoku_mid, args=(f,)),
    Thread(target=solver.solvesudoku_mid2, args=(f,)),
    Thread(target=solver.solvesudoku_leftbottom, args=(f,)),
    Thread(target=solver.solvesudoku_leftbottom2, args=(f,)),
    Thread(target=solver.solvesudoku_rightbottom2, args=(f,)),
    Thread(target=solver.solvesudoku_lefttop, args=(f,)),
    Thread(target=solver.solvesudoku_righttop, args=(f,)),
    Thread(target=solver.solvesudoku_rightbottom, args=(f,))
]

t = threading.Thread(target=drawsudoku, args=(5, 20))


def solve_draw_thread5():
    global boxcount1
    global f
    f = open('steps.txt', 'w')
    for thread in threads5:
        thread.start()
    for thread in threads5:
        thread.join()
    f.close()
    for i in range(247):
        canvas.create_line(700 + solver.timecount5[i] * 1.2, 500 - solver.boxcount[i],
                           700 + solver.timecount5[i + 1] * 1.2,
                           500 - solver.boxcount[i + 1], width=1, fill="red")
    Thread(target=drawsudoku, args=(5, 20)).start()


def solve_draw_thread10():
    global f
    f = open('steps.txt', 'w')
    for i in range(len(threads10)):
        threads10[i].start()
    for thread in threads10:
        thread.join()
    f.close()
    for i in range(247):
        canvas.create_line(700 + solver.timecount10[i] * 1.1, 500 - solver.boxcount[i],
                           700 + solver.timecount10[i + 1] * 1.1,
                           500 - solver.boxcount[i + 1], width=1, fill="green")
    Thread(target=drawsudoku, args=(5, 20)).start()


img = PhotoImage(width=1, height=1)
Button(top, text="5 Thread İle Çöz", width=120, height=25, image=img, compound='c',
       bg="#C0C0C0", activebackground="#D8D8D8", font=("Arial", 11), borderwidth=0,
       cursor="hand2", bd=0, relief="sunken", command=solve_draw_thread5).place(x=80, y=650)

Button(top, text="10 Thread İle Çöz", width=120, height=25, image=img, compound='c',
       bg="#C0C0C0", activebackground="#D8D8D8", font=("Arial", 11), borderwidth=0,
       cursor="hand2", bd=0, relief="sunken", command=solve_draw_thread10).place(x=420, y=650)

t.start()

top.mainloop()
