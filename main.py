# Scottie's Fantabulous Deadlock Quiz (that nobody will understand)
# Author: Faron Matthews (scottie)
# A quiz/questionnaire program built for CS 104 Project 1

#Variables
lives = 3
answer = 0
Qstate = 1
#Welcome
print("Welcome to Scottie's Fantabulous Deadlock Quiz...!")
print("You'll be asked a question, and you must respond with the number of the answer you wish to submit.")
#Quiz Main
#Question 1: Toxic Bullets
while Qstate == 1 and lives > 0:
    print("Does the item Toxic Bullets do damage based on current health or max health?")
    print("1. Current Health\n2. Max Health")
    answer = int(input("Answer: "))
    if answer == 2:
        print("Correct!")
        Qstate += 1
    else:
        lives -= 1
        print("Incorrect! You have lost a life!")
        if lives == 0:
            print("You have failed the quiz...better luck next time!")
#Question 2: Lanes
while Qstate == 2 and lives > 0:
    print("How many lanes were on the map before the map rework in 2025?")
    print("1. 3\n2. 4\n3. 5")
    answer = int(input("Answer: "))
    if answer == 2:
        print("Correct!")
        Qstate += 1
    else:
        lives -= 1
        print("Incorrect! You have lost a life!")
        if lives == 0:
            print("You have failed the quiz...better luck next time!")
#Question 3: Major Update Time
while Qstate == 3 and lives > 0:
    print("When was the last major update (as of September 18th 2026)?")
    print("1. January\n2. March\n3. June")
    answer = int(input("Answer: "))
    if answer == 1:
        print("Correct!")
        Qstate += 1
    else:
        lives -= 1
        print("Incorrect! You have lost a life!")
        if lives == 0:
            print("You have failed the quiz...better luck next time!")
#Question 4: Item Economy
while Qstate == 4 and lives > 0:
    print("How many souls does a tier 4 item cost?")
    print("1. 1,600\n2. 3,200\n3. 6,400")
    answer = int(input("Answer: "))
    if answer == 3:
        print("Correct!")
        Qstate += 1
    else:
        lives -= 1
        print("Incorrect! You have lost a life!")
        if lives == 0:
            print("You have failed the quiz...better luck next time!")
#Question 5: Hero Release
while Qstate == 5 and lives > 0:
    print("Who was the most recently released Hero?")
    print("1. Graves\n2. Apollo\n3. Celeste")
    answer = int(input("Answer: "))
    if answer == 2:
        print("Correct!")
        Qstate += 1
    else:
        lives -= 1
        print("Incorrect! You have lost a life!")
        if lives == 0:
            print("You have failed the quiz...better luck next time!")
#results
if Qstate == 6 and lives > 0:
    print("Congratulations on completing my Fantabulous Deadlock Quiz!")
    print(f"You managed to complete all five questions with {lives} lives remaining!")
