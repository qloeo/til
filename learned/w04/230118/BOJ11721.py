# BOJ11721.py
# String = str(input())
String = "skfdjkeiajfabcdefghijklmnopqrstuvndkjsfliajabcxzqppyz"
print(String)
while True:
    print(String[0:10])
    del_str = String[0:10:1]
    String = String.strip(del_str)
    print(String)
    if bool(String) == False:
        break

String = str(input())
# String = "skfdjkeiajfabndkjsfliajabcxzqppyz"
while True:
    print(String[0:10])
    String = String.lstrip(String[0:10])
    if bool(String) == False:
        break