def replace_special_chars(s):
    special_chars = ['!', '%', '#', '@']
    count = 0
    for char in special_chars:
        count += s.count(char)
        s = s.replace(char, '')
    return count, s.lower()

input_str = input()
replacement_count, output_str = replace_special_chars(input_str)

print(replacement_count)
print(output_str)