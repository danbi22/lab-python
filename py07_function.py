import logging

from pip._internal.cli.cmdoptions import retries

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

def make_lotto_list(tickets):
    lottos = []
    for _ in range(tickets):
        lotto = set() #set
        while True:
            lotto.add(random.randrange(1, 46))
            if len(lotto) == 7:
                lottos.append(lotto)
                break

    return lottos

print('lotto', make_lotto_list(5))

def plus_and_minus(x, y):
    return x + y, x - y

print(plus_and_minus(2, 3))

def find_max_and_min(num_list):
    max = num_list[0]
    min = num_list[0]
    for x in num_list:
        if x > max:
            max = x
        if x < min:
            min = x
    return max, min

print(find_max_and_min(list))

def find_max_and_index(num_list):
    max = num_list[0]
    max_index = 0
    for i, v in enumerate(num_list):
        if v > max:
            max = v
            max_index = i

    return max, max_index

print(find_max_and_index(list))

'''
Default argument(기본 인수)
    함수를 정의할 때 파라미터에 설정된 기본값.
        함수를 호출할 때 파라미터에 값을 전달하지 않으면, 기본값이 사용됨.
        함수를 호출할 때 파라미터에 값을 전달하면, 기본값은 무시되고 전달한 아규먼트가 사용됨.
    (주의) 함수를 정의할 때, default argument를 갖는 파라미터들은 반드시 default argument를 갖지 않는 파라미터들 위에 선언해야함
        기본값을 갖지 않는 파라미터들을 먼저 선언하고, 기본값을 갖는 파라미터들을 뒤에 선언해야함. 
'''

def repeat_message2(msg, n=1):
    for _ in range(n):
        print(msg)

print(repeat_message2('안녕하세요'))
print(repeat_message2('안녕하세요', 3))

# def test(n=1, msg):
#     pass

'''
argument 전달 방법:
    positional argument: 함수 정의에서 선언된 파라미터 순서대로 아규먼트들을 전달하는 방법
    keyword argument: param=value 형식으로 아규먼트들을 전달하는 방법.
        keyword argument 방식에서는 파라미터의 순서를 지키지 않아도 됨.
    (주의) 함수 호출할 때 position 방식과 keyword 방식을 함께 사용하는 경우에는, 
    반드시 positional argument를 먼저 사용하고, keyword argument는 나중에 사용해야함
'''

'''
가변길이 인수(variable-length argument)
    함수를 호출할 때, 전달하는 argument의 개수가 임의로 변할 수 있는 것.
        :argument를 전달하지 않아도 됨.
    함수를 정의할 때 파라미터 이름 앞에 *를 사용하면 가변길이 인수를 전달받을 수 있음.
    함수 내부에서 가변길이 인수는 튜플로 취급
        for-in 반복문 사용가능
        인덱스 사용가능
    (주의) 
        가변길이 인수는 keyword방식으로는 전달할 수 없음.
        함수를 정의할 때, 가변길이 인수를 갖는 파라미터는 오직 1개만 선언 가능
'''
def add_all(*values):
    total = 0
    for x in values:
        total += x
    return total

print(add_all())
print(add_all(1))
print(add_all(1, 2, 3, 4, 5))

# 가변길이 인수 뒤에 파라미터가 잇는 경우, 그 파라미터는 keyword 방식으로 아규먼트를 전달 할 수 있음
def test(*x, y):
    print(x)
    print(y)

print(test(1, 2, 3, y = 5))

print(1,2,3,4)

def keyword_only(*, x, y, z):
    print(f'x={x}, y={y}, z={z}')

print(keyword_only(x=1, y=2, z=3))

print(1, 2, 3, sep='-')
print('hello', end=' ')
print('python')

'''
가변길이 키워드 인수(variable-length keyword argument)
    함수를 정의할 때 파라미터 이름 앞에 **를 붙임
    가변길이 인수: 함수를 호출할 때 전달하는 아규먼트의 개수 제한이 없음
    keyword argument: 함수를 호출할 때 반드시 param=value 형식으로 전달해야 함.
    함수 내부에서 가변길이 키워드 인수는 dict로 취급함
    함수 호출할 때 파라미터 이름은 아무렇게나 전달해도 됨.
    가변길이 키워드 인수는 함수에서 1개만 사용가능
'''

def test2(**kwargs):
    print(kwargs)

test2()

test2(x=1, msg='hello')

def make_emp_info(emp_no, emp_name, **kwargs):
    emp = {'emp_no':emp_no, 'emp_name':emp_name}
    for k, v in kwargs.items():
        emp[k] = v

    return emp

print(make_emp_info(1, 'king'))

print(make_emp_info(2, '홍길동', email='gildong@test.com', dept='HR'))