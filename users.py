from abc import ABC

class User(ABC):
    def __init__(self,name,email,phone,address):
        self.name = name 
        self.email = email
        self.phone = phone
        self.address = address


class Customar(User):
    def __init__(self, name, email, phone, address):
        super().__init__(name, email, phone, address)
        self.cart = Order()

    def view_menu(self,restaurent):
        restaurent.menu.show_menu()

    def add_to_cart(self,restaurent,item_name,quantity):
        item = restaurent.menu.find_item(item_name)
        if item:
            item.quantity = quantity
            self.cart.add_items(item)
            print("Item Added!!")
        else:
            print("Item Not Found!!")

    def view_cart(self):
        print("****View Cart****")
        print("Name\tPrice\tQuantity")
        for item,quantity in self.cart.items.items():
            print(f'{item.name}\t{item.price}\t{quantity}')
        print(f"Total Price: {self.cart.total_price}")
    

class Order:
    def __init__(self):
        self.items = {}

    def add_items(self,item):
        if item in self.items:
            self.items[item] += item.quantity
        else :
            self.items[item] = item.quantity
    
    def remove(self,item):
        if item in self.items:
            del self.items[item]

    def total_price(self):
        return sum(item.price * quantity for item,quantity in self.items.items())

    def clear(self):
        self.items = {}

class Employee(User):
    def __init__(self, name, email, phone, address,age,designation,salary):
        super().__init__(name, email, phone, address)
        self.age = age
        self.designation = designation
        self.salary = salary

class Admin(User):
    def __init__(self, name, email, phone, address):
        super().__init__(name, email, phone, address)

    def add_employee(self,restaurent,employee):
        restaurent.add_employee(employee)

    def view_employee(self,restaurent):
        restaurent.view_employee()

    def add_new_item(self,restaurent,item):
        restaurent.menu.add_menu_item(item)

    def remove_item(self,restaurent,item):
        restaurent.menu.remove_item(item)


class Restaurent:
    def __init__(self,name):
        self.name = name
        self.employees = []
        self.menu = Menu()

    def add_employee(self,employee):
        self.employees.append(employee)

    def view_employee(self):
        print("Employee List -")
        for emp in self.employees:
            print(emp.name,emp.email,emp.phone,emp.address)


class Menu:
    def __init__(self):
        self.items = []
    
    def add_menu_item(self,item):
        self.items.append(item)

    def find_item(self,item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item
        return None
    
    def remove_item(self,item_name):
        item = self.find_item(item_name)
        if item:
            self.items.remove(item)
            print("Item Deleted!!")
        else :
            print("Item Not Found!!")

    def show_menu(self):
        print("**********Menu**********")
        print("Name\tPrice\tQuantity")
        for item in self.items:
            print(f'{item.name}\t{item.price}\t{item.quantity}')


class FoodItem:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


mamar_restaurent = Restaurent("Mamar Restaurent")

menu = Menu()
item = FoodItem("Pizza",150,12)
item1 = FoodItem("Barger",80,20)

admin = Admin('alu','alu@gamil.com',1234,'dhaka')
admin.add_new_item(mamar_restaurent,item)
admin.add_new_item(mamar_restaurent,item1)



customar1 = Customar('alu','alu@gamil.com',1234,'dhaka')

customar1.view_menu(mamar_restaurent)