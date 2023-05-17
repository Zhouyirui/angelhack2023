'''
Removes duplicates from an input string, s
'''
def remove_dupes(s): # O(|s|)
    prev = s[0]
    char_arr = [prev]
    for i in range(len(s)):
        c = s[i]
        if (c != prev):
            char_arr.append(c)
            prev = c
    return "".join(char_arr)

'''
Input:
    nodes(str): string representing nodes to disconnect
'''
def disconnect(nodes, memo):
    if (len(nodes) == 1): return 1

    min_moves = float("inf")
    for i in range(len(nodes)): # try deleting ith char
        rem_string = nodes[:i] + nodes[i+1:]
        rem_string = remove_dupes(rem_string)
        num_moves = None
        if (rem_string in memo):
            num_moves = memo[rem_string]
        else:
            num_moves = disconnect(rem_string, memo)
            memo[rem_string] = num_moves
        total_moves = num_moves + 1
        if (total_moves < min_moves):
            min_moves = total_moves
    return min_moves


def disconnect_wrapper(nodes):
    nodes = remove_dupes(nodes)
    memo = dict()
    return disconnect(nodes, memo)


nodes1 = "aabbaa" # sol = 2
nodes2 = "aabbbcccaacccaa" # sol = 4
nodes3 = "abcba" # sol = 3
node_series = "kjslaqpwoereeeeewwwefifjdksjdfhjdksdjfkdfdlddkjdjfjfjfjjjjfjffnefhkjgefkgjefkjgkefjekihutrieruhigtefhgbjkkkknbmssdsdsfdvneurghiueor"
print(disconnect_wrapper(node_series))