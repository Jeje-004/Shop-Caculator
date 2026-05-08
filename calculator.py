Basketitems = []
Costitems = []

print("""**** Welcome to iShop Calculator ****""")

Basket = int(input("How many items are there in your basket today? "))

print("Let's get to counting them...")

for calculator in range(0, Basket):

    Item = input(f"Please tell me the name of item number {calculator + 1}: ")

    Price = float(input(f"What is the price of {Item}? "))

    Basketitems.append(Item)
    Costitems.append(Price)

# THE LOOP ENDS HERE

Hm = input("Would you like to see your entire basket items? ").lower()

if Hm == "yes":
    print(Basketitems)

else:
    print("Ok!")

Hmm = input("Would you like to see how much it'll cost? ").lower()

if Hmm == "yes":
    print(sum(Costitems))

else:
    print("Ok!")