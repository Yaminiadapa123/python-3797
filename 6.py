car_name = "Mahindra"
actual_price = 1700000
down_payment = 160000
interest_rate = 9
loan_years = 4  

loan_amount = actual_price - down_payment

# Calculate EMI components
R = interest_rate / (12 * 100)  # Monthly interest rate
N = loan_years * 12             # Loan period in months

# EMI formula
EMI = loan_amount * R * (1 + R) ** N / ((1 + R) ** N - 1)
total_payable = EMI * N
total_interest = total_payable - loan_amount

# Output without using round()
print(f"\nCar Name            : {car_name}")
print(f"Actual Price        : ₹{actual_price:.2f}")
print(f"Down Payment        : ₹{down_payment:.2f}")
print(f"Loan Amount         : ₹{loan_amount:.2f}")
print(f"Monthly EMI         : ₹{EMI:.2f}")
print(f"Total Payable       : ₹{total_payable:.2f}")
print(f"Total Interest Paid : ₹{total_interest:.2f}")
