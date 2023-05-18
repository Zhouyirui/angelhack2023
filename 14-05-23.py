from collections import defaultdict

sentence = "kjslaqpwoereeeeewwwefifjdksjdfhjdksdjfkdfdlddkjdjfjfjfjjjjfjffnefhkjgefkgjefkjgkefjekihutrieruhigtefhgbjkkkknbmssdsdsfdvneurghiueor"


def count_letter(s):
    d = defaultdict(lambda: 0)
    for i in s:
        d[i] += 1
    print(d)

sentence = sentence.replace("a", "")
sentence = sentence.replace("m", "")
sentence = sentence.replace("v", "")
sentence = sentence.replace("q", "")
sentence = sentence.replace("p", "")
print(sentence)

def compress_sentence(sentence):
    if sentence == "":
        return
    result = sentence[0]
    for i in sentence:
        if i == result[-1]:
            continue
        result += i
    print(result)
    return result

s = compress_sentence(sentence)
count_letter(s)