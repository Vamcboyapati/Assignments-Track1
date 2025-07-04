# 1.What is a string in Python?

#A string in python is a sequence of characters.It is enclosed by "" 0r ''.

# 2.What is indexing in a string?

# Indexing allows you to access individual characters in a string using their position. Indexing starts from 0


# 3.Given text = 'hello', what is text[0]? 

#It prints the first most character of a string i.e "h"

text='hello'
print(text[0])
# output:h

# 3 a. What will be the output of text[4]? 

#The output of text[4] is o
text='hello'
print(text[4])
# output:o

# 3 b. What does text[-1] give?

#It gives last character of a string i.e "o"
text='hello'
print(text[-1])
#output:o

# 4.If name = 'Ajay', what is the value of name[0] + name[3]? 

#The value of name[0] + name[3] is "Ay"
name="Ajay"
print(name[0]+name[3])
# output:Ay

# 4 a. What happens if you try name[10]?

#It throws IndexError i.e (index out of range)
print(name[10])
#Error:IndexError: string index out of range


# 5. Given s = 'Python', what is s[0:2]?
# "py"
s='python'
print(s[0:2])

#5 a. What does s[5:1] return?
print(s[5:1])
#empty string, because default step is forward and start > stop

# 6.Predict the output for string s =  'Python' . If the code is print(s[2: -1 :2])

#as the step is 2, It starts from t and ends with o
#As it skips the h,the output will be "to"

#7. Write code to print the last 3 letters of 'elephant'.

s='elephant'
print(s[-3])
#output:ant

# 8.How to get only the middle 3 letters from 'Science'?
s = 'Science'
print(s[2:5])  
# Output: 'ien'


# 9.What is the difference between s[2:5] and s[2:5:1]?

#Both give same output,but in the s[2:5:1] ,it clearly stated the step value of 1.
s = 'Science'
s[2:5]     
# Output: ien
s[2:5:1]   
# Output: ien