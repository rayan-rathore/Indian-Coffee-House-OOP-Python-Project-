
from coffee_data import MENU, resources


class MenuItem:
    def __init__(self, name, cost, water=0, milk=0, coffee=0,sugar = 0, spices=None):
        self.menu = MENU
        self.name = name
        self.cost = cost
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.sugar = sugar
        self.spices = spices

        self.ingredients ={
            "water": water,
            "milk" : milk,
            "coffee": coffee,
            "sugar" : sugar
        }
        self.spices = spices if spices is not None else {}

espresso = MenuItem(
    name="Espresso",
    cost=50,
    water=50,
    coffee=18
)

latte = MenuItem(
    name="Latte",
    cost=75,
    water=200,
    milk=150,
    coffee=24
)

cappuccino = MenuItem(
    name="Cappuccino",
    cost=150,
    water=250,
    milk=100,
    coffee=24
)

filter_coffee = MenuItem(
    name="Filter Coffee",
    cost=40,
    water=50,
    milk=100,
    coffee=18,
    sugar=10
)

masala_coffee = MenuItem(
    name="Masala Coffee",
    cost=120,
    water=50,
    milk=150,
    coffee=15,
    spices={"cinnamon": 1, "cardamom": 2, "ginger": 5}
)

beaten_coffee = MenuItem(
    name="Beaten Coffee",
    cost=80,
    water=20,
    milk=200,
    coffee=10,
    sugar=15
)

sukku_kaapi = MenuItem(
    name="Sukku Kaapi",
    cost=60,
    water=200,
    coffee=5,
    spices={"dry_ginger": 10, "jaggery": 20, "pepper": 2}
)

