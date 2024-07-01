#-----------------------------------------------
# list 데이터 자료형 살펴보기
# - list와 메모리
#-----------------------------------------------
## list 생성-------------------------------------
nums=[10, 20]    #생성자
nums2=list([10, 20])

print(f'nums의 id => {id(nums)}')
print(f'nums[0]의 id => {id(nums[0])}')
print(f'nums[1]의 id => {id(nums[1])}')
print('*'*20)
print(f'nums2의 id =>{id(nums2)}')
print(f'nums2[0]의 id => {id(nums2[0])}')
print(f'nums2[1]의 id => {id(nums2[1])}')