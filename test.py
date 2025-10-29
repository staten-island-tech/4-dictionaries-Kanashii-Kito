Cart = []
Cost = 0

'''Delivery_Corporation'''
Delivery_Corporation = [
{
    "Name": "Standard || Route and Speed",
    "Cost": 2499.99,
    "Department": "Semi Truck Shipping", 
    "Description": "Packages From The Depths Hell.",
},

{
    "Name": "Premium || Route and Speed",
    "Cost": 4999.99,
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
    print(Cart)
    print("Type of Delivery Packages: Standard  ||  Premium  ||  Insurance")
    Package_Order = input("What Type of Delivery would you like? State 'OID' when you're done. :  ")





























# '''----------'''

# Cart = []
# Total_Cost = 0

# '''Delivery_Corporation'''

# Standard = {
#     "Name": "Standard Route and Speed",
#     "Cost": 2499.99,
#     "Department": "Semi Truck Shipping", 
#     "Description": "Packages From The Depths Hell.",
# }

# Premium = {
#     "Name": "Premium Route and Speed",
#     "Cost": 4999.99,
#     "Department": "Semi Truck Shipping", 
#     "Description": "Faster Delivery of Packages From The Depths Hell.",
# }

# Insurance = {
#     "Name": "Package Insurance",
#     "Cost": 99999.99,
#     "Department": "Semi Truck Shipping", 
#     "Description": "Insurance for your Packages from Hell."
# }

# Print = ("Standard")
# Print = ("Premium")
# Print = ("Insurance")

# Package_Order = input("What Type of Delivery would you like? State 'OID' when you're done.")

# while Package_Order != "OID":
#     for index, item in enumerate(best_buy_items):
#         print= (index, ":", item["name"])