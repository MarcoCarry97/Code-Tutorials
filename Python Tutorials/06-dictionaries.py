#the dictionaries are collections of values that use the key-value paradigm.

#the key-value paradigm is a way allowing us to get a specific value using a given key.

#the lists uses this paradigm, in this case
#the key is an integer number and the value can be everything

fruits=["Apple","banana","orange"]

fruits[1] #in this case, the value is a string

numbers=[1,2,3,4,5,6,7,8,9]

numbers[4] #in this case the value is an integer

#for lists, the type of the key is always an integer.

#In the case of the dictionaries, the key can have different types
#Generally, we use dictionaries with string keys, however this is not a rule.

#We declare a dictionary in these modes:

dictio=dict() #empty dictionary
dictio1={}      #empty too
car1=dict(brand="Ford",model="Fiesta",year="2014") #dictionary with some keys
car2={"brand"="Ford","model"="Fiesta","year"="2014"}

#if we use len() on a dictionary, it returns the number of keys inside it

len(dictio2) #it is 4

#To access an element of the dictionary, we use the same notation of the lists:

car=dict(brand="Ford",model="Fiesta",year="2014")

car["brand"] #Ford

car.get("model") #Fiesta

#To write in a specific key, we proceed as follow:

car["model"]="Kuga"

car.update({"model":"Kuga"})

#To get the keys and the values of a dictionary, we use these methods:

car.keys() #list of keys of car: [brand,model,year]
car.values() #list of values of car: [Ford,Kuga,2014]
car.items() #list of (key,value) of car:
            #[(brand,Ford),(model,Kuga),(year,2014)]

#to check if a key is in a dictionary, we use the keyword "in":

def isInDict1(dictio,key):
    if(key in dictio):
        return True
    else:
        return False

def isInDict2(dictio,key):
    return key in dictio

#to remove a key from a dictio, the methods are the same of the lists:

car.pop("model")

car.popitem() #remove the last element inserted

del car["brand"]

del car #WARNING, IT DELETE ALL THE DICTIONARY AND THE VARIABLE

car.clear() #same of "del car", but it doesn't cancel the variable


#dictionaries can be nested
address={"name"="Viale Luigi Euinaudi","civic":6,"city"="Tortona"}

person={"name"="Guglielmo","surname"="Marconi","age":43,"address"=address}

print(person)
