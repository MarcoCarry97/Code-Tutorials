#loops are pieces of code that are repeated for a certain amount of time
#or until a specific condition is not respected anymore

#the for loop iterate until there are no elements:

def iterate(n):
    for i in range(0,n):
        print(i)

#the function above use a  variable i, it assumes a different values at every
#iteration. In the first iteration, i is equal to 0, instead in the last one
#it is equal to n-1 because range(a,b) generate numbers from a to b-1
        
#for loops are useful for iterating elements in a list or a set,
#but this is a spoiler of the next lesson XD

#while loops run the code until the given condition is not respected anymore:

def loopUntilLower(a,b):
    while(a>b):
        print(a)
        a=a-1

