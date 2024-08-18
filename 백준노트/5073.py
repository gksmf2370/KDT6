while True:
    a = list(map(int, input().split()))
    if a[0] == 0 and len(set(a)) == 1:
        break

    if len(set(a)) == 1:
        print('Equilateral')
    elif sum(a) - max(a) > max(a):
        if len(set(a)) == 2:
            print('Isosceles')
        else:
            print('Scalene')
    else:
        print('Invalid')
