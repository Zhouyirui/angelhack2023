DEBUG = False

'''
Removes duplicates from an input string, s, by recording the indices of dupes
in ignore_idx
'''
def remove_dupes(s, ignore_idx): # O(|s|)
    prev = None
    for i in range(len(s)):
        if (i in ignore_idx): continue
        c = s[i]
        if (prev == None): # initialize prev
            prev = c
            continue
        if (c == prev):
            ignore_idx.add(i)
        else:
            prev = c
    return

'''
Checks the chars to the left and right of idx to see if they can be combined, 
ignoring idx and any indices in ignore_idx
'''
def combine(s, idx, ignore_idx):
    # find left
    i = idx - 1
    left_char = None
    while (i >= 0):
        if (i not in ignore_idx):
            left_char = s[i]
            break
        i -= 1
    # find right
    j = idx + 1
    right_char = None
    while (j < len(s)):
        if (j not in ignore_idx):
            right_char = s[j]
            break
        j += 1
    if (left_char == None or right_char == None):
        return None
    if (left_char == right_char):
        ignore_idx.add(i) # or j, doesn't matter
        return i

def disconnect(nodes, memo, ignore_idx, tabs):
    num_rem_chars = len(nodes) - len(ignore_idx)
    if (num_rem_chars == 0):
        if (DEBUG): print(tabs, "0 letter")
        return 0
    elif (num_rem_chars == 1):
        if (DEBUG): print(tabs, "one letter")
        return 1

    min_moves = float("inf")
    for i in range(len(nodes)): # try deleting ith char
        if (i in ignore_idx): continue
        ignore_idx.add(i)
        if (DEBUG): print(tabs, i, "- ignore_idx:", ignore_idx)
        ignored_idx = combine(nodes, i, ignore_idx)
        key = frozenset(ignore_idx)
        num_moves = None
        if (key in memo):
            num_moves = memo[key]
        else:
            num_moves = disconnect(nodes, memo, ignore_idx, tabs + "  ")
            memo[key] = num_moves
        if (DEBUG): print(tabs, i, "- num_moves:", num_moves)
        total_moves = num_moves + 1
        min_moves = min(min_moves, total_moves)
        # undo
        ignore_idx.remove(i)
        if (ignored_idx != None): ignore_idx.remove(ignored_idx)
        if (DEBUG): print(tabs, "undo ignore_idx:", ignore_idx)
    return min_moves


def disconnect_wrapper(nodes):
    memo = dict()
    ignore_idx = set()
    remove_dupes(nodes, ignore_idx)
    tabs = "" # DEBUG
    return disconnect(nodes, memo, ignore_idx, tabs)


nodes1 = "aabbaa" # sol = 2
nodes2 = "aabbbcccaacccaa" # sol = 4
nodes3 = "abcba" # sol = 3
node_series = "kjslaqpwoereeeeewwwefifjdksjdfhjdksdjfkdfdlddkjdjfjfjfjjjjfjffnefhkjgefkgjefkjgkefjekihutrieruhigtefhgbjkkkknbmssdsdsfdvneurghiueor"
print(disconnect_wrapper(nodes1))
print(disconnect_wrapper(nodes2))
print(disconnect_wrapper(nodes3))
# print(disconnect_wrapper(node_series))