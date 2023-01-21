# BOJ_5622_다이얼.py

dial_dic = {
    "A":2, "B":2, "C":2,
    "D":3, "E":3, "F":3,
    "G":4, "H":4, "I":4,
    "J":5, "K":5, "L":5,
    "M":6, "N":6, "O":6,
    "P":7, "Q":7, "R":7, "S":7,
    "T":8, "U":8, "V":8,
    "W":9, "X":9, "Y":9, "Z":9,
}

Alphabet = input()
result = 0

for a in Alphabet:
    # print(a)
    # print(dial_dic[a])
    result += dial_dic[a]
    result += 1
print(result)