def map_custom(func, seq):
    for item in seq:
        yield func(item)

# Входные данные через eval, чтобы принимать корректные лямбда-функции и последовательности
func_in, seq_in = eval(input()), eval(input())

for x in map_custom(func_in, seq_in):
    print(x)