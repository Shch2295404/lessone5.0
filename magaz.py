class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]

    def get_price(self, item_name):
        return self.items.get(item_name, None)

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price

# Создание объектов классов
central_store = Store("ЦЕНТРАЛЬНЫЙ", "МОСКВА")
north_store = Store("СЕВЕРНЫЙ", "САНКТ-ПЕТЕРБУРГ")
south_store = Store("ЮЖНЫЙ", "РОСТОВ НА ДОНУ")

# Добавление уникальных товаров в каждый магазин
central_store.add_item("яблоки", 500)
central_store.add_item("бананы", 350)
central_store.add_item("апельсины", 450)

north_store.add_item("груши", 600)
north_store.add_item("киви", 900)
north_store.add_item("ананасы", 1000)

south_store.add_item("виноград", 700)
south_store.add_item("персики", 800)
south_store.add_item("сливы", 550)

# Тестирование методов на одном из созданных магазинов (например, "ЦЕНТРАЛЬНЫЙ")
print(f"Товары в магазине {central_store.name} до изменений: {central_store.items}")

# Добавление товара
central_store.add_item("лимоны", 0.4)
print(f"Товары после добавления лимонов: {central_store.items}")

# Обновление цены
central_store.update_price("бананы", 0.65)
print(f"Товары после обновления цены на бананы: {central_store.items}")

# Удаление товара
central_store.remove_item("апельсины")
print(f"Товары после удаления апельсинов: {central_store.items}")

# Запрос цены товара
price = central_store.get_price("яблоки")
print(f"Цена на яблоки: {price}")

# Запрос цены товара, которого нет в ассортименте
price = central_store.get_price("ананасы")
print(f"Цена на ананасы (отсутствуют в ассортименте): {price}")