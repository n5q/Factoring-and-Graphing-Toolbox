from tkinter import Tk, Canvas, Label, Entry, Button
from FactoringToolbox import factor
#from GraphingCalculatorToolbox import *
from GraphingCalculatorToolboxImproved import graphingCalculator

root= Tk()
root.title("Trinomial Factoring and Graphing Toolbox")

screen = Canvas(root, width = 400, height = 300,bg = "#263238")
screen.pack()

label1 = Label(root, text="Trinomial Factoring and Graphing Toolbox",font=("helvetica", 14),bg = "#263238",fg="white")
screen.create_window(200, 25, window=label1)

label2 = Label(root, text="Enter your trinomial:",font = ("helvetica", 11),bg = "#263238",fg="white")
screen.create_window(200, 100, window=label2)

trinomialEntry = Entry (root,bd=0,fg="white",justify="center",insertbackground="white")
screen.create_window(200, 140, window=trinomialEntry,)
trinomialEntry.config({"background": "#425761"})
trinomialEntry.config(bd=0,fg="white",justify="center",insertbackground="white")

def drawGraph():
    
    graph = graphingCalculator(int(sizeInput.get()))

    graph.draw_axes(int(xMinInput.get()),int(xMaxInput.get()),int(yMinInput.get()),int(xIncInput.get()),int(yIncInput.get()))

    graph.makeTableofValues(int(numPointInput.get()),str(trinomialEntry.get()))

    graph.plotPoints()

    graphOptions.destroy()

def graphOutput():

    global graphOptions
    global sizeInput
    global xMinInput
    global xMaxInput
    global yMinInput
    global xIncInput
    global yIncInput
    global numPointInput
    #global equationInput

    graphOptions = Tk()
    graphOptions.title("Graph Options")
    screen = Canvas(graphOptions,width=200,height=600,bg="#263238")
    screen.pack()
    
    sizeInput = Entry(graphOptions,bd=0,fg="white",justify="center",insertbackground="white")
    sizeInputLabel = Label(graphOptions, text = "Enter screen size:",font = ("helvetica", 11),bg="#263238",fg="white")
    screen.create_window(100,25, window = sizeInputLabel)
    screen.create_window(100,50, window = sizeInput)
    sizeInput.config({"background": "#425761"})

    xMinInput = Entry(graphOptions,bd=0,fg="white",justify="center",insertbackground="white")
    xMinInputLabel = Label(graphOptions, text = "Enter minimum x:",font = ("helvetica", 11),bg="#263238",fg="white")
    screen.create_window(100,100, window = xMinInputLabel)
    screen.create_window(100,125, window = xMinInput)
    xMinInput.config({"background": "#425761"})

    xMaxInput = Entry(graphOptions,bd=0,fg="white",justify="center",insertbackground="white")
    xMaxInputLabel = Label(graphOptions, text = "Enter maximum x:",font = ("helvetica", 11),bg="#263238",fg="white")
    screen.create_window(100,175, window = xMaxInputLabel)
    screen.create_window(100,200, window = xMaxInput)
    xMaxInput.config({"background": "#425761"})

    yMinInput = Entry(graphOptions,bd=0,fg="white",justify="center",insertbackground="white")
    yMinInputLabel = Label(graphOptions, text = "Enter minimum y:",font = ("helvetica", 11),bg="#263238",fg="white")
    screen.create_window(100,250, window = yMinInputLabel)
    screen.create_window(100,275, window = yMinInput)
    yMinInput.config({"background": "#425761"})

    xIncInput = Entry(graphOptions,bd=0,fg="white",justify="center",insertbackground="white")
    xIncInputLabel = Label(graphOptions, text = "Enter x increment:",font = ("helvetica", 11),bg="#263238",fg="white")
    screen.create_window(100,325, window = xIncInputLabel)
    screen.create_window(100,350, window = xIncInput)
    xIncInput.config({"background": "#425761"})

    yIncInput = Entry(graphOptions,bd=0,fg="white",justify="center",insertbackground="white")
    yIncInputLabel = Label(graphOptions, text = "Enter y increment:",font = ("helvetica", 11),bg="#263238",fg="white")
    screen.create_window(100,400, window = yIncInputLabel)
    screen.create_window(100,425, window = yIncInput)
    yIncInput.config({"background": "#425761"})

    numPointInput = Entry(graphOptions,bd=0,fg="white",justify="center",insertbackground="white")
    numPointInputLabel = Label(graphOptions, text = "Enter number of points:",font = ("helvetica", 11),bg="#263238",fg="white")
    screen.create_window(100,475, window = numPointInputLabel)
    screen.create_window(100,500, window = numPointInput)
    numPointInput.config({"background": "#425761"})

    drawGraphButton = Button(graphOptions, text = "Graph", command = drawGraph, bg = "#182024",fg = "green",font = ("helvetica", 9, "bold"),highlightthickness= 0,borderwidth=4,relief="flat")
    screen.create_window(100,550, window = drawGraphButton)
    

def factorOutput():
    
    erase = Label(root,text="                                                                                ",bg="#263238",fg="white",)
    screen.create_window(200,170,window=erase)
    x = trinomialEntry.get()
    factorOutput = factor(x)
    label3 = Label(root,text=factorOutput,bg="#263238",fg="white",font = ("helvetica", 9, "bold"))
    screen.create_window(200,170,window=label3)

factorButton = Button(root, text = "Factor",relief="flat", bg = "#182024",highlightthickness= 0,borderwidth=4, fg = "brown",font = ("helvetica", 9, "bold"), command = factorOutput)
screen.create_window(200,205,window=factorButton)

graphButton = Button(root, text = "Graph",relief="flat",highlightthickness= 0,borderwidth=4, bg = "#182024", fg = "green", font = ("helvetica", 9, "bold"), command = graphOutput)
screen.create_window(200,250, window=graphButton)


root.mainloop()
