# 1.	Add an integer and float. What is the result’s type?

a=2+2.2
print(a)
print(type(a))
#output:
#4.2
#<class 'float'>

# 2.	Create a string and access its:

# string1="10000 coders"

# 1.	First character
#string1[0]
# 2.	Last character
#string1[-1]
# 3.	A substring from index 2 to 5
#string1[2:6]

# 3.	Concatenate two strings and print the result.

a='vam'
b='c'
result=a+b
print(result)

# 4.	Define list. What are the difference between List and Tuple.

#list is a ordered collection of heterogenous elements

# list is mutable ,represented by []and tuple is immutable,represented by ().

# 5.	Write a programme to print a list in reverse order.

list1=[1,2,3,4,5,6]
print(list1[::-1])
#output:
#[6, 5, 4, 3, 2, 1]

# 6.	Create a tuple of 4 elements. Print the first and last element.
tuple=(1,2,3,4)
print(tuple[0])
print(tuple[-1])

# output:
# 1
# 4

# 7.	Try changing a value in a tuple. What happens?
tuple[2]=4
#TypeError: 'tuple' object does not support item assignment

# 8.	Create a dictionary of 3 students with their marks. Print the dictionary.

marks={'sai':57,'vamsi':35,'visw':80}
print(marks)
#output:
#{'sai': 57, 'vamsi': 35, 'visw': 80}

# 9.	Access the marks of one student using their name.

print(marks['vamsi'])
# output:
#35

# 10.	Update the marks of an existing student.
marks['vamsi']=30
print(marks['vamsi'])
#output:
#30

# 11.	Can I access a key using a value in a dictionary.
# No,You can't access a key using a value in a dictionary.

# 12.	 Can I have duplicate values and keys in a dictionary? What happens if I wanted try to duplicate key in a dictionary? 

#yes, you can have duplicate values but you can't have duplicate keys in a dictionary.If you wanted to duplicate key in a dictionary ,it will result in re-assignment of key to another value and it will print only last assigned pair by overwrite the previous one.

# 13.	Print all multiples of 17 using range. Numbers should start from -34 and end below 400.

print(list(range(-34,400,17)))

#output:
#[-34, -17, 0, 17, 34, 51, 68, 85, 102, 119, 136, 153, 170, 187, 204, 221, 238, 255, 272, 289, 306, 323, 340, 357, 374, 391]
