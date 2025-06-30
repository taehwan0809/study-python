##자료형
#int=숫자형(정수)
#float = 소수형 숫자
#str = 문자열
#list = 리스트형
#bool = 참거짓
#dict = 키와값
#input = 입력 받는 거

##입력값 받고 출력하기
# a = int(input())
# print(a)

##리스트에 대해
# b라는 리스트에 [1,2,3,True,'c']  b라는 리스트에 12추가 하고 싶어
# b.append()=리스트 마지막에 값을 추가   extend()=인덱스 번호를 추가
#pop remove= 둘 다 삭제

##if문
# if a>10: 
#     print(f"{a}가 10보다 큼")



##코드업 문제 풀기


#1. print("\"Hello World\"")


#2. inhak = int(input())
#   if inhak%7 == 0:
#     print("multiple")
#   else:
#     print("not multiple")

#3. week = int(input())
# if week %2 == 0:
#     print("enjoy")
# else:
#     print("oh my god")


ball = int(input())
if ball >= 30 and  ball <= 40 or ball >= 60 and ball <= 70:
    print("win")
else:
    print("lose")