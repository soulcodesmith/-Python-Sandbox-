name = input("What's your name? ")
print("Welcome", name, "to this adventure" )

answer = input("You are on a dirt road, it has come to an end and you can either go left or right, which way would you like to go? ").lower()


if answer == "left":
    answer = input("You come to a river and You can walk around it or smim? Type 'Walk' to walk around and 'swim' to swim across. ").lower()
    
    if answer == "swim":
        print(" You swim across and eaten by an alligator.")
        
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lose the game! ")
    else:
        print("Not a vaild option, You loose!")

elif answer == "right":
    print("Yet to update! Please hang on.")

else:
    print("Not a vaild option, You lose!")

