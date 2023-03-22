from utils.class_Product import Product

telephone = Product("Iphone", "100000", 10)

"""тестируем методы класса Product"""
def test_get_product():
    assert Product.get_product(telephone) == "Товар: Iphone\nЦена: 100000\nНаличие в магазине: 10"

def test_get_discount():
    assert Product.get_discount(telephone) == "Товар: Iphone\nЦена: 85000\nНаличие в магазине: 10"

def test_app_prod_list():
    assert Product.app_prod_list(telephone, telephone) == None

