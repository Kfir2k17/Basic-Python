# 1
def sum_digits(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10
    return sum


# 2
def reverse(num):
    new = 0
    while num > 0:
        new *= 10
        new += num % 10
        num //= 10
    return new


# 3
def count_digits(num):
    count = 0
    while num > 0:
        count += 1
        num //= 10

    return count
