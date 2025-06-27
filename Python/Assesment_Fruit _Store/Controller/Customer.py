import json
from Controller.Utils import log_transaction, clear_screen
from Controller import fruits_manager as fm
def browse_fruits():
    clear_screen()
    stock = fm.load_stock()
    if not stock :
        print("[!] No fruits available in stock.")
        return
    else:
        fm.view_stock()

def buy_fruit():
    clear_screen()
    stock = fm.load_stock()
    
    if not stock:
        print("[!] No fruits available for purchase.")
        return
    
    print("\n--- Purchase Fruit From Below ---")
    for name, qty in stock.items():
        print(f"{name}: {qty} unit(s)")

    name = input("Enter the fruit name to purchase: ").strip().capitalize()
    if name not in stock:
        print(f"[!] {name} is not available.")
        return
    max_quantity = stock[name]
    qty = int(input(f"Enter quantity (max {max_quantity}): "))
    if qty >max_quantity:
        print(f"[!] Only {max_quantity} unit(s) of {name} available.")
        return

    stock[name] -= qty
    if stock[name] == 0:
        del stock[name]
        
    fm.save_stock(stock)
    log_transaction(f"Customer purchased {qty} unit(s) of {name}.")
    print(f"Purchased {qty} {name}(s) successfully.")