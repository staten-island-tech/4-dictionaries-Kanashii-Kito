'''Lovely pain of why is it continuing even when i don't eenter the right things'''


Cart = []
Total_Cost = 0

Delivery_Corporation = [
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

Package_Order = input("What Type of Delivery would you like? Input the Number before the name of said Type of Delivery. State 'OIDN' when you're done: ")

while Package_Order != "OIDN":
    try:
        index = int(Package_Order)
        if 0 <= index < len(Delivery_Corporation):
            Cart.append(Delivery_Corporation[index])
            print(f"Added: {Delivery_Corporation[index]['Name']}")
        
        else:
            print("Invalid option, try again.")
    
    except ValueError:
        print("Please enter a valid number or 'OIDN'.")
    
    Package_Order = input("Select another (or 'OIDN' to finish): ")

# --------------------  Confirmation  --------------------
Comfirm = input("Enter 'ORDER COMFIRM' in all caps to confirm your order. If you would like to modify your cart please enter 'DOC': ")

for index, item in enumerate(Cart):
    print(index, ":", item["Name"])

if Comfirm.upper() == "DOC":
    Package_Order = input("Enter the number of the item to remove (or 'OIDN' to finish): ")
    while Package_Order != "OIDN":
        try:
            index = int(Package_Order)
            if 0 <= index < len(Cart):
                removed = Cart.pop(index)
                print(f"Removed: {removed['Name']}")
            else:
                print("Invalid option, try again.")
        except ValueError:
            print("Please enter a valid number or input 'OIDN'.")
        Package_Order = input("Enter another to remove (or input 'OIDN' to finish): ")

if Comfirm.upper() == "ORDER COMFIRM":
    print("Your order has been confirmed.")









# --------------------   Order ID with receipt   --------------------
import random
ran = random.randint(10000000, 11000000)
print(f"Your OIDN / Order Identification Number is: {ran}")


Total_Cost = sum(item["Cost"] for item in Cart)

print("Your Receipt:")
for item in Cart:
    print(f"- {item['Name']} (${item['Cost']:,.2f})")

print(f"Total Cost: ${Total_Cost:,.2f}")









# -------------------- Signature --------------------
sign = input("Please sign with space or '-': ")
if sign == "-":
    print("Thank you for signing your life away. You are now property of the state.")
elif sign == " ":
    print("Hai, friend. || Please go to 48°52.6'S 123°23.6'W to pick up your package.")











































