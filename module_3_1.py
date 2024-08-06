def count_calls():
    global calls
    calls += 1
    return calls


def string_info(string):
    count_calls()
    string = (len(string), string.upper(), string.lower())
    return string


def is_contains(string, list_to_search):
    count_calls()
    string = string.lower()
    list_to_search = [i.lower() for i in list_to_search]
    return string in list_to_search


calls = 0

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)

