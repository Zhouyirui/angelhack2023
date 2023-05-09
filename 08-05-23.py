from itertools import permutations
number = "1867"

number_set = set(number)

permuted = [int("".join(i)) for i in list(permutations(number_set))]


def solution():
    divisible = []
    for i in permuted:
        if i % 7 == 0:
            divisible.append(i)
    print(divisible)
    return (min(divisible) + max(divisible)) / 2


print(solution())
