


#IMPORTS MATH LIBRARY
from math import *

#DETERMINES IF B AND/OR C VALUES ARE PRESENT
def getTerms(trinomial):

  global aTerm
  global bTerm
  global cTerm

  aTerm = False
  bTerm = False
  cTerm = True


  #CHECKS IF THE CHARACTER X APPEARS MORE THAN ONCE TO DETERMINE IF B IS PRESENT
  for i in trinomial:

    if i == "x":

      if trinomial[trinomial.index(i)+1] == "^":

        if aTerm == True:
          bTerm = True

        else:
          aTerm = True

  #CHECKS IF LAST TERM IS B
  if trinomial[-1] == "x":
    cTerm = False

#PULLS A B AND C VALUES FROM A STRING IN THE FORM "AX^2 + BX + C"
def getABC(trinomial):

  #CONVERTS STRING TO LIST AND REMOVES UNNECESSARY CHARACTERS
  trinomialArray = []

  for i in trinomial:
    trinomialArray.append(i)

  for i in trinomialArray:
    if i == "^":
      x = (trinomialArray.index(i)-1)
      square = (trinomialArray.index(i)+2)
      del trinomialArray[x:square]

  for i in trinomialArray:
    if i == "x":
      del trinomialArray[trinomialArray.index(i)]

  for i in trinomialArray:
    if i == "-":
      trinomialArray[trinomialArray.index(i)+1] = "-" + trinomialArray[trinomialArray.index(i)+1]
      trinomialArray[trinomialArray.index(i)] = "+"

  abc = ""
  for i in trinomialArray:
    abc = abc + i

  abcArray = abc.split("+")  

  for i in range(2):
    if abcArray[i] == "":
      abcArray[i] = "1"

  global a
  global b
  global c 
  a = 0
  b = 0
  c = 0

      


  #DETERMINES WHICH INDEX OF THE ARRAY TO ASSIGN TO EACH VARIABLES DEPENDING ON THE OUTPUT OF GETTERMS()
  
  if abcArray[0] == "" and aTerm == True and bTerm == True and cTerm == True:
    a = abcArray[1]
    b = abcArray[2]
    c = abcArray[3]
    a = int(a)
    b = int(b)
    c = int(c)
  elif aTerm == True and bTerm == True and cTerm == True:
    a = abcArray[0]
    b = abcArray[1]
    c = abcArray[2]
    a = int(a)
    b = int(b)
    c = int(c)
  elif abcArray[0] == "" and aTerm == True and bTerm == True and cTerm == False:
    a = abcArray[1]
    b = abcArray[2]
    a = int(a)
    b = int(b)
  elif aTerm == True and bTerm == True and cTerm == False and len(abcArray) == 3:
    a = abcArray[1]
    b = abcArray[2]
    a = int(a)
    b = int(b)
  elif aTerm == True and bTerm == True and cTerm == False:
    a = abcArray[0]
    b = abcArray[1]
    a = int(a)
    b = int(b)
  elif abcArray[0] == "" and aTerm == True and bTerm == False and cTerm == True:
    a = abcArray[1]
    c = abcArray[2]
    a = int(a)
    c = int(c)
  elif aTerm == True and bTerm == False and cTerm == True:
    a = abcArray[0]
    c = abcArray[1]
    a = int(a)
    c = int(c)
  elif abcArray[0] == "" and aTerm == True and bTerm == False and cTerm == False:
    a = abcArray[1]
    a = int(a)
  elif aTerm == True and bTerm == False and cTerm == False:
    a = abcArray[0]
    a = int(a)


#FILLS ARRAY WITH ALL FACTORS OF A NUMBER
def factors(num,array):
  for i in range(1,abs(num)+1):
    if num%(i) == 0:
        array.append(i)
 
#RETURNS GREATEST COMMON FACTOR OF 3 ARRAYS 
def getGCF(a,b,c):
    aFactors = []
    bFactors = []
    cFactors = []
    commonFactors = []
    factors(c,cFactors)
    factors(b,bFactors)
    factors(a,aFactors)
    for i in aFactors:
        for j in bFactors:
            for k in cFactors:
                if i == j == k:
                    commonFactors.append(i)
                    commonFactors.append(i*-1)

    if commonFactors == [1,-1]:
      return(1)

    else:
      return(commonFactors[len(commonFactors)-2])

#DIVIDES A B AND C BY A COMMON FACTOR
def commonFactor(aF,bF,cF,factor):
  global a
  global b
  global c
  global aOld
  global bOld
  global cOld
  aOld = a
  bOld = b
  cOld = c
  a = int(aF/factor)
  b = int(bF/factor)
  c = int(cF/factor)

