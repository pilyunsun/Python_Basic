# 함수(method, funtion)
# - 어떤 일을 수행하는 코드 묶음
# - 반복적으로 동작해야하는 일들!

# ex) 아침마다 보고서를 만들려면 15줄에 코드를 작성하고 실행
#       -> 매일 아침마다 15줄 코드 작성 및 실행(비효율적)
#       => 15줄 코드를 함수로 정의하고 함수를 실행(효율적)

# 함수 개발 가이드라인
# 1.함수 이름
#   + 함수 내용은 가능하면 짧게 작성(line 줄이기 )
#   + 함수 이름에 함수의 역할과 의도를 명확히 드러낼 것!
# ex) def print_hello():
#           print("hello")

# 2.함수의 역할
#   + 하나의 함수에는 유사한 역할을 하는 코드만 포함
#   + 함수는 한 가지 기능만 명확히 정의
#   ex) def add)_value(x,y):
#       return x+y

# 3.함수를 만들어야 하는 이유
#   + 공통적으로 사용된느 코드는 함수로 생성
#   + 복잡한 로직이 사용되는 경우 식별 가능한 이름의 함수로 생성

# 함수의 종류
# 1.내장 함수(Built-in function)
#   + python에서 내부적으로 제공하는 함수
#   ex) print(), len(), type(),format(), list(),tuple()
#

#   2.외장함수(library or module)
#   + 라이브러리: 다른 사람이 만든 코드 묶음
#   + import문을 통해서 라이브러리 모듈을 제공
#   ex) import pandas as pd
#       df_data = pd.read_excel("path...")

# 3.사용자 정의 함수
#   + 개발자가 직접 만들어서 사용하는 함수

# 함수 이름 규칙
# Naming Rule => snake_case

# 함수 정의
# 1.기본 함수 문법
# def 함수명(parameter1,paramether2,///):
#     실행문
#     return 반환값

# 2.함수 정의시 "def" 키워드 사용(define)
# 3.인자 정의: 함수 입력 값
# 4.return: 함수 종료 의미
# 5.return 반환갑: 함수 종료 + 호출문으로 반환값 전달(tuple)
# 6.return 생략가능 -> 들여쓰기 종료되면 함수 종료
# 7,parameter와 return은 사용하지 않을수도 있음
#   (입력과 반환이 없는 함수도 존재)

# 1.함수 정의

# def sun_two_value(x,y):
#     n= x-y
#     print(f"결과: {n}")
#     return n

# 2.함수 호출
#   - 반환값이 없으면 none 출력
#   - 반환값이 있으면 출력함
#   * 함수 호출문을 실행하면 함수가 종료되고 호출했던 곳으로
#     돌아옴
#   * 돌아올 때 반환값이 있으면 호출문 = 반환값
#   * 돌아올 떄 반환값이 없으면 호출문 = none
# num = sun_two_value(5,8)
# print(num)


# 이름과 나이를 출력하는 함수

# def print_info(name,age):
#     print(f"이름: {name}, 나이: {age}")
#
#
# name = input("이름: ")
# age = int(input("나이: "))
# print_info(name,age)

# Default parameter
#   - 만약에 함수 호출시 입력해야하는 parameter가 empty인 경우
#   - Default parameter로 대체해주는 기능!
# ex) def test(a=1,b=5,c=3):    (o)
# ex) def test(a,b=5,c=3):      (o)
# ex) def test(a,b,c=3):        (o)
# ex) def test(a=1,b,c):        (x)
# ex) def test(a,b=5,c):        (x)
# ex) def test(a=1,b=5,c):    (x)


# return
#   - 기본적으로 함수 종료 의미
#   -return 반환값: 함수 호출문으로 값 전달(tuple type)
#   -return 만 사용하면 함수 호출문으로 none 값 전달
#   -return이 없는 경우 들여쓰기 종료되면 함수 종료로 간주
#   -return문 뒤에 오는 코드들은 실행 안됨(error x)


# def soju_yn(age):
#     if age >= 20:
#         return 1  # 0: 구매 가능
#         pass
#     else:
#         return 0  #1: 구매 불가
#
# age = int(input("나이: "))
# result = soju_yn(age)
# if result == 1:
#     print("소주 구매가 가능합니다")
# elif result == 0:
#     print("소주 구매가 불가능합니다")

# 변수의 범위
#   - 변수가 참조 가능한 코드사용이 범위를 명시
#   - 함수내의 변수는 자신이 속한 코드 블록이 종료되면 소멸
#   - 특정 코드블럭 안에서 선언된 변수를 지역변수
#   - 반대로 가장 상단에 정의되어 프로그램 종료 전까지
#   유지되는 변수를 전역 변수
#   -같은 이름의 지역변수,전역변수 존재하는 경우
#     가까운(지역변수)가 우선순위가 더 높음

num1 = 10 # 전역 변수
num2 = 20 # 전역 변수

def test(num1,num2):
    print(num1+num2)
    return num1+num2
test(30,40)
print(num1,num2)

# 함수 내에서 함수 밖의 전역변수를 변경하고 싶은 경우?
# 1.return 반환값
a = 1 #전역
print(a) #1 출력

def var_test(a):
    a = a+1  # 지역
    return a
a = var_test(3)
print(a)

# 2. global 키워들르 사용하는 방법(권장 x, 사용금지)
a = 1
print(a)

def var_test():
    global a
    a = a +1
var_test()
print(a)

# Variable length paramter(가변 길이 인자)
#   - 인자(parameter): 함수 입력값
#   - 함수 입력값의 개수가 함수를 호출할 때마다 매번 다른 경우
#       ->가변 길이 인자를 사용해야함!!!


# ex) format(),print()
#       print("hi"), print(",hi","hello")

# 1.tuple type: *args
def test(*args):
    for item in args:
        print(item)
test(10,20,30,40)
# 2.dict type: **kwargs
def test(**kwargs):
    for key, value in kwargs.items():
        print(key,value)




















