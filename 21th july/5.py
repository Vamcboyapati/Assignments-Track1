number=123
mul=1
while number>0:
  rem=number%10
  mul*=rem
  number=number//10
print(mul)