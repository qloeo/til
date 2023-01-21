# BOJ_10988_팰린드롬.py
# String = str(input())
# if String[0:] == String[::-1]:
#     print(1)
# else:
#     print(0)


# while 문으로 풀기.... 그냥 위에꺼 가져다붙임... 이건 푼것도 아니다 ㅠㅠ
String = input()

while True:
    if String[0:] == String[::-1]:
        print(1)
    if String[0:] != String[::-1]:
        print(0)
    break

# 김탁희 쌤 풀이
# 1. Input
word = 'level'

# 2. 값 초기화(단어이 인덱스)
# start : 0
# end :len(word) -1
start = 0
end = len(word) -1
is_pal = True

# 3. while
# start 값이 end 보다 작을 때 , 
while start < end:
    # word[start], word[end] 비교해서
    # 다르면, 팰린드롬이 아니다!
    # print[word[start], word[end]]
    if word[start] != word[end]:
        is_pal = False
        break

    # 매 반복이 끝나면
    # start는 1씩 증가하고
    # end는 1씩 감소
    start += 1
    end -= 1

# 4. 출력
# 팰린드롬이면 1, 아니면 0을 출력한다.
if is_pal:
    print(1)
else:
    print(0)
# print(int(is_pal)) 라고 해도된다.

# 아주 아주 간단한식
word = 'tomato'
print(int(word == word[::-1]))