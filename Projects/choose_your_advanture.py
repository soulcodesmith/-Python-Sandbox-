name = input("What's your name? ")
print("Welcome", name, "to this adventure" )

answer = input("You are on a dirt road, it has come to an end and you can either go left or right, which way would you like to go? ").lower()


if answer == "left":
    answer = input("You come to a river and you can walk around it or swim? Type 'Walk' to walk around and 'swim' to swim across. ").lower()
    
    if answer == "swim":
        print(" You swim across and eaten by an alligator.")
        
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lose the game! ")
    else:
        print("Not a vaild option, You loose!")

elif answer == "right":
    answer == input("You come to a bridge, it looks wobbly. Do you want to cross the bridge or go back (cross/back) ?").lower()

    if answer == "cross":
        print("You cross the bridge and meet a strager. Do you talk to them (yes/no) ?").lower()
        if answer == "yes":
            print("You won, Congratulations!")
        elif answer == "no":
            print ("You lose!")
        else:
            print("Not a valid option, You lose")
    
    elif answer == "back":
        print("You go back and lose!")
    else:
        print("Not a vaild option, You lose!")
else:
    print("Not a vaild option, You lose!")

print("Thank you!")

