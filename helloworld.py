#x = 5 #Integer
#y = "John" #Can be single or double quotes for a string
#Comments are useful

#This is functionally a comment
#That supports multiline
#Variables must
#Start with a letter or _
#Only supports A-z 0-9 and +
#Variables are case sensitive
#
#print("Hello, World!")
#if 5 > 2:
#    print("Five is greater than two!") #Also a comment
#
#print(x)
#print(y)
#
#x, y, z, = "Orange", "Banana", "Cherry"
#print(x)
#print(y)
#print(z)
#
#x = y = z = "Grape"
#print(x)
#print(y)
#print(z)
#
#x = "awesome"
#print("Python is " + x)
#
#x = "Python is "
#y = "awesome"
#z = x + y
#print(z)
#
#x = 5
#y = 10
#print (x + y)
#
#x = "awesome"
#def myfunc():
#    print("Python is " + x)
#
#myfunc()
#
#x = "awesome"
#
#def myfunc2():
#    x = "fantastic" #Vars defined in a function only work in that function
#    print("Python is " + x)
#
#myfunc2()
#print("Python is " + x)
#
#def myfunc3():
#    global x # Indicates that the variable belongs in the global scope
#    x = "fantastic"
#
#myfunc3()
#
#print("Python is " + x)
#
#
#
#Data Types:
#Text Type	    | str                           | x = "Hello World"
#Numeric Types	| int, float, complex           | x = 20 x = 20.5 x = 1j
#Sequence Types	| list, tuple, range            | x = ["apple", "banana", "cherry"] x = ("apple", "banana", "cherry") x = range(6)
#Mapping Type	|                               | x = {"name" : "John", "age" : 36}
#Set Types       | set, frozenset                | x = {"apple", "banana", "cherry"} x = frozenset({"apple", "banana", "cherry"})
#Boolean Type	| bool                          | x = True
#Binary Types	| bytes, bytearray, memoryview  | x = b"Hello" x = bytearray(5) x = memoryview(bytes(5))
#
#x = 5
#print(type(x))
#
#x = 35e3
#y = 12E4
#z = -87.7e100
#
#print(x)
#print(y)
#print(z)
#
#x = 1 #This is an integer
#y = 2.8 #This is a float
#z = 1j #This is a complex
#
#a = float(x) #This creates a float variable from a integer
#b = int(y) #This creates an integer variable from a float
#c = complex(x) #This creates a complex from a integer
#
#print(a)
#print(b)
#print(c)
#
#
#import random
#print(random.randrange(1, 10))
#
#x = int(1)
#y = int(1.4)
#z = int("1")
#These are all the same integer values
#
#'hello' is the same as "hello"
#
#a = '''this is a 
#multiline string
#I wonder how this prints'''
#print(a)
#
#
#
#a = "Hello, World!", "Goodbye, World!", "Goodnight, World!", "Welcome, World!", "Good morning, World!"
#print(a[0])
#print(a[2:5])
#
#b = " Hello, World! "
#print(b[2:5])
#print(b[-5:-2])
#
#print(len(b))
#print(len(a[2]))
#
#print(b)
#print(b.strip())
#print(b.lower())
#print(b.upper())
#print(b.replace("H", "J"))
#print(b)
#a = b.split(",")
#print(a[1])
#
#
#txt = "The rain in Spain stays mainly in the plain"
#x = "ain" in txt
#y = "ain" not in txt
#print(x)
#print(y)
#
#
#
#a = "Hello"
#b = "World"
#c = a + " " + b
#print(c)
#
#age = 21
#txt = "My name is Zack, and I am {}"
#print(txt.format(age))
#
#quantity = 3
#itemno = 567
#price = 49.95
#myorder = "I want {} pieces of item {} for {} dollars."
#print(myorder.format(quantity, itemno, price))
#myorder2 = "I want {2} pieces of item {0} for {1} dollars."
#print(myorder2.format(quantity, itemno, price))
#
#
#
#
#
#\'	    Single Quote	
#\\	    Backslash	
#\n	    New Line	
#\r	    Carriage Return	
#\t	    Tab	
#\b	    Backspace	
#\f	    Form Feed	
#\ooo	Octal value	
#\xhh	Hex value
#txt = "We are the so-called \"Vikings\" from the north."
#print(txt)
#
#capitalize()	|Converts the first character to upper case
#casefold()	    |Converts string into lower case
#center()	    |Returns a centered string
#count()	        |Returns the number of times a specified value occurs in a string
#encode()	    |Returns an encoded version of the string
#endswith()	    |Returns true if the string ends with the specified value
#expandtabs()	|Sets the tab size of the string
#find()	        |Searches the string for a specified value and returns the position of where it was found
#format()	    |Formats specified values in a string
#format_map()	|Formats specified values in a string
#index()	        |Searches the string for a specified value and returns the position of where it was found
#isalnum()	    |Returns True if all characters in the string are alphanumeric
#isalpha()	    |Returns True if all characters in the string are in the alphabet
#isdecimal()	    |Returns True if all characters in the string are decimals
#isdigit()	    |Returns True if all characters in the string are digits
#isidentifier()	|Returns True if the string is an identifier
#islower()	    |Returns True if all characters in the string are lower case
#isnumeric()	    |Returns True if all characters in the string are numeric
#isprintable()	|Returns True if all characters in the string are printable
#isspace()	    |Returns True if all characters in the string are whitespaces
#istitle()	    |Returns True if the string follows the rules of a title
#isupper()	    |Returns True if all characters in the string are upper case
#join()	        |Joins the elements of an iterable to the end of the string
#ljust()	        |Returns a left justified version of the string
#lower()	        |Converts a string into lower case
#lstrip()	    |Returns a left trim version of the string
#maketrans()	    |Returns a translation table to be used in translations
#partition()	    |Returns a tuple where the string is parted into three parts
#replace()	    |Returns a string where a specified value is replaced with a specified value
#rfind()	        |Searches the string for a specified value and returns the last position of where it was found
#rindex()	    |Searches the string for a specified value and returns the last position of where it was found
#rjust()	        |Returns a right justified version of the string
#rpartition()	|Returns a tuple where the string is parted into three parts
#rsplit()	    |Splits the string at the specified separator, and returns a list
#rstrip()	    |Returns a right trim version of the string
#split()	        |Splits the string at the specified separator, and returns a list
#splitlines()	|Splits the string at line breaks and returns a list
#startswith()	|Returns true if the string starts with the specified value
#strip()	        |Returns a trimmed version of the string
#swapcase()	    |Swaps cases, lower case becomes upper case and vice versa
#title()	        |Converts the first character of each word to upper case
#translate()	    |Returns a translated string
#upper()	        |Converts a string into upper case
#zfill()	        |Fills the string with a specified number of 0 values at the beginning
#
#
#
#print(10 > 9)
#print(10 == 9)
#print(10 < 9)
#
#a = 200
#b = 33
#
#if b > a:
#    print("b is greater than a")
#else:
#    print("b is not greater than a")
# 
#print(bool("Hello"))
#print(bool(15)) 
#
#
#x = "Hello"
#y = 15
#
#print(bool(x))
#print(bool(y))
#
#def myFunction() :
#    return True
#
#if myFunction():
#    print("YES!")
#else:
#    print("NO!")
#
#x = 200
#print(isinstance(x,int))

