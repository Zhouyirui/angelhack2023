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


def to_int(char):
    return ord(char) - 97


# counts the number of removals needed
count = 0
# remove all consequtive letters in the sentence to simplify it
cleaned_sentence = compress_sentence(sentence)

# a matrix that records, for each substring, whether a certain letter can be removed last
# if the value is 1, I can remove that character last. if the value is 0, I will not remove it last.
matrix = [[0 for i in range(26)] for j in range(len(cleaned_sentence))]

for i in range(len(cleaned_sentence)):
    character = cleaned_sentence[i]
    prev_line = matrix[i - 1]
    matrix[i] = prev_line.copy()
    char_to_int = to_int(character)
    # if current character has appeared before,
    # I will remove all letter between the current character and its previous occurance
    # e.g. "abcda" -> i will remove "bcd" before i remove "aa"
    # since I greedily remove "bcd" before "aa", I change the value from 1 to 0
    if prev_line[char_to_int] == 1:
        # dont increase count
        j = i - 1
        while cleaned_sentence[j] != character and j >= 0:
            # remove all characters that appear between (i.e. the "bcd" in "abcda")
            matrix[i][to_int(cleaned_sentence[j])] = 0
            j -= 1
    # elif current character has not appeared before
    else:
        count += 1
        # I can choose to remove the current character last
        matrix[i][char_to_int] = 1
print("result is ", count)
