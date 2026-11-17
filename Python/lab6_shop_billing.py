print(f"="*40)
print(f"    CLOTHING STORE BILLING SYSTEM   ")
print("="*40)
name = input("Enter customer Name: ")
garment = input("Enter Garment Name: ")
price = float(input("Enter price of one garment: "))
no_garment = int(input("Enter Number of Garments: "))

total_amount = price * no_garment

print(f"="*40)
print(f"        BILL        ")
print(f"="*40)
print(f"Cumtomer Name   : {name}")
print(f"Garment Name    : {garment}")
print(f"Price per Unit  : {price:.1f} ")
print(f"Quentity        : {no_garment}")
print(f"Total Amount    : {total_amount:.1f}")
print(f"="*40)