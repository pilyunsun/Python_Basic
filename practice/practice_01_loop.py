#
# # 입력 된 단수를 출력하는 코드
# # dan = int(input("단수: "))
# # for i in range(1,10):
# #     print(f"{dan}x{i} = {dan*i}")
#
# # 문제2) 2단부터 9단까지 출력하는 코드
# # 2단 9단까지 출력 => 중첩for
# # for i in range(2,10):
# #     for j in range(1,10):
# #         print(f"{i}x{j} = {i*j}")
# #
# # print("="*100)
# # 문제 3) list a의 평균값을 계산하세요.
# a = [1,2,3,4,5,99,87,54,2,5,4]
# # total => 총합
# total = 0
# for num in a:
#     total +=num
# length = len(a)
# result = total/ length
# # round(값, 소수점숫자) : 반올림
# print(round(result,2))
#
# # 문제4) list b에서 최소값 찾기!
# b = [22, 1, 4, 7, 98]
#
# num_min = b[0] # 최소값 담을 공간
# for x in b:
#     if x <num_min:
#         num_min = x
#
#
# print(num_min) # 1 출력
#
# # 문제5) list c의 최소값,최대값 찾기
# c = [2,5,7,1,8]
#
# num_max = c[0] # 최소값 담을 공간
# for x in c:
#     if x >num_max:
#         num_max = x
#
# print(num_min) # 1 출력
# print(num_max) # 8 출력
#
# print("="*100)
# #사용자가 입력한 값 1,2,3 통과
# # 아닌 경우 다시 입력하도록
#
# count = 0
# while True:
#     if count >=4:
#         print("프로그램을 사용할 수 없습니다.")
#         break
#     num = int(input("값: "))
#     # if 4>num>0: # num = 1,2,3
#     if num in [1,2,3]:
#         print(f"{num}을 입력하셨습니다.")
#         break
#     else:
#         print("1,2,3,의 값만 입력해주세요.")
#         count+=1

# 문제7) 1부터 100 까지 총합을 출력하는 코드
# - for문으로 작성
# - while문으로 작성
# sum = 0
# result = 0
# for i in range(1,101):
#     sum += 1
#     result += sum
# print(sum)

# count = 0
# result = 0
# while count < 100:
#     count += 1
#     result += count
#     if count == 100:
#         break
# print(result)











