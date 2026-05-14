
class MoneyMachine:
    def __init__(self):
        self.profit  = 0
        self.money_received = 0

    def report(self):
        """print the current profit accumulated by the machine"""
        print(f"Money received : {self.profit}")

    def process_coin(self):
        print("💰 Please insert the coins. 1, 2, 5, 10, 20 ")

        coin_values = {
            "₹1": 1,
            "₹2": 2,
            "₹5": 5,
            "₹10": 10,
            "₹20": 20
        }
        total_inserted = 0
        for coin_name, coin_value in coin_values.items():
            try:
                count = int(input(f"How many {coin_name} coins? :"))
                total_inserted += count * coin_value
            except ValueError:
                print("Invalid input. Counting as 0 coins.")

        self.money_received = total_inserted
        return self.money_received

    def make_payment(self, cost):
         """returns true when payment is accepted, or false if money is insufficient."""
         #run the process the coin first to update the received money.
         self.process_coin()

         if self.money_received >= cost:
             change = self.money_received - cost
             if change > 0:
                 print(f"here is ₹{change} in change.")
             self.profit += cost
             self.money_received = 0
             return True
         else:
             print(f"Sorry, that's not enough money. ₹{self.money_received} refunded.")
             return False
























