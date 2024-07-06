# [1] str 점수 4개 리스트
jumsu=input().split()

# [2] str 점수 --> int 형변환
jumsu=list(map(int, jumsu))

# [3] 4과목의 점수를 0이상 100이하 범위 검사
if (0<=int(jumsu[0])<=100) and (0<=int(jumsu[1])<=100) and (0<=int(jumsu[2])<=100) and (0<=int(jumsu[3])<=100):
    if (sum(jumsu)/len(jumsu))>=80:
        print("합격")
    else :
        print("불합격")
else:
    print("잘못된 점수 입니다.")