#print(10 + 5)
#   Operator        |Name                                                                               |Example
#      +	        |Addition	                                                                        |x + y	
#      -	        |Subtraction	                                                                    |x - y	
#      *	        |Multiplication	                                                                    |x * y	
#      /	        |Division	                                                                        |x / y	
#      %	        |Modulus	                                                                        |x % y	
#      **	        |Exponentiation	                                                                    |x ** y	
#      //	        |Floor division	                                                                    |x // y
#      =	        |  x = 5	                                                                        |x = 5	
#      +=	        |  x += 3	                                                                        |x = x + 3	
#      -=	        |  x -= 3	                                                                        |x = x - 3	
#      *=	        |  x *= 3	                                                                        |x = x * 3	
#      /=	        |  x /= 3	                                                                        |x = x / 3	
#      %=	        |  x %= 3	                                                                        |x = x % 3	
#      //=	        |  x //= 3	                                                                        |x = x // 3	
#      **=	        |  x **= 3	                                                                        |x = x ** 3	
#      &=	        |  x &= 3	                                                                        |x = x & 3	
#      |=	        |  x |= 3	                                                                        |x = x | 3	
#      ^=	        |  x ^= 3	                                                                        |x = x ^ 3	
#      >>=	        |  x >>= 3	                                                                        |x = x >> 3	
#      <<=	        |  x <<= 3	                                                                        |x = x << 3
#==	                |Equal	                                                                            |x == y	
#!=	                |Not equal	                                                                        |x != y	
#>	                |Greater than	                                                                    |x > y	
#<	                |Less than	                                                                        |x < y	
#>=	                |Greater than or equal to	                                                        |x >= y	
#<=	                |Less than or equal to	                                                            |x <= y
#and                |Returns True if both statements are true	                                        |x < 5 and  x < 10	
#or	                |Returns True if one of the statements is true	                                    |x < 5 or x < 4	
#not                |Reverse the result, returns False if the result is true	                        |not(x < 5 and x < 10)
#is                 |Returns True if both variables are the same object	                                |x is y	
#is                 |not	Returns True if both variables are not the same object	                    |x is not y
#in                 |Returns True if a sequence with the specified value is present in the object	    |x in y	
#notin	            |Returns True if a sequence with the specified value is not present in the object	|x not in y
#& 	                |AND	                                                                            |Sets each bit to 1 if both bits are 1
#|	                |OR	                                                                                |Sets each bit to 1 if one of two bits is 1
#^	                |XOR	                                                                            |Sets each bit to 1 if only one of two bits is 1
#~ 	                |NOT	                                                                            |Inverts all the bits
#<<	                |Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
#>>	                |Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off


