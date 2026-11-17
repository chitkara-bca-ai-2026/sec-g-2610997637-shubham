print(f"="*40)
print(f"    SCHOOL RESULT PROCESSING    ")
print(f"="*40)
name = input("Enter student Name : ")
roll = int(input("Enter Roll Number : "))

print(f"---Enter Marks for 5 subjects (0-100)---")
sub_1 = int(input("Enter marks for subject 1: "))
sub_2 = int(input("Enter marks for subject 2: "))
sub_3 = int(input("Enter marks for subject 3: "))
sub_4 = int(input("Enter marks for subject 4: "))
sub_5 = int(input("Enter marks for subject 5: "))

# calculation
total_marks = float(sub_1 + sub_2 + sub_3 + sub_4 + sub_5)
percentage =total_marks / 500 *100

if percentage>=90 and percentage<=100 :
    Result  = "pass"
    Grade   = "A+"
    Remarks = "Outstanding"

elif percentage>=80 and percentage<=89 :
    Result  = "pass"
    Grade   = "A"
    Remarks = "Excellent"

elif percentage>=70 and percentage<=79 :
    Result  = "pass"
    Grade   = "B"
    Remarks = "Very Good"  

elif percentage>=60 and percentage<=69 :
    Result  = "pass"
    Grade   = "c"
    Remarks = "Good"

elif percentage>=50 and percentage<=59 :
    Result  = "pass"
    Grade   = "D"
    Remarks = "satisfactory"   

elif percentage>=40 and percentage<=49 :
    Result  = "pass"
    Grade   = "E"
    Remarks = "Bad"

else:
    Result  = "Fail"
    Grade   = "F"
    Remarks = "Very Bad"

print(f"="*40)
print(f"    STUDENT REPORT CARD     ")
print(f"="*40)
print(f"Student Name : {name}")    
print(F"Roll number  : {roll}")
print(f"-"*40)

print(f"Total Marks  : {total_marks}/500.0")
print(f"Percentage   : {percentage:.2f}%")
print(f"Result       : {Result}")
print(f"Grade        : {Grade}")
print(f"Remarks      : {Remarks}")

print(f"="*40)

