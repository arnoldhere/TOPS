import json
import os
from Controller.Utils import log_transaction
STOCK_FILE_URL = 'data/stock.json'

def load_stock():
    try:
        file = open(STOCK_FILE_URL , 'r')
        return json.load(file)
        # with open(STOCK_FILE_URL, 'r') as file:
            # return json.load(file)
    except Exception as e:
        print("Error in load stock -> " , e)
        return {}
    
def save_stock(stock):
    try:
        with open(STOCK_FILE_URL, 'w') as file:
            json.dump(stock , file , indent=4)
    except Exception as e:
        print("Error in save stock -> " , e)
        return {}

def add_stock():
    try:
        os.system('cls' if os.name == 'nt' else 'clear')  # clears the screen
        stock = load_stock()
        name = input("Enter fruit name : ").strip().capitalize() 
        qty = int(input("Enter Quantity : "))
        
        if name in stock:
            stock [name] += qty
        else:
            stock [name] = qty
        
        save_stock(stock)
        print(f"{name} stock updated successfully.")
        log_transaction(f"Added {qty} {name}(s) to stock.")

    except Exception as e:
        print("Error in add stock -> " , e)
        return {}

def view_stock():
    os.system('cls' if os.name == 'nt' else 'clear')  # clears the screen
    stock = load_stock()
    print("\n--- Available Fruit Stock ---")
    for name, qty in stock.items():
        print(f"{name}: {qty} unit(s)")
    print("-" * 30)

def edit_stock():
    os.system('cls' if os.name == 'nt' else 'clear')  # clears the screen
    stock = load_stock()
    name = input("Enter fruit name to update: ").strip().capitalize()
    
    if name in stock:
        qty = int(input("Enter Quantity to update : "))
        stock[name] = qty
        save_stock(stock)
        log_transaction(f"Updated {name} stock to {qty}.")
        print(f"{name} stock updated successfully.")
    else:
        print("Stock not found....!!")   
