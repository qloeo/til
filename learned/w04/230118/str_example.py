# str_example.py
# 2789	유학 금지	https://www.acmicpc.net/problem/2789
remove_str = "CAMBRIDGE"
String = list(input())

for rs in remove_str:
    for s in range(len(String)):
        if rs == String[s]:
            String[s] = ""
for result in String:
    print(result, end ="")
# remove로 지우고 출력도 가능
# compare비교하다.

# 한글자씩 비교

string = "KARIJERA"
compare_word = "CAMBRIDGE" #비교 알파벳
result = "" # 새로운 결과 문장

# 한 글자 씩 비교, 인덱스 활용 순회
for index in range(len(string)):
    # print(string[index])
    char = string[index]

    # 포함되지 않은 문자 찾기
    # print(char, char not in compare_word)
    if char not in compare_word:
        # 포함되지 않은 문자라면
        # 방법1. end 속성을 활용
        # ptint)char, end="")

        # 방법 2 새로운 문자열 만들기(추천)
        result += char

print(result)



# String = String.strip("CAMBRIDGE")

# print(String)

# 2675	문자열 반복	https://www.acmicpc.net/problem/2675

# 10988	팰린드롬인지 확인하기	https://www.acmicpc.net/problem/10988
String = str(input())
if String[0:] == String[::-1]:
    print(1)
else:
    print(0)

# 17249	태보태보 총난타	https://www.acmicpc.net/problem/17249

# 2941	크로아티아 알파벳	https://www.acmicpc.net/problem/2941
# 물자열 메서드 .replace(찾을 값, 변경 값)
# 찾을 값(영어 알파벳) -> 변경값(크로아티아 알파벳)으로 변환

# 10809	알파벳 찾기	https://www.acmicpc.net/problem/10809


