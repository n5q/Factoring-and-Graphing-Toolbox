from tkinter import Tk, Canvas
from time import sleep
import re

class graphingCalculator():
  def __init__(self, size):
    myInterface = Tk()
    self.screen_size = size

    self.screen = Canvas(myInterface, width=screen_size, height=screen_size, background="white")
    self.screen.pack()
  
  @staticmethod
  def getScaleFactor(a, b):
    return a/b

  ################ NEW FUNCTION ################
  #gets values of a, b, and c: works with decimals too
  def get_values(self, eqn):
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










def input_screen_size(size): #let user choose the screen size
  tk = Tk()
  global screen_size
  screen_size = size

  global screen
  screen = Canvas(tk, width=screen_size, height=screen_size, background="white")
  screen.pack()

getScaleFactor = lambda a, b : a/b

################ NEW FUNCTION ################
#gets values of a, b, and c: works with decimals too
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
  try: index = re.search(r"(\+|-)(\d)*(\d |(\.(\d)*(\d )))", eqn).start() #too long to explain
  except: c = 0 #error: can't find c
  else: c = float(eqn[index:-1])

  #return dictionary of values
  return {"a" : a, "b" : b, "c" : c}



################ NEW PROCEDURE ################
#uses arguments to create the numbers for our axes
def draw_numbers(initial_values, scaled_values, distance, x, y):
  #print("FUNCTION:", initial_values, scaled_values)

  for i in range(int(distance)//int(scaled_values['xIncrement'])+1): #x Numbers
    screen.create_text(scaled_values['xMin']+i*scaled_values['xIncrement'], y, text = initial_values['xMin']+i*initial_values['xIncrement'])

  for i in range(int(distance)//int(scaled_values['yIncrement'])+1): #y numbers
    screen.create_text(x, scaled_values['yMin']-i*scaled_values['yIncrement'], text = initial_values['yMin']+i*initial_values['yIncrement'])

################ NEW FUNCTION ################
#use arguments to create origin
def get_origin(initial_values, scaled_values):
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
def draw_axes(xMin, xMax, yMin, xIncrement, yIncrement):
  global origin
  global scaleFactor
  global distance
  global xMinTOV
  global xMaxTOV

  xMinTOV = xMin
  xMaxTOV = xMax
  origin = ["x", "y"]
  xAxis, yAxis = False, False
  distance = xMax - xMin
  yMax = yMin + distance
  scaleFactor = getScaleFactor(screen_size, distance)
  #print("SCALEFACTOR:", scaleFactor)

  ## Width of squares to determine scaling for points when plotting
  global widthX
  global widthY
  widthX = screen_size/(xMax-xMin) 
  widthY = screen_size/(yMax-yMin)
  
  initial_values = {"xMin": xMin, "xMax": xMax, "yMin": yMin, "xIncrement": xIncrement, "yIncrement": yIncrement}

  xMin *= scaleFactor
  xMax *= scaleFactor
  yMin *= scaleFactor
  yMax *= scaleFactor
  distance *= scaleFactor
  yIncrement *= scaleFactor
  xIncrement *= scaleFactor
  #print(xMin, xMax, yMin, yMax, yIncrement, xIncrement)
  
  xMax -= xMin
  yMax -= yMin
  xMin = 0
  yMin = 0
  yMin, yMax = yMax, yMin

  #print(xMin, xMax, yMin, yMax, yIncrement, xIncrement)

  scaled_values = {"xMin": xMin, "xMax": xMax, "yMin": yMin, "yMax": yMax,"xIncrement": xIncrement, "yIncrement": yIncrement}

  for i in range(int(distance)//int(xIncrement)): #x lines
    screen.create_line(xMin+i*xIncrement, 0, xMin+i*xIncrement, yMin, width = 1)
  for i in range(int(distance)//int(yIncrement)): #y lines
    screen.create_line(0, yMax+i*yIncrement, xMax, yMax+i*yIncrement, width = 1)
    
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
  #print("origin: ", origin)

  get_origin(initial_values, scaled_values)

  draw_numbers(initial_values, scaled_values, distance, x, y)


################ NEW FUNCTION ################
#use arguments to make a table of values
def makeTableofValues (numPoints, eq):
    
    global xValues
    global yValues
    global numbPoints
    numbPoints = numPoints
    equation = eq

    #uses the get_values function to get the a,b,c values
    values = get_values(equation)

    #define abc values in variables
    a = values['a']
    b = values['b']
    c = values['c']
    xValues = []
    yValues = []
    get_values (equation)
    xIncrease = (xMaxTOV-xMinTOV)/numPoints
    x = xMinTOV

    #uses abc values to find x and y values
    for _ in range  (numPoints):
        yValue = a*x**2 + b*x + c
        xValues.append (x) ##Scale the points based on the origin -- we don't have an origin yet
        yReal = yValue #to scale, multiply by the width of the Ysquares and add it to the origin
        yValues.append (yReal)
        x = x + xIncrease

    #xvv = print (xValues,yValues)
    return xValues, yValues


################ NEW FUNCTION ################
#use arguments to plot points for the user
def plotPoints ():
  xPlotValue = []
  yPlotValue = []
  pointsPlot = []

  #scales the x and y values to the screen 
  for i in range (numbPoints):
    xv = xValues[i]*widthX + origin [0] 
    yv = origin [1] - (yValues[i]*widthY) - screen_size 
    xPlotValue.append (xv)
    yPlotValue.append (yv)

  #plotting the points
  for t in range(numbPoints-1):
      pointsPlot.append(screen.create_line (xPlotValue[t], yPlotValue[t], xPlotValue[t+1], yPlotValue[t+1], fill = "red", smooth= "true", width = 3))

  #xx = print (xPlotValue, yPlotValue)
  return (pointsPlot)
