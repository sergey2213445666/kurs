from collections import defaultdict
from typing import List, Tuple

def fill_specializations(specializations: List[Tuple[str, str]]):
    specialization_dict = defaultdict(list)
    for spec, name in specializations:
        specialization_dict[spec].append(name)
    return specialization_dict

# Ввод данных в формате кортежей специализация-имя
data = []
while True:
    try:
        spec, name = input().split()
        data.append((spec, name))
    except ValueError:
        break

specialization_dict = fill_specializations(data)
print(dict(specialization_dict))