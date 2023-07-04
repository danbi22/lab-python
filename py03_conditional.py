'''
else가 없는 조건문
    if 조건식:
        조건식이 참일 때 실행할 코드 (블록)

    if 조건식 뒤에는 반드시 콜론(:)을 사용해야 함.
    코드 블록을 작성할 때 {}를 사용하지 않음.
    if 블록 안의 문장들은 반드시 같은 크기로 들여쓰기(indentation)을 해야 함.
'''

n = 100
if n > 0:
    print('양수')
    print('if 블록 끝')
print('if 블록 바깥') # if 블록과 상관없이 무조건 실행하는 문장

'''
else가 있는 조건문
    if 조건식:
        참일 때 실행할 코드 블록
    else:
        거짓일 때 실행할 코드 블록
'''

n = 124
if n % 2:
    print('홀수')
else:
    print('짝수')

'''
파이썬에서 참(True)로 취급하는 값:
    0이 아닌 숫자들.
    1개 이상의 문자를 가지고 있는 문자열.
    1개 이상의 원소를 가지고 있는 리스트(와 비슷한 객체)
'''

'''
chained conditional
    if 조건식1:
        조건식1이 참일 때 실행할 코드 블록
    elif 조건식2:
        조건식2가 참일 때 실행할 코드 블록
    else:
        위의 모든 조건이 거짓일 때 실행할 코드 블록
'''

# Ex1. 정수 3개를 입력받고 변수에 저장. 평균이 90이상이면 'A', 80이상이면 'B', 70이상이면 'C', 70미만이면 'F'를 출력

java = int(input('자바점수>>>'))
sql = int(input('sql점수>>>'))
python = int(input('python점수>>>'))
sum = sum((java, python, sql))
avg = sum/3
if avg >= 90:
    print('A')
elif avg >= 80:
    print('B')
elif avg >= 70:
    print('c')
else:
    print('F')