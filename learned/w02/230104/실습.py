# 1부터 사용자가 입력한 양의 정수까지의 총합을 구하는 코드를 작성하시오.

target_number = 10
n = 0
result = 0

# 조건 : target_number >= n
# 반복 때마다 n+1, result 더하기!

while target_number >= n :
    result += n
    n += 1
   # print(result, n)
print(result)

