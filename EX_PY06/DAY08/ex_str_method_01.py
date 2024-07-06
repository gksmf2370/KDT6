# -----------------------------------------
# str 데이터 타입 전용 함수 즉, 메서드 살펴보기
# ------------------------------------------
msg='Hello 0705'
#    0123456789
#[원소/요소 인덱스 찾기 - find(문자1개 또는 문자열)]
# - 'H'의 인덱스
idx=msg.find('H')
print(f'H의 인덱스 : {idx}')

# - '7'의 인덱스
idx=msg.find('7')
print(f'7의 인덱스 : {idx}')

# - 'llo'의 인덱스 #l이 시작하는 인덱스가나옴
idx=msg.find('llo')
print(f'H의 인덱스 : {idx}')

# - 'llO'의 인덱스  => 대소문자 일치, 존재하지 않으면 -1 결과로 줌
idx=msg.find('llO')
print(f'H의 인덱스 : {idx}')

#[원소/요소 인덱스 찾기 - index(문자1개 또는 문자열)]
#- 'H'의 인덱스
idx=msg.index('H')
print(f'H의 인덱스 : {idx}')

#- 'h'의 인덱스 : 존재하지 않으면 Error 발생
if 'h' in msg:  # 'h'의 유무를 먼저 판별
    idx=msg.index('h')
    print(f'h 인덱스 : {idx}') 

#-------------------------------------
# 문자열에 동일한 문자가 여러개 존재하는 경우
#--------------------------------------
msg="Good luck good"
# #    01234567890123

cnt=msg.count('o')
print(f'cnt>={cnt}')
idx=-1
for n in range(cnt):
    idx=msg.find('o',idx+1)
    print(f'{n+1}번째 o의 인덱스 : {idx}')

# # - 'o'의 인덱스 찾기 => 첫번째 'o'인덱스
# print(msg.index('o'))


# # - 'o'의 인덱스 찾기 => 두번째, 'o'인덱스
# # - "od luck good"
# idx=msg.find('o', idx+1)
# print(f'두번째 o의 인덱스 : {idx}')

# # - 'o'의 인덱스 찾기 => 세번째, 'o'인덱스
# # - "d luck good"
# idx=msg.find('o', idx+1)
# print(f'세번째 o의 인덱스 : {idx}')

# # - 'o'의 인덱스 찾기 => 네번째, 'o'인덱스
# # - "od"
# idx=msg.find('o', idx+1)
# print(f'네번째 o의 인덱스 : {idx}')

#-------------------------------------
# 문자열의 뒷부분부터 찾기하는 메서드 ==> rfind(), rindex()
#--------------------------------------
msg="Happy"
#    01234

# - 첫번째 'p'의 인덱스 찾기
idx=msg.rfind('p')
print(f'p의 인덱스: {idx}')

# - 두번째 'p' 인덱스 찾기
#"Happy"
# 012
idx=msg.rfind('p', 0, idx) # 0 = 시작인덱스 , idx를 넣은이유 idx앞에꺼부터 찾아나가서
print(f'p의 인덱스: {idx}')

# - 파일명에서 확장자 txt, jpeg, xlsx, zip, gz 찾기
# - hello.txt, 2024년상반기경제분석.doc

files=['hello.txt', '2024년상반기경제분석.doc', 'kakao_12345566879.jpg']
for file in files:
    # '.' 인덱스 찾기
    dot_idx=file.find('.')
    # str에서 확장자만 출력
    print(file[:dot_idx])


