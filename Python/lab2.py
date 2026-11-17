

name = input("enter employee name: ")
print(type(name))
employee_id = (input("enter employee id:"))
print(type(employee_id))
salary = int(input("enter salary:"))
print(type(salary))
department = input("enter Department:")
print(type(department))
active = bool(input("Is the employee active? (yes/no):"))
print(type(active))



if active == "yes":
    print("true", active)
else:
    print("false", active)


print(f"Name       : {name}" )
print(f"ID         : {employee_id}")
print(f"Salary     : {salary:.2f}")
print(f"Department : {department}" )
print(f"Active     : {active}") # proble
