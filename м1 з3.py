left = int(input())
right = int(input())

is_inside = True
while True:
    try:
        num = int(input())
    except ValueError:
        break
    
    if num < left or num > right:
        is_inside = False

print(is_inside)