#RETURNS EQUIVALENT FRACTION FROM A FLOAT
def floatToFraction(decimal):
  decimal = decimal*-1
  decimalArray = str(decimal)
  decimalArray = decimalArray.split(".")

  if len(decimalArray[1]) > 10:
    return("end")

  else:
    decimalArray[0] = int(decimalArray[0])
    wholeNum = decimalArray[0]
    numerator = decimal - wholeNum
    denominator = int("1" + "0"*len(decimalArray[1]))
    numerator = int(numerator*denominator)
    GCF = (getGCF(numerator,int(denominator),int(denominator)))
    numerator = int(numerator/GCF)
    denominator = int(denominator/GCF)
    numerator = numerator + (wholeNum*denominator)
    return(str(numerator) + "/" + str(denominator))

#SOLVES FOR ROOTS USING QUADRATIC FORMULA
def solveQuadratic(a,b,c):

  global root1
  global root2

  root1 = ((b*-1) + sqrt((b**2) - (4*a*c))) / (2*a)
  tempArray = str(root1).split(".")

  if tempArray[1] == "0":
    root1 = int(root1)*-1

  else:
    root1 = floatToFraction(root1)

    if root1 == "end":
      return("end")

  root2 = ((b*-1) - sqrt((b**2) - (4*a*c))) / (2*a)
  tempArray = str(root2).split(".")

  if tempArray[1] == "0":
    root2 = int(root2)*-1

  else:
    root2 = floatToFraction(root2)

    if root2 == "end":
      return("end")

#RETURNS FACTORED TERM FROM TWO ROOTS
def factorRoot(root):
  if type(root) == int:
    if root > 0:
      root = "(x + " + str(root) + ")"

    elif root == 0:
      coefficient = str(getGCF(a,b,b))

      if coefficient == "1":
        coefficient = ""

      elif coefficient == "-1":
        coefficient = "-"
      root = coefficient + "x"

    else:
      root = root*-1
      root = "(x - " + str(root) + ")"

  elif type(root) == str:
    root = root.split("/")

    for i in range(2):
      root[i] = int(root[i])
    coefficient = root[1]
    num = root[0]

    if num > 0:
      root = "(" + str(coefficient) + "x + " + str(num) + ")"

    if num < 0:
      num = num*-1
      root = "(" + str(coefficient) + "x - " + str(num) + ")"

  return(root)

#DETERMINES IF A NUMBER IS A PERFECT SQUARE
def isPerfectSquare(num):
  root = sqrt(abs(num))
  if int(root + 0.5) ** 2 == abs(num):
    return(True)
  else:
    return(False)
  
#FACTORS THE STRING USING FUNCTIONS ABOVE
def factor(trinomial):
  global a
  global b
  global c
  global aOld
  getTerms(trinomial)
  getABC(trinomial)

  if bTerm == True and cTerm == False:
    commonFactor(a,b,c,getGCF(a,b,b))

  elif bTerm == False and cTerm == True:
    commonFactor(a,b,c,getGCF(a,c,c))

  else:
    commonFactor(a,b,c,getGCF(a,b,c))

  if ((b**2) - (4*a*c)) < 0:
    return("This trinomial cannot be factored")

  else:
    solveQuadratic(a,b,c)

    if root1 == "end" or root2 == "end":

      if bTerm == False:

        if isPerfectSquare(a) == True and isPerfectSquare(c) == True:
          perfectSquare = "(" + str(int(sqrt(abs(a)))) + "x" + " " + "+" + " " + str(int(sqrt(abs(c)))) + ")" + "(" + str(int(sqrt(abs(a)))) + "x" + " " + "-" + " " + str(int(sqrt(abs(c)))) + ")"
          return(perfectSquare)
        else:
          return("This trinomial cannot be factored")
        

      elif a != aOld:

          coefficient = str(getGCF(aOld,bOld,bOld))
          if b > 0:
              b = "+" + str(b)
          
          if c > 0:
              c = "+" + str(c)

          if a == 1:
            a = ""
          if b == 1:
            b = ""

          return(coefficient + "(" + str(a) + "x^2" + b + "x" + c + ")")        

      else:
          return("This trinomial cannot be factored")
    else:
      if bTerm == True and cTerm == False:
        coefficient = str(getGCF(aOld,bOld,bOld))

      elif bTerm == False and cTerm == True:
        coefficient = str(getGCF(aOld,cOld,cOld))    
          
      else:
        coefficient = str(getGCF(aOld,bOld,cOld))

      if coefficient == "1":
        coefficient = ""

      if factorRoot(root1) == factorRoot(root2):
        return(coefficient + factorRoot(root1) + "^2")
        
      else:
        if ")" not in factorRoot(root2):
          return(factorRoot(root2) + factorRoot(root1))
        else:
          return(coefficient + factorRoot(root1) + factorRoot(root2))



##################################################################################
#                                 END OF PROGRAM                                 #




