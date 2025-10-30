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
    Cart.append(Package_Order)
    print(f"Types of Delivery Packages in ur Cart:  {Cart}")
    for index, item in enumerate(Delivery_Corporation):
        print(index, ":", item["Name"])
    Package_Order = input("What Type of Delivery would you like? State 'OID' when you're done. :  ")


for item in Delivery_Corporation:
    if item["Name"] in Cart:
        Total_Cost += item["Cost"]

print("\nYour Cart:  ")
for item in Cart:
    print(f"- {item}")

print(f"Total Cost: ${Total_Cost:,.2f}")


'''------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''




# stuff below is from chat gpt that i'll attempt to understand and throw in to my code to help me make it better
'''Would you like me to show how to display the cost next to each cart item (e.g. “Premium || Fast Route and Speed — $4,999.99”)? It’s an easy and nice upgrade.'''




Cart = []
Total_Cost = 0

Delivery_Corporation = [
    {"Name": "Standard || Normal Route and Speed", "Cost": 2499.99},
    {"Name": "Premium || Fast Route and Speed", "Cost": 4999.99},
    {"Name": "Hell || Idk Route and Speed", "Cost": 19999.99},
    {"Name": "Package || Insurance", "Cost": 99999.99},
]

for index, item in enumerate(Delivery_Corporation):
    print(index, ":", item["Name"])

Package_Order = input("Select the number of the Delivery you’d like (or 'OID' to finish): ")

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

print("\nYour Cart:")
for item in Cart:
    print(f"- {item['Name']} (${item['Cost']:,.2f})")

print(f"\nTotal Cost: ${Total_Cost:,.2f}")




for item in Delivery_Corporation:
    if item["Name"].lower() in [x.lower() for x in Cart]:
        Total_Cost += item["Cost"]






















