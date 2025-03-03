#Updated 1 Feb 2025
#Watch the video here: https://www.youtube.com/watch?v=YKxvDL3JxEA or follow the instructor led demo
#Implement all the code shown in the video.
#Modify the code so the checks from 12 and under for the $8 price tag
#and 62 and older for the $12 price tag.

print("Welcome to the menu ordering system")

customer_age = int(input("What is the age of the customer? "))

price = 0

if customer_age <= 12:
    price = 8
elif customer_age >= 62:
    price = 12
else:
    price = 12

print(f"The cost for this customer is ${price}.")

drinkyesno = input("Add a drink? Y/N? ")

if drinkyesno == "y":
    smalllarge = input("Small or Large? S/L? ")
    if smalllarge == "l":  
        price += 2
    else:
        price += 1 

print(f"The total cost is ${price}.")

drinkYesNo == input("Add a drink? Y/N? ")

if drinkYesNo == "y":
  smallLarge = input("Small or Large? S/L? ")
  if smallLarge == "L":
         price += 2
else:
  price += 1
