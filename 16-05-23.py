C = "1"
D = "0"
layout = [[C, C, C, C, D],
          [C, D, D, D, D],
          [C, D, D, C, D],
          [D, C, D, C, D],
          [C, C, D, C, C],
          ]
test = [[D, D, D, D, C],
        [C, D, D, C, D],
        [C, D, D, C, C],
        [D, D, C, D, D],
        [C, D, D, D, D],
        ]


def print_layout(layout):
    print("---layout---")
    for i in layout:
        print(" ".join(i))
    print("------------")

print_layout(layout)
def generate_hash(layout):
    rows_joined = ["".join(i) for i in layout]
    # print(rows_joined)
    all_joined = "".join(rows_joined)
    # print(all_joined)
    return all_joined


def change_layout(layout):
    new_layout = [[D for i in range(5)] for j in range(5)]
    # print_layout(new_layout)
    for i in range(5):
        for j in range(5):
            count = count_adj(layout, i, j)
            if layout[i][j] == C and count == 1:
                new_layout[i][j] = C
            elif layout[i][j] == D and (count == 1 or count == 2):
                new_layout[i][j] = C
    # print_layout(new_layout)
    return new_layout

def is_valid(r, c):
    return r >= 0 and r < 5 and c >= 0 and c < 5

def count_adj(layout, r, c):
    count = 0
    if is_valid(r + 1, c):
        count += int(layout[r + 1][c])
    if is_valid(r - 1, c):
        count += int(layout[r - 1][c])
    if is_valid(r, c + 1):
        count += int(layout[r][c + 1])
    if is_valid(r, c - 1):
        count += int(layout[r][c - 1])
    return count

def solution(l):
    visited = set()
    while True:
        l = change_layout(l)
        hash = generate_hash(l)
        if hash in visited:
            print(hash)
            count = 0
            for i in range(len(hash)):
                if hash[i] == "1":
                    count += 2**i
            print(count, "count")
            break
        else:
            visited.add(hash)

solution(layout)


