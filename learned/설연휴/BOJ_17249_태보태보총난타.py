# BOJ_17249_태보태보총난타.py

String = input()
# String = " @===@==@=@==(^0^)==@=@===@"
result_left = 0
result_right = 0

for s in String:
    if s == "@" :
        result_left += 1
    elif s == "(" :
        break

reversed_String = String[::-1]

for s in reversed_String:
    if s == "@":
        result_right += 1
    elif s == ")" :
        break

print(f"{result_left} {result_right}")