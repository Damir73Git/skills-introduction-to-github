my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0
while len(my_list > i:
    print(my_list[i])
    i = i + 1        
    if my_list[i] < 0:
        my_list.remove(my_list[i])
        break











