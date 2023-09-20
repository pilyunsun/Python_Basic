# 컬렉션 타입
# - 변수 하나에 값을 여러개 저장
# - 실질적으로 변수에 컬렉션 1개가 저장
# - 리스트(list), 튜플(Tuple), 딕트(Dictionary), 세트(set)

# 1. 리스트(List)
# - 시퀀스 자료형(연속 된 값 저장)
# - 대괄호 사용[]
# - 정렬 가능
# - mutable(생성된 후 변경 가능)
#   index 사용(Slicing 가능)
# - paking 과 unpaking 가능
# - 맴버함수: append(), extend(), insert(), remove(), pop(), index(), sorted(), reverse(), clear() 등등
# - 2차원 리스트는 표(table)과 동일한 형태

# 리스트 초기화(생성)
list_a = [1,2,3]
list_b = []
list_c = ["chosun", 98, 3.14, [1, 2, 3]]
print(list_c[0])
print(list_c[1:3]) # 리스트 슬라이싱

# 패킹과 언패킹
list_d = ["A","B","C"] #패킹
a, b, c = list_d # 언패킹

# append(): 리스트 맨 마지막에 값 추가!
a = [1,2,3,4,5]
a.append(10)
print(a)

# insert() : 원하는 인덱스에 값 추가!
a.insert(1,"A")
print(a)

# extend(): 리스트 병합(List A + B)
a = [1,2,3]
b = [3,4,5]
# a.append(b) -> [1, 2, 3, [3, 4, 5]]
a.extend(b)
print(a)
# or print(a+b)

#remove(): 값으로 삭제
a = ["a","b","c"]
a.remove("b")
print(a)
#pop: 인덱스로 삭제
b = ["a", "b", "c"]
b.pop(0) # 값을 삭제 전 변수에 담아서 삭제 후에 사용 가능! (선택사항)
print(b)
print(c)

# index(): 찾고자 하는 값의 인덱스 반환
a = [1,2,3]
print(a.index(3)) # 인덱스 반환

# sort() and sorted(): 리스트 값 정렬!
# - sort(): 원본 값 정렬 (주의: 보통 원본 값을 수정 하는 경우 극히 드믐)
# - sorted(): 복제 한 값 정렬
a = [9,3,2,1,5,8,10]
b = sorted(a)
print(a)
print(b)