# Make a program that validates phone numbers, social security numbers, and zipcodes.
# Display invalid if user inputs an invalid form of order.
import re

# Create order for phone number.
def validatePhoneNum(phone):
    pattern = re.compile(r'^(\+?\d{1,2}\s?)?(\(?\d{3}\)?[\s.-]?)?\d{3}[\s.-]?\d{4}$')
    return bool(pattern.match(phone))

# Create order for social security number.
def validateSSNNum(ssn):
    pattern = re.compile(r'^\d{3}-\d{2}-\d{4}$')
    return bool(pattern.match(ssn))

# Create order for zipcode.
def validateZipcode(zip):
    pattern = re.compile(r'^\d{5}(-\d{4})?$')
    return bool(pattern.match(zip))

def main():
    phone = input("Enter phone number: ")
    ssn = input("Enter social security number: ")
    zip = input("Enter a zipcode: ")

# Display the phone number, social security number and zip code
# Use else for constraints

    if validatePhoneNum(phone):
        print(f"The phone number {phone} is valid.")
    else:
        print(f"The phone number {phone} is invalid.")

    if validateSSNNum(ssn):
        print(f"The social security number {ssn} is valid.")
    else:
        print(f"The social security number {ssn} is invalid.")

    if validateZipcode(zip):
        print(f"The zip code {zip} is valid.")
    else:
        print(f"The zip code {zip} is invalid.")

if __name__ == "__main__":
    main()






