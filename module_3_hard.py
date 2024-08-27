def get_summa(*args):
    total_summ = 0

    for i in args:
        if isinstance(i, int):
            total_summ += i
        elif isinstance(i, str):
            total_summ += len(i)
        elif isinstance(i, (list, tuple, set)):
            for j in i:
                total_summ += get_summa(j)
        elif isinstance(i, dict):
            for key, value in i.items():
                total_summ += get_summa(key)
                total_summ += get_summa(value)
                
    return total_summ


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = get_summa(data_structure)
print(result)