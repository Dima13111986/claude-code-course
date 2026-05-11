"""Utility functions for basic numeric operations on lists."""


def calculate_average(numbers):
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)


def find_max(numbers):
    max_value = numbers[0]
    for n in numbers:
        if n > max_value:
            max_value = n
    return max_value


if __name__ == "__main__":
    data = [10, 20, 30, 40, 50]
    print("Average:", calculate_average(data))
    print("Max:", find_max(data))
    print("Empty average:", calculate_average([]))