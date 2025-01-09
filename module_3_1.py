calls = 0
def count_calls():
    global  calls
    calls = 4
    print(calls)
print(calls)
count_calls()
print(calls)


def string_info(string):
    return len(string), string.upper(), string.lower()


def is_contains(string, list_to_search):
    string = string.lower()
    list_to_search = [item.lower() for item in list_to_search]
    return string in list_to_search

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))