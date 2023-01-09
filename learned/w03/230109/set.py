"""
Set
세트를 활용하면 다른 컴터이너에서 중복된 값을 쉽게 제거할 수 있음.
다느 이후의 순서가 무시되므로 순서가 중요한 경우 사용할 수 있음.
- 아래 리스트에서 고유한 지역의 개수는?
"""
locations = ['서울', '서울', ' 대전', '광주', '서울', '대전', '부산', '부산']
result =[]

# 지역을 하나씩 반복
for location in locations:
    #만약에 결과가 통에 없다면,
    if location not in result:
        #결과 통에 추가
        result.append(location)

print(result)
print(len(result))
print(set(locations))
print(len(set(locations)))

