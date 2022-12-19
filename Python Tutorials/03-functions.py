#a function is a piece of code, we can call and run in every moment.
# we declare it using the keyword "def", also they can have a limitless number of variables:

def func1():
    print("This is a function of one variable")

def func2(var1):
    print("This is a function with one variable, the value is: "+str(var1))

def func3(var1:int,var2:float):
    print("function of two variables, two numbers precisely: "+str(var1)+" "+str(var2))

#a function can return a value, we can do it using the keyword 'return'

def rectangleArea(base:float,height:float)->float:
    area:float=base*height
    return area

def triangleArea(base:float, height:float)->float:
    areaRect:float=rectangleArea(base,height)
    area:float=areaRect/2
    return area

#as we can see in the second function, we called the first one in the code.
#This is an example of how the function are useful! In fact they allows to recycle
#the code writing it only one time.

#a function is a type, so we can return functions from other functions:

def genericArea():
    def squareArea(l:float)->float:
        area:float=l*l
        return area
    return squareArea

def otherGenericArea():
    return triangleArea

#in the first function, the function we returned is defined inside the function itself
#in the second one we returned a function defined previously

#it is also possible call a function inside its body, it is code recursion and it works
#in this way:
#there are some base case the function ends
#there recursive cases, in these the function call itself
#the common case of recursive function is the fibonacci' succession:

def fibonacci(n:int)->int:
    if(n==0): #base case
        return 0
    elif(n==1): #another base case
        return 1
    else: #recursive case
        tmp:int=fibonacci(n-1)
        return n+tmp

#there is also a special time of functions called lambda expressions,
#they are useful to model simple calculus, for example:
    
rectArea=lambda base,height:base*height
    
triArea=lambda base: lambda height: base*height/2

area1=rectArea(5,3) #returns 15
area2=triArea(6)(4) #returns 12

#why does triArea need a different type of call respect rectArea?
#Because the lambda expressions return the value of the right of :,
#so triArea returns a function that return an integer value
    
