str='helloworld'
print(str[2:])
print(str[:-1])
print(str[:])

#Data = collection of Information
#Datatypes=Structures in which your data
#Numeric datatypes=integer,float,complex.(for numeric values)
#Boolean datatypes = True or false.
print(2==4)
#sequence datatypes = (one followed by another)#string,list,tuple,set
#string is a sequence datatype
#ordered collection of heterogenous (different datatypes)elements.
list1=[1,2,3,4,5,['hello','world'],8.5]
print(list1[-2][0])
#list is mutable i.e we can change the elements positions
#tuple is immutable data type,once we declare tuple ,we can't change the elements of the tuple(fast relative to list)
tuple1=(1,2,3,4,5)

#set is unordered and mutable (since it is unordered ,we can't do indexing theough sets)
#string is immutable

str2='abdul'
str2='kalam'
print(str2)
#range is used to help indexing 
#dictionary(collecton of key,value pairs)
dic1={
  1:"mahesh",
  2:"ntr",
  3:"allu",
  4:"prabhas"
}
for key,values in dic1.items():
  print(f"{key}:{values}")
  
