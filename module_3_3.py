def print_params(a, b, c):
    print(a,b,c)

print_params(1,'строка',True)

def print_params(b,c):
    print(b,c)

print_params(b = 25, c = [1,2,3])

def print_params(a,b,c):
    print(a,b,c)
value_list = [54,True,'Строка']
value_dict ={ 'a': 55, 'b' : False, 'c' : 'Графа'}
print_params(**value_dict)
print_params(*value_list)

def print_params(a,b,c):
    print(a,b,c)
value_list_2 = [54.32, 'Строка']
print_params(*value_list_2,42)
