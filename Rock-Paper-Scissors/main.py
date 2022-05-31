import os
import random

GameOptions = ['R', 'P', 'S']
UserChoice = ''
CPUChoice = ''

print("Welcome to Rock-Paper-Scissors!")

while (True):
    UserChoice = input("Pick an Option [R, P or S]: ")

    if (UserChoice != 'R') and (UserChoice != 'P') and (UserChoice != 'S'):
        print("Please Enter a Valid Option!")
        input()
        os.system("cls")
        continue

    CPUChoice = random.choice(GameOptions)
    print("Player (%s) : CPU (%s)" % (UserChoice, CPUChoice))

    if (UserChoice == CPUChoice):
        print("It's a Tie!")
        input()
        continue
    
    if (UserChoice == 'R') and (CPUChoice == 'P'):
        print("CPU Wins!")
        break
    elif (UserChoice == 'R') and (CPUChoice == 'S'):
        print("You Win!")
        break
    elif (UserChoice == 'P') and (CPUChoice == 'R'):
        print("You Win!")
        break
    elif (UserChoice == 'P') and (CPUChoice == 'S'):
        print("CPU Wins!")
        break
    elif (UserChoice == 'S') and (CPUChoice == 'R'):
        print("CPU Wins!")
        break
    elif (UserChoice == 'S') and (CPUChoice == 'P'):
        print("You Win!")
        break

input()
        

