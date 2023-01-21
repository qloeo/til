# BOJ_2947.py
Number_list = list(map(int,input().split()))
good_Numbers = [1,2,3,4,5]

while True:
    for i in range(len(Number_list)-1):
        if Number_list[i] > Number_list[i+1]:
            result = Number_list[i]
            Number_list[i] = Number_list[i+1]
            Number_list[i+1] = result
            print(*Number_list)
    if Number_list == good_Numbers :
        break
