# decorators are used to modify the behavior of function or class method without changing the code of the function or method itself.
# decorators are used to add previous or post functionality to the function or method.
# decorators are useful for:
#   Modify Behavior Without Changing Code
#   You can add behavior (like caching) to existing functions without editing their code. 
#   This is especially helpful when working with third-party libraries or legacy code.


def log_transaction(func):
    def wrapper():
        print("1. Logging transaction")
        func()
        print("3. Transaction logged")
    return wrapper

@log_transaction
def process_payment():
    print("2. Processing payment...")

process_payment()

###
def check_access(func):
    def wrapper(employee):
        if employee.get('role') == 'admin':
            func(employee)
        else:
            print("Access denied")
    return wrapper

@check_access
def delete_employee(employee):
    print(f"Employee {employee['name']} has been deleted")

admin = {'name': 'John Doe', 'role': 'admin'}
employee = {'name': 'Ana banana', 'role': 'employee'}

#delete_employee(admin)
#delete_employee(employee)

### Nested decorators ###

def check_access_privilege(privilege):
    def check_access(func):
        def wrapper(employee):
            if employee.get('role') == privilege:
                return func(employee)
            else:
                print("Access denied")
        return wrapper
    return check_access


def log_action(func):
    def wrapper(employee):
        print(f"Action: {func.__name__}")
        return func(employee)
    return wrapper

@check_access_privilege('admin')
@log_action
def delete_employee_nested(employee):
    print(f"Employee {employee['name']} has been deleted")

delete_employee_nested(admin)

### Class Decorators ###
class Circle:

    def __init__(self, radius):
        self._radius = radius

    @property
    def area(self):
        return 3.1416 * (self._radius ** 2)
    
    @property
    def radius(self):
        return self._radius
    
circle = Circle(5)
print(circle.area)
print(circle.radius)
