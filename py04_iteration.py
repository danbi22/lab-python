'''
for 반복문
    for 변수 in iterable_type:
        반복해서 실행할 코드 블록

    iterable_type: 반복가능한 타입
        range, list, tuple, dict, set, str, ...
    range() 함수:
        range(stop): 0 <= x < stop 범위의 1씩 증가하는 정수들을 차례로 반환.
        range(start, stop): start <= x < stop 범위의 1씩 증가하는 정수들을 차례로 반환.
        range(start, stop, step):
        step > 0: start <= x < stop 범위의 step 만큼씩 증가하는 정수들을 차례로 반환.
        step < 0: start >= x > stop 범위의 step 만큼씩 감소하는 정수들을 차례로 반환.
'''

for x in range(5):
    print(x)

print("=" * 8)

for x in range(1, 6):
    print(x)

print("=" * 8)

for x in range(0, 11, 2):
    print(x)

print("=" * 8)

for x in range(10, 0, -2):
    print(x)

print("=" * 8)

for x in range(10, 0):
    print(x)

'''
중첩 반복문
    for x in iterable1:
        for y in iterable2:
            코드 블록
'''

# 구구단 2단부터 9단까지 출력.

for x in range(2, 10):
    print(x, '단')
    for y in range(1, 10):
        print(f'{x} x {y} = {x*y}')
        if y == 9:
            print()
'''
문자열에서 사용 가능한 산술 연산자:
    문자열 + 문자열: 문자열 이어붙이기(concatenate)
    문자열 * 정수, 정수 * 문자열: 문자열(정수만큼) 반복해서 복사해 붙이기
'''

'''
break와 continue
    break: 반복(iteration)을 종료. break가 포함된 가장 가까운 반복문을 빠져나옴.
    continue: 반복문 내부의 실행을 멈추고, 그 다음 iteration을 계속해서 수행
'''
for x in range(5):
    if x == 2:
        break
    print(x)

for x in range(5):
    if x == 2:
        continue
    print(x)
'''
다음과 같이 출력.

2 x 1 = 2
2 x 2 = 4
----------
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
----------
...
----------
5 x 1 = 5
...
5 x 5 = 25
----------
'''

for x in range(2,10):
    print(x,'단')
    for y in range(1,10):
        print(f'{x} x {y} = {x*y}')
        if y == x:
            break
    print('-' * 10)

'''
while 반복문

    [초기화 문장]
    while 조건식:
        반복할 코드 블록
        [조건(변수)를 변경하는 문장]
'''

'''
다음과 같이 출력하는 코드를 while 문으로 작성.

*
**
***
****
*****
'''

n = 1
while n <= 5:
    print('*' * n)
    n += 1

# 1 이상 10 미만의 홀수들을 출력하는 코드를 while문으로 작성

n = 1
while n <= 10:
    if n % 2 != 0:
        print(n)
    n += 1