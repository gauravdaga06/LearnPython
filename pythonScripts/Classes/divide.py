def safe_divide(a:float , b: float ) -> float | None :
    try:
        return a / b
    except ZeroDivisionError as error:
        return None

x = safe_divide(10,0)
print(x)
