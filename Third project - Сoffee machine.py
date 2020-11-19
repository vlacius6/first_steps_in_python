class CofeeMachine:
    water = 400
    milk = 540
    beans = 120
    cups = 9
    money = 550
    
    def print_state(self):
        print("""The coffee machine has:
        {} of water
        {} of milk
        {} of coffee beans
        {} of disposable cups
        {} of money""".format(self.water, self.milk, self.beans, self.cups, self.money))
    
    def after_work(self, q, w, e, r, t):
        self.water += q
        self.milk += w
        self.beans += e
        self.cups += r
        self.money += t

    def need_action(self):
        action = input("\nWrite action (buy, fill, take, remaining, exit):\n")
        if action == "buy":
            self.buy()
        elif action == "fill":
            self.fill()
        elif action == "take":
            self.take()
        elif action == "remaining":
            self.remaining()
        elif action == "exit":
            exit()
    
    def remaining(self):
        print()
        self.print_state()
        self.need_action()
    
    def buy(self):
        what_coffee = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
        if what_coffee == "1":
            if int(min((self.water / 250), (self.beans / 16))) >= 1:
                self.after_work(-250, 0, -16, -1, 4)
                self.need_action()
            else:
                print("I have enough resources, making you a coffee!\n")
                self.need_action()
        elif what_coffee == "2":
            if int(min((self.water / 350), (self.milk / 75), (self.beans / 20))) >= 1:
                self.after_work(-350, -75, -20, -1, 7)
                self.need_action()
            else:
                print("I have enough resources, making you a coffee!\n")
                self.need_action()
        elif what_coffee == "3":
            if int(min((self.water / 200), (self.milk / 100), (self.beans / 12))) >= 1:
                self.after_work(-200, -100, -12, -1, 6)
                self.need_action()
            else:
                print("I have enough resources, making you a coffee!\n")
                self.need_action()
        elif what_coffee == "back":
            self.need_action()
    
    def fill(self):
        self.after_work(int(input("Write how many ml of water do you want to add:\n")), 0, 0, 0, 0)
        self.after_work(0, int(input("Write how many ml of milk do you want to add:\n")), 0, 0, 0)
        self.after_work(0, 0, int(input("Write how many grams of coffee beans do you want to add:\n")), 0, 0)
        self.after_work(0, 0, 0, int(input("Write how many disposable cups of coffee do you want to add:\n")), 0)
        self.need_action()
    
    def take(self):
        print(f'I gave you ${self.money}')
        self.money = 0
        self.need_action()



my_cm = CofeeMachine()


my_cm.need_action()