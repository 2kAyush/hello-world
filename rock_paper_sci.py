import random


name = input('Enter your name: ')
print('Hello,', name)
reader = open('rating.txt', 'r')
rating = 0
my_dic = {
        'rock': ['fire', 'scissors', 'snake', 'human', 'tree', 'wolf', 'sponge'],
        'fire': ['scissors', 'snake', 'human', 'tree', 'wolf', 'sponge', 'paper'],
        'scissors': ['snake', 'human', 'tree', 'wolf', 'sponge', 'paper', 'air'],
        'snake': ['human', 'tree', 'wolf', 'sponge', 'paper', 'air', 'water'],
        'human': ['tree', 'wolf', 'sponge', 'paper', 'air', 'water',  'dragon'],
        'tree': ['wolf', 'sponge', 'paper', 'air', 'water',  'dragon', 'devil'],
        'wolf': ['sponge', 'paper', 'air', 'water',  'dragon', 'devil', 'lightning'],
        'sponge': ['paper', 'air', 'water',  'dragon', 'devil', 'lightning', 'gun'],
        'paper': ['air', 'water',  'dragon', 'devil', 'lightning', 'gun', 'rock'],
        'air': ['water',  'dragon', 'devil', 'lightning', 'gun', 'rock', 'fire'],
        'water': ['dragon', 'devil', 'lightning', 'gun', 'rock', 'fire', 'scissors'],
        'dragon': ['devil', 'lightning', 'gun', 'rock', 'fire', 'scissors', 'snake'],
        'devil': ['lightning', 'gun', 'rock', 'fire', 'scissors', 'snake', 'human'],
        'lightning': ['gun', 'rock', 'fire', 'scissors', 'snake', 'human', 'tree'],
        'gun': ['rock', 'fire', 'scissors', 'snake', 'human', 'tree', 'wolf']
        }

for line in reader:
    lis = line.split()
    if lis[0] == name:
        rating = int(lis[1])
        break

lis = input()
if lis != '':
    lis = lis.split(',')
else:
    lis = ['rock', 'paper', 'scissors']
print("Okay, let's start")

while True:
    s = input()
    if s == '!rating':
        print('Your rating:', rating)
        continue
    if s == '!exit':
        print('Bye!')
        break
    if s not in lis or s not in my_dic:
        print('Invalid input')
        continue
    choice = random.choice(lis)
    if s == choice:
        print(f'There is a draw ({s})')
        rating += 50
    else:
        if s in my_dic and choice in my_dic[s]:
            print(f'Well done. Computer chose {choice} and failed')
            rating += 100
        elif choice in my_dic and s in my_dic[choice]:
            print(f'Sorry, but computer chose {choice}')
reader.close()
