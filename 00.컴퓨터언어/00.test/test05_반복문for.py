
#0~10 사이의 짝수 합 출력하기
'''for x in range(0,11,2):
    print(x)'''

tmp = 0
total = 0
for x in range(0,11,2):
    print(tmp + x)
    tmp += x
    total = total + x
    

print(tmp)
print(total)

print()

#0~10 사이 홀수의 곱 출력하기
mul = 1
for x in range(1,11,2):
    mul = mul*x
print(mul)

print()

#나만의 프로젝트_ 위에 반복문 단계 하나하나 다 보이게 만들어보기

mul_2 = 1
for x in range(1,11,2):
    print('x = ',x)
    print('mul_2 = ', mul_2)
    print('x*mul_2=',x*mul_2)
    mul_2 = mul_2*x
    print('new mul_2=',mul_2)
    print()

print(mul_2)


#변수 aa로 0부터 10 사이 3씩 띄우기
for aa in range(0,10,3):
    print(aa)





#반복문 이용해서 삼각형 그리기
import turtle as t

for i in range(3):
    t.forward(100)
    t.left(120)
    










    
