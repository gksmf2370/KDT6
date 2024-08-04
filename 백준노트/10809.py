# a, ord('a')=97  chr(97)=a

name=list(input())

for i in range(97,123):
    if chr(i) in name:
        
        print(name.index(chr(i)),end=' ')
    else: print(-1, end=' ')