#thislist = ["apple", "banana", "cherry"]
#print(thislist)
#
#thatlist = ["apple", "banana", "cherry", "apple", "cherry"]
#print(thatlist)
#
#print(len(thatlist))
#
#mylist = list(("cat", "dog", "bird"))
#print(mylist)
#print(mylist[-1])
#print(thatlist[2:5])

#fruitlist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
#print(fruitlist[2:])
#print(fruitlist[-4:-1])
#if "apple" in fruitlist:
#    print("Yes, 'apple' is in the frutislist")

#thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
#thislist[1:3] = ["blackcurrant", "watermelon"]
#print(thislist)
#
#thislist.insert(6, "watermelon")
#print(thislist)
#
#thislist.append("cherry")
#print(thislist)
#
#tropical = ["mango", "pineapple", "papaya"]
#thislist.extend(tropical)
#print(thislist)
#
#thistuple= ("kiwi", "orange")
#thislist.extend(thistuple) #You can extend tuples dictionaries and sets into lists
#print(thislist)

#thislist = ["apple", "banana", "cherry", "mango", "pineapple", "papaya", "banana"]
#thislist.remove("cherry")
#print(thislist)
#
#thislist.pop(2)
#print(thislist)
#
#del thislist[3]
#print(thislist)
#
#thislist.clear()
#print(thislist)

#thislist = ["apple", "banana", "cherry", "mango", "pineapple", "papaya", "banana"]
#for x in thislist:
#  print(x)
#  
#for i in range(len(thislist)):
#    print(thislist[i])
#
#i = 0
#while i < len(thislist):
#    print(thislist[i])
#    i = i + 1
#    
#[print x for x in thislist]
#
#thislist = ["apple", "banana", "cherry", "mango", "pineapple", "papaya", "banana"]
#
#while "banana" in thislist:
#    thislist.remove("banana")
#
#print(thislist)
#
#fruits = ["apple", "banana", "cherry", "mango", "pineapple", "papaya", "banana"]
#newlist = []
#
#for x in fruits:
#    if "a" in x:
#        newlist.append(x)
#        
#print(newlist)
#
#newlist = [x for x in fruits if "a" in x] #newlist = [expression for item in iterable if condition == True]
#print(newlist)
#
#newlist = [x for x in fruits if x != "apple"] #If x is not apple add to new list
#print(newlist)
#
#newlist = fruits
#print(newlist)
#
#newlist = [x for x in range(10)]
#print(newlist)
#
#newlist = [x for x in range(10) if x < 5]
#print(newlist)
#
#newlist = [x.upper() for x in fruits]
#print(newlist)
#
#newlist = ['hello' for x in fruits]
#print(newlist)
#
#newlist = [x if x != "banana" else "orange" for x in fruits]
#print(newlist)
#
#fruits = ["apple", "Banana", "cherry", "mango", "pineapple", "papaya", "banana"] #Uppercase is sorted first
#fruits.sort(key = str.lower) #Makes the sort case insensitive
#print(fruits)
#
#thislist = [100, 50, 65, 82, 23]
#thislist.sort(reverse = True)
#print(thislist)
#
#def myfunc(n):
#    return abs(n-50)
#
#thislist.sort(key = myfunc)
#print(thislist)
#
#fruits.reverse()
#print(fruits)
#
#thislist = ["apple", "banana", "cherry"]
#mylist = thislist.copy()
#print(mylist)
#
#mylist = list(thislist)
#print(mylist)
#
#list1 = ["a", "b", "c"]                                #These all do the same thing
#list2 = [1, 2, 3]                                      #These all do the same thing
#                                                       #These all do the same thing
#list3 = list1 + list2                                  #These all do the same thing
#print(list3)                                           #These all do the same thing
#                                                       #These all do the same thing
#for x in list2:                                        #These all do the same thing
#    list1.append(x)                                    #These all do the same thing
#print(list1)                                           #These all do the same thing
#                                                       #These all do the same thing
#list2.extend(list1)                                    #These all do the same thing
#print(list2)                                           #These all do the same thing

