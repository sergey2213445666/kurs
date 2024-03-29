#codenig: utf-8
low = int(input())
high = int(input())
between = True
while line := input():
    if between:
        between = low <= int(line) <= high
print(between)