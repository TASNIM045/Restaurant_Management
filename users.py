from abc import ABC

class User(ABC):
    def __init__(self,name,email,phone,address):
        self.name = name 
        self.email = email
        self.phone = phone
        self.address = address

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

    def viewEmployee(self,restaurent):
        restaurent.view_employee()


class Restaurent:
    def __init__(self,name):
        self.name = name
        self.employees = [] 

    def add_employee(self,employee):
        self.employees.append(employee)

    def viewEmployee(self):
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
            if item == item_name:
                return item
        return None
    
    def remove_item(self,item_name):
        item = self.find_item(item_name)
        if item:
            self.items.remove(item)
            print("Item Deleted!!")
        else :
            print("Item Not Found!!")