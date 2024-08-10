def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params(5, 3)
print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

value_list = [4, False, 'gtx']
value_dict = {'a': 132, 'b': 82.3, 'c': 'film'}

print_params(*value_list)
print_params(**value_dict)

values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)