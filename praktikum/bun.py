class Bun:
    #модель булочки бургера: можно дать название и цену.

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def get_name(self) -> str:
        return self.name

    def get_price(self) -> float:
        return self.price