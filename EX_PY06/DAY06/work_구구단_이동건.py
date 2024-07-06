# ----------------------
# [1]  하나의 for로 구구단 작성하기
# -------------------------
for k in range(1, 73):
    i = (k - 1) // 9 + 2
    j = (k - 1) % 9 + 1

    print(f'{i} * {j} = {i * j}')

# ------------------------------------
# [2] 구구단 전체 출력 => 가로로 출력
for i in range(1,10):

    for d in range(2,6):
        print(f'{d} * {i} = {i*d:<2}' , end='   ')
    print('')

print('')
for i in range(1,10):

    for d in range(6,10):
        print(f'{d} * {i} = {i*d:<2}' , end='   ')
    print('')
