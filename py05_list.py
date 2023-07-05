'''
list
    여러 개의 값들을 하나의 변수에 저장하기 위한 테이터 타입
    element(원소, 요소): 리스트에 저장되는 각각의 값.
    index(인덱스): 리스트에서 원소가 저장된 위치
        리스트의 인덱스는 0부터 시작
        리스트의 마지막 인덱스는 (원소 개수 -1)
    리스트는 원소들을 추가, 삭제, 변경할 수 있음.
        tuple과 다른 점!
'''

# 숫자들을 저장하는 리스트
numbers = [1, 2, 3, 10, 20, 30]
print(numbers) # 리스트를 출력하면 [값1, 값2] 형식으로 출력된다

'''
인덱싱(indexing)
인덱스를 사용해서 리스트의 원소를 참조하는 방법
'''

print(numbers[0])

print(numbers[5])

print(numbers[-1])

print(numbers[-6])

print(numbers[-0])

'''
slicing
    인덱스를 사용해서 리스트의 부분집합(리스트)를 잘라내는 방법
    list[start:end]
    
    start <= index < end 범위의 인덱스 위치의 원소들을 잘라냄.
    start를 생략한 경우에는 첫번째 원소부터 잘라냄
        list[0:5]과 list[:5]는 같은 결과
    end를 생략한 경우에는 마지막 원소까지 잘라냄
    리스트를 slicing한 결과는 또다른 새로운 리스트
'''

print(numbers[1:4])

print(numbers[3:6])

print(numbers[3:])

print(numbers[:3])

print(numbers[-3:])

'''
문자열(str)
    문자들의 리스트
    문자열은 인덱스를 사용할 수 있음.
        indexing, slicing가능
'''

message = '안녕하세요, 여러분!' # 11개의 문자들로 이루어진 리스트

print(message[0])

print(message[:5])

print(message[7:12])

print(message[-4:])

# 문자열 산술 연산: +, *
print('hello' + 'python')
print('hello' * 3)

'''
리스트의 산술 연산
    list + list
    list * int 또는 int * list
'''

print([1, 2, 3] + [4, 5, 6]) # concatenate

print(numbers * 2) # replicate

print(numbers)

# list와 for 반복문
for x in 'hello':
    print(x)

numbers = [1, 10, 5, 100]
for x in numbers:
    print(x)

for i in range(len(numbers)): # 0 <= x < len
    print(i, ':', numbers[i])

for i, v in enumerate(numbers):
    print(i, ':', v)

indexed_numbers = [(index, number) for index, number in enumerate(numbers)]
print(indexed_numbers)

numbers1 = [1, 3, 5]
numbers2 = [10, 11, 12]

print('-' * 50)

result = [] # 빈(empty) 리스트
for i in range(len(numbers1)):
    result.append(numbers1[i] + numbers2[i])
print(result)

# 파이썬에서 난수를 만드는 방법:

import random # random 모듈을 임포트

# random 모듈의 random() 함수를 호출
print(random.random()) # 0 <= < 1의 실수 난수를 리턴.

#random 모듈의 randrange() 함수를 호출
print(random.randrange(3)) # 0~2의 난수를 리턴

print(random.randrange(1, 4)) # 1 ~ 3 사이의 난수를 리턴

'''
Exercises
    Ex 1.
        1. 빈 리스트를 생성.
        2. 1 이상 10 이하의 정수 난수 5개를 저장.
        3. 리스트의 모든 정수들의 합을 출력.
        4. 리스트의 모든 정수들의 평균을 출력.
'''
empty = []
for _ in range(5):
    empty.append(random.randrange(1, 11))

print(sum(empty))
print(sum(empty)/5)

'''
    Ex 2.
        1. 빈 리스트(numbers)를 생성.
        2. 10 이상, 100 미만의 정수 난수 10개를 numbers에 저장.
        3. numbers에서 짝수들만 선택해서 evens 리스트를 만들고 출력.
        4. numbers에서 홀수들만 선택해서 odds 리스트를 만들고 출력.
'''
numbers = []
for _ in range(10):
    numbers.append(random.randrange(10, 100))

evens = []
odds = []
for x in numbers:
    if x % 2 == 0:
        evens.append(x)
    else:
        odds.append(x)

print(evens)
print(odds)

'''
    Ex 3.
        1. 빈 리스트 numbers를 만듦.
        2. -10 이상 10 이하인 범위의 정수 난수 10개를 numbers에 저장.
        3. numbers의 원소가 양수이면 True, 그렇지 않으면 False를 저장하는 is_positive 리스트를 만들고 출력.
'''

numbers = []

for _ in range(10):
    numbers.append(random.randrange(-10, 11))

is_positive = []
for x in numbers:
    if x >= 0:
        is_positive.append(True)
    else:
        is_positive.append(False)
print(f'is_positive: {is_positive}')

'''
    Ex 4.
        1. gender_codes 리스트에 0 또는 1을 랜덤하게 10개를 저장.
        2. gender_codes의 값이 0이면 'Male', 그렇지 않으며 'Female'을 저장하는 genders 리스트를 만들고 출력.
'''

gender_codes = [random.randrange(0, 1) for _ in range(10)]

genders = ['Male' if code == 0 else 'Female' for code in gender_codes]

print(genders)

'''
    Ex 5.
        1. numbers1: 100 미만의 정수 난수 10개를 저장하는 리스트.
        2. numbers2: 100 미만의 정수 난수 10개를 저장하는 리스트.
        3. multiplication: numbers1과 numbers2의 같은 인덱스에 있는 원소들끼리의 곱셈 결과를 저장하는 리스트.
        4. subtraction: numbers1의 원소에서 같은 인덱스에 있는 numbers2의 원소를 뺀 값을 저장하는 리스트.
        5. numbers1, numbers2, multiplication, subtraction를 출력.
'''

numbers1 = [random.randrange(100) for _ in range(10)]
numbers2 = [random.randrange(100) for _ in range(10)]
multiplication = [numbers1[i] * numbers2[i] for i in range(len(numbers1))]
subtraction = [numbers1[i] - numbers2[i] for i in range(len(numbers1))]
print(f'numbers1: {numbers1}')
print(f'numbers2: {numbers2}')
print(f'multiplication: {multiplication}')
print(f'subtraction: {subtraction}')



# 1 ~ 10 정수들을 순서대로 리스트에 저장: [1, 2, 3, ..., 9, 10]
list = [x for x in range(1, 11)]
print(list)


# [1, 4, 9, 18, ..., 81, 100]
list = [x ** 2 for x in range(1,11)]
print(list)

# [0, 10) 범위의 난수 10개를 저장하는 리스트
list = [random.randrange(0, 10) for _ in range(10)]
print(list)




'''
List comprehension(리스트 내포)

    filtering:
        [value for x in iterable if condition]
        필요한 것만 리스트에 넣겠다
    
    mapping:
        [value1 if condition else value2 for x in iterable]
        바꾸어서 리스트에 넣겠다
'''