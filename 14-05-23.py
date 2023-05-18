from collections import defaultdict

sentence = "kjslaqpwoereeeeewwwefifjdksjdfhjdksdjfkdfdlddkjdjfjfjfjjjjfjffnefhkjgefkgjefkjgkefjekihutrieruhigtefhgbjkkkknbmssdsdsfdvneurghiueor"
test1 = "abccbaabccba"

def count_letter(s):
    d = defaultdict(lambda: 0)
    for i in s:
        d[i] += 1
    return d

def remove_singular(s):
    d = count_letter(s)
    for i in d.keys():
        if d[i] == 1:
            s = s.replace(i, "")
    return s

def compress_sentence(sentence):
    if sentence == "":
        return
    result = sentence[0]
    for i in sentence:
        if i == result[-1]:
            continue
        result += i
    return result

# def remove_middle(sentence):
#     if sentence == "":
#         return
#     result = sentence[0]
#     for i in range(1, len(sentence) - 1):
#         if result[-1] == sentence[i + 1] and sentence[i] != sentence[i + 1]:
#             continue
#         else:
#             result += sentence[i]
#     result += sentence[-1]
#     # print(result)
#     return result
def to_int(char):
    return ord(char) - 97
count = 0
cleaned_sentence = compress_sentence(sentence)
matrix = [[0 for i in range(26)] for j in range(len(cleaned_sentence))] 
print(matrix)
for i in range(len(cleaned_sentence)):
    character = cleaned_sentence[i]
    prev_line = matrix[i - 1]
    # print(prev_line, "prevline")
    matrix[i] = prev_line.copy()
    # print(matrix, "matrix now")
    char_to_int = to_int(character)
    if prev_line[char_to_int] == 1:
        # dont increase count
        # remove characters that appear between
        j = i - 1
        while cleaned_sentence[j] != character and j >= 0:
            matrix[i][to_int(cleaned_sentence[j])] = 0
            j -= 1
        
    else:
        count += 1
        matrix[i][char_to_int] = 1
print(count)
