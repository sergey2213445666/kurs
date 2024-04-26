def average(numbers):
    nums = [int(num) for num in numbers.split()]
    return sum(nums) / len(nums)

while True:
    sequence = input()
    if sequence == "":
        break
    print(average(sequence))