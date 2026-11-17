import sys
print(f"="*40)
print(f"        CALENDER VERIFICATION SYSTEM        ")
print(f"="*40)

year = int(input("Enter the year: "))
print(f"-"*40)
if year <=0:
    print("invalid enter a valid year")
    sys.exit() # stop doing and exit agar if is incorrect 

if year % 400 ==0:
    print(f"Status: LEAP YEAR")
    print(f"Days in year: 366 days")
    print(f"Days in february: 29 days ")
    print(f"Reason: divisible by 400 not a century year")
    
elif year % 100==0:
    print(f"Status: common year")
    print(f"Days in year: 365 days ")
    print(f"Days in february: 28 days")
    print(f"Reason: not divisible by 400 ")

elif year % 4==0:
    print(f"Status: LEAP YEAR")
    print(f"Days in year: 366 days")
    print(f"Days in february: 29 days ")
    print(f"Reason: divisible by 4 not a century year")

else:
    print(f"Status: common year")
    print(f"DAys in year: 365 days ")
    print(f"Days in febuary: 28 days")
    print(f"Reason: not divisible by 4 ")

print(f"-"*40)

