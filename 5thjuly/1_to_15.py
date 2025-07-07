# 1.	What is a data type in Python?
# Datatype is a structure in which the data is aligned.

# 2.	List all the data types that we have in Python?
 #Numeric(int,float,complex numbers),sequence(list,tuple),dictionary,Boolean(values(True/False)),None,Set and Frozen set

# 3.	What is the difference between mutable and immutable data types?
#Immutable data type cannot be modified after created once.
#Where as mutable datatypes can be modified after creation. 

# 4.	What is the difference between int, float, and complex?
#int: Only whole numbers.

#float: Numbers with decimal points.

#complex: Numbers with a real and imaginary part, denoted by j

# 5.	Which data type is used to represent text in Python?
#string data type is used to represent text in python

# 6.	What is the output of type(521) and type("521")?

print(type(521))
print(type("521"))
#output:
# <class 'int'>
# <class 'str'>

# 7.	What is the difference between list, tuple, and set?

# list:
# represented by []
# ordered
# mutable
# allows duplicate
# suports indexing
# tuple:
# represented by ()
# ordered
# immutable
# allows duplicate
# supports indexing
# set:
# represented by {}
# unordered
# mutable
# doesnot allow duplicate
# doesnot support indexing

# 8.	How is a dictionary different from a list?

# list is a  ordered collection of heterogenious elements
#  where as dictionary is a collection of key and value pairs

# 9.	What is the default data type of a number with a decimal point?

# The default data type of a number with a decimal point in Python is float.

# 10.	Declare variables of type int, float, string, and complex.

# Integer
a = 10

# Float
b = 3.14

# String
c = "Hello, World!"

# Complex
d = 2 + 3j

# 11.	Take any 3 datatypes examples and check type of each variable using the type() function.

a= 10
b=3.14
c=2+3j
print(type(a),type(b),type(c))
#output
#<class 'int'> <class 'float'> <class 'complex'>

# 12.	What happens if you try to add a string and an integer?

#You will get type Error
a="vamsi"
b=10
print(a+b)
#output:
#TypeError: can only concatenate str (not "int") to str

# 13.	What is the output of:
# 1.	x = [1, 2, 3]
# 2.	y = (1, 2, 3)
# 3.	z = {1, 2, 3}
# 4.	print(type(x), type(y), type(z))

x = [1, 2, 3]
y = (1, 2, 3)
z = {1, 2, 3}
print(type(x), type(y), type(z))

#output:
# <class 'list'> <class 'tuple'> <class 'set'>

# 14.	Can you change a value in a tuple once it is defined? Why or why not?

#we can't change a value in a tuple once it is defined because tuple is immutable and we can't do item assignment in tuple.

# 15.	Is reassignment possible for immutable datatypes?
#yes,Reassignment possible for immutable data types
#example
a='Hello'
a='world'
print(a)

#output:
#world (a is reassigned to world)