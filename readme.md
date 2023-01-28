# Stack & Queue
- 데이터 구조 == 데이터 + 구조 : 어떻게 저장하고 어떻게 활용(조작)할 수 있는지 ..

## Stack
- 한 쪽에서만 넣고 빼는 자료구조 (push, pop)
- LIFO(Last-in First-out, 후입선출)
- 이전 작업의 기업(뒤집기, 되돌리기, 되돌아가기)

```py
sum(range(1,45)))
```
- 괄호매칭, 함수 호출(재귀 호출), 백트래킹, DFS(깊이 우선 탐색)
- top : A[-1]
- 예제 : 제로

## Queue
- FIFO(First-in First-out, 선입선출)
-  dequeu : 큐의 맨 앞 데이터를 가져오는 행위
    - pop(0)
- enqueue : 큐의 맨 뒤에 데이터를 삽입하는 행위
    - append
- 프로세스 관리(데이터 버퍼), 클라이언트/서버(Message Queue) 
- BFS(너비 우선 탐색), 다익스트라(우선순위 큐)
- 예제 : 카드1

### Depue 덱
```py
from collections import deque
```
- 덱은 양방향. 큐보다 빠르다.
- 예제 : 카드1