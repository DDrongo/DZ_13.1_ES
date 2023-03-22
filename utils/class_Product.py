
class Product:

    """класс имеет два атрибута: коффециэнт скидки и пустой список для созданных экземпляров"""

    discount_15 = 0.85
    all = []

    """иницализатор принимает имя, цену и количество товара на складе"""
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    """Метод возвращает данные экземпляра """
    def get_product(self):
        return f"Товар: {self.name}\nЦена: {self.price}\nНаличие в магазине: {self.quantity}"

    """Метод применяет скидку к цене и возвращает данные экземпляра """
    def get_discount(self):
        self.new_price = round(int(self.price) * self.discount_15)
        return f"Товар: {self.name}\nЦена: {self.new_price}\nНаличие в магазине: {self.quantity}"

    """Метод добавляет экземпляр к атрибуту [all] """
    def app_prod_list(self, product_app):
        self.product_app = product_app
        self.all.append(self.product_app)


