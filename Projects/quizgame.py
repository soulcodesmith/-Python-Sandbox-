print("Welcome to the quiz game")

Playing = input("Do you want to play? ")

if Playing.lower() != "yes":
    quit()

print("Okay! Let's Play!")
score = 0



answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print ('Correct')
    score +=1
else:
    print("Incorrect")

answer = input("What is Raycast? ")
if answer.lower() == "mac spotlight":
    print('Correct')
    score +=1
else:
    print("Incorrect")

answer = input("What is Claude? ")
if answer.lower() == "ai assistant":
    print('Correct')
    score +=1
else:
    print("Incorrect")

print("You got " + str(score) + " questions Correct! ")
print("You got " + str((score/3) * 100) + " % ")