#append()	|Adds an element at the end of the list
#clear()	|Removes all the elements from the list
#copy()	    |Returns a copy of the list
#count()	|Returns the number of elements with the specified value
#extend()	|Add the elements of a list (or any iterable), to the end of the current list
#index()	|Returns the index of the first element with the specified value
#insert()	|Adds an element at the specified position
#pop()	    |Removes the element at the specified position
#remove()	|Removes the item with the specified value
#reverse()	|Reverses the order of the list
#sort()	    |Sorts the list
#
#fruits = ["apple", "banana", "cherry"]
#print(fruits[1])
#
#thistuple = ("apple", "banana", "cherry", "orange", "apple")
#print(thistuple)
#print(len(thistuple))
#
#thistuple = ("apple",) #Tuples with one item need a comma at the end or they will not be recgonized as a tuple
#print(type(thistuple))
#
#tuple1 = ("apple", "banana", "cherry")
#tuple2 = (1, 5, 7, 9, 3)
#tuple3 = (True, False, False)
#tuple4 = ("abc", 34, True, 40, "male")
#
#print(type(tuple4))
#thistuple = tuple(("apple", "banana", "cherry"))
#print(thistuple)
#
#thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
#print(thistuple[1])
#print(thistuple[-1])
#print(thistuple[2:5])
#print(thistuple[:4])
#print(thistuple[2:])
#print(thistuple[-4:-1])
#
#if "apple" in thistuple:
#    print("Yes, 'apple' is in the fruits tuple")
#
#x = ("apple", "banana", "cherry")      #This is to convert a tuple to a list to edit an item then back to a tuple I have no idea why anyone would do this
#y = list(x)                            #This is to convert a tuple to a list to edit an item then back to a tuple I have no idea why anyone would do this
#y[1] = "kiwi"                          #This is to convert a tuple to a list to edit an item then back to a tuple I have no idea why anyone would do this
#x = tuple(y)                           #This is to convert a tuple to a list to edit an item then back to a tuple I have no idea why anyone would do this
#                                       #This is to convert a tuple to a list to edit an item then back to a tuple I have no idea why anyone would do this
#print(x)                               #This is to convert a tuple to a list to edit an item then back to a tuple I have no idea why anyone would do this
#
#fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
#
#(green, yellow, *red) = fruits
#
#print(green)
#print(yellow)
#print(red)
#
#thistuple = ("apple", "banana", "cherry")
#for x in thistuple:
#    print(x)
#    
#for i in range(len(thistuple)):
#    print(thistuple[i])
#    
#i = 0 
#while i < len(thistuple):
#    print(thistuple[i])
#    i = i + 1
#
#tuple1 = ("a", "b", "c")
#tuple2 = (1, 2, 3)
#
#tuple3 = tuple1 + tuple2
#print(tuple3)
#
#fruits = ("apple", "banana", "cherry")
#mytuple = fruits * 2
#
#print(mytuple)
#
#count()	|Returns the number of times a specified value occurs in a tuple
#index()	|Searches the tuple for a specified value and returns the position of where it was found
#
#thisset = {"apple", "banana", "cherry", "apple"} #This is unordered and will appear in a random order everytime you call it and duplicate values are ingnored
#print(thisset)
#print(len(thisset))
#
#thatset = set(("apple", "banana", "cherry"))
#print(thatset)
#
#thisset = {"apple", "banana", "cherry"}
#
#for x in thisset:
#    print(x)
#
#print("banana" in thisset)
#
#thisset.add("orange")
#
#print(thisset)
#
#tropical = {"pineapple", "mango", "papaya"}
#
#thisset.update(tropical)
#
#print(thisset)
#
#mylist = ["kiwi", "orange"]
#
#thisset.update(mylist)
#
#print(thisset)

