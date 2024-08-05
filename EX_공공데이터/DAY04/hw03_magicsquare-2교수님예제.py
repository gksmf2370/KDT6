'''
    파이썬 홀수차 마방진 소스 코드

'''

#--------------------------------------------------------------------------
#  배열 출력 함수
#--------------------------------------------------------------------------
def print_matrix(matrix, size):
    for i in range(size):
        for j in range(size):
            print(f"{matrix[i][j]:2d}", end=" ")
        print()

#--------------------------------------------------------------------------
# 마방진 계산 함수
#--------------------------------------------------------------------------
def magicsquare(size):
    y = 0
    x = size//2; #  3 //2 = 1 => [0][1][2] 가운데 인덱스 계산

    next_y = 0
    next_x = 0

    print("Magic Square ({0}x{1})".format(size, size))
    # [0] * size: 행의 크기
    # [0][0][0]
    # [0][0][0]
    # [0][0][0]
    matrix = [[0]*size for i in range(size)]  # 2 차원 리스트 생성

    for n in range(size*size):
        matrix[y][x] = n+1      # (0, 2)에 1을 대입
        # 대각선 위쪽 방향으로 이동함
        next_y = y - 1
        next_x = x + 1

        # y축 방향으로 배열의 범위가 벗어난 경우, 마지막 행으로 이동 (size-1, y+1)
        if next_y < 0:
            next_y = size-1

        # x축 방향으로 배열의 범위가 벗어난 경우, 첫번째 열로 이동 (x-1, 0)
        if next_x >= size:
            next_x = 0

        # 이동하려는 위치에 이미 값이 있는 경우
        if matrix[next_y][next_x] != 0:
            y += 1
        else:
            y = next_y; # 다음 이동할 위치를 i, j에 저장
            x = next_x;

    print_matrix(matrix, size)


def main():
    size = 0
    while True:
        size = int(input("홀수차 배열의 크기를 입력하세요: "))
        if size % 2 == 1:
            magicsquare(size)
            break
        else:
            print("짝수를 입력하였습니다. 다시 입력하세요.")

main()