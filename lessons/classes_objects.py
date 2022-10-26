"""Example of a class and object instantiation."""


class Pizza:
    """Models the idea of a pizza."""

    # Attribute Definitions
    size: str
    toppings: int
    extra_cheese: bool

    def __init__(self, size: str, toppings: int, extra_cheese: bool):
        self.size = size
        self.toppings = toppings
        self.extra_cheese = extra_cheese

    def price(self, tax: float) -> float:
        """Calculate the price of a Pizza."""
        total: float = 0.0
        if self.size == "large":
            total += 10.0
        else:
            total += 8.0
        total += self.toppings * 0.75
        if self.extra_cheese:
            total += 1.0
        total *= tax
        return total


a_pizza: Pizza = Pizza("large", 3, False)
print(f"Price: ${a_pizza.price(1.05)}")

b_pizza: Pizza = Pizza("small", 0, True)
print(f"Price: ${b_pizza.price(1.05)}")