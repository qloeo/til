# 9093.py
TestCase = int(input())
Result = []
for t in range(TestCase):
    String = list(map(str, input().split()))
    # String = ['I', 'am', 'happy', 'today']
    for s in String[0:]:
        Result.append(s[::-1])
    # for p in range(Result[0:]):
    print(Result[0:])
    print(str(Result[0:]))
    print(Result[0])
    Result = []
