class Coffee:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.balance = 550

    def state(self):
        print('The coffee machine has:')
        print(f'{self.water} of water')
        print(f'{self.milk} of milk')
        print(f'{self.beans} of coffee beans')
        print(f'{self.cups} of disposable cups')
        print(f'{self.balance} of money')

    def buy(self):
        print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back to main_menu:')
        choice = input()
        if choice == 'back':
            return
        if choice == '1':
            water = 250
            milk = 0
            beans = 16
            balance = 4
        elif choice == '2':
            water = 350
            milk = 75
            beans = 20
            balance = 7
        else:
            water = 200
            milk = 100
            beans = 12
            balance = 6
        if self.water < water:
            print('Sorry, not enough water')
            return
        elif self.milk < milk:
            print('Sorry, not enough milk')
            return
        elif self.beans < beans:
            print('Sorry, not enough beans')
            return
        elif self.cups == 0:
            print('Sorry, not enough cup')
            return
        else:
            print('I have enough resources, making you a coffee!')
        self.water -= water
        self.milk -= milk
        self.beans -= beans
        self.balance += balance
        self.cups -= 1

    def fill(self):
        print('Write how many ml of water do you want to add:')
        water = int(input())
        print('Write how many ml of milk do you want to add:')
        milk = int(input())
        print('Write how many grams of coffee beans do you want to add:')
        beans = int(input())
        print('Write how many disposable cups of coffee do you want to add:')
        cups = int(input())
        self.water += water
        self.milk += milk
        self.cups += cups
        self.beans += beans

    def take(self):
        print(f'I gave you {self.balance}')
        self.balance = 0


cof = Coffee()
while True:
    print('Write action (buy, fill, take, remaining, exit):')
    ch = input()
    if ch == 'exit':
        break
    if ch == 'take':
        cof.take()
    elif ch == 'buy':
        cof.buy()
    elif ch == 'fill':
        cof.fill()
    elif ch == 'remaining':
        cof.state()
