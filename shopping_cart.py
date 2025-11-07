# -*- coding: utf-8 -*-
"""
Created on Fri Nov  7 01:18:30 2025

@author: pc
"""

from item import Item
from exceptions import ItemNotFoundError

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                self.items.remove(item)
                return
        raise ItemNotFoundError(f"Item '{item_name}' not found in cart")

    def total_price(self):
        return sum(item.price * item.quantity for item in self.items)

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __contains__(self, item_name):
        return any(item.name.lower() == item_name.lower() for item in self.items)

    def __add__(self, other):
        new_cart = ShoppingCart()
        new_cart.items = self.items.copy()

        if isinstance(other, Item):
            new_cart.add_item(other)
        elif isinstance(other, ShoppingCart):
            new_cart.items.extend(other.items)
        else:
            raise TypeError("Can only add Item or ShoppingCart")

        return new_cart

    def __str__(self):
        if not self.items:
            return "Shopping Cart is empty."

        result = "\n--- Shopping Cart ---\n"
        for item in self.items:
            result += str(item) + "\n"
        result += f"Total Price: {self.total_price()}"
        return result
