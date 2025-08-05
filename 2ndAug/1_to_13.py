# 1
def add(a,b):
  print(a+b)

add(11,12)

# 2

def sqr(num):
  print(num**2)
sqr(5)

# 3

def odd_even(num1):
  print('Even' if num1%2==0 else 'odd')
odd_even(23)

# 4

def fact(num):
  fact=1
  if num==1:
    return 1
  for i in range(2,num+1):
    fact*=i
  print(fact)
fact(3)

# 5

def greatest_of_3(a,b,c):
  if a>b and a>c:
    print(a)
  elif b>a and b>c:
    print(b)
  else:
    print(c)
greatest_of_3(2,3,4)

# 6

def count_vowels(strng):
  count=0
  for j in strng:
    if j in 'aeiouAEIOU':
      count+=1
  print(count)
count_vowels('Vamsi')


# 7
def sum_list(list1):
  sum=0
  for i in list1:
    sum+=i
  print(sum)

list1=[1,2,3,4,5]
sum_list(list1)

# 8
def rev_string(strng):
  print(strng[::-1])
rev_string('vamsi')

# 9

def polindrome_strng(strng):
  if strng==strng[::-1]:
    print('Given string is polindrome')
  else:
    print('Given string is not polindrome')

polindrome_strng('Vamsi')

# 10

def evennum_of_list(list1):
  for i in list1:
    if i%2==0:
      print(i,end=' ')
  print()
list1=[1,2,3,4,5,6]
evennum_of_list(list1)


# 11

def area_of_circle(r):
  print(3.14*(r**2))

area_of_circle(2)

# 12

def len_of_string(strng):
  count=0
  for i in strng:
    count+=1
  print(count)

len_of_string('vamsi')

# 13

def sum_of(*numbers):
  print(sum(numbers))

sum_of(1,2,3,4,5)