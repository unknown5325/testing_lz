import math

def task1(a, b, c, d):
    try:
        a = float(a)
        b = float(b)
        c = float(c)
        d = float(d)
        return math.sqrt(a-b) / (c-d)
    except ValueError:
        print("Нужны другие значения")
    except ZeroDivisionError:
        print(f"Значение {d} равно значнию {c}. Деление на 0")
    

