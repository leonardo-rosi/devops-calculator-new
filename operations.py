def sum (a: float, b: float) -> float:
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a + b
    else:
        return None

def subtract (a: float, b: float) -> float:
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a - b
    else:
        return None

def multiply (a: float, b: float) -> float:
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a * b
    else:
        return None

def divide (a: float, b: float) -> float:
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        if b == 0:
            return None
        return a / b
    else:
        return None
