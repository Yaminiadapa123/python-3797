student_name = input("Enter student name: ")
student_grade = int(input("Enter student grade level: "))
academic_toppers_status = input("Academic Status (yes/no): ").lower()
base_tuition_fee = int(input("Base tuition fee: "))

discount_percentage = 0
add_discount = 0  # Ensure always defined

# Validate grade
if 1 <= student_grade <= 12:
    print("Valid student grade")
else:
    print("Student grades are invalid")

# Main discount logic
if 9 <= student_grade <= 12:
    if academic_toppers_status == "yes":
        discount_percentage = 20
    else:
        discount_percentage = 10
elif 6 <= student_grade <= 8:
    discount_percentage = 5
elif student_grade < 6:
    discount_percentage = 0

# Additional special grade discounts
if student_grade == 10:
    add_discount = 3
elif student_grade == 12:
    add_discount = 5

# Total and final calculation
total_discount = discount_percentage + add_discount
discount_amount = base_tuition_fee * (total_discount / 100)
final_fee = base_tuition_fee - discount_amount

# Output
print(f"Student Name: {student_name}")
print(f"Student Grade: {student_grade}")
print(f"Academic Toppers Status: {academic_toppers_status}")
print(f"Base Tuition Fee: {base_tuition_fee}")
print(f"Total Discount: {total_discount}%")
print(f"Discount Amount: {discount_amount}")
print(f"Final Tuition Fee: {final_fee}")
