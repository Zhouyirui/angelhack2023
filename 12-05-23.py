# This is an alternate solution for Question 5

encoded = "1111101111111111000111111100101111110101111111110011011111111111000100111111010\
0111100110111111100101111010010111111000111111111110001101111110101110011011111\
1111110001101111010011111100101111110010110111111101001111001101111111111100010\
11101100011111110111111111001110111111111110001111110111111101011111111110001111\
11011111110011111111111000111101111111011111111010011111111110001001111110100110\
01111111111000111011111111110101111101111111010111110111111010011110011111111110\
00100111111010011001111111111000111111011111111110001110011111011111110011111110\
01011111011111100011101111111111100011111111010111101110111111111110001111111110\
11111110101111111100011001111111111000111111111110001111111111100011111111010111\
1010011111110101111111111000100111111011011111101101101001111111000111111100111\
11111111000111111011111101001111111111000111111110101111011101111111111100011111\
11011011110111111110000011111110011101"

dictionary = {'a': '00',
              'b': '01',
              'c': '10',
              'd': '1100',
              'e': '1101',
              'f': '1110',
              'g': '111100',
              'h': '111101',
              'i': '111110',
              'j': '1111110000',
              'k': '1111110001',
              'l': '1111110010',
              'm': '1111110011',
              'n': '1111110100',
              'o': '1111110101',
              'p': '1111110110',
              'q': '1111110111',
              'r': '1111111000',
              's': '1111111001',
              't': '1111111010',
              'u': '1111111011',
              'v': '1111111100',
              'w': '1111111101',
              'x': '1111111110',
              'y': '1111111111',
              'z': '11111111110000',
              ' ': '11111111110001'}

reversed_dict = {}

for d in dictionary.items():
    reversed_dict[d[1]] = d[0]


results = []

decoded = ""
sentence = encoded
reversed_dict_filtered = reversed_dict.copy()
# remove the encoding for y first to prevent confusion for z and space
reversed_dict_filtered.pop("1111111111")

while len(sentence) > 0:
    found = False
    for j in range(max(len(sentence), 14)):
        binary = sentence[0:j]
        if binary in reversed_dict_filtered:
            decoded += reversed_dict_filtered[binary]
            sentence = sentence[j:]
            found = True
    if not found:
        break
print(sentence)
print(decoded)

# decoded sentence is : i love angelhack code challenge because it is fun and exciting and i dislike the word   that appears in the phrase
# since there are 3 spaces in a row betweeh the words "word" and "that". I can deduce that is a word that is wrongly deciphered as space
decoded = ""
sentence = '11111111110001'
while len(sentence) > 0:
    found = False
    for j in range(max(len(sentence), 14)):
        binary = sentence[0:j]
        if binary in reversed_dict:
            decoded += reversed_dict[binary]
            sentence = sentence[j:]
            found = True
    if not found:
        break
print(decoded)

# decoded word: yab
