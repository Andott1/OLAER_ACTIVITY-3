# This program calculates the 6% tax amount of user inputted amount.

# Prompts user to input amount
Amount = float(input("Enter Amount: "))

#Constant value of 6% tax
TAX = 0.06

#Calculates tax amount
Tax = Amount * TAX

#Rounds the Tax variable to 2 decimal
Rounded_tax = round(Tax, 2)

#Prints the rounded tax amount
print("6% Tax Amount: " + str(Rounded_tax))
