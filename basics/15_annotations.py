# annotations are used to specify the type of the variable
# but you have to be careful this annotations are not enforced

integer: int = 102
string: str = "hello"
boolean: bool = True
float_number: float = 3.14
list_of_integers: list[int] = [1, 2, 3, 4, 5]

def add_numbers(x: int, y: int) -> int:
    return x + y

class Employee:
    name: str
    age: int
    salary: float
    
    def __init__(self, name: str, age: int, salary: float):
        self.name = name
        self.age = age
        self.salary = salary