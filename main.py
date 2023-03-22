from utils.class_Product import Product

"Создаём экземпляр класса 'telephone'"
telephone = Product("Iphone14ProMax", "159000", "5")

"Добавляем экземпляр в список"
telephone.app_prod_list(telephone)
print()

"Выводим данные без приминения скидки"
print("До применения скидки:")
print(telephone.get_product()+"\n")

"Выводим данные после приминения скидки"
print("После применения скидки:")

"Применяем скидку"
print(telephone.get_discount())
print()

"Добавляем экземпляр в список"
print(f"В списке:{telephone.all}")


"Повторяем вышепроделанное с новым экземпляром"
game_console = Product("SonyPlayStation5", "52000", "5")
game_console.app_prod_list(game_console)
print()
print("До применения скидки:")
print(game_console.get_product()+"\n")
print("После применения скидки:")
print(game_console.get_discount())
print()

"Выводим список экземпляров"
print(f"В списке:{Product.all}")