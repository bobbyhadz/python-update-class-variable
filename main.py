# Updating class variables in Python

class Employee():
    # 👇️ class variable
    cls_id = 'employee'

    def __init__(self, name, salary):
        # 👇️ instance variables
        self.name = name
        self.salary = salary

    # ✅ update class variable
    @classmethod
    def set_cls_id(cls, new_cls_id):
        cls.cls_id = new_cls_id
        return cls.cls_id

    # ✅ update instance variable
    def set_name(self, new_name):
        self.name = new_name
        return new_name


print(Employee.cls_id)  # 👉️ employee
Employee.set_cls_id('new_employee_id')
print(Employee.cls_id)  # 👉️ new_employee_id

bob = Employee('Bobbyhadz', 100)

bob.set_name('Bobbyhadz2')
print(bob.name) # 👉️ Bobbyhadz2