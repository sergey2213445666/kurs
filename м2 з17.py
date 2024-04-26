def filter_custom(func, seq):
    for item in seq:
        if func(item):
            yield item

# Входные данные через eval, чтобы принимать корректные лямбда-функции и последовательности
func_in, seq_in = eval(input()), eval(input())

for x in filter_custom(func_in, seq_in):
    print(x)