#thisset = {"apple", "banana", "cherry"}
#
#thisset.remove("banana")
#thisset.discard("guava") #This will not error if the item doesn't exist
#
#
#print(thisset)
#
#thisset.pop()
#
#print(thisset)
#
#thisset.clear() #no Values left
#
#print(thisset)
#
#del thisset #destroys set
#
#print(thisset)
#
#set1 = {"a", "b", "c"}
#set2 = {1, 2, 3}
#
#set3 = set1.union(set2)
#print(set3)
#
#set1.update(set2)
#print(set1)
#
#x = {"apple", "banana", "cherry"}
#y = {"google", "microsoft", "apple"}
#
#z = x.intersection(y)  #new set with matching items
#
#print(z)
#
#x.intersection_update(y) #updates set with matching items
#
#print(x)
#
#x.symmetric_difference_update(y) #updates set with nonmatching items
#print(x)
#
#z = x.symmetric_difference(y) #new set with nonmatching items
#print(z)

#add()	                        |Adds an element to the set
#clear()	                    |Removes all the elements from the set
#copy()	                        |Returns a copy of the set
#difference()	                |Returns a set containing the difference between two or more sets
#difference_update()	        |Removes the items in this set that are also included in another, specified set
#discard()	                    |Remove the specified item
#intersection()	                |Returns a set, that is the intersection of two other sets
#intersection_update()	        |Removes the items in this set that are not present in other, specified set(s)
#isdisjoint()	                |Returns whether two sets have a intersection or not
#issubset()	                    |Returns whether another set contains this set or not
#issuperset()	                |Returns whether this set contains another set or not
#pop()	                        |Removes an element from the set
#remove()	                    |Removes the specified element
#symmetric_difference()	        |Returns a set with the symmetric differences of two sets
#symmetric_difference_update()	|inserts the symmetric differences from this set and another
#union()	                    |Return a set containing the union of sets
#update()	                    |Update the set with the union of this set and others
#
#thisdict= { #will error if there are duplicates
#    "brand": "ford",
#    "model": "Mustang",
#    "year": 1964,
#    "colors": ["red", "white", "blue"]
#}#left side is keys right side it items key:items
#print(thisdict)
#print(thisdict["brand"])
#print(len(thisdict))
#x = thisdict["model"]
#print(x)
#z = thisdict.get("colors")
#print(z)
#y = thisdict.keys()
#print(y)
#thisdict["colors"] = "white"
#print(y)
#w = thisdict.values()
#print(w)
#q = thisdict.items()
#print(q)
#if "model" in thisdict:
#    print("Yes, 'model' is one of the keys in the thisdict dictionary")
#
#thisdict = {
#    "brand": "Ford",
#    "model": "Mustang",
#    "year": 1964
#}
#thisdict["year"] = 2020             #This is the same thing
#thisdict.update({"year": 2020})     #This is the same thing
#
#
#x = thisdict.items()
#print(x)
#
#thisdict = {
#    "brand": "Ford",
#    "model": "Mustang",
#    "year": 1964
#}
#thisdict.update({"color": "red"})
#print(thisdict)
#
#thisdict = {
#    "brand": "Ford",
#    "model": "Mustang",
#    "year": 1964
#}
#thisdict.pop("model")
#print(thisdict)
#thisdict.popitem()
#print(thisdict)
#del thisdict["brand"]
#print(thisdict)
#del thisdict
#thisdict = {
#    "brand": "Ford",
#    "model": "Mustang",
#    "year": 1964
#}
#print(thisdict)
#thisdict.clear()
#print(thisdict)
#
#thisdict = {
#    "brand": "Ford",
#    "model": "Mustang",
#    "year": 1964
#}
#for x in thisdict:
#    print(x)
#
#for x in thisdict:              #Same shit different shape
#    print(thisdict[x])          #Same shit different shape
#                                #Same shit different shape
#for x in thisdict.values():     #Same shit different shape
#    print(x)                    #Same shit different shape
#
#for x in thisdict.keys():
#    print(x)
#
#for x, y in thisdict.items():
#    print(x, y)
#
#thisdict = {
#    "brand": "Ford",
#    "model": "Mustang",
#    "year": 1964
#}
#mydict = thisdict.copy()    #Why are there 2 ways to do the same thing
#print(mydict)               #Why are there 2 ways to do the same thing
#                            #Why are there 2 ways to do the same thing
#thatdict = dict(thisdict)   #Why are there 2 ways to do the same thing
#print(mydict)               #Why are there 2 ways to do the same thing

