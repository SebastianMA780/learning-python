def divide(a: int, b: int) -> float:	
    #validate types
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("a and b must be integers")
    if b == 0:
        raise ValueError("b cannot be zero")
    
    return a / b

try:
    print(divide(10, 2))  # 5.0
    print(divide(10, 0)) # b cannot be zero
except Exception as e:
    print(e)

try:
    print(divide(10, 3))  # 5.0
    print(divide(10, '2')) # a and b must be integers
except Exception as e:
    print(e)