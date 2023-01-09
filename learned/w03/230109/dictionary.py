# dictionary : 키와 값의 모음
# 지역 별 갯수를 구하세요
locations = ['서울', '서울', ' 대전', '광주', '서울', '대전', '부산', '부산']
result = {}

# for location in locations:
#     # 만약에 result에 있으면 값 추가
#     if location in result:
#         result[location] += 1
#     # 만약에 result에 없으면 키 값 추가
#     else:
#         result[location] = 1

# print(result)

for location in locations:
    # 만약에 result에 있으면 값 추가
    # if location in result:
    result[location] = result.get(location, 0) + 1

print(result)