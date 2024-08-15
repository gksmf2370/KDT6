# 높이가 V미터인 나무 막대
# 낮에 A미터 올라갈수있다 대신 자는동안 B미터 미끄러진다
# 모두 올라가는데 얼마나걸리는지
# 입력 A B V
# 2 1 5              출력 4
import sys

a, b, v=map(int,sys.stdin.readline().split())
# 도달하는 날을 x라했을떄 미끄러지는 날은 x-1일
# ax-b(x-1) = v       =>            x= (v-b)/(a-b)
x= (v-b)/(a-b)
if x == int(x):
    print(int(x))
else:
    print(int(x)+1)
