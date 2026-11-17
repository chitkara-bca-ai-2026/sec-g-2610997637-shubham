from math import pow, sqrt, ceil, floor
import math
print(f"="*40)
print(f"        ENGINEERING CALCULATION TOOL        ")
print(f"="*40)
value = float(input("Enter a numercial value: "))
exponent = float(input("Enter an exponent: "))
decimal = float(input("Enter a decimal measurement: "))


print(f"---Result---")
print(f"Value   : {value:.1f}")
print(f"Exponent : {exponent:.1f}")
print(f"Power (pow) : {math.pow(value,exponent):.1f}")
print(f"Square Root (sqrt)  : {math.sqrt(value):.4f}")
print(f"Decimal value  : {decimal:.1f}")
print(f"Ceil value  : {math.ceil(decimal):.0f}") #its gives nearst upper value
print(f"Floor value  : {math.floor(decimal)}")

print(f"="*40)