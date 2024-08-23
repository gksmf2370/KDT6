import sys

a = int(sys.stdin.readline().strip())
log = set()

for _ in range(a):
    name, status = sys.stdin.readline().strip().split()
    if status == 'enter':
        log.add(name)
    elif status == 'leave':
        log.remove(name)

for i in sorted(log, reverse=True):
    print(i)
    