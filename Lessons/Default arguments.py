# default arguments = default value for certain perameters
# changes if the function is called with a new value; otherwise it uses default value
def net_price(list_price, discount = 0, tax = 0.05):
   return list_price * (1 - discount) * (1 - tax)

print(net_price(500, 0.1, 0))