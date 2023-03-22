from utils.class_Product import Product

telephone = Product("Iphone14ProMax", "159000", "5")
telephone.app_prod_list(telephone)
print()
print("До применения скидки:")
print(telephone.get_product()+"\n")
print("После применения скидки:")
print(telephone.get_discount())
print()
print(f"В списке:{telephone.all}")



game_console = Product("SonyPlayStation5", "52000", "5")
game_console.app_prod_list(game_console)
print()
print("До применения скидки:")
print(game_console.get_product()+"\n")
print("После применения скидки:")
print(game_console.get_discount())
print()
print(f"В списке:{Product.all}")