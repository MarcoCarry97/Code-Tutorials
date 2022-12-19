#boolean values are values that can be True or False
#we can use them for many reasons, for example to evaluate
#if a number is greater than another. In this case we can use arithmetic operators:

def compare(a,b):
    value=a>b
    return value

#> is an dual arithmetic operator, it return True if the value a is greater than
#the value b, False otherwise
# there are many arithmetic operators, which are: >,>=,<,<=,==

# WARNING: don't confuse = with ==, the first one assign a value to a variable,
#the second one compare two numbers and return True if they are equals, False otherwise

#there is a way to combine more simple arithmetic operators?
#Yes, we use the boolean operators

#the operator not returns the opposite boolean value, so:

notT=not True #is False

notF=not False #is True

#the operator or returns True if almost one of the operands is True

TorT=True or True #is True

TorF=True or False #is True

ForT=False or True #is True

ForF=False or False #is False

#the operator and returns True if all the operands are True

TandT=True and True #is True

TandF=True and False #is False

FandT=False and True #is False

FandF=False and False #is False

#If we want to test if a number is in a specific range, how can we do?
#In this way:

def isInRange(limitLeft,limitRight,testValue):
    return limitLeft<=testValue and testValue<=limitRight

def isInRange2(limitLeft,limitRight,testValue):
    return limitLeft<=testValue<=limitRight

#and if is it outside the range?

def isOutRange(limitLeft,limitRight,testValue):
    return not isInRange(limitLeft,limitRight,testValue)

#boolean variables are useful with the if statement, it is a special instruction
#which allow us to execute a part of code respect to another in base of a condition

def alwaysExecuted(): #it always execute the print
    if(True):
        print("It is True")

def neverExecuted(): #it never execute the print
    if(False):
        print("It is True")

def executeIfGreater(n,m): #it print n if is greater than m
    if(n>m):
        print(n)

#in order to make more complex things, we can other instructions with if:
#else executes the code that follow if the condition of if is false

#elif is a sort of union between if and else: it executes the code that follows
#if the condition of if is false and its condition is true

def max(a,b):
    if(a>=b):
        return a
    else:
        return b

def isNonNegative(n):
    if(n>0):
        return True
    elif(n==0):
        return True
    else:
        return False

def isNotPositiveOneNorTwo(n):
    if(n==1):
        return False
    elif(n==2):
        return False
    elif(n>0):
        return False
    else:
        return True
    
    

    


