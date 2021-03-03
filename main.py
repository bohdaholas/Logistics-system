from random import randint

class Location:
    def __init__(self, city, post_office):
        self.city = city
        self.post_office = post_office


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Item name is {self.name} and its price is {self.price}"


class Vehicle:
    def __init__(self, vehicle_num, is_available):
        self.vehicle_num = vehicle_num
        self.is_available = is_available


class Order:
    def __init__(self, username, city, post_office, items):
        self.order_id = randint(1000, 5000)
        self.username = username
        self.location = city, post_office
        self.items = items
        self.vehicle = None
        print(str(self))

    def __str__(self):
        total_price = sum([item.price for item in list(self.items)])
        return f"Your order #{self.order_id} is sent to {self.location}. Total price: {total_price} UAH."


class LogisticSystem:
    def __init__(self, vehicles):
        self.orders = []
        self.vehicles = vehicles

    def place_order(self, order):
        self.orders.append(order)

    def track_order(self, order_id):



