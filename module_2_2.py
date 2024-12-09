first = int(input("Введите число: "))
second = int(input("Введите число: "))
third = int(input("Введите число: "))
if second != third and first != second and first != third :
    print(0)
elif first == second == third:
    print(3)
elif   second == third or first == second or first == third :
    print(2)
