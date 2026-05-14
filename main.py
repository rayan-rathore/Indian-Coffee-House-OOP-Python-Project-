from coffeemaker import CoffeeMaker
from menu import Menu
from moneymachine import MoneyMachine

def main():
    # Initialize the core objects of the coffee machine.
    coffee_menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine =  MoneyMachine()

    is_on = True
    while is_on:
        # display the menu to the customer.
        coffee_menu.show_menu()

        # prompt user for choice
        choice = input("what would you like? (espresso / latte / cappuccino etc...) ").lower()
        if choice == "off":
            print("\nShutting down the coffee machine. Goodbye!")
            is_on = False

        elif choice == "report":
            coffee_maker.report()
            print("Type 'Refill' for refilling ingredients to their maximum capacity.")
            money_machine.report()


        elif choice == "refill" or "Refill":
            coffee_maker.refill_resources()

        # handle the normal coffee order
        else:
            drink = coffee_menu.find_drink(choice)

            # If the drink object exists, proceed with checking stock
            if coffee_maker.is_resource_sufficient(drink):
                print(f"\n💰 Total Amount Due: ₹{drink.cost}")
                print("-" * 30)
                # Check if there are enough ingredients in the machine
                if money_machine.make_payment(drink.cost):
                    # Dispense coffee and deduct stock resources
                    coffee_maker.make_coffee(drink)
        print("\n" + "*" * 40 + "\n")

if __name__ == "__main__":
    main()