# 예제_10.py
# 리스트, 조건문

n = 10
total = 0

for number in range(0, n +1):   
    if number % 2 == 0:         
        total += number * 2     
    elif number % 2 == 1:       
        total += number + 1 * 3 

print(total) 

"""
처음에 range에 n+1 이 좀 헷갈렸어요 ;; n 이 갑자기(ㅠㅠ) 생겨서요..
for문을 n+1 만큼 진행하라는 것 같습니다..
n t number
10 0 0
10 0 1
10 4 2
10 4+4=8 3
10 8+6=14 4
10 14+8=22 5
10 22+8=30 6
10 30+12=42 7
10 42+10=52 8
10 52+16=68 9
10 68+12=80 10
10 80+20=100

100
"""