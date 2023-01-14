# 명세서

# 클래스 이름 Calculator

# 인스턴스 변수
# number1 , number2 정수타입

# 생성자
# 두개의 정수를 인자로 받아서 number1, number2에 저장합니다.

# 메소드
# plus = number1 + number2를 반환(return)합니다.
# minus = number1 - number2를 반환(return)합니다.
# multiply = number1 * number2를 반환(return)합니다.
# division = number1 // number2를 반환(return)합니다.
# print = 인스턴스 변수와 모든 사칙연산 결과를 출력(print)합니다.

## Class
class Calculator:
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def print(self):
        print(f'number1 = {self.number1}, number2 = {self.number2}')
        print(f'합 : {self.plus()}')
        print(f'빼기 : {self.minus()}')
        print(f'곱 : {self.multiply()}')
        print(f'몫 : {self.division()}')
    
    def plus(self):
        return self.number1 + self.number2

    def minus(self):
        return self.number1 - self.number2
    
    def multiply(self):
        return self.number1 * self.number2
    
    def division(self):
        return self.number1 // self.number2


# 출력 예시
# plus 실행코드
calculator = Calculator(10, 5)
print(calculator.plus())

calculator.number1 = -2
calculator.number2 = 2
print(calculator.plus())
# 출력
# 15
# 0

# minus 실행코드
calculator = Calculator(10, 5)
print(calculator.minus())

calculator.number1 = -2
calculator.number2 = 2
print(calculator.minus())
# 출력
# 5
# -4

# multiply
calculator = Calculator(10,5)
print(calculator.multiply())

calculator.number1 = -2
calculator.number2 = 2
print(calculator.multiply())
# 출력
# 50
# -4

# division
calculator = Calculator(10, 5)
print(calculator.division())

calculator.number1 = -2
calculator.number2 = 2
print(calculator.division())
# 2
# -1

# print
calculator = Calculator(10, 5)
calculator.print()

calculator.number = -2
calculator.number = 2
calculator.print()
# munber = 10, number2 = 5
# 합 15
# 빼기 5
# 곱 50
# 몫 2
# number1 = -2, number2 =5
# 합 0
# 빼기 -4
# 곱 -4
# 몫 -1