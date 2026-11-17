print(f"="*40)
print(f"        DATA CONVERSION UTILITY         ")
print(f"="*40)

name = input("Enter Product Name   : ")
price = float(input("Enter Price   : "))
qu = int(input("Enter Quentity     : "))

total_price=price*qu
amount_str =str(total_price)



print(f"-"*40)
print(f"        TYPE CASTING SUMMARY        ")
print(f"-"*40)
print(f"Variable        value           Python Type     ")
print(f"-"*40)
print(f"Product_name    {name}          {type(name)}")
print(f"Price           {price}         {type(price)}")
print(f"Quentity        {qu}            {type(qu)}")
print(f"total_price     {total_price}   {type(total_price)}")
print(f"amount_str      {amount_str}    {type(amount_str)}")
print(f"-"*40)


print(f"-"*40)
print(f"                TAX INVOICE             ")
print(f"-"*40)
print(f"Product Name   : {name} ")
print(f"Price per Unit : Rs.{price:.2f}")
print(f"Quantity       : {qu}")
print(f"-"*30)
print(f"Invice Total   :Rs. {total_price:.1f}")
print("="*40)

