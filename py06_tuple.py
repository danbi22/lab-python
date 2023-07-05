'''
tuple(튜플)
    하나의 변수에 여러 개의 값들을 저장하기 위한 자료 타입.
    저장된 원소(아이템)등을 변경할 수 없는 리스트
        append(), remove()와 같은 원소를 변경하는 메서드(기능)은 제공하지 않음.
    인덱스 기반 자료 타입
        indexing, slicing
        음수 인덱스도 사용 가능
'''

# 숫자들을 저장하는 튜플
numbers = (1, 2, 12, 123,123,123,41,24)
print(numbers) # 출력 형식은  형태로 나옴
# list와 tuple 형식 차이 [값1, 값2] / (값1, 값2)

print(type(numbers))

# indexing: 인덱스를 사용해서 원소 1개를 참조하는 방법
print(numbers[0])

# slicing: 자르기, 부분집합
print(numbers[:3])
print(numbers[-3:])

# decomposition(분해)
odds = (1, 3, 5)
a = odds[0]
b = odds[1]
c = odds[2]
print(a, b, c)

x, y, z = (1, 3, 5)
print(x, y, z)

# tuple & for
for x in odds:
    print(x)

# 2차원 리스트/튜플
numbers = [
    [1, 2, 3],
    (1, 2, 3)
]

print(len(numbers)) # 2차원 리스트 numbers의 원소 개수

print(numbers[0])
print(numbers[1])

print(numbers[0][0])
print(numbers[1][0])

import random
# Ex1. 2x2 모양의 [0, 10) 범위의 정수 난수들을 저장하는 2차원 리스트 array1을 만드고 출력하세요.
array1 = [[random.randrange(0,10) for _ in range(2)], [random.randrange(0,10) for _ in range(2)]]
print(array1)

# Ex2. 2x2 모양의 [0, 10) 범위의 정수 난수들을 저장하는 2차원 리스트 array2을 만드고 출력하세요.
array2 = [[random.randrange(0,10) for _ in range(2)] for _ in range(2)]
print(array2)

# Ex3. array1과 array2의 같은 인덱스의 원소들끼리의 덧셈 결과를 저장하는 2차원 리스트 add를 만들고 출력하세요.
add = [ [ array1[0][i] + array2[0][i] for i in range(2)], [array1[1][i] + array2[1][i] for i in range(2)]]
print(add)

add = [] # 1차원 배열등을 저장할 빈 배열
for row1, row2 in zip(array1, array2):
    temp = [] # 덧셈 결과를 저장할 빈 배열
    for x, y in zip(row1, row2):
        temp.append(x + y)
    add.append(temp)

print(add)

add = [[x + y for x, y in zip(row1, row2)] for row1, row2 in zip(array1, array2)]

print(add)

'''
Set(집합)
    중복된 데이터를 허용하지 않음: {1, 2, 2, 3, 3} = {1, 2, 3}
    인덱스 기반의 자료구조가 아님. 인덱스가 없음
        데이터의 저장 순서가 중요하지 않음: {1, 2, 3} = {3, 1, 2}
        indexing, slicing 기능을 제공하지 않음.
        for-in 구문에서 사용할 수 있는 iterable 타입.
'''

s = {1, 2, 2, 3, 3}
print(s)
print(type(s))

# Set의 기능(메서드)
s.add(5)
print(s)

s.add(5) # add(x) 메서드가 n 번 실행 되어도 x는 한번만 들어간다.
print(s)

s.remove(3)
print(s)

s.pop() # 어떤 요소가 지워질지 모르나 지워진 값을 반환을 해줌.
print(s)

s1 = {1, 2, 3, 4}
s2 = {2, 3, 5, 6}

print(s1.union(s2))

print(s1.intersection(s2))

print(s1.difference(s2))

print(s2.difference(s1))

'''
dict
    dictionary(사전) 형식의 데이터 타입
    키(key)를 기반으로 값(value)를 저장하는 데이터 타입
        list, tuple: 인덱스 기반의 데이터 타입
        dict: key-value 기반의 데이터 타입
        dict에서 key의 역할은 1개 아이템의 값(value)를 찾기 위한 용도
'''
students = {1: '홍길동', 2: '허균', 3: '오쌤'}
print(students)
print(type(students))

# dict에서 키를 사용하는 방법은 list 또는 tuple과 만찬가지로 인덱스 연산자( [] )를 사용함.
print(students[1])

students[10] = '홍길동' # dict에 새로운 key-value 아이템을 추가

print(students[2])

students.pop(3) # dict에서 해당하는 key의 아아템(key: value)을 삭제

book = {
    'title': '점프 투 파이썬',
    'authors': ['박응용', '웨스 매키니'],
    'isbn': 123456789
}

print(book)

# dict & for
contact = {
    'no': 1,
    'name': '다한',
    'phone': ['010-0000-0000', '010-1111-1111'],
    'email': {
        'compony': 'ekgks@ajou.ac.kr',
        'persnal': 'dbekgks@gmail.com'
    }
}

print(contact)

for k in contact: # 키들을 출력
    print(k)

for k in contact:
    print(k, ':', contact[k])

print(contact.keys())

print(contact.values())

print(contact.items())

for k, v in contact.items():
    print(k, v)

# dictionary Comprehension

emp_no = [1001, 1002, 2001, 2002] # 직원 번호
emp_name = ['King', 'Scott', 'Allen', 'Tiger'] # 직원 이름

# emp_no를 key로 하고 emp_name을 value로 dict를 만들고 출력
emp = {} # key-value를 저장할 빈 dict
for no, name in zip(emp_no, emp_name):
    emp[no] = name
print(emp)

emp = {k: v for k, v in zip(emp_no, emp_name)}
print(emp)

strings = ['hello', 'java', 'sql', 'python', 'javascript']
string_lengths = dict() # 빈 dict
for k in strings:
    string_lengths[k] = len(k)
print(string_lengths)

string_lengths = {k: len(k) for k in strings}
print(string_lengths)

