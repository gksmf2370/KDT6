# 내가 작성한 코드로는 메모리 에러가발생한다.

import sys
a = int(sys.stdin.readline())

b = [int(sys.stdin.readline().strip()) for _ in range(a)]
b.sort()

for i in range(a):
    print(b[i])

## 챗지피티 한테 물어보기
# 메모리해결을 위해 계수 정렬알고리즘을 사용해야한다.
import sys

# 입력 값의 범위가 1 ~ 10000 이므로 해당 크기의 배열을 생성
count = [0] * 10001

a = int(sys.stdin.readline())

# 각 숫자의 출현 횟수를 기록
for _ in range(a):
    num = int(sys.stdin.readline().strip())
    count[num] += 1

# 출현 횟수를 기반으로 정렬된 결과 출력
for i in range(10001):       # 배열을 순회하며 출현 횟수가 0보다 큰 숫자를 반복해서 출력합니다.
    if count[i] > 0:
        for _ in range(count[i]):
            print(i)