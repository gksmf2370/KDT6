command=input("4칙연산자 1개와 숫자 2개 입력:\n(예: + 10 3):").split()
print(command)

# ['+', '5', '9']
if command[0]=='+': 
    result=int(command[1])+int(command[2])
elif command[0]=='-':
    result=int(command[1])-int(command[2])
elif command[0]=='*':
    result=int(command[1])*int(command[2])
elif command[0]=='/':
    result=int(command[1])/int(command[2])
print(result)