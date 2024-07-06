# ------------------------------------------
# 리스트 전용의 함수 즉, 메서드
# - 리스트의 원소/요소를 제어하기 위한 함수들
# -----------------------------------------
datas=[11, 22, 33]
nums=datas
print(f'datas=> {datas}\nnums =>{nums}')
nums[0]='백'

print(f'datas=> {datas}\nnums =>{nums}')

## 메서드 - 리스트 복사해주는 메서드 copy() ------
## 얕은 복사임!!! ==> 깊은 복사는 모듈 추가!
nums2=datas.copy()
nums2[0]='A'
print(f'datas=> {datas}\nnums =>{nums2}')