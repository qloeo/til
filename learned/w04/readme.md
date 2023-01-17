# 시간복잡도 & 빅오표기법
- 알고리즘을 비교하려면 무엇이 필요할까? : 특정한 기준이 필요하다.
    - 컴퓨터를 실행시키는데 드는 리소스는?
        1. CPU(시간)
        2. 메모리
        3. 디스크
    ### 시간 복잡도 계산하기
        1. Sequence of statement
            - 총 시간 = 시간(statement 1)+ ...... + 시간(statement k)
            - 1 * k = k
        2. 조건문
            if (조건):
                code block1
            else:
                code block2
            - Sequence of statement로 구성된 코드 블록 중 하나가 실행됨
            - 총 시간 = max(시간(code block1), 시간(code block2))
        3. 반복문
            for i in range(N):
                code block1
            - 반복 N번, 코드 블록도 N번 실행


            for i in range(N):
                for j in range(M):
                    code block1
            - 중첩 반복문
            - 외부 반복 N번, 내부 반복 M번 실행 == N * M번 실행


            for j in range(M):
                code block1

            for j in range(M):
                code block1
            - N번 + M번


            for i in range(N):
                for j in range(N):
                    code block1

            for j in range(N):
                code block2
            - N * N = N제곱 ----> N제곱 + N
            

            for i in range(M):
                for j in range(i, N):
                    code block1
            - 0 일 때 N번, 1일 때 N-1번, ... N + N-1 + ... + 1?!

        ## 빅오(O) 표기법
        1.
        count() 
        6n + 4 ---> O(n)

        2.
        count()
        3n + 2 ---> O(n)

        3.
        count()
        3n제곱 + 6n + 1 ---> O(n제곱)

        - 입력 n 이 '무한대'로 커진다고 가정하고 시간 복잡도를 간단하게 표시하는 것
        - '최고차항'만 남기고 계수와 상수 제거
        - 따라서, 원래 1과 2는 소요시간 2배 차이가 났지만, 점근적 표기법에 의해 동일한 시간 복잡도를 나타냄.

        ### (일반적인 상황에서) 1초가 걸리는 입력의 크기
        - O(N) : 1억(기준)
        - O(N*logN) : 500만
        - O(N제곱) : 1만
        - O(N세제곱) : 500
        - O(2^N) : 20
        - O(N!) : 10

        - O(1) : 단순계산 -> a+b, 100*200
        - O(N) : 리스트 순회, 1중 for문
        - O(N^2) : 2중 리스트 순회, 2중 for문

        ### log N 

        ### 1. 1부터 n까지 일일이 더하기 2. 가우스의 합 공식

        ### 두 코드의 시간 복잡도 차이는? -> 없다.
        1.
        for i in range(N):
            tmp = 0
            for number in numbers:
                if tmp < number:
                    tmp = number
        2.
        for i in range(N):
            max_value = max(numbers)

# 리스트
1. 배열(Array)
2. 연결 리스트(linked list)
- 파이썬 리스트
number = [10, 2, 5, 7]

for number in numbers:
    if number % 2 ==0:
        numbers.pop()
    print(number)
- 결과
    1. number 10 => pop => [10, 2, 5]
    2. number 2 => pop => [10, 2]
- 다른 방법
    1. 별도의 리스트를 추가하거나 관리를 하는 형태
    2. 인덱스로 접근해서 값을 변화 시킨다.
    3. 리스트를 copy해서 쓴다.
3. 리스트 컴프리헨션(List Comprehension) : 파이썬의 꽃