# BOJ_10809_알파벳찾기.py
A = "abcdefghijklmnopqrstuvwxyz"
# A = [ "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

# S = input()
# S = "BAEKJOON"
S = "baekjoon"

for i in A: 
    print(S.find(i), end=' ') 
    # A 입력문자가 있으면 순서대로 번호를 붙여 index출력. 없으면 -1 출력