"""
파이썬 자료 타입(data type)

    숫자 타입:
        int: 정수
        float: 실수
    문자열 타입
        str
    논리 타입
        bool:True/False
    객체 타입

    파이썬에서는 변수를 선언할 때 자료 타입을 명시하지 않음.
    변수의 자료 타입은 코드가 실행 때 결정됨(인터프리터가 해석할 때 자료타입이 결정)
"""
pi = 3.14
print(pi)
print(type(pi))

'''
명시적 타입 변환(캐스팅)
    int(arg): arg를 정수 타입으로 변환해서 리턴.
    float(arg): arg를 실수 타입으로 변환해서 리턴.
    str(arg): arg를 문자열로 변환해서 리턴
'''
n = input('정수 입력>>> ') # input('콘솔에 띄워줄 문구'): 콘솔에서 입력을 받는 함수
print(n)

print(type(n)) # input 받은 값은 문자열로 변환됨

print(int(n) + 1)

print(n + str(1))

print(type(n + str(1)))

'''
산술 연산자 ( +, -, *, /, //, %, ** )
    /: 소수점까지 계산하는 나눗셈.
    //: 나눈 몫
    %: 나눈 나머지.
    **: 거듭제곱
'''

print(10/3)

print(10//3)

print(10%3)

print(10**3)

'''
비교 연산자, 논리 연산자
    비교연산자: ==, !=, >, <, >=, <=
    논리연산자: and, or, not
'''

x = 100
print((x > 50) and (x < 150))

print(50 < x < 150)
