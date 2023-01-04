number = int(input('숫자를 입력해주세요 >'))
print(number +10 )

string = input('좋아하는 음식을 입력해주세요 >')
print('좋아하는 음식:', string)

name = input('이름을 입력해주세요 >')
year = int(input('태어난 년도를 입력해 주세요 >'))
age = 2023 - year + 1
print('저의 이름은', name,'이고, 올해 나이는', age, '입니다.')

#풀이
name = '하니'
age = 19.9
print(name + '는' + str(age) + '살입니다'
print('{}는 {}살 입니다.'.format(name,age))
print(f'{name}는 {age}살 입니다.') #3.6+

str1 = input('첫 번째 문장을 입력해주세요 >')
str2 = input('두 번째 문장을 입력해주세요 >')
print(str1,str2)

num1 = int(input('숫자를 입력해주세요 >'))
print(-num1)

num1 = int(input('첫 번째 숫자를 입력해주세요 >'))
num2 = int(input('두 번째 숫자를 입력해주세요 >'))
print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1//num2)
print(num1%num2)

num1 = int(input('첫 번째 숫자를 입력해주세요 >'))
num2 = int(input('두 번째 숫자를 입력해주세요 >'))
num3 = int(input('세 번째 숫자를 입력해주세요 >'))
print((num1+num2+num3)//3)

num1 = int(input('첫 번째 숫자를 입력해주세요 >'))
num2 = int(input('두 번째 숫자를 입력해주세요 >'))
num3 = int(input('세 번째 숫자를 입력해주세요 >'))
num4 = int(input('네 번째 숫자를 입력해주세요 >'))
num5 = int(input('다섯 번째 숫자를 입력해주세요 >'))
print('[', num1,',', num2,',', num3, ',', num4, ',', num5, ']')

str = input('문자열을 입력해주세요 >')
num = int(input('숫자를 입력해주세요 >'))
print(str*num)
10
num1 = int(input('첫 번째 숫자를 입력해주세요 >'))
num2 = int(input('두 번째 숫자를 입력해주세요 >'))
num3 = int(input('세 번째 숫자를 입력해주세요 >'))
num4 = int(input('네 번째 숫자를 입력해주세요 >'))
num5 = int(input('다섯 번째 숫자를 입력해주세요 >'))
print(num1 + num2 + num3 + num4 + num5)

#풀이
result = 0
n1 = int(input('첫 번째 정수형 숫자를 입력해주세요 >'))
result += n1
n1 = int(input('두 번째 정수형 숫자를 입력해주세요 >'))
result += n2
n1 = int(input('세 번째 정수형 숫자를 입력해주세요 >'))
result += n3
n1 = int(input('네 번째 정수형 숫자를 입력해주세요 >'))
result += n4
n1 = int(input('다섯 번째 정수형 숫자를 입력해주세요 >'))
result += n5
print(result)

result = 0
result += int(input('첫 번째 정수형 숫자를 입력해주세요 >'))
print(result)
result += int(input('두 번째 정수형 숫자를 입력해주세요 >'))
print(result)
result += int(input('세 번째 정수형 숫자를 입력해주세요 >'))
print(result)
result += int(input('네 번째 정수형 숫자를 입력해주세요 >'))
print(result)
result += int(input('다섯 번째 정수형 숫자를 입력해주세요 >'))
print(result)