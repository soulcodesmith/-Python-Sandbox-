import random

# The Function: random.randrange(start, stop)
#This function returns a randomly selected element from the range created by range(start, stop)
# but doesn't include the last number in the range. it won't include 11 it only goes to 10 max not 11.

#r = random.randrange(-5,11)
#print(r)

# random.randit(start,stop)
# it includes the last number in the range.

#c = random.randint(-5,11)
#print(c)

# project - loop. 
#

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('Please type a number larger than 0, next time! ')
        quit()
else:
     print('Please type a number next time!')
     quit()
random_number = random.randint(0, top_of_range)
guesses = 0


while True:
    guesses += 1 # This counts EVERY attempt

    user_guess = input('Make a guess: ')
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number next time!')
        continue

    if user_guess == random_number:
        print('You got it!')
        break
    elif user_guess > random_number:
            print("You were above the number!")
    else:
        print("You were below the number")

print("You got it in", guesses, 'guesses')
