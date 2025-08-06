def check_valid_triangle(a,b,c):
  if a+b>c and b+c>a and c+a>b:
    print("Traingle is valid")
  else:
    print("Not valid")

check_valid_triangle(4,2,3)