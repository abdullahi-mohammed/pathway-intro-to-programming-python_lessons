# Author: Abdullahi Mohammed
# Date:   25th, jan. 2024.
# Purpose: Advenure Game
# Stretch Challenge: I shared the game with my friends to play and they all get to know what they had to do to be successful in life. They all told me that the game is useful to know what one can do to be successful in life. it was really a good game.- I also implemented a three choice level.


# LIFE SUCCESS ADVENTURE GAME

#1- you woke up on a monday morning. what do you rather do STAND up from bed or CONTINUE sleeping.

#2- STAND - you stand up and perform your morning chores. then do you go to WORK or OUTING.
#   CONTINUE - you continue sleeping and wake up late - close to afternoon. do you rather go to PLAY football or stay home and WATCH movie

#3- WORK -  you stood up from bed early and went to work. you made sure to apply both HIGH DEFFERENCE AND HIGH INITIATIVE or HIGH DEFFERENCE AND LOW INITIATIVE or LOW DEFFERENCE AND LOW INITIATIVE in your work.
#   OUTING - you stood up from bed early and went for outing. you went out with your friends to have a GOOD or BAD time.

#3  PLAY - you continue sleeping, woke up late and went to play football. you made sure to apply both HIGH DEFFERENCE AND HIGH INITIATIVE or HIGH DEFFERENCE AND LOW INITIATIVE or LOW DEFFERENCE AND LOW INITIATIVE in your work.
#  WATCH - you continue sleeping, woke up late and went to watch movie. you have a GOOD or BAD time.

# ----------------------------------------------------------------------------------------------------------------------------

# WON
#    HIGH DEFFERENCE AND HIGH INITIATIVE - Hooray! You won. you became successful in life.
     
# DRAW
#    HIGH DEFFERENCE AND LOW INITIATIVE - Its a draw. There's chance for improvement.
#    GOOD - Its a draw. There's chance for improvement.

# LOOSE
#     LOW DEFFERENCE AND LOW INITIATIVE - You loose! TRY AGAIN.
#     BAD - You loose! TRY AGAIN.


first_choice = input("you woke up on a monday morning. what do you rather do STAND up from bed or CONTINUE sleeping.\n")

if first_choice.upper() == "STAND":
    second_choice = input("you stand up and perform your morning chores. then do you go to WORK or OUTING.\n")
    if second_choice.upper() == "WORK":
        third_choice = input("you stood up from bed early and went to work. you made sure to apply both HIGH DEFFERENCE AND HIGH INITIATIVE or HIGH DEFFERENCE AND LOW INITIATIVE or LOW DEFFERENCE AND LOW INITIATIVE in your work.\n")
        if third_choice.upper() == "HIGH DEFFERENCE AND HIGH INITIATIVE":
            print("Hooray! You won. you became successful in life.\n")
        elif third_choice.upper() == "HIGH DEFFERENCE AND LOW INITIATIVE":
            print("Its a draw. There's chance for improvement.\n")
        elif third_choice.upper() == "LOW DEFFERENCE AND LOW INITIATIVE":
            print("You loose! TRY AGAIN.\n")
        else:
            print("Wrong Choice\n")   

    elif second_choice.upper() == "OUTING":
        third_choice = input("you stood up from bed early and went for outing. you went out with your friends to have a GOOD or BAD time.\n")
        if third_choice.upper() == "GOOD":
            print("Its a draw. There's chance for improvement.\n")
        elif third_choice.upper() == "BAD":
            print("You loose! TRY AGAIN.\n")
        else:
            print("Wrong Choice\n")    
    else:
        print("Wrong Choice\n")

elif first_choice.upper() == "CONTINUE":
    second_choice = input("you continue sleeping and wake up late - close to afternoon. do you rather go to PLAY football or stay home and WATCH movie.\n")
    if second_choice.upper() == "PLAY":
        third_choice = input("you continue sleeping, woke up late and went to play football. you made sure to apply both HIGH DEFFERENCE AND HIGH INITIATIVE or HIGH DEFFERENCE AND LOW INITIATIVE or LOW DEFFERENCE AND LOW INITIATIVE in your work.\n")
        if third_choice.upper() == "HIGH DEFFERENCE AND HIGH INITIATIVE":
            print("Hooray! You won. you became successful in life.\n")
        elif third_choice.upper() == "HIGH DEFFERENCE AND LOW INITIATIVE":
            print("Its a draw. There's chance for improvement.\n")
        elif third_choice.upper() == "LOW DEFFERENCE AND LOW INITIATIVE":
            print("You loose! TRY AGAIN.\n")
        else:
            print("Wrong Choice\n")    

    elif second_choice.upper() == "WATCH":
        third_choice = input("you continue sleeping, woke up late and went to watch movie. you have a GOOD or BAD time.\n")
        if third_choice.upper() == "GOOD":
            print("Its a draw. There's chance for improvement.\n")
        elif third_choice.upper() == "BAD":
            print("You loose! TRY AGAIN.\n")
        else:
            print("Wrong Choice\n")    

    else:
        print("Wrong Choice\n")

else:
    print("Wrong Choice\n")