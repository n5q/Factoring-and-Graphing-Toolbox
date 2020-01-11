from tkinter import Tk, Canvas
from time import sleep
import re

class graphingCalculator():
  def __init__(self, size):
    myInterface = Tk()
    self.screen_size = size

    self.screen = Canvas(myInterface, width=self.screen_size, height=self.screen_size, background="white")
    self.screen.pack()
    self.origin = ["x", "y"]
  
  @staticmethod
  def getScaleFactor(a, b):
    return a/b

  ################ NEW FUNCTION ################
  #gets values of a, b, and c: works with decimals too
  @staticmethod
  def get_values(eqn):
    eqn += " " #add whitespace to signify end of string
    index = 0
    index2 = None

    #Find value of a
    try: index = eqn.index('x^2')
    except: a = 0 #error: can't find a
    else:
      if eqn[0:index] == "-": a = -1
      else: a = float(eqn[0:index]) if index > 0 else 1
    
    #Find value of b
    try: index2 = re.search(r"(x(\+|-| ))", eqn).start() #x and (+ or - or whitespace)
    except: b = 0 #error: can't find b
    else:
      try: b = float(eqn[index+3:index2]) if a != 0 else float(eqn[index:index2])
      except: b = 1

    #find value of c
    try: index = re.search(r"(\+|-)(\d)*(\d |(\.(\d)*(\d )))", eqn).start() #more regex
    except: c = 0 #error: can't find c
    else: c = float(eqn[index:-1])

    #return dictionary of values
    return {"a" : a, "b" : b, "c" : c}
  
  ################ NEW PROCEDURE ################
  #uses arguments to create the numbers for our axes
  def draw_numbers(self, initial_values, scaled_values, distance, x, y):
    screen = self.screen
    for i in range(int(distance)//int(scaled_values['xIncrement'])+1): #x Numbers
      screen.create_text(
        scaled_values['xMin']+i*scaled_values['xIncrement'], y, text = initial_values['xMin']+i*initial_values['xIncrement']
      )

    for i in range(int(distance)//int(scaled_values['yIncrement'])+1): #y numbers
      screen.create_text(
        x, scaled_values['yMin']-i*scaled_values['yIncrement'], text = initial_values['yMin']+i*initial_values['yIncrement']
      )

  ################ NEW FUNCTION ################
  #use arguments to create origin
  def get_origin(self, initial_values, scaled_values):
    screen = self.screen
    screen_size = self.screen_size
    origin = self.origin

    for i in range(screen_size): #Plot x and y axis by going through the entire screen and finding their locations
      if initial_values['xMin']+i*initial_values['xIncrement'] == 0: #Y Axis
        screen.create_line(scaled_values['xMin']+i*scaled_values['xIncrement'], 0, scaled_values['xMin']+i*scaled_values['xIncrement'], screen_size, width = 2.5)
        yAxis = True
        x = scaled_values['xMin']+i*scaled_values['xIncrement']-25

      if initial_values['yMin']+i*initial_values['yIncrement'] == 0: #X Axis
        screen.create_line(0, scaled_values['yMin']-i*scaled_values['yIncrement'], screen_size, scaled_values['yMin']-i*scaled_values['yIncrement'], width = 2.5), 
        xAxis = True
        y = scaled_values['yMin']-i*scaled_values['yIncrement']+25

    if xAxis == False or y > screen_size-25:
      y = 575
      origin[1] = 0 - initial_values["xMin"]
    if yAxis == False or x < 25:
      x = 25
      origin[0] = 0 - initial_values["yMin"]

    origin[0] = x+25 if yAxis == True else origin[0]
    origin[1] = y-25 if xAxis == True else origin[1]
    origin[1] += screen_size
    return origin

  ################ NEW PROCEDURE ################
  #draw axis with arguments
  def draw_axes(self, xMin, xMax, yMin, xIncrement, yIncrement):
    self.xMinTOV = xMin
    self.xMaxTOV = xMax
    xAxis, yAxis = False, False
    self.distance = xMax - xMin
    yMax = yMin + self.distance
    scaleFactor = self.scaleFactor = self.getScaleFactor(self.screen_size, self.distance)
    #print("SCALEFACTOR:", scaleFactor)

    ## Width of squares to determine scaling for points when plotting
    self.widthX = self.screen_size/(xMax-xMin) 
    self.widthY = self.screen_size/(yMax-yMin)
    
    self.initial_values = initial_values = {
      "xMin": xMin,
      "xMax": xMax,
      "yMin": yMin,
      "xIncrement": xIncrement,
      "yIncrement": yIncrement
    }

    xMin *= scaleFactor
    xMax *= scaleFactor
    yMin *= scaleFactor
    yMax *= scaleFactor
    self.distance *= scaleFactor
    yIncrement *= scaleFactor
    xIncrement *= scaleFactor
    #print(xMin, xMax, yMin, yMax, yIncrement, xIncrement)
    
    xMax -= xMin
    yMax -= yMin
    xMin = 0
    yMin = 0
    yMin, yMax = yMax, yMin

    #print(xMin, xMax, yMin, yMax, yIncrement, xIncrement)

    self.scaled_values = scaled_values = {
      "xMin": xMin,
      "xMax": xMax,
      "yMin": yMin,
      "yMax": yMax,
      "xIncrement": xIncrement, 
      "yIncrement": yIncrement
    }

    for i in range(int(self.distance)//int(xIncrement)): #x lines
      self.screen.create_line(xMin+i*xIncrement, 0, xMin+i*xIncrement, yMin, width = 1)
    for i in range(int(self.distance)//int(yIncrement)): #y lines
      self.screen.create_line(0, yMax+i*yIncrement, xMax, yMax+i*yIncrement, width = 1)
      
    for i in range(self.screen_size): #Plot x and y axis by going through the entire screen and finding their locations
      if initial_values['xMin']+i*initial_values['xIncrement'] == 0: #Y Axis
        self.screen.create_line(scaled_values['xMin']+i*scaled_values['xIncrement'], 0, scaled_values['xMin']+i*scaled_values['xIncrement'], self.screen_size, width = 2.5)
        yAxis = True
        x = scaled_values['xMin']+i*scaled_values['xIncrement']-25

      if initial_values['yMin']+i*initial_values['yIncrement'] == 0: #X Axis
        self.screen.create_line(0, scaled_values['yMin']-i*scaled_values['yIncrement'], self.screen_size, scaled_values['yMin']-i*scaled_values['yIncrement'], width = 2.5), 
        xAxis = True
        y = scaled_values['yMin']-i*scaled_values['yIncrement']+25

    if xAxis == False or y > self.screen_size-25:
      y = 575
      self.origin[1] = 0 - initial_values["xMin"]
    if yAxis == False or x < 25:
      x = 25
      self.origin[0] = 0 - initial_values["yMin"]

    self.origin[0] = x+25 if yAxis == True else self.origin[0]
    self.origin[1] = y-25 if xAxis == True else self.origin[1]
    self.origin[1] += self.screen_size
    #print("origin: ", origin)

    self.get_origin(initial_values, scaled_values)

    self.draw_numbers(initial_values, scaled_values, self.distance, x, y)
  
  ################ NEW FUNCTION ################
  #use arguments to make a table of values
  def makeTableofValues (self, numPoints, eq):
    self.numbPoints = numPoints
    equation = eq

    #uses the get_values function to get the a,b,c values
    values = self.get_values(equation)

    #define abc values in variables
    a = values['a']
    b = values['b']
    c = values['c']
    self.xValues = []
    self.yValues = []
    #get_values (equation)
    xIncrease = (self.xMaxTOV-self.xMinTOV)/numPoints
    x = self.xMinTOV

    #uses abc values to find x and y values
    for _ in range  (numPoints):
      yValue = a*x**2 + b*x + c
      self.xValues.append (x) ##Scale the points based on the origin -- we don't have an origin yet
      yReal = yValue #to scale, multiply by the width of the Ysquares and add it to the origin
      self.yValues.append (yReal)
      x = x + xIncrease

    #xvv = print (xValues,yValues)
    return self.xValues, self.yValues
  
  ################ NEW FUNCTION ################
  #use arguments to plot points for the user
  def plotPoints (self):
    xPlotValue = []
    yPlotValue = []
    pointsPlot = []

    #scales the x and y values to the screen 
    for i in range (self.numbPoints):
      xv = self.xValues[i]*self.widthX + self.origin [0] 
      yv = self.origin [1] - (self.yValues[i]*self.widthY) - self.screen_size 
      xPlotValue.append (xv)
      yPlotValue.append (yv)

    #plotting the points
    for t in range(self.numbPoints-1):
      pointsPlot.append(self.screen.create_line (xPlotValue[t], yPlotValue[t], xPlotValue[t+1], yPlotValue[t+1], fill = "red", smooth= "true", width = 3))

    #xx = print (xPlotValue, yPlotValue)
    return (pointsPlot)

if __name__ == "__main__":
  graph = graphingCalculator(int(input("Please enter Screen Size: "))) #user inputs screen size

  graph.draw_axes(int(input("Please enter xMin: ")),int(input("Please enter xMax: ")),int(input("Please enter yMin: ")),int(input("Please enter increment for x: ")),int(input("Please enter increment for y: "))) #User draws up a grid

  TOV = graph.makeTableofValues (int(input("Please enter number of points: ")), input("Enter equation: y=")) #Using given data, user enters desired number of points and an equation (in the function)
  #graph.plotPoints(TOV[0], TOV[1]) #makeTableofValues returns a tuple of a list of x values and a list of y values
  graph.plotPoints()

  graph.screen.update()
  graph.screen.mainloop()