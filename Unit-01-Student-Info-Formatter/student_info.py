# Student Info Formatter

# Collect user information
first_name = input("Enter your first name: ")
surname = input("Enter your surname: ")
age = int(input("Enter your age: "))
favourite_number = float(input("Enter your favourite number: "))

# Full name
full_name = f"{first_name} {surname}"

# Display greeting
print(f"\nWelcome, {full_name}!")

# Display name in different formats
print("UPPERCASE:", full_name.upper())
print("Title Case:", full_name.title())

# Calculate age in months
age_in_months = age * 12
print("Age in months:", age_in_months)

# Round favourite number
print("Favourite number (rounded):", round(favourite_number, 2))

# Display data types
print("\nData Types")
print("First Name:", type(first_name))
print("Surname:", type(surname))
print("Age:", type(age))
print("Favourite Number:", type(favourite_number))
