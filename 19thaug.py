num=int(input())
result=0
temp=num
while temp>0:
  rem=temp%10
  result+=rem**len(str(num))
  temp//=10
if result==num:
  print("given number is an armstrong number")
else:
  print("Given number is not an armstrong number")