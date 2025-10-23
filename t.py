'''Slot Machines'''

quarters = int(input("Amount of quarters she has. | Input Total Quarters:  "))
first = int(input("First Slot Machine | Input amount of time this Slot Machine was played already:  "))
second = int(input("Second Slot Machine | Input amount of time this Slot Machine was played already:  "))
third = int(input("Third Slot Machine | Input amount of time this Slot Machine was played already:  "))

count = 0

while quarters > 0:
    first += 1
    quarters -= 1
    count += 1
    if first == 35:
        quarters += 30
        first = 0

    second += 1
    quarters -= 1
    count += 1
    if second == 100:
        quarters += 60
        second = 0

    third += 1
    quarters -= 1
    count += 1
    if third == 10:
        quarters += 9
        third = 0

print(f"Martha plays {count} times before going broke.")


'''----------------------------------------------------------------------------------------------------------------------------------'''
'''Explaination Below :D'''

'''Slot Machines'''

quarters = int(input("Amount of quarters she has. | Input Total Quarters:  "))    # This the amount of quarters she has or the amount you would like her to have.
first = int(input("First Slot Machine | Input amount of time this Slot Machine was played already:  "))    #This is how many times the first slot machine has already been played.
second = int(input("Second Slot Machine | Input amount of time this Slot Machine was played already:  "))    #JUST READ THE DAM "----" I AIN'T TYPING ALL THIS OUT:c
third = int(input("Third Slot Machine | Input amount of time this Slot Machine was played already:  "))    # read the comment stuff in the line above this one.

count = 0    # This is how many times she's played.

while quarters > 0:     # while loop saying to continue if the amount of quarters she has and/or gets from playing slots is greater than 0.
    # before you say why I didn't use != || It's because if I did, and the number of quarters somehow became negative, this would break. So the greater sign would be better.
    first += 1     # adds 1 to the counter of the first slot machine so it knows when to payout and how many times it's been played.
    quarters -= 1    # subtracts a quarter per play.
    count += 1    # adds 1 to the amount of times, she has played. NOT THE AMOUNT THAT THE SLOT MACHINE WAS PLAYED.
    if first == 35:      # the first slots machine pays out at 35 plays.
        quarters += 30    # if the machine does payout, it would give her 30 more quarters.
        first = 0      # set the amount of time it's been played to zero so it knows when to payout next.

    second += 1    # adds 1 to the counter of the second slot machine so it knows when to payout and how many times it's been played.
    quarters -= 1    # subtracts a quarter per play.
    count += 1    # adds 1 to the amount of times, she has played. NOT THE AMOUNT THAT THE SLOT MACHINE WAS PLAYED.
    if second == 100:    # the second slots machine pays out at 100 plays.
        quarters += 60    # if the machine does payout, it would give her 60 more quarters.
        second = 0    # set the amount of time it's been played to zero so it knows when to payout next.

    third += 1    # adds 1 to the counter of the third slot machine so it knows when to payout and how many times it's been played.
    quarters -= 1    # subtracts a quarter per play.
    count += 1    # adds 1 to the amount of times, she has played. NOT THE AMOUNT THAT THE SLOT MACHINE WAS PLAYED.
    if third == 10:    # the third slots machine pays out at 10 plays.
        quarters += 9    # if the machine does payout, it would give her 9 more quarters.
        third = 0    # set the amount of time it's been played to zero so it knows when to payout next.

print(f"Martha plays {count} times before going broke.")