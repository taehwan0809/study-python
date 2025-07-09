##자료형
#int=숫자형(정수)
#float = 소수형 숫자
#str = 문자열
#list = 리스트형
#bool = 참거짓
#dict = 키와값
#input = 입력 받는 거


#map() = 문자열을 숫자열로 바꿀 때 사용

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


##출력하기 문제
#1. print("\"Hello World\"")


##입력 받기&&if문
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

#4. ball = int(input())
# if ball >= 30 and  ball <= 40 or ball >= 60 and ball <= 70:
    # print("win")
# else:
    # print("lose")

#5. year, month, day = map(int,input().split()) 
# buzi = year - month + day
# if buzi%10==0:
#     print("대박")
# else:
#     print("그럭저럭")

##버블 정렬
#6. a,b = (input().split())
# c= 0
# c= a
# a= b
# b= c
# print(a,b)

##for문
#7. i = int(input())
# for star in range(i):
#     print("*",end="")

##축구의 신 문제
#now,goal = map(int,input().split())
# for i in range(now,90,5):
#     goal +=1
# print(goal)

