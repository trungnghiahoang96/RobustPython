from typing import Tuple

class BLTSandwich:
    def __init__(self):
        self.cost = 6.95
        self.name = 'BLT'
        # This class handles a fully constructed BLT sandwich
        # ... 

    def split_in_half(self) -> Tuple['BLTSandwich', 'BLTSandwich']:
        # Instructions for how to split a sandwich in half
        # Cut along diagonal, wrap separately, etc.
        # Return two sandwiches in return
        return (BLTSandwich(), BLTSandwich())

class Chili:
    def __init__(self):
        self.cost = 4.95
        self.name = 'Chili'
        # This class handles a fully loaded chili
        # ... 

    def split_in_half(self) -> Tuple['Chili', 'Chili']:
        # Instructions for how to split chili in half
        # Ladle into new container, add toppings
        # Return two cups of chili in return
        # ...
        return (Chili(), Chili())

class BaconCheeseburger:
    def __init__(self):
        self.cost = 11.95
        self.name = 'Bacon Cheeseburger'
        # This class handles a delicious Bacon Cheeseburger
        # ... 

    # NOTE! no split_in_half method

import math
def split_order(order):
    dishes = order.split_in_half()
    assert len(dishes) == 2
    for half_dish in dishes:
        half_dish.cost = math.ceil(half_dish.cost) / 2
        half_dish.name = "½ " + half_dish.name
    return dishes

sandwich = BLTSandwich()
dishes = split_order(sandwich)
assert dishes[0].cost == 3.5
assert dishes[0].name == "½ BLT" 
assert dishes[0].cost == dishes[1].cost
assert dishes[0].name == dishes[1].name
