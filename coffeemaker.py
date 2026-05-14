import time
from prettytable import PrettyTable

class CoffeeMaker:
    def __init__(self):
        # initial inventory setup for the coffee machine
        self.resources = {
            "water": 2000,
            "milk": 1000,
            "coffee": 500,
            "sugar": 500,
            "cinnamon": 100,
            "cardamom": 200,
            "ginger": 500,
            "dry_ginger": 100,
            "jaggery": 200,
            "pepper": 200,
        }
    def report(self):
        #prints a detailed formatted report of the inventory using prettytable.
        table = PrettyTable()
        table.field_names = ["Ingredient", "Available Amount"]

        table.add_row(["water", f"{self.resources.get('water',0)} ml"])
        table.add_row(["milk", f"{self.resources.get('milk', 0)} ml"])
        table.add_row(["coffee", f"{self.resources.get('coffee', 0)} gm"])
        table.add_row(["sugar", f"{self.resources.get('sugar', 0)} gm"])

        spices = ["cinnamon","cardamom","ginger","dry_ginger","jaggery","pepper"]
        for spice in spices:
            if spice in self.resources:
                clean_name = spice.replace("_"," ").title()
                table.add_row([clean_name,f"{self.resources[spice]} gm"])

        print("\n" + "=" * 12 + " INVENTORY REPORT " + "=" * 12)
        print(table)

    def is_resource_sufficient(self, drink):
        """returns true when order can be made, false when ingredients are insufficient"""
        standard_ingredients = {
            "water": drink.water,
            "milk": drink.milk,
            "coffee": drink.coffee,
            "sugar": drink.sugar
        }
        for ingredients, required_amount in standard_ingredients.items():
            if required_amount > self.resources[ingredients]:
                print(f"sorry, there is not enough {ingredients}")
                return False
        for spice, required_amount in drink.spices.items():
            if required_amount > self.resources[spice]:
                print(f"sorry, there is not enough {spice}")
                return False
        clean_name = drink.name.title()
        print(f"Great choice! We have enough ingredients to make your {clean_name}. 👍")
        print("Proceeding to payment...")
        return True


    def make_coffee(self, order):
        """deduct the required ingredients from the internal resources."""
        self.resources["water"] -= order.water
        self.resources["milk"] -= order.milk
        self.resources["coffee"] -= order.coffee
        self.resources["sugar"] -= order.sugar
        for spice, required_amount in order.spices.items():
            self.resources[spice] -= required_amount

        print(f"\n ⚙️ Grinding beans and brewing your {order.name.title()}...")

        bar_length = 20
        for i in range(bar_length + 1):
            percent = int((i / bar_length) * 100)
            # Creates an animation link like: [██████░░░░░░░░░░░] 30%
            progress_bar = "█" * i + "░" * (bar_length - i)
            print(f"\r[{progress_bar}] {percent}% Complete", end="", flush=True)
            time.sleep(0.10)  # Controls the speed of the animation

        print(f"\n\n☕ Your fresh {order.name.title()} is ready.☕")
        print(f"☕ Enjoy your delicious {order.name.title()}! ☕")


    def refill_resources(self):
        """refill the machine's ingredients to their maximum capacity"""
        self.resources = {
            "water": 2000,
            "milk": 1000,
            "coffee": 500,
            "sugar": 500,
            "cinnamon": 100,
            "cardamom": 200,
            "ginger": 500,
            "dry_ginger": 100,
            "jaggery": 200,
            "pepper": 200,
        }
        print("\n✅ Machine successfully refilled! All systems ready.")

























