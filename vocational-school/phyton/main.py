# import stuff
import math
import os
import time



# setting variables
base_price = 4
whipped_cream_price = 2
Espresso_dopio_price = 3
good_deeds_requirement = 4
menu = ["Coffee" , "Latte" , "Espresso" , "Cappucino"]
Yes_or_No = ["Yes" , "No"]
unwanted_Names = ["Ben" , "Patricia" , "Loki"]
menu.sort()

time_start = time.time()

name = ""
while len(name) <= 2:
    while not name.isalpha():
        name = input("What's your first name?\n")

# Name input and check, if name = unwanted
if name in unwanted_Names:
    evil_status  = ""
    while not evil_status in Yes_or_No:
        evil_status = input("Are you evil, " + name + "?\nAnswer with Yes or No\n")
    while True:
        try:
            good_deeds = int(input("How many good deeds have you done today, " + name + "?\n"))
            break
        except:
            print("That's not a valid number(only int)!")
    if evil_status == "Yes" and good_deeds < good_deeds_requirement:
        print("We dont want ya here Evil " + name + "!")
        exit()
    else:
        print("I'm so sorry for asking you!\nBut...\n")
else:
    print("Heow " + name + ", what can I do for ya?\n")

costumer_wish = ""
while not costumer_wish in menu:
    for x in menu:
        print(x)
    costumer_wish = input("What ya want?\n")
    if not costumer_wish in menu:
        print("Sorry, we don't have " + str(costumer_wish) + " here! Please choose something from above.\n")
    else:
        print("Okay! Got it!\n\n")

amount = 0
while amount < 1:
    while True:
        try:
            amount = int(input("How many " + costumer_wish + "'s would ya like to have?\n"))
            break
        except:
            print("That's not a valid option!")

# setting prices depending on product
if costumer_wish == "Coffee":
    price = base_price
elif costumer_wish == "Latte":
    price = base_price * 1.25
    # setting prices depending on whipped cream true or false
    whipped_cream = input("Would you like to have some whipped cream on it by paying " + str(whipped_cream_price) + "€s more?\nAnswer with Yes or No!\n")
    if whipped_cream == "Yes":
        price = whipped_cream_price + price
        print("Your Whipped cream has been added to your " + costumer_wish + " for a price of " + str(whipped_cream_price) + "€s !")
    else:
        price = base_price * 1.25
elif costumer_wish == "Espresso":
    price = base_price * 1.75
    # setting prices depending on espresso dopio true or false
    Espresso_dopio = input("Would you like to have to a Espresso dopio instead?\nAnswer with Yes or No!\n")
    if  Espresso_dopio == "Yes":
        price = Espresso_dopio_price + price
        print("You ordered a Espresso dopio for a price of " + str(Espresso_dopio_price) + "€s !")
    else:
        price = base_price * 1.75
elif costumer_wish == "Cappucino":
    price = base_price * 2


#calculating price in background
total = amount * price

# check if plural or singular
if amount >= 2:
    print(name + ", your " + str(amount) + " " + costumer_wish + "s are gettin made right neow.\nNow ya just gotta pay " + str(total) + "€s")
else:
    print(name + ", your " + str(amount) + " " + costumer_wish + " is gettin made right neow.\nNow ya just gotta pay " + str(total) + "€s")



payment = 0
while payment == 0:
    try:
        payment = int(input("Enter the amount of money your paying here:\n"))
        break
    except:
        print("That's not a valid number(only int)!")



# check if payment is right
if payment == total:
    base_time = 15 # Base time it takes to Produce anything
    production_time = base_time * amount
    print("Please stand by while we're doing the final touches to your order!\nThe estimated time is around " + str(production_time) + "s!")
    time.sleep(production_time)
    if amount >= 2:# check if plural or singular
        print("There ya go, " + name + "!\nHere are ya " + str(amount) + " " + costumer_wish + "'s ! \nHave a good one!")
    else:
        print("There ya go, " + name + "!\nHere's ya " + str(amount) + " " + costumer_wish + "! \nHave a good one!")
elif payment > total:
    Overpayment = payment - total
    print("You paid me " + str(Overpayment) + "€ too much")
else:
    Underpayment = total - payment
    print("You paid me " + str(Underpayment) +"€ too less")

#calculating time_spent in background
time_end = time.time()
time_spent = time_end - time_start
print("You spent " + str(round(time_spent)) + " seconds in our beautiful coffe shop!")

#missing_item = input("In that Time.\nDid you experience any missing item on our menu?\nAnswer with Yes or No!\n")
#if missing_item == "Yes":
#    menu.append(input("Please enter it here:\n"))
#    print("Your item " + menu[-1] + " got added to our menu")
# else:
#    exit()
#
# print("Next time your gonna see " + missing_item + " in the menu as well!")