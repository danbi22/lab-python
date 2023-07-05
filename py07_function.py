import logging

logging.basicConfig(level=logging.DEBUG)
'''
function(함수): 기능을 수행하는 코드 블록.
argument: 함수를 호출하는 곳에서 함수에게 전달하는 값(들)
parameter: argument를 저장하기 위해서 함수 선언부에서 선언하는 지역 변수.
return value: 함수가 기능의 수행 결과로 리턴하는 값.
    return value가 있는 함수
    return value가 없는 함수
파이썬 함수 정의 방법:
    def function_name([param, ...]):
        ["""문서화 주석 - 함수 기능 설명, 파라미터 설멍, 리턴 값 설명"""]
        함수 기능 구현
        [return 값]

    return value가 없는 경우에
        return 문장을 생략
        return None 명시할 수도 있음
'''
def subtract(x, y):
    """2개의 숫자 x, y를 전달받아서 x-y결과를 리턴하는 함수"""
    return x-y

result = subtract(2, 1)

def repeat_message(message, n):
    """문자열(massage)과 양의 정수(n)을 전달받아서, message를 n번 출력하는 함수"""
    print(message * n)
    for _ in range(n):
        print(message)

result = repeat_message('하이', 4)
print(result)

import random
'''
Ex 1.
    함수 이름: make_list
    기능: start 이상 end 미만의 정수 난수 n개를 갖는 리스트를 반환하는 함수.
'''
def make_list(start, end, n):
    return [random.randrange(start, end) for _ in range(n)]

print(make_list(2,6,6))

'''
Ex 2.
    함수 이름: calc_sum
    기능: 숫자들의 리스트를 전달받아서, 리스트의 모든 원소들의 합을 리턴하는 함수.
'''
def calc_sum(list):
    n = 0
    for x in list:
        n += x
    return n

list = [1, 2, 3, 4, 5]
print(calc_sum(list))

'''
Ex 3.
    함수 이름: calc_mean
    기능: 숫자들의 리스트를 전달받아서, 리스트의 원소들의 평균을 리턴하는 함수.
'''

def calc_mean(list):
    n = 0
    for x in list:
        n += x
    n = n / len(list)
    return n

print(calc_mean(list))

'''
Ex 4.
    함수 이름: calc_var
    기능: 숫자들의 리스트를 전달받아서, 리스트의 원소들의 분산(variance)을 리턴하는 함수.
    분산 = (값 - 평균)**2 들의 평균
'''
def calc_var(list):
     avg = sum(list) / len(list)
     vlist = [(k-avg)**2 for k in list]
     variance = sum(vlist) / len(vlist)
     return variance

print(calc_var(list))
