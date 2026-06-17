import math

def task1(a = 4, b = 3, c = 2, d= 1):
    try:    
        a = float(a)
        b = float(b)
        c = float(c)
        d = float(d)
        y = math.sqrt(a-b) / (c-d)
        return y
    except ValueError:
        print("Введите другие значения")
    except TypeError:
        print("Введите другие значения")
    except ZeroDivisionError:
        print(f"Значение {d} равно значнию {c}. Деление на 0")
    except OverflowError:
        print("Введите значение поменьше")

    if  a < b:
        raise ValueError("Введите другие значения")
    if not all(isinstance(x, float) for x in (a, b, c, d)):
        raise ValueError("Введите другие значения")
    if c == d:
        raise ZeroDivisionError(f"Значение {d} равно значнию {c}. Деление на 0") 
    if a > 10**400:
        raise ValueError("Введите другие значения")
