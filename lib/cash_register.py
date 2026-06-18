"""
Cash Register Module

This module implements a CashRegister class that simulates a basic point-of-sale system.
It handles adding items, applying discounts, and voiding transactions.
"""

class CashRegister:
    """
    A cash register that tracks items, totals, and transactions.
    
    Attributes:
        discount (int): Percentage discount to apply to total (0-100)
        total (float): Current total price of all items
        items (list): List of item names added (including duplicates for multiples)
        previous_transactions (list): List of transaction dictionaries
    """
    
    def __init__(self, discount=0):
        """
        Initialize a new CashRegister instance.
        
        Args:
            discount (int, optional): Discount percentage. Defaults to 0.
        """
        # Set discount with validation
        self.discount = discount
        
        # Initialize empty state
        self.total = 0.0
        self.items = []
        self.previous_transactions = []
    
    @property
    def discount(self):
        """Get the current discount percentage."""
        return self._discount
    
    @discount.setter
    def discount(self, value):
        """
        Set the discount percentage with validation.
        
        Args:
            value (int): Discount percentage (0-100)
        """
        # Ensure discount is an integer
        if not isinstance(value, int):
            print("Not valid discount")
            self._discount = 0
            return
        
        # Ensure discount is between 0-100 inclusive
        if 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")
            self._discount = 0
    
    def add_item(self, item, price, quantity=1):
        """
        Add an item to the cash register.
        
        Args:
            item (str): Name of the item
            price (float): Price per unit
            quantity (int, optional): Number of items. Defaults to 1.
        """
        # Calculate total price for this item
        item_total = price * quantity
        
        # Add to total
        self.total += item_total
        
        # Add item name to items list for each quantity (for multiples)
        for _ in range(quantity):
            self.items.append(item)
        
        # Record transaction with details
        transaction = {
            'item': item,
            'price': price,
            'quantity': quantity,
            'item_total': item_total
        }
        self.previous_transactions.append(transaction)
    
    def apply_discount(self):
        """
        Apply the discount to the total price.
        
        If no discount is set, prints a message and returns.
        The discount is applied as a percentage off the total.
        """
        # Check if there is a discount to apply
        if self.discount == 0:
            print("There is no discount to apply.")
            return
        
        # Apply discount as percentage off
        if self.discount > 0:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            # Round to 2 decimal places for currency
            self.total = round(self.total, 2)
            
            # Format the total without trailing zeros if it's a whole number
            if self.total.is_integer():
                total_str = str(int(self.total))
            else:
                total_str = f"{self.total:.2f}"
            
            # Print success message with updated total
            print(f"After the discount, the total comes to ${total_str}.")
    
    def void_last_transaction(self):
        """
        Void the most recent transaction.
        
        Removes the last transaction from previous_transactions,
        subtracts its total from the overall total,
        and removes the item from the items list.
        """
        # Check if there are transactions to void
        if not self.previous_transactions:
            print("No transactions to void.")
            return
        
        # Get the last transaction
        last_transaction = self.previous_transactions.pop()
        
        # Subtract the item total from the overall total
        self.total -= last_transaction['item_total']
        self.total = round(self.total, 2)
        
        # Remove the item from items list for each quantity
        for _ in range(last_transaction['quantity']):
            if last_transaction['item'] in self.items:
                self.items.remove(last_transaction['item'])