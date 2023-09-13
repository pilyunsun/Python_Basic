# 주석(comment) : 단순 메모, 실행 x

# 출력 함수(print)
 # - ()안의 갑을 출력
 # - 변수 값 확인 용도 또는 메세지 출력 용도
print("Hello Python")
print("=" * 200)

print("hello world")

 # 문자열 타입(string Type)
# - python: '',"" ->string

# - c,java:''(char),""(string)
# -문번: \(역슬러시) + @
# - 문자열 내의 일부 문자의 의미를 달리하여 특정한 효과 주기
# - 예) \n: 한 줄 개행, \t:탭 (8칸 공백)
print("hello \nPython");
print("hello \tPython");

#공부 tip)
# - 몇 버전부터 ~ 나온 기술(신기술) -> 신기술 공부, 구기술 공부 x

# 자료형(type)
# - python의 모든 자료형은 객체
# - c,java언어 문자형: 'A','E'
# 1) 문자열: "hello","hi"
# 2) 정수형: 3,0,-1
# 3) 실수형: 3.14,0.0,-2.2
# 4) 논리형: true,False

# 예) 다양한 종류의 자료형을 사용하는 이유
# JAVA 정수형: byte,short,int,long
#   python 정수형: int
# 이유는: 자원(메모리)를 효율적으로 사용하기 위해서!
#   예: 자료형은 담을 수 있는 크기의 범위가 지정되어 있음
#   예를 들어서 int는(-10000~10000)까지 담을 수 있다고 가정
#   그런데 우리 회사에서 특정 값이 0~9만 사용!
#   int를 사용하게 되면 메모리 낭비, 이런 경우 크기의 범위가 더
#   작은 자료형을 사용하면 좋음(short)

# python 동적 타이핑 언어 -> python 실행 될 떄 type을 지정!
# type() 함수: ()안의 값의 type을 확인할때 사용
print(type("ABC"))
print(type(123))

# 형 변환(Type Casting)
# - Type Casting을 사용하면 값을 원하는 자료형으로 변환 가능
# 1) int(): 자료형으로 변환
# 2) float(): 실수형으로 변환
# 3) str(): 문자열형으로 변환