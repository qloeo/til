# dic_ex.py

# 1. Input 대체
# members = [
#     "Jay", "John", "John", "Jay", "Jack", "Jack", "John", "Jo", "Jo", "Jack"
# ]

# jay = 0
# john = 0

# for member in members:
#     if member == "Jay":
#         jay +=1
#         .
#         .
#         .
#         .


#  for 문
members = [
    "Jay", "John", "John", "Jay", "Jack", "Jack", "John", "Jo", "Jo", "Jack"
]

count = {} 

for member in members:
    # if member in count:
    #     count[member] = count[member] + 1
    # else:
    #     count[member] = 1
    count[member] = count.get(member, 0) + 1

# 메서드  
count_items = count.items()
print(count_items)


# 흑마법
from collections import Counter 
new_count_items = Counter(members)
print(new_count_items)
# 위대한흑마법
print(Counter('pen pineapple apple pen'))
print(Counter('pen pineapple apple pen').most_common())
print(Counter('pen pineapple apple pen').most_common(2))