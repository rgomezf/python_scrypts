
# Function called digit_sum that takes a positive integer n as input
# and returns the sum of all that number's digits.
def digit_sum(n):
    total = 0
    right_number = 0
    left_number = n
    while left_number != 0:
        right_number = left_number % 10
        left_number = left_number // 10
        total += right_number

    return total
