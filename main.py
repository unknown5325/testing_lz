import unittest
from rtest import rtesting
from atest import Testingg

def main():
    ch = int(input("Ручная проверка - 0, Автоматическая проверка - 1: "))
    match ch:
        case 0:
            a = rtesting()
            print(a)
        case 1:
            if __name__ == "__main__":
                unittest.main()


if __name__ == "__main__":
    main()