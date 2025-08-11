def user_menu(operation):
  print("1.square 2.cube 3.exit")
  if operation=='square'or operation=='1':
    input_num=int(input("Enter a num :"))
    print(input_num**2)
  elif operation=='cubic' or operation=='2':
    input_num=int(input("Enter a num :"))
    print(input_num**3)
  else:
    print("Exit the code")

while True:
  operation=input("Enter an operation: ").lower()
  if operation=='exit' or operation=='3':
    print("Exiting")
    break
  user_menu(operation)
  
    



  