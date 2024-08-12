import re

# compile() 사용 안함
m = re.match('[a-z]+', 'Python')
print(m)
print(re.search('apple', 'I like apple!')) # apple 패턴, I like apple: 검색 문자열

# compile() 사용: 객체 생성
p = re.compile('[a-z]+') # 알파벳 소문자
m = p.match('python')
print(m)
print(p.search('I like apple 123'))

m = re.match('[a-z]+', 'pythoN') #소문자 1개이상
print(m)

m = re.match('[a-z]+', 'PYthon') # 소문자 1개이상
print(m)

print(re.match('[a-z]+', 'regex python')) # 문자열 처음에 공백포함
print(re.match('[a-z]+', ' regexpython')) 
print(re.match('[a-z]+', 'regexpythoN'))
print(re.match('[a-z]+$', 'regexpythoN'))  # $: 문자열의 마지막에 소문자 1회 이상 검사
print(re.match('[a-z]+', 'regexPython'))
print(re.match('[a-z]+$', 'regexpython'))

# findall() 일치하는 모든 문자열을 리스트로 리턴
p= re.compile('[a-z]+') # 알파벳소문자
print([p.findall('life is too short! Regular expression test')])

# search() 일치하는 첫 번째 문자열만 리턴
result = p.search('I like apple 123')
print(result)

result = p.findall('I like apple 123')
print(result)