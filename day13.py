#finding bugs practice in codes 


############## Even Odd code bugs 
def check_even_odd(number):
    """
    This function checks if a given number is even or odd.
    A number is even if it is divisible by 2, otherwise it is odd.
    """
    if number % 2 = 0:      #In this line there is a error  
        return "even"
    else:
        return "odd"

# Input: number to check
number = int(input("Enter a number: "))

# Output: whether the number is even or odd
result = check_even_odd(number)
print(f"The number {number} is {result}.")

########################## leap year code ###############################

def is_leap_year(year):
    """
    This function checks if a given year is a leap year.
    A year is a leap year if:
    - It is evenly divisible by 4
    - Except if it is evenly divisible by 100, then it is not a leap year
    - Except if it is evenly divisible by 400, then it is a leap year
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Input: year to check
year = int(input("Enter a year: "))

# Output: whether the year is a leap year or not
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")




