#the lists are collections of values. In general the values of a list have the same type.

#we can declare a variable of type list in this way:

l1=list() #variable without type containing a list

l2:list=list() #variable of type list containing a list

l3:list=None #variable of type list containing nothing

#What is list()? It is a constructor, a special function allows us to create objects,
#a list in this case. We'll explain better the concept of constructor in the future.

#we can also create a list in these ways

l4=[] #empty list

l5=[1] #list of one element

l6=[1,2,3,4] #list of four elements

#this method is more flexible than list(), however list() returns useful when we have to
#convert an object into a list without reinventing the hot water

#to access the single elements of a list, we uses the indexes, they starts from 0:

lis=[3,1,2,5,7]

lis[0] #element 3

lis[3] #element 5

lis[4] #element 7

#lis[10] #ERROR

#We can also access using negative numbers, in this way we start from the ending:

lis[-1] #element 7

lis[-3] #element 2

#lis[-7] #ERROR

#We can also get a sublist in this way:

i=2
j=4
lis[i:j] #sublist between i and j(not included)

lis[::] #a copy of lis

lis[:j] #sublist from 0 to j

lis[i:] #sublist from i to the end

#To get the size of a list, we use the function len():

len(lis) #the size is 5

#Now we see these examples:

def printList1(lis):
    for i in range(0,len(lis)):
        print(lis[i])

def printList2(lis):
    for elem in lis:
        print(elem)

#In order to print all the list, we use a variable i and a for loop for iterating the list.
#In this way we can manage every element using the same code.

#Which is the difference between the first function and the second one? Nothing,
#the second function uses a different for loop, in fact the variable elem contain lis[i]

#Using the keyword "in" we can check if an element is in the list or not

def isInList1(lis,elem):
    if(elem in lis):
        return True
    else:
        return False

#or, more simply:

def isInList2(lis,elem):
    return elem in lis

#there are more ways for adding elements to a list:

lis.insert(4,5) #add 5 to the position 4 of the list the list

lis.append(5) #add 5 at the end of the list

lis+=[5,4] #add 5 and 4 at the end of the list

lis.extend([3,4,5,6]) #add 3,4,5 and 6 ad the end of the list

#Instead, we use these methods to remove and element from a list:

fruits=["apple","banana","strawberry","coconut","orange"]

fruits.remove("coconut") # remove the element coconut from the list

fruits.pop(1) #remove the element at position 1 from the list

fruits.pop() #if we don't specify the index, the function remove the last element

del fruits[0] #delete the element 2 from the list fruit

del fruits #if we don't specify the index, del delete alla the list and the variable

lis.clear() #same as the previous but the variable is not cancelled


