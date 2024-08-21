import sys
a = int(sys.stdin.readline())
b = [int(sys.stdin.readline().strip()) for _ in range(a)]
b.sort()

#for i in range(a):
#    print(b[i])

# 개선점

# 출력도 한 번에 처리
sys.stdout.write('\n'.join(map(str, b)) + '\n')  # sys.stdout.write('\n'.join(map(str, b)) + '\n')

sys.stdout.write('\n'.join(map(str, b)) + '\n')