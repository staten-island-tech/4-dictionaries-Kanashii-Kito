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


# for item in Delivery_Corporation:
#     if item["Name"] in Cart:
#         Total_Cost += item["Cost"]


# Calculate total cost
Total_Cost = sum(item["Cost"] for item in Cart)

print("\nYour Receipt:")
for item in Cart:
    print(f"- {item['Name']} (${item['Cost']:,.2f})") # better formated one

print(f"\nTotal Cost: ${Total_Cost:,.2f}") # better formated one


'''------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
























