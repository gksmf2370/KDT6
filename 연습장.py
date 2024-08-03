# 바구니 N개 바구니안에는 1~N까지번호가있음
#가장처음바구니는 공X, 바구니에는 공1개만가능
# M번 공을넣음, 한번넣을때 바구니범위를 정함
# 정한 바구니에 모두 같은번호가 적혀있는공을넣음
# 공이 이미들어있는경우에는 들어있는거 뺴고 새로운걸로넣ㅇㅁ
# 공을 어덯게 넣을지 주어졌을때, M번 공을넣은 이후에
# 각 바구니에 어떤 공이들어있는지 정해라

# 2 5 6 은 2번부터 5번바구니까지 6번공을 넣음

n, m = map(int,input().split())

new_list=[0]*n

for i in range(m):
    a, b, c = map(int,input().split())
    new_list[a-1:b]=[c]*(b-a+1)

for i in range(len(new_list)):
    print(new_list[i], end=' ')