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
    def __init__(self, vehicle_num):
        self.vehicle_num = vehicle_num
        self.is_available = True


class Order:
    def __init__(self, user_name, city, post_office, items):
        self.order_id = randint(1000, 5000)
        self.user_name = user_name
        self.location = city, post_office
        self.items = items
        self.total_price = sum([item.price for item in list(self.items)])
        self.vehicle = None
        print(self)

    def __str__(self):
        return f"Your order #{self.order_id} is sent to {self.location[0]}. Total price: {self.total_price} UAH."


class LogisticSystem:
    def __init__(self, vehicles):
        self.orders = []
        self.vehicles = vehicles

    def place_order(self, order):
        for vehicle in self.vehicles:
            if vehicle.is_available:
                vehicle.is_available = False
                self.orders.append(order)
                return None
        return "There is no available vehicle to deliver an order."

    def track_order(self, order_id):
        for order in self.orders:
            if order.order_id == order_id:
                return print(order)
        return "No such order."
