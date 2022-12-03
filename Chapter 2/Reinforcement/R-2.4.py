"""Write a Python class, Flower, that has three instance variables of type str,
int, and float, that respectively represent the name of the flower, its number
of petals, and its price. Your class must include a constructor method
that initializes each variable to an appropriate value, and your class should
include methods for setting the value of each type, and retrieving the value
of each type."""



class Flower:
    def __init__(self, name: str, num_petals: int, price: float):
        self.name = name
        self.num_petals = num_petals
        self.price = price

    def set_name(self, name: str) -> None:
        self.name = name

    def set_num_petals(self, num_petals: int) -> None:
        self.num_petals = num_petals

    def set_price(self, price: float) -> None:
        self.price = price

    def get_name(self) -> str:
        return self.name

    def get_num_petals(self) -> int:
        return self.num_petals

    def get_price(self) -> float:
        return self.price