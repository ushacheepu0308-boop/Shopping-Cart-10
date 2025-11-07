# -*- coding: utf-8 -*-
"""
Created on Fri Nov  7 01:17:19 2025

@author: pc
"""

class Item:
    def __init__(self, name, price, quantity=1):
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)

    def __str__(self):
        return f"Item: {self.name}, Price: {self.price}, Qty: {self.quantity}"
