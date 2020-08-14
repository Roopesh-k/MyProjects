class CoffeeMachine:
    
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee_beans = 120
        self.cups = 9
        self.money = 550

    def buy(self):
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        user_order = input()

        if user_order == "1":
            if self.water >= 250 and self.coffee_beans >= 16:
                print('I have enough resources, making you a coffee!')
                self.water -= 250
                self.coffee_beans -= 16
                self.money += 4
                self.cups -= 1
                print()
            else:
                if (self.water - 250) < 0:
                    print('Sorry, not enough water!')
                elif (self.coffee_beans - 16) < 0:
                    print('Sorry, not enough coffee beans!')                
                print()

        elif user_order == "2":
            if self.water >= 350 and self.milk >= 75 and self.coffee_beans >= 20:
                print('I have enough resources, making you a coffee!')
                self.water -= 350
                self.milk -= 75
                self.coffee_beans -= 20
                self.money += 7
                self.cups -= 1
                print()
            else:
                if (self.water - 350) < 0:
                    print('Sorry, not enough water!')
                elif (self.coffee_beans - 20) < 0:
                    print('Sorry, not enough coffee beans!')
                elif (self.milk - 75) < 0:
                    print('Sorry, not enough milk!')
                print()

        elif user_order == "3":
            if self.water >= 200 and self.milk >= 100 and self.coffee_beans >= 12:
                print('I have enough resources, making you a coffee!')
                self.water -= 200
                self.milk -= 100
                self.coffee_beans -= 12
                self.money += 6
                self.cups -= 1
                print()
            else:
                if (self.water - 200) < 0:
                    print('Sorry, not enough water!')
                elif (self.coffee_beans - 12) < 0:
                    print('Sorry, not enough coffee beans!')
                elif (self.milk - 100) < 0:
                    print('Sorry, not enough milk!')
                print()

        elif user_order == "back":
            print()

    def fill(self):
        print("Write how many ml of water do you want to add:")
        self.water += int(input())
        print("Write how many ml of milk do you want to add:")
        self.milk += int(input())
        print("Write how many grams of coffee beans do you want to add:")
        self.coffee_beans += int(input())
        print("Write how many disposable cups of coffee do you want to add:")
        self.cups += int(input())
        print()

    def take(self):
        print(f"I gave you ${self.money}")
        self.money = 0
        print()

    def remaining(self):
        print(f'''The coffee machine has:
        {self.water} of water
        {self.milk} of milk
        {self.coffee_beans} of coffee beans
        {self.cups} of disposable cups
        {self.money} of money''')
        print()


coffee_machine = CoffeeMachine()
while True:
    print("Write action (buy, fill, take, remaining, exit):")
    action = input()

    if action == "buy":
        coffee_machine.buy()

    elif action == "fill":
        coffee_machine.fill()

    elif action == "take":
        coffee_machine.take()

    elif action == "remaining":
        coffee_machine.remaining()

    elif action == "exit":
        exit()