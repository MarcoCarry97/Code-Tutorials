
#Hola, if you use IDLE3, you can open this file
#and run the function with the command line


#this is a function, it print the string "Hello, World!"
def helloworld():
    print("Hello, World!");

#we declare a function using the keyword 'def' and the name of the function.
#between the brackets we can write the variables we need, for example:

def hello(name:str):
    print("Hello "+name);

#this functions takes one parameter as input, this parameter is a string
#Now we see this function:

def readAndHello():
    var1="Hello"
    var2:str=input("Write a name\n")
    print(var1+", "+var2)

#In this function we have two variable declarations:
    #var1 is variable without a specific type, so it can take all the types of values
    #var2 is a variable of type string (str), it can take only strings as values
    
#input() is a function, it blocks the execution and allows the user to write some text
#the execution restarts when we push ENTER
#input() return a string, so if we want for example an integer value, we have to convert it.

def readIntAndPrint():
    var1=input("Type a number\n")
    print(var1)
    
#Python has 9 types:
    #integers: int
    #floating points: float
    #strings: str
    #lists: list
    #dictionaries: dict
    #sets: set
    #tuples: tuple
    #complexes: complex
    #booleans: bool
