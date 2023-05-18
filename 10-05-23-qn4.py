def solution(arr, debug=False):
    arr.sort()
    min_cost = float('inf')
    for i in range(len(arr)): # exclude i
        if (debug): print("======== ", i, "===========")
        j = 0
        cost = 0
        elem1, elem2 = None, None
        while (j < len(arr)):
            if (j == i):
                if (debug): print("Exclude", arr[j])
                j += 1
                continue
            if (elem1 == None):
                elem1 = arr[j]
            elif (elem2 == None):
                elem2 = arr[j]
                if (debug): print("Pair: ", elem1, elem2)
                pair_cost = abs(elem1 - elem2)
                cost += pair_cost
                elem1, elem2 = None, None
            else:
                print("Error!")
                return
            j += 1
        if (debug): print("cost:", cost)
        min_cost = min(min_cost, cost)
    return min_cost

input = [1, 3, 54, 712, 52, 904, 113, 12, 135, 32, 31, 56, 23, 79, 611, 123, 677, 232, 997, 101, 111, 123, 2, 7, 24, 57, 99, 45, 666, 42, 104, 129, 554, 335, 876, 35, 15, 93, 13]
print(solution(input))

# Other test cases
'''
input2 = [1, 2, 4]
print(solution(input2))

input3 = [4, 2, 8, 1, 9]
print(solution(input3))
'''
