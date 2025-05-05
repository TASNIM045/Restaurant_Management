from food_item import FoodItem
from menu import Menu
from users import Customar,Employee,Admin
from restaurent import Restaurent
from orders import Order

restaurent = Restaurent("Mamar Restaurent")

def customar_menu():
    name = input("Enter you name : ")
    email = input("Enter your email : ")
    phone = input("Enter you phone")
    address = input("Enter you address : ")
    customar = Customar(name=name,email=email,phone=phone,address=address)


    while True:
        print(f"Welcome To Our Restaurent {customar.name}")
        print("1. View Menu")
        print("2. Add item to cart")
        print("3.View Cart")
        print("4. PayBill")
        print("5. Exit")

        choice = int(input("Enter Your Choice : "))
        if choice == 1:
            customar.view_menu(restaurent)
        elif choice == 2:
            item_name = input("Enter item name : ")
            item_quantity = int(input("Enter item quantity : "))
            customar.add_to_cart(restaurent,item_name,item_quantity)
        elif choice == 3:
            customar.view_cart()
        elif choice == 4:
            customar.pay_bill()
        elif choice == 5:
            break
        else:
            print("Invalid Input")