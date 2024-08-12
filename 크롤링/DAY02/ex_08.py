import re

# 전방 긍정 탐색 : 문자열이 (won을 포함하고 있으면 won 앞의 문자열 리턴) , 패턴과 일치하는 문자열을 만나면 패턴의 앞문자열반환(?=패턴)
lookahead1 = re.search('.+(?=won)', '1000 won')
if(lookahead1 != None):
    print(lookahead1.group())
else:
    print('None')

lookahead2 = re.search('.+(?=am)', '2023-01-26 am 10:00:01')
print(lookahead2.group())
# 전방 부정 탐색 (?!) : 4자리 숫자 다음에 '-'를 포함하지 않으면 앞의 문자열 리턴, 패턴과 일치하지 않는 문자열을 만나면 패턴 앞의 문자열 반환: (?!패턴)
lookahead3 = re.search('\d{4}(?!-)', '010-1234-5678')   #-가 패턴
print(lookahead3)


# 후방 긍정 탐색 ('am' 다음에 문자가 1개 이상 있으면 , 해당 문자열 리턴), 패턴과 일치하는 문자열을 만나면 패턴 뒤의 문자열 반환: (?<=패턴)
lookbehind1 = re.search('(?<=am).+', '2023-01-26 am 11:10:01')
print(lookbehind1)

lookbehind2 = re.search('(?<=:).+', 'USD: $51')
print(lookbehind2)

# 후방 부정 탐색('\b': 공백)
# 공백 다음에 $기호가 없고 숫자가 1개 이상이고 공백이 있는 경우
lookbehind4 = re.search(r'\b(?<!\$)\d+\b', 'I paid $30 for 100 apples.')
print(lookbehind4)

