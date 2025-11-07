# -*- coding: utf-8 -*-
"""
Created on Fri Nov  7 01:17:38 2025

@author: pc
"""

from shopping_cart import ShoppingCart
from item import Item
from exceptions import ItemNotFoundError

def main():
    cart = ShoppingCart()

    while True:
        print("\n--- Shopping Cart Menu ---")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. View Cart")
        print("4. Show Cart Length")
        print("5. Check if Item Exists")
        print("6. Total Price")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Item name: ")
            price = float(input("Price: "))
            qty = int(input("Quantity: "))
            item = Item(name, price, qty)
            cart.add_item(item)
            print("Item added!")

        elif choice == "2":
            name = input("Enter item name to remove: ")
            try:
                cart.remove_item(name)
                print("Item removed!")
            except ItemNotFoundError as e:
                print(e)

        elif choice == "3":
            print(cart)

        elif choice == "4":
            print("Items in cart:", len(cart))

        elif choice == "5":
            name = input("Enter item name: ")
            print(name in cart)

        elif choice == "6":
            print("Total Price:", cart.total_price())

        elif choice == "7":
            print("Exiting...")
            break

        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
