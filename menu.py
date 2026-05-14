"""Menu class

Data: the MENU dictionary
Actions:

Show the menu to the user
Return the details of a specific drink
Check if a user's choice is valid"""

from coffee_data import  MENU
from prettytable import PrettyTable
from menuItem import latte, espresso, cappuccino, masala_coffee, beaten_coffee, sukku_kaapi, filter_coffee


class Menu:
    def __init__(self):
        self.menu = [
            espresso,
            latte,
            cappuccino,
            filter_coffee,
            masala_coffee,
            beaten_coffee,
            sukku_kaapi
        ]

    def show_menu(self):
        print("\n☕ Welcome to the Indian Coffee House!☕")

        table = PrettyTable()
        table.field_names = ["Coffee Drinks", "Price"]

        for item in self.menu:
            table.add_row([item.name.title(), f"₹{item.cost}"])
        print(table)


    def find_drink(self, order_name):
        for item in self.menu:
            if item.name.lower() == order_name.lower():
                return item
        print(f"sorry, {order_name} is not available.")
        return None

