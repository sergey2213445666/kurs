import sys

words = sys.stdin.read().split()
total_length = sum(len(word) for word in words)
average_length = total_length / len(words) if len(words) > 0 else 0
print("{:.2f}".format(average_length))