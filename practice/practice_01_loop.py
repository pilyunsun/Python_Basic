
# 입력 된 단수를 출력하는 코드
# dan = int(input("단수: "))
# for i in range(1,10):
#     print(f"{dan}x{i} = {dan*i}")

# 문제2) 2단부터 9단까지 출력하는 코드
# 2단 9단까지 출력 => 중첩for
# for i in range(2,10):
#     for j in range(1,10):
#         print(f"{i}x{j} = {i*j}")
#
# print("="*100)
# 문제 3) list a의 평균값을 계산하세요.
a = [1,2,3,4,5,99,87,54,2,5,4]
# total => 총합
total = 0
for num in a:
    total +=num
length = len(a)
result = total/ length
# round(값, 소수점숫자) : 반올림
print(round(result,2))

# 문제4) list b에서 최소값 찾기!
b = [22, 1, 4, 7, 98]