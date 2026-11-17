

tuition_fee = float(input("Enter Tuition Fee: "))
lab_fee = float(input("Enter Lab fee: "))
lib_fee = float(input("Enter Library fee: "))
exam_fee = float(input("Enter exam fee: "))
dis_amount = float(input("Enter Discount Amount: "))

# calcuiation
total_fee = tuition_fee + lab_fee + lib_fee + exam_fee
fee_aft_diss = total_fee - dis_amount
annual_fee = fee_aft_diss * 2 
month_inst = annual_fee / 12

# printing them
print(f"Tuition Fee: {tuition_fee}")
print(f"Lab Fee: {lab_fee}")
print(f"Library Fee: {lib_fee}")
print(f"Exam Fee: {exam_fee}")
print(f"Total Fee: {total_fee}")
print(f"Discount: {dis_amount}")
print(f"Fee after Discount: {fee_aft_diss}")
print(f"Annual Fee: {annual_fee}")
print(f"Monthly Installment: {month_inst:.2f}")
