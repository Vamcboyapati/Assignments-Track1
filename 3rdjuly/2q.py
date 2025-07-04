product1_price=250
qty1=3
product2_price=420
qty2=6

subtotal=(product1_price*qty1 + product2_price*qty2)
tax=subtotal*0.18
totalcost=tax+subtotal

print("----Detailedbill----")
print(f"product 1: {qty1} x Rs{product1_price} = Rs{product1_price*qty1}")
print(f"product 2: {qty2} x Rs{product2_price} = Rs{product2_price*qty2}")
print(f"subtotal : Rs{subtotal}")
print(f"tax (18%) : Rs{tax}")
print(f"total : Rs{totalcost}")

#output:
# ----Detailedbill----
# product 1: 3 x Rs250 = Rs750
# product 2: 6 x Rs420 = Rs2520       
# subtotal : Rs3270
# tax (18%) : Rs588.6
# total : Rs3858.6



