from Controller import fruits_manager as fm
from Controller import Customer as cm

def main_menu():
    print("\n========== Fruit Store ==========")
    print("1. Manager")
    print("2. Customer")
    print("3. Exit")
    print("=================================")
def Manager_menu():
    print("\n========== Fruit Store ==========")
    print("1. Add Fruit Stock")
    print("2. View Fruit Stock")
    print("3. Update Fruit Stock")
    print("4. Exit")
    print("=================================")
    
def Customer_menu():
    print("\n========== Fruit Store ==========")
    print("1. Browse Fruits (Customer)")
    print("2. Purchase Fruit (Customer)")
    print("3. Exit")
    print("=================================")


while True:
    try:
        main_menu()
        ch = int(input("Enter choice : "))
        if ch ==1:
            Manager_menu()
            x = int(input("Enter choice : "))
            if x == 1:
                fm.add_stock()
            elif x== 2:
                fm.view_stock()
            elif x== 3:
                fm.edit_stock()   
            elif x==3:
                print("See you soon...Goodbye!")
                break
        elif ch==2:
            Customer_menu()
            y = int(input("Enter choice : "))
            if y== 1:
                cm.browse_fruits()
            elif y== 2:
                cm.buy_fruit()
            elif y== 3:
                print("See you soon...Goodbye!")
                break
    except Exception as e:
        print(e)