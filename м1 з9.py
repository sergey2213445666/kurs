input_string = input().lower()
unique_chars = set(input_string) - {' '}
print(' '.join(sorted(list(unique_chars))))