#thatfamily = {
#    "child1" : {
#        "name" : "Emil",
#        "year" : 2004
#    },
#    "child2" : {
#        "name" : "Tobias",
#        "year" : 2007
#    },
#    "child3" : {
#        "name" : "Linus",
#        "year" : 2011
#    }
#}
#
#child1 = {
#    "name" : "Emil",
#    "year" : 2004
#}
#child2 = {
#    "name" : "Tobias",
#    "year" : 2007
#}
#child3 = {
#    "name" : "Linus",
#    "year" : 2011
#}
#
#myfamily = {
#    "child1" : child1,
#    "child2" : child2,
#    "child3" : child3
#}
#
#print(myfamily)
#
#clear()	    |Removes all the elements from the dictionary
#copy()	        |Returns a copy of the dictionary
#fromkeys()	    |Returns a dictionary with the specified keys and value
#get()	        |Returns the value of the specified key
#items()	    |Returns a list containing a tuple for each key value pair
#keys()	        |Returns a list containing the dictionary's keys
#pop()	        |Removes the element with the specified key
#popitem()	    |Removes the last inserted key-value pair
#setdefault()	|Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
#update()	    |Updates the dictionary with the specified key-value pairs
#values()	    |Returns a list of all the values in the dictionary
#
#a = 33
#b = 200
#if b > a:
#    print("b is greater than a")
#
#a = 33
#b = 33
#if b > a:
#    print("b is greater than a")
#elif a == b:                        #This is else if but shorter for some reason
#    print("a and b are equal")
#
#a = 200
#b = 33
#if b > a :
#    print("b is greater than a")
#elif a == b:
#    print("a and b are equal")
#else:
#    print("a is greater than b")
#
#if b > a:
#    print("b is greater than a")
#else:
#    print("b is not greater than a")
#
#if a > b: print("a is greater than b")
#
#print("A") if a > b else print("b")
#
#print("A") if a > b else print ("=") if a == b else print ("B")
#
#a = 200
#b = 33
#c = 500
#if a > b and c > a:
#    print("Both conditions are True")
#
#if a > b or a > c:
#    print("At least one of the conditions is True")
#    
#x = 41
#
#if x > 10:
#    print("Above ten,")
#    if x > 20:
#        print("and also above 20!")
#    else:
#        print("but not above 20.")
#
#a = 33
#b = 200
#    if b > a:       #Need to have pass if you have an empty if statement
#        pass        #Need to have pass if you have an empty if statement
#
#fruit = ["apple"]
#i = 1
#while i < 30:
#    fruit.extend(fruit)
#    print(len(fruit))
#    i += 1
#
#i = 1
#while i < 6:
#    print(i)
#    if i ==3:
#        break
#    i +=1
#
#i = 0
#while i > 6:
#    i += 1
#    if i ==3:
#        continue
#    print(i)
#
#i = 1 
#while i > 6:
#    print(i)
#    i += 1
#else:
#    print("i is no longer less than 6")
#
#fruits = ["apple", "banana", "cherry"]
#for x in fruits:
#    print(x)
#
#for x in "banana":
#    print(x)
#
#for x in fruits:
#    print(x)
#    if x == "banana":
#        break
#
#for x in fruits:
#    if x == "banana":
#        break
#    print(x)
#    
#for x in fruits:        #Continue stops that iteration where it stands and moves to the next one
#    if x == "banana":   #Continue stops that iteration where it stands and moves to the next one
#        continue        #Continue stops that iteration where it stands and moves to the next one
#    print(x)            #Continue stops that iteration where it stands and moves to the next one
#
#for x in range(6):
#    print(x)
#    
#for x in range (2, 6):
#    print(x)
#    
#for x in range(2, 30, 3):
#    print(x)
#    
#for x in range(6):
#    print(x)
#else:
#    print("Finally finished!")
#    
#adj = ["red", "big", "tasty"]
#fruits = ["apple", "banana", "cherry"]
#
#for x in adj:
#    for y in fruits:
#        print(x, y)
#    
#for x in [0, 1, 2]:
#    pass
#
#def my_function():
#    print("Hello from a function")
#my_function()
#
#def my_function(fname):
#    print(fname + " Refsnes")
#my_function("Emil")
#my_function("Tobias")
#my_function("Linus")
#
#def my_function(fname, lname):
#    print(fname + " " + lname)
#
#my_function("Zack", "Blanke")
#
#def my_function(*kids):
#    print("The youngest child is " + kids[2])
#    
#my_function("Zack", "Brooke", "Linus")
#
#def my_function(child3, child2, child1):
#    print("The youngest child is " + child3)
#    
#my_function(child1 = "Zack", child2 = "Brooke", child3 = "Linus")
#
#def my_function(**kid):
#    print("His last name is " + kid["lname"])
#    
#my_function(fname = "Zack", lname = "Blank")
#
#def my_function(country = "Norway"):
#    print("I am from " + country)
#    
#my_function("Sweden")
#my_function("India")
#my_function()
#my_function("Brazil")
#
#def my_function(food):
#    for x in food:
#        print(x)
#
#fruits = ["apple", "banana", "cherry"]
#
#my_function(fruits)
#        
#def my_function(x):
#    return 5 * x
#
#print(my_function(3))
#print(my_function(5))
#print(my_function(9))
#
#def myfunction():
#    pass
#
#def tri_recursion(k):
#    if(k > 0):
#        result = k + tri_recursion(k-1)
#        print(result)
#    else:
#        result = 0
#    return result
#
#print("\n\nRecustion Example Results")
#tri_recursion(6)
#
#x = lambda a : a + 10
#print(x(5))
#
#x = lambda a, b : a * b
#print(x(5, 6))
#
#x = lambda a, b, c : a + b + c
#print(x(5, 8, 2))
#
#def myfunc(n):
#    return lambda a : a * n
#
#mydoubler = myfunc(2)
#mytripler = myfunc(3)
#
#print(mydoubler(11))
#print(mytripler(11))
#
#cars = ["Ford", "Volvo", "BMW", "Volvo"]
#
#x = cars[0]
#print(x)
#
#cars[0] = "Toyota"
#x = cars[0]
#print(x)
#
#x = len(cars)
#print(x)
#
#for x in cars:
#    print(x)
#
#cars.append("Honda")
#print(cars)
#
#cars.pop(1)
#print(cars)
#
#cars.remove("Volvo")
#print(cars)
#
#append()	|Adds an element at the end of the list
#clear()	|Removes all the elements from the list
#copy()	    |Returns a copy of the list
#count()	|Returns the number of elements with the specified value
#extend()	|Add the elements of a list (or any iterable), to the end of the current list
#index()	|Returns the index of the first element with the specified value
#insert()	|Adds an element at the specified position
#pop()	    |Removes the element at the specified position
#remove()	|Removes the first item with the specified value
#reverse()	|Reverses the order of the list
#sort()	    |Sorts the list
#
#class MyClass:
#    x = 5
#
#p1 = MyClass()
#print(p1.x)
#
#class Person:
#    def __init__(self, name, age):
#        self.name = name    
#        self.age = age
#
#    def myfunc(self):
#        print("Hello me name is " + self.name + ", I am " + format(self.age) + " years old")
#
#p1 = Person("John", 36)
#p1.myfunc()
#
#p1.age = 40
#p1.myfunc()
#
#del p1.age
#p1.myfunc()
#
#del p1
#p1.myfunc()
#
#class Person:
#    def __init__(self, fname, lname):
#        self.firstname = fname
#        self.lastname = lname
#
#    def printname(self):
#        print(self.firstname, self.lastname)
#
##Use ther Person class to create an object, and then execute the printname method:
#
#x = Person("John", "Doe")
#x.printname()
#
#class Student(Person):
#    pass
#x = Student("Mike", "Olsen")
#x.printname()
#











































