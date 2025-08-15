# Get user inputs
car_name = input("Enter Car Name: ")
actual_price = float(input("Enter Actual Price (₹): "))
down_payment = float(input("Enter Down Payment (₹): "))
interest_rate = float(input("Enter Interest Rate (% per annum): "))
loan_years = int(input("Enter Loan Tenure (years): "))

# Calculate loan amount
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
