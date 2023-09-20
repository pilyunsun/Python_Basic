# 컬렉션 타입
# - 변수 하나에 값을 여러개 저장
# - 실질적으로 변수에 컬렉션 1개가 저장
# - 리스트 ( List ), 튜플 ( Tuple ), 딕셔너리 ( Dictionary ), 셋 ( Set )

# 1. 리스트 ( List )
# - 시퀀스 자료형 ( 연속된 값 저장 )
# - 정렬 가능
# - mutable ( 생성 된 후 변경 가능 )
# - index 사용 ( Slicing 가능 )
# - paking가 unpacking 가능
# - 멤버함수 : append(), extent(), insert(), remove(), pop(), count(), sort(), reverse(), clear() 등등
# * 2차원 리스트는 표 ( table )과 동일한 형태

# 리스트 초기화 ( 생성 )
list_a = [1, 2, 3]
list_b = []
list_c = ["chosun", 98, 3.14, [1, 2, 3]] # 전체 1차원 리스트 [ 1, 2, 3 ]은 2차원 리스트

print(list_a)
print(list_b)
print(list_c)

print(list_c[1:3]) # 리스트 슬라이싱
print(list_c[0]) # 리스트에서 단일 값 추출
print(list_c[3][1]) # 2차원 리스트 값 추출

# 패킹과 언패킹
list_d = ['A', 'B', 'C', 'D'] # 패킹
a, b, c, d = list_d # 언패킹
# JAVA, C의 경우 -> a = list_d[0]

#append() : 리스트 맨 뒤에 값 추가
a = [1,2,3,4,5]
a.append(10)
print(a)

# insert( 인덱스 ( 위치 ), 값 ) : 리스트의 원하는 인덱스 ( 위치 )에 원하는 값 추가 가능
# - ex ) a.insert( 0, 100 ) : a 리스트의 0번쨰 인덱스에 100추가
a.insert(0, 0)
print(a)

# extent() : 리스트 확장 ( 리스트 + 리스트 )
a = [ 1, 2, 3 ]
b = [ 3, 4, 5 ]

# a.apppend( b ) -> [ 1, 2, 3, [ 3, 4, 5 ] ]
# print( a + b ) -> 실제론 병합 x, 병합된 값만 출력
a.extend( b ) # a 리스트에 b 리스트를 확장, a를 기준으로 병합
print(a)

# remove() : 값으로 삭제
a = [ 1, 2, 3, 4, 5 ]
a.remove( 3 )
print( a )

#pop() : 인덱스로 삭제
b = [ 1, 2, 3, 4, 5 ]
b.pop( 0 )
print( b )

#index() : 찾고자 하는 값의 인덱스 출력
c = [ 1, 2, 3, 4, 5 ]
print(c.index(3)) #인덱스 반환

# sort() and sorted() : 리스트 정렬
# - sort() : 리스트 자체를 정렬
# - sorted() : 복제한 값 정렬
a = [ 1, 5, 3, 4, 2 ]
b = sorted( a ) # a 리스트를 복제한 b 리스트를 정렬 ( a 리스트는 그대로 ), 오름차순
b = sorted( a, reverse = True ) # 내림차순 정렬

print( a )
print( b )