def is_correct_string(s):
    if 'i' in s or 'e' in s:
        return False
    if 'a' in s or 'o' in s:
        return True
    return False

input_str = input()
print(is_correct_string(input_str))