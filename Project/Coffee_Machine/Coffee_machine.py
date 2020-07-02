class coffee_machine_app():
    def __init__(self, money_machine = 550, water_machine = 400, milk_machine = 540, coffee_machine = 120,cups_machine = 9):
        self.money_machine = money_machine
        self.water_machine = water_machine
        self.milk_machine = milk_machine
        self.coffee_machine = coffee_machine
        self.cups_machine = cups_machine
        self.resource_coffee = [[4,250,0,16],[7,350,75,20],[6,200,100,12]]
 
    def state_coffee_machine(self):
        print()
        print('The coffee machine has:')
        print(self.water_machine,'of water')
        print(self.milk_machine,'of milk')
        print(self.coffee_machine,'of coffee beans')
        print(self.cups_machine,'of disposable cups')
        print(self.money_machine,'of money')
 
    def select_flavor(self):
        print()
        print('What do you want to buy?'
              ' 1 - espresso,'
              ' 2 - latte,'
              ' 3 - cappuccino,'
              ' back - to main menu:')
        response = input()
        if response == 'back':
            return 0
        return int(response)
 
 
    def action_buy(self):
        coffee_selected = self.select_flavor()
        flag_w = self.check_resourse(coffee_selected)
        if flag_w:
            if coffee_selected == 1:
                self.money_machine += 4
                self.water_machine -= 250
                self.coffee_machine -= 16
                self.cups_machine -= 1
            elif coffee_selected == 2:
                self.money_machine += 7
                self.water_machine -= 350
                self.milk_machine -= 75
                self.coffee_machine -= 20
                self.cups_machine -= 1
            elif coffee_selected == 3:
                self.money_machine += 6
                self.water_machine -= 200
                self.milk_machine -= 100
                self.coffee_machine -= 12
                self.cups_machine -= 1
 
    def action_fill(self):
        print()
        print('Write how many ml of water do you want to add:')
        self.water_machine += int(input())
        print('Write how many ml of milk do you want to add:')
        self.milk_machine += int(input())
        print('Write how many grams of coffee beans do you want to add:')
        self.coffee_machine += int(input())
        print('Write how many disposable cups of coffee do you want to add:')
        self.cups_machine += int(input())
 
    def action_take(self):
        print()
        print('I gave you $'+str(self.money_machine))
        self.money_machine -= self.money_machine
 
    def check_resourse(self, choice):
        if self.water_machine >= self.resource_coffee[choice-1][1] and self.milk_machine >= self.resource_coffee[choice-1][2] and self.coffee_machine >= self.resource_coffee[choice-1][3] and self.cups_machine > 0:
            print('I have enough resources, making you a coffee!')
            return 1
        else:
            if self.water_machine < self.resource_coffee[choice-1][1]:
                print('Sorry, not enough water!')
            if self.milk_machine < self.resource_coffee[choice-1][2]:
                print('Sorry, not enough milk!\n')
            if self.coffee_machine < self.resource_coffee[choice-1][3]:
                print('Sorry, not enough beans!\n')
            if self.cups_machine < 1:
                print('Sorry, not enough cups\n') 
            return 0
 
    def action(self):
        print('Write action (buy, fill, take, remaining, exit):')
        action_input = input()
        while action_input != 'exit':
            if action_input == 'buy':
                self.action_buy()
            elif action_input == 'fill':
                self.action_fill()
            elif action_input == 'take':
                self.action_take()
            elif action_input == 'remaining':
                self.state_coffee_machine()
            print() 
            print('Write action (buy, fill, take, remaining, exit):')
            action_input = input()
 
def main():
    coffee_machine = coffee_machine_app()
    coffee_machine.action()
 
 
if __name__ == '__main__':
    main()