# 04_2027_대각선출력하기.py
for i in range (5):
    for j in range(5):
        if i == j:
            print('#',end='')
        else:
            print('+',end='')
    print()
