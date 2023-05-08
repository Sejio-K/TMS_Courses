class Singleton(type):
    """
    Метакласс для создания синглтона.
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Product:
    def __init__(self, id, name, price, amount):
        self.id = id
        self.name = name
        self.price = price
        self.amount = amount


class Store(metaclass=Singleton):
    """
    Синглтон-класс, представляющий магазин.
    """

    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)


class Basket:
    def __init__(self, id, products=None):
        self.id = id
        self.products = products or []


class Customer:
    def __init__(self, id, money, products_to_buy, store):
        self.id = id
        self.money = money
        self.products_to_buy = products_to_buy
        self.store = store
        self.basket = Basket(id)

    def add_product_to_basket(self, product):
        if product in self.store.products and self.money >= product.price:
            self.basket.products.append(product)
            self.money -= product.price
            self.store.products.remove(product)
        else:
            print(f"Product {product.name} is either not available or you don't have enough money")

    def buy_products(self):
        for product_name in self.products_to_buy:
            for product in self.store.products:
                if product.name == product_name:
                    self.add_product_to_basket(product)
                    break

    def show_basket(self):
        print(f"Products in the basket of Customer {self.id}:")
        for product in self.basket.products:
            print(f"- {product.name}")
        print()

    def show_remaining_money(self):
        print(f"Remaining money for Customer {self.id}: {self.money}")


# создаем продукты и добавляем их в магазин
store = Store()
store.add_product(Product(1, "Milk", 1.0, 10))
store.add_product(Product(2, "Cheese", 5.0, 5))
store.add_product(Product(3, "Bread", 0.5, 20))

# создаем покупателей и добавляем им корзины
customer1 = Customer(1, 10.0, ["Milk", "Bread"], store)
customer2 = Customer(2, 5.0, ["Cheese"], store)
customer1.buy_products()
customer2.buy_products()

# выводим содержимое корзин и оставшиеся деньги
customer1.show_basket()
customer1.show_remaining_money()
customer2.show_basket()
customer2.show_remaining_money()

# выводим список продуктов в магазине после покупок
print("Products in the store:")
for product in store.products:
    print(f"- {product.name} ({product.amount} left)")