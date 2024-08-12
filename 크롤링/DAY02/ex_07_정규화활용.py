import re
# ^.. $ 을 명시해야 정확한 자리수 검사가 이루어짐
tel_checker = re.compile(r'^(\d{2,3})-(\d{3,4})-(\d{4})$')

print(tel_checker.match('02-123-4567'))
match_groups =tel_checker.match('02-123-4567').groups()
print(match_groups)

print(tel_checker.match('053-950-45678'))  # 마지막 숫자의 자리수가 맞지 않음
print(tel_checker.match('053950-4567'))     # dash(-)가 없음


tel_number = '053-950-4567'
tel_number = tel_number.replace('-', '')
print(tel_number)

tel_checker1 = re.compile(r'^(\d{2,3})(\d{3,4})(\d{4})$')
print(tel_checker1.match(tel_number))
print(tel_checker1.match('0239501234')) #0239501234

## 
tel_checker = re.compile(r'^(\d{2,3})-(\d{3,4})-(\d{4})$')
m= tel_checker.match('02-123-4567')
 
print(m.groups())  # groups는 튜플로 받음 
print('group(): ', m.group()) # group은 전체 문자열 반환
print('group(0): ', m.group(0))
print('group(1): ', m.group(1))
print('group(2,3): ', m.group(2,3))
print('start():', m.start()) # 매칭된 문자열의 시작 인덱스
print('end(): ', m.end()) # 매칭된 문자열의 마지막 인덱스+1

cell_phone = re.compile(r'^(01(?:0|1|[6-9]))-(\d{3,4})-(\d{4}$)')

print(cell_phone.match('010-123-4567'))
print(cell_phone.match('019-1234-5678'))
print(cell_phone.match('001-123-4567'))
print(cell_phone.match('010-1234567'))

