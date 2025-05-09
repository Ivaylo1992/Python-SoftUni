from project.product import Product


class ProductRepository:
    def __init__(self) -> None:
        self.products: list[Product] = []

    def add(self, product: Product) -> None:
        self.products.append(product)

    def find(self, product_name: str) -> Product | None:
        for product in self.products:
            if product.name == product_name:
                return product
        return None

    def remove(self, product_name: str) -> None:
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)

    def __repr__(self) -> str:
        result = []

        for product in self.products:
            result.append(f"{product.name}: {product.quantity}")

        return '\n'.join(result)