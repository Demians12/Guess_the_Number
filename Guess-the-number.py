import random as rd

print("\n-------------Welcome to the game GUESS THE NUMBER--------------\n")
name = input("\nWhat is your name?\n")
print(f"\nNice to meet you {name}!. Let's play! \n")



number1 = 0

number = rd.randint(1, 10)

for number1 in range(4):
    print(f"{name}, try a number between 1 and 10")
    trying = input()
    trying = int(trying)

    if trying < number:
        print("Too low! try a higher number\n")
    elif trying > number:
        print(f"Too high! try a lower number\n")
    elif trying == number:
        break

if trying == number:
    print(f"Very good {name}, the correct number is {number}")

















