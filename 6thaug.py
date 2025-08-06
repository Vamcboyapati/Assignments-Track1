def check_right_angle_triangle(a,b,c):
  sides=sorted([a,b,c])
  a,b,c=sides
  if a+b<=c:
    print('invalid triangle')
    return
  elif a**2+b**2==c**2:
    print("Given sides are from right angle triangle")
  else:
    print("Given sides are not from right angle triangle")
  
a,b,c=map(int,input("Enter the three sides of the triangle:").split(' '))
check_right_angle_triangle(a,b,c)