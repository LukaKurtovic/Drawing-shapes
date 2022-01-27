import tkinter as Tk
from tkinter import *
from tkinter import filedialog as fd



class GrafObj:

    def __init__(self, boja, startX, startY):
        self.boja = boja
        self.startX = startX
        self.startY = startY

    def GetColor(self):
        return self.boja

    def SetColor(self, boja):
        self.boja = boja

    def draw(self, C):
        pass


class Linija(GrafObj):

    def __init__(self, boja, startX, startY, endX, endY):
        self.boja = boja
        self.startX = startX
        self.startY = startY
        self.endX = endX
        self.endY = endY

    def draw(self, C):
        C.create_line((self.startX, self.startY, self.endX, self.endY), fill=self.boja)


class Trokut(Linija):

    def __init__(self, boja, point1X, point1Y, point2X, point2Y, point3X, point3Y):
        self.boja = boja
        self.point1X = point1X
        self.point1Y = point1Y
        self.point2X = point2X
        self.point2Y = point2Y
        self.point3X = point3X
        self.point3Y = point3Y

    def draw(self, C):
        C.create_polygon((self.point1X, self.point1Y, self.point2X, self.point2Y, self.point3X, self.point3Y),
                         outline=self.boja, fill = 'grey')


class Pravokutnik(GrafObj):

    def __init__(self, boja, pointX, pointY, height, width):
        self.boja = boja
        self.pointX = pointX
        self.pointY = pointY
        self.height = height
        self.width = width

    def draw(self, C):
        C.create_rectangle((self.pointX, self.pointY, self.pointX + self.width, 
        self.pointY + self.height), outline=self.boja)


class Krug(GrafObj):

    def __init__(self, boja, point1X, point1Y, radius):
        self.boja = boja
        self.point1X = point1X
        self.point1Y = point1Y
        self.radius = radius

    def draw(self, C):
        C.create_oval((self.point1X - self.radius, self.point1Y - self.radius, self.point1X + self.radius, self.point1Y + self.radius), outline=self.boja)


class Elipsa(Krug):

    def __init__(self, boja, point1X, point1Y, radiusX, radiusY):
        self.boja = boja
        self.point1X = point1X
        self.point1Y = point1Y
        self.radiusX = radiusX
        self.radiusY = radiusY

    def draw(self, C):
        C.create_oval((self.point1X - self.radiusX, self.point1Y - self.radiusY, self.point1X + self.radiusX,
                       self.point1Y + self.radiusY), outline=self.boja)


class Application(Frame):
    def Open(self):
        filepath = fd.askopenfilename()
        self.readFile(filepath)
    def readFile(self, filepath):
        file1 = open(filepath, 'r')
        for line in file1:
            objects = line.split()
            print(objects[0])
            if objects[0] == "Line":
                linija = Linija(objects[1], objects[2], objects[3], objects[4], objects[5])
                linija.draw(self.C)
                print("Linija nacrtana")
            elif objects[0] == "Triangle":
                trokut = Trokut(objects[1], objects[2], objects[3], objects[4], objects[5], objects[6], objects[7])
                trokut.draw(self.C)
                print("Trokut nacrtan")
            elif objects[0] == "Rectangle":
                pravokutnik = Pravokutnik(objects[1], float(objects[2]), float(objects[3]), float(objects[4]), float(objects[5]))
                pravokutnik.draw(self.C)
                print("Pravokutnik nacrtan")
            elif objects[0] == "Circle":
                krug = Krug(objects[1], float(objects[2]), float(objects[3]), float(objects[4]))
                krug.draw(self.C)
                print("krug nacrtan")
            elif objects[0] == "Ellipse":
                elipsa = Elipsa(objects[1], float(objects[2]), float(objects[3]), float(objects[4]), float(objects[5]))
                elipsa.draw(self.C)
                print("Elipsa nacrtana")
        file1.close()

    

       
    def Close(self):
        exit()   

    def CreateWidgets(self):
        self.C = Canvas(self, height=600, width=800, background="grey")
        self.C.pack()
        self.filemenu.add_command(label="Open", command=self.Open)
        self.filemenu.add_command(label="Exit", command=self.Close)
        self.menu.add_cascade(label="File", menu=self.filemenu)


    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.menu = Menu(self.master)
        self.master.config(menu=self.menu)
        self.filemenu = Menu(self.menu, tearoff=0)
        self.CreateWidgets()
        self.pack()
    


root = Tk()
app = Application(root)
app.mainloop()

