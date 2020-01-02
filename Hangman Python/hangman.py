import random

words = ["happy day", "knives", "chillies", "horses", "javascript", "developer", "cottage cheese" ]

random.shuffle(words)

answer = list(words[1])

display = []

display.extend(answer)

for i in range(len(display)):
    display[i] = "_"

print (' '.join(display))
print ("\n\n")

count = 0

while count < len(answer):

    guess = input("Please guess a letter: ")

    guess = guess.lower()

    for i in range(len(answer)):
        if answer[i] == guess:
            display[i] = guess
            count += 1

    print(' '.join(display))
    print("\n\n\n")

print("You Guessed It!!!!")