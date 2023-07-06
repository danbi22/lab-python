'''
1급 객체(first-class object)로서의 함수
    함수는 변수에 할당할 수 있음
    함수의 파라미터에 아규먼트로 다른 함수를 전달할 수 있음.
        함수는 아규먼트가 될 수 있다.
    함수는 다른 함수의 리턴 값이 될 수 있음
    함수 내부에서 다른 함수를 정의할 수 있음
'''
# 함수를 변수에 할당
def twice(x):
    return 2 * x

result = twice(100) # 함수 호출 결과(리턴 값)을 변수에 저장

double = twice # 함수 (객체)를 변수에 저장
print(double)

print(double(12))

# 함수를 아규먼트로 사용
def calculate(x, y, fn):
    result = fn(x, y)
    return result

def plus(x, y):
    return x + y

print(calculate(1, 2, plus))

def minus(x, y):
    return x - y

print(calculate(1, 2, minus))

'''
내부 함수, 함수 리턴
'''

def make_increment(n): # 외부 함수
    def add_n(x): # 내부함수, 지역함수
        return x + n # 내부함수는 외부 함수의 지역 변수(파라미터 포함)들을 사용할 수 있음.
    return add_n

increse_by_2 = make_increment(2)
print(increse_by_2)

print(increse_by_2(100))

increse_by_10 = make_increment(10)

print(increse_by_10(100))

make_increment(5)(100)

'''
Lambda expression(람다 표현식)

    lambda param1, param2, ...: expression
    
    이름이 없는 함수 표기법
    함수 이름 없이 함수의 파라미터 선언과 반환 값 또는 반환 식으로 만 함수를 정의하는 방법.
    파이썬은 2줄 이상의 문장이 포함된 람다 표현식 문법을 제공하지 않음.
'''
minus = lambda x, y: x - y
print(minus)
print(minus(1, 2))

print(calculate(2, 3, lambda x, y: x * y))
print(calculate(2, 3, lambda x, y: x / y))

'''
Ex 1. calculate 함수에 2개의 숫자 중에서 더 큰 수를 리턴하는 람다 표현식을 전달
'''

print(calculate(2, 3, lambda x, y: x if x > y else y ))

'''
Ex 2. calculate 함수에, 첫번째 아규먼트가 크면 True, 그렇지 않으면 False를 리턴하는 람다 표현식 전달
'''

print(calculate(5, 3, lambda x, y: True if x > y else False))

'''
filter 함수 
    조건에 맞는 원소들만 선택
'''

def my_filter(iterable, fn):
    """
    리스트 iterable의 원소들 중에서 함수 fn의 호출 결과 값이 True인 원소들로만 이루어진 리스트를 리턴

    :param iterable: 리스트
    :param fn: 아규먼트가 1개이고, True/False를 리턴하는 함수.
    :return: 리스트
    """
    list = []
    for x in iterable:
        if fn(x) == True:
            list.append(x)

    return list

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_filter(list, lambda x: True if x % 2 == 0 else False))

'''
map 함수 
    원소들을 규칙에 따라서 다른 값으로 변환.
'''

def my_mapper(iterable, fn):
    """
    리스트 iterable의 원소들을 함수 fn의 리턴 값으로 변환한 리스트를 리턴
    :param iterable: 리스트
    :param fn: 아규먼트가 1개이고 리턴값이 있는 함수.
    :return:
    """
    list = [fn(x) for x in iterable]

    return list

print(list)
print(my_mapper(list, lambda x: x + 1))

'''
리스트 numbers의 원소들의 제곱으로 이루어진 리스트
'''
print(my_mapper(list, lambda x: x**2))


# 리스트 numbers의 원소가 짝수이면 'even', 홀수이면 'odd'를 저장하는 리스트
print(my_mapper(list, lambda x: 'even' if x % 2 != 0 else 'odd'))

strings = ['python', 'java', 'javascript', 'sql']

# strings가 가지고 있는 문자열의 길이들로 이루어진 리스트
print(my_mapper(strings, lambda x: len(x)))

# strings의 문자열들을 모두 대문자로 변환한 리스트
print(my_mapper(strings, lambda x: x.upper()))