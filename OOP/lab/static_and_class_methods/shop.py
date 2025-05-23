class Shop:
    def __init__(self, name: str, shop_type: str, capacity: int):
        self.name = name
        self.type = shop_type
        self.capacity = capacity
        self.items = {}

    @classmethod
    def small_shop(cls, name: str, shop_type: str) -> "Shop":
        capacity = 10
        return cls(name, shop_type, capacity)

    def add_item(self, item_name: str) -> str:
        current_stock_count = sum([qty for qty in self.items.values()])

        if current_stock_count >= self.capacity:
            return "Not enough capacity in the shop"

        if not self.items.get(item_name, None):
            self.items[item_name] = 0

        self.items[item_name] += 1

        return f"{item_name} added to the shop"

    def remove_item(self, item_name: str, amount: int) -> str:
        if not self.items.get(item_name, None):
            return f"Cannot remove {amount} {item_name}"

        if self.items[item_name] < amount:
            return f"Cannot remove {amount} {item_name}"

        self.items[item_name] -= amount

        if self.items[item_name] == 0:
            del self.items[item_name]

        return f"{amount} {item_name} removed from the shop"

    def __repr__(self) -> str:
        return f"{self.name} of type {self.type} with capacity {self.capacity}"


fresh_shop = Shop("Fresh Shop", "Fruit and Veg", 50)
small_shop = Shop.small_shop("Fashion Boutique", "Clothes")
print(fresh_shop)
print(small_shop)
print(fresh_shop.add_item("Bananas"))
print(fresh_shop.remove_item("Tomatoes", 2))
print(small_shop.add_item("Jeans"))
print(small_shop.add_item("Jeans"))
print(small_shop.remove_item("Jeans", 2))
print(small_shop.items)


