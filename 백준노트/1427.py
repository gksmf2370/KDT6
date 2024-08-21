import sys
a=sys.stdin.readline().strip()


result = list(a)
result.sort(reverse=True)

sys.stdout.write(''.join(result))