Cart = []
TD_OIDN = True
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
Package_Order = input("What Type of Delivery would you like? Input the Number before the name of said Type of Delivery. State 'OIDN' when you're done. :  ")


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


# Calculate total cost

Total_Cost = sum(item["Cost"] for item in Cart)

print("\nYour Receipt:")
for item in Cart:
    print(f"- {item['Name']} (${item['Cost']:,.2f})") # better formated one
    # if you forget:
        # the comma is so we can have a comma every 3 numbers and 2f is for a decimal point and 2 decimals

print(f"\nTotal Cost: ${Total_Cost:,.2f}") # better formated one

'''-------------------------------------------------------------------------------------------------------------------------------------------------- it messsed up here'''

Comfirm = input("Enter 'ORDER COMFIRM' In all Caps to comfirm ur order. If you would like to select more or remove something please state 'DOC' in all caps.")

if Comfirm.upper() == "DOC":
    TD_OIDN = True


if Comfirm.upper() == "ORDER COMFIRM":
    TD_OIDN = False


if TD_OIDN == False:
    print("Ur Order Has Been Comfirmed.")



elif TD_OIDN == True:
    while Package_Order != "OIDN":
        try:
            index = int(Cart)
            if 0 <= index < len(Cart):
                Cart.pop(Cart[index])
                print(f"Removed: {Cart[index]['Name']}")
            else:
                print("Invalid option, try again.")
        except ValueError:
            print("Please enter a valid number or 'OIDN'.")
        
        Package_Order = input("Select another (or 'OIDN' to finish): ")


'''------------------------------------------------------------------------------------------------------------------------------'''






import random

ran = random.randint(10000000,11000000)
print (f"Your OIDN  /  Order Identification Number is:  {ran}")




print ("Please input space or '-' to sign.")

sign = input ("Please sign:  ")
if sign == "-":
    print ("Thank you for signing ur life away. We now own you. You are now property of the state.")
elif sign == " ":
    print ("Hai, friend. || Please Go to  48°52.6'S Latitude and 123°23.6'W Longitude to pick up ur package.")



























