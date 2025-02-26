import num_functions


# 1
def mds(ls):
    place = 0
    max_sum = num_functions.sum_digits(ls[0])
    max = ls[0]

    l = len(ls)
    i = 1
    while i < l:
        current_sum = num_functions.sum_digits(ls[i])

        if current_sum > max_sum:
            place = i
            max_sum = current_sum
            max = ls[i]

        i += 1

    return max_sum, place


# 2
def revall(ls):
    i = 0
    l = len(ls)
    while i < l:
        ls[i] = num_functions.reverse(ls[i])
        i += 1

# 3
def dmm(ls):
    max_dig = num_functions.count_digits(ls[0])
    min_dig = num_functions.count_digits(ls[0])
    max = ls[0]
    min = ls[0]

    for item in ls:
        dig = num_functions.count_digits(item)
        if dig > max_dig:
            max_dig = dig
            max = item

        if dig < min_dig:
            min_dig = dig
            min = item

    return max, min