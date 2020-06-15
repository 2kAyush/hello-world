# Write your code here
import random
print("H A N G M A N")
choice = input('Type "play" to play the game, "exit" to quit: ')
lis = ['python', 'java', 'kotlin', 'javascript']
c_word = random.choice(lis)
w_lis = list(c_word)
b_lis = list(c_word)
count = 0
check = []
for i in range(len(b_lis)):
    b_lis[i] = '-'
while choice == 'play':
    while count < 8:
        print()
        print("".join(b_lis))
        letter = input("Input a letter: ")

        if len(letter) > 1 or len(letter) == 0:
            print("You should input a single letter")

        elif not letter.islower():
            print("It is not an ASCII lowercase letter")

        elif letter in check:
            print("You already typed this letter")

        elif letter in w_lis:
            check.append(letter)

            for i in range(len(w_lis)):
                if w_lis[i] == letter:
                    b_lis[i] = letter

        else:
            count += 1
            check.append(letter)
            print("No such letter in the word")

    if w_lis == b_lis:
        print("You survived!\n")
        choice = input('Type "play" to play the game, "exit" to quit: ')
    else:
        print("You are hanged!\n")
        choice = input('Type "play" to play the game, "exit" to quit: ')
