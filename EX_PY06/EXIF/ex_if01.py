# ---------------------------------------------
# 리스트에 데이터 있다 없다 
# - 있는 경우 : "*"     <= len([])  0보다 크면
# - 없는 경우 : "없다"
# ---------------------------------------------
# nums=[9]
# print( len(nums) )

# if len(nums)>0:
#     print("*")
# else: 
#     print("없다")

# ---------------------------------------------
# 데이터 22
# - 10보다 큰 데이터일 경우 숫자만큼 *을 출력
# - 10이하인 경우 *을 1개만 출력
# ---------------------------------------------
data=2 

if data>10:             # 22>10 --> True   2>10 --> False
    print( '*' * data )
else: 
    print('*')