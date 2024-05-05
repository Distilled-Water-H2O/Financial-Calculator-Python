def compound_interest(principal, rate, time, period):
    """
    Calculates the future value of an investment with compound interest.
    
    Args:
        principal (float): The initial amount invested
        rate (float): The annual interest rate as a decimal (e.g., 0.05 for 5%)
        time (int): The number of years for the investment
        period (int): The number of times interest is compounded per year
    
    Returns:
        float: The future value of the investment
    """
    amount = principal * (1 + (rate / period)) ** (period * time)
    return round(amount, 2)

def present_value(future_value, rate, time, period):
    """
    Calculates the present value of a future amount.
    
    Args:
        future_value (float): The future amount
        rate (float): The annual interest rate as a decimal (e.g., 0.05 for 5%)
        time (int): The number of years
        period (int): The number of times interest is compounded per year
    
    Returns:
        float: The present value
    """
    amount = future_value / (1 + (rate / period)) ** (period * time)
    return round(amount, 2)

def annuity_future_value(payment, rate, time, period):
    """
    Calculates the future value of a series of equal payments (annuity).
    
    Args:
        payment (float): The amount of each periodic payment
        rate (float): The annual interest rate as a decimal (e.g., 0.05 for 5%)
        time (int): The number of years
        period (int): The number of times interest is compounded per year
    
    Returns:
        float: The future value of the annuity
    """
    amount = payment * ((((1 + rate / period) ** (period * time)) - 1) / (rate / period))
    return round(amount, 2)

print("Welcome to the Financial Calculator!")
print("1. Compound Interest")
print("2. Present Value")
print("3. Annuity Future Value")

while True:
    
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == '1':
        principal = float(input("Enter the principal amount: "))
        rate = float(input("Enter the annual interest rate (e.g., 0.05 for 5%): "))
        time = int(input("Enter the time in years: "))
        period = int(input("Enter the number of times interest is compounded per year: "))
        future_value = compound_interest(principal, rate, time, period)
        print(f"The future value of the investment is: {future_value}")
    
    elif choice == '2':
        future_value = float(input("Enter the future amount: "))
        rate = float(input("Enter the annual interest rate (e.g., 0.05 for 5%): "))
        time = int(input("Enter the time in years: "))
        period = int(input("Enter the number of times interest is compounded per year: "))
        present_value = present_value(future_value, rate, time, period)
        print(f"The present value is: {present_value}")
    
    elif choice == '3':
        payment = float(input("Enter the periodic payment amount: "))
        rate = float(input("Enter the annual interest rate (e.g., 0.05 for 5%): "))
        time = int(input("Enter the time in years: "))
        period = int(input("Enter the number of times interest is compounded per year: "))
        future_value = annuity_future_value(payment, rate, time, period)
        print(f"The future value of the annuity is: {future_value}")
    
    else:
        print("Invalid choice. Please try again.")
    
