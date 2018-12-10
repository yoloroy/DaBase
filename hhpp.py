from tkinter import *
from tkinter import messagebox
from hashlib import md5
import numpy


HEIGHT = 700
WIDTH = 1000
matrix = []
num_points = 0


def load_data():
    global data
    global points
    points = []
    data = numpy.loadtxt('db.txt', dtype='int')

    for i in range(len(data)):
        points.append((WIDTH/(len(data)-1)*i, (10-data[i])*HEIGHT/10))


def render_point(x, y, name):
    c.create_text(x, y,
                  text=str(name),
                  font="Arial {}".format(16),
                  fill='orange')


def render_points():
    for i in range(len(data)):
        render_point(points[i][0], points[i][1], data[i])


def render_graph(x1, y1, x2, y2):
    c.create_line(x1, y1, x2, y2, fill="white")#, arrow=LAST)


def render_graphs():
    for i in range(1, len(data)):
        render_graph(*points[i % len(data)-1], *points[i % len(data)])


def on_closing():
    if messagebox.askokcancel("Quit", "do u want to quit?"):
        root.destroy()


def check():
    answer = mb.askyesno(title="Вопрос", message="Перенести данные?")
    if answer == True:
        s = entry.get()
        entry.delete(0, END)
        label['text'] = s


def create_desk():
    global root
    global c
    global entry
    root = Tk()
    root.title("Graphs visualisation")
    root.protocol("WM_DELETE_WINDOW", on_closing)

    #entry = Entry()
    #entry.pack(pady=10)
    #Button(text='Передать', command=check).pack()

    c = Canvas(root, width=WIDTH,
               height=HEIGHT,
               bg="black")
    c.bind('<Button-1>', updateQue)
    c.pack()


def updateQue(event):
    global data
    data_new = numpy.loadtxt('db.txt', dtype='int')
    if md5(str(data).encode()) != md5(str(data_new).encode()):
        c.create_polygon(0, 0,
                         0, HEIGHT,
                         WIDTH, HEIGHT,
                         WIDTH, 0, fill = "#000",
                                outline = '#000')
        load_data()
        c.create_line(0, HEIGHT / 10 * (10 - sum(data) / len(data)),
                      WIDTH, HEIGHT / 10 * (10 - sum(data) / len(data)), fill="grey")
        print(sum(data) / len(data))
        render_graphs()
        render_points()
        c.update()


data = "Data base"
create_desk()

updateQue(None)

root.mainloop()
