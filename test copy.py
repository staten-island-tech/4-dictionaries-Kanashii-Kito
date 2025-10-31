Cart = []
Total_Cost = 0

'''Delivery_Corporation'''
Delivery_Corporation = [
{
    "Name": "Standard || Normal Route and Speed",
    "Cost": 2499.99,
    "Department": "Semi Truck Shipping", 
    "Description": "Packages From The Depths Hell.",
},

{
    "Name": "Premium || Fast Route and Speed",
    "Cost": 4999.99,
    "Department": "Semi Truck Shipping", 
    "Description": "Faster Delivery of Packages From The Depths Hell.",
},

{
    "Name": "Hell || Idk Route and Speed",
    "Cost": 19999.99,
    "Department": "Semi Truck Shipping", 
    "Description": "Faster Delivery of Packages From The Depths Hell.",
},

{
    "Name": "Package || Insurance",
    "Cost": 99999.99,
    "Department": "Semi Truck Shipping", 
    "Description": "Insurance for your Packages from Hell."
},

{
    "Name": "Contract || Contract",
    "Cost": 0.00,
    "Department": "NDC-M", 
    "Description": "N/A."
},
]
for index, item in enumerate(Delivery_Corporation):
    print(index, ":", item["Name"])
Package_Order = input("What Type of Delivery would you like? State 'OID' when you're done. :  ")


while Package_Order != "OID":
    try:
        index = int(Package_Order)
        if 0 <= index < len(Delivery_Corporation):
            Cart.append(Delivery_Corporation[index])
            print(f"Added: {Delivery_Corporation[index]['Name']}")
        else:
            print("Invalid option, try again.")
    except ValueError:
        print("Please enter a valid number or 'OID'.")
    
    Package_Order = input("Select another (or 'OID' to finish): ")


# Calculate total cost

Total_Cost = sum(item["Cost"] for item in Cart)

print("\nYour Receipt:")
for item in Cart:
    print(f"- {item['Name']} (${item['Cost']:,.2f})") # better formated one
    # if you forget:
        # the comma is so we can have a comma every 3 numbers and 2f is for a decimal point and 2 decimals

print(f"\nTotal Cost: ${Total_Cost:,.2f}") # better formated one



import random

ran = random.randint(10000000,11000000)
print (f"Your OID/Order Identification Number is:  {ran}")




print ("Please input space or '-' to sign.")

sign = input ("Please sign:  ")
if sign == "-":
    print ("Thank you for signing ur life away. We now own you. You are now property of the state.")
elif sign == " ":
    print ("Hai, friend.")


























