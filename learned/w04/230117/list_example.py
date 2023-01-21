# 10818	최소, 최대	https://www.acmicpc.net/problem/10818
Test_Case = int(input())
Numbers = list(map(int, input().split()))
Numbers_min = Numbers[0]
Numbers_max = Numbers[0]

for n in Numbers[1:]:
    if n < Numbers_min:
        Numbers_min = n
    elif n > Numbers_max:
        Numbers_max = n

print(Numbers_min, Numbers_max)


# 11720	숫자의 합	https://www.acmicpc.net/problem/11720
N = int(input())
Numbers = input()
Number_list = list(Numbers)
result = 0

for n in Number_list:
    result += int(n)
print(result)


# 2750	수 정렬하기	https://www.acmicpc.net/problem/2750
N = int(input())
Number_list = []

for t in range(N):
    Number = int(input())
    Number_list.append(Number)
    # print(Number_list)
Number_list.sort()
for i in range(N):
    print(Number_list[i])

# 2562	최댓값	https://www.acmicpc.net/problem/2562

# 내일.. 아니 오늘을 위해서 잠을 ....