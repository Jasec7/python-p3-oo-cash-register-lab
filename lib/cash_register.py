#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount = 0):
    self.total = 0
    self.discount = discount
    self.items = []

  def add_item(self, title, price, quantity = 1):
    self.total += price * quantity
    self.last_transaction = price * quantity
    for _ in range(quantity):
      self.items.append(title)

  
  def apply_discount(self):
    if self.discount == 0:
        print("There is no discount to apply.")
    else:
        new_total = self.total * (100 - self.discount) / 100
        if new_total.is_integer():
            new_total = int(new_total)
        self.total = new_total
        print(f"After the discount, the total comes to ${new_total}.")

  def void_last_transaction(self):
      updated_total = self.total - self.last_transaction
      updated_total = float(updated_total)
      self.total = updated_total