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
        self.employees = [] 

    def add_employee(self,name,email,phone,address,age,designation,salary):
        employee = Employee(name,email,phone,address,age,designation,salary)
        self.employees.append(employee)
        print(f'${name} is added!')

    def viewEmployee(self):
        print("Employee List -")
        for emp in self.employees:
            print(emp.name,emp.email,emp.phone,emp.address)


ad = Admin('abul','abul@gmail.con',12345,"dhaka")
ad.add_employee("karim","karim@gmail.com",654111,"Dhaka",21,'helping hand',12000)

ad.viewEmployee()