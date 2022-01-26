# title: Python 기초 프로그래밍(정준수) 
# purpose: 파이썬 프로그래밍 개념 정리
# sign means: 
#1. 여러줄에 걸친 문장은 #제목: 으로 해당 내용의 시작을 알리고, '''(시작) '''(종료) 혹은 #n로서 작성했습니다.
#2. 대단원은 ###으로 시작을 알리고, <> 괄호(화살괄호)안에 대단원 제목을 작성했습니다.
#3. 소단원은 '## 소단원의 제목'으로 시작을 알리고, 이윽고 '-' 11개 사용이후 소단원 시작은 '@', 소단원 종료는 '/'로서 표기 했습니다. 
#4. 단순하게 내용의 구분감을 주기 위해선 '#' 이후에 여러 '$' 표시를 주었습니다.
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ 
 
#파이썬 이용/특징:
'''
- 장점
1. 데이터 취급할때 사용한다.
2. 인공지능 학습에 사용한다.
3. 데이터 베이스 연동에 사용한다.

- 단점
시스템 밀접한 프로그래밍이나, 모바일 프로그래밍엔 부적합하다.

- 특징
파이썬의 특정 부분의 구별 = 들여쓰기 (C언어에선 세미콜론';')
'''
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

### <파이썬 자료형>


## 파이썬 숫자형 ----------@
#파이썬 숫자형 e,o,x의 대소문자 구분이 없습니다.(e = exponent(e표기법), o = octal, x = hexadecimal)
'''
a1 = 1234
print(a1)
a2 = 123.4
print(a2)
a3 = 12e10
print(a3)
a4 = 12E-10
print(a4)
a5 = 0o17
print(a5)
a6=0xA
print(a6)
a7 =1+2j
print(a7)
a8 = 0b110
print(a8)

#파이썬 제공 내장함수: bin(), oct(), hex() 리턴타입은 문자열 입니다.
value = 60
b = bin(value)
o = oct(value)
h = hex(value)
print(b)
print(o)
print(h)

#파이썬 제공 내장함수: format() 리턴타입은 문자열, 파라미터는 정수와 반환되는 대상의 진수형태 문자열 입니다.
value = 60
b = format(value, '#b')
o = format(value, '#o')
h = format(value,'#x')
print(b)
print(o)
print(h)

b = format(value, 'b')
o = format(value, 'o')
h = format(value, 'x')
print(b)
print(o)
print(h)

#다른 진수형태에서 10진수로 반환 리턴타입은 숫자, 파라미터는 문자열과 변환되는 대상의 진수형태 정수 입니다.
b = int(b, 2)
o = int(o, 8)
h = int(h, 16)
print(b)
print(o)
print(h)


#어떤 진수형태에서 다른 진수형태로 바꾸기. 리턴타입은 문자열, 파라미터는 정수입니다.
o = oct(0b1000)
h = hex(0b1111)
s = str(0b1111)
print(o)
print(h)
print(s)

#문자열 .format() 이용
s = "2진수: {0:#b}, 8진수: {0:#o}, 10진수: {0:#d}, 16진수: {0:#x}".format(60)
print(s)
s = "2진수: {0:b}, 8진수: {0:o}, 10진수: {0:d}, 16진수: {0:x}".format(60)
print(s)

#사칙연산, 거듭제곱, 몫, 나머지 연산자 (+, -, *, /, **, //, %)
print(3+4.1)
print(3-4)
print(3*4)
print(2/3)
print(3**3)
print(3.2//3)
print(3.2%3)
'''
## 파이썬 숫자형 ----------/


## 파이썬 문자형 ----------@
'''
#문자열(string) 의 예시 "string",'string'
s1 = "Hello Python"
s2 = 'Hello Python'
print(s1)
print(s2)

#escape \ 사용: 줄바꿈 \n, 탭\t, 따옴표 혹은 escape 문자출력 \' or \\
s1 = "Hell\to\n\'Python\'\\"
print(s1)

#여러줄에 걸쳐진 문자열 저장 """ or \''' (\사용은 '특수문자가 본래 기능을 하지 않게 하려함)
s1 = """Hello
World"""
print(s1)
s2 = """Hello
World"""
print(s2)

#문자열의 연산 *: 여러줄반복, +: 문자열 합치기
A = "Life is short" + ',' + "you need Python"
print(A)
print(A*3)

#문자열 인덱싱과 슬라이싱(문자열은 immutable불변 자료형)
A = 'Life is short, you need python'
print(A[0])
print(A[-1])

print(A[0:])    #문자열의 0번 인덱스 부터 문자열의 끝까지 0:
print(A[0:3])   #문자열의 0번 인덱스 부터 3번 인덱스의 앞 까지 0:3
print(A[:3])    #문자열의 시작(0번 인덱스) 부터 3번 인덱스의 앞 까지 :3 
print(A[:-1])   #문자열의 시작(0번 인덱스) 부터 끝의 앞까지 :-1
print(A[0:-1])  #문자열의 0번 인덱스 부터 끝의 앞까지 0:-1  

#주요 문자열 함수 starswith(), endswith(), find(), count(), strip()
A = '   Hello Python World '
print(A)
print(len(A))
print(A.startswith('Li')) #참이면 True 반환 거짓이면 False 반환
print(A.startswith(" "))
print(A.endswith('thon'))
print(A.endswith("d "))
print(A.find('py')) #참이면 시작 인덱스, 거짓이면 -1 반환
print(A.find("Py")) 
print(A.count('He')) #등장 횟수(대소분자 구별)
print(A.count("h")) 
print(A.strip()) #양 옆 공백 제거
print(A)

#문자열의 포메팅(formating)
#formating method 1: format() 사용
print("지금은 {}시 {}분 입니다.".format(3, 29))
#formating method 2: %자료형 %값 사용
# %d:정수, %s:문자열, %f:실수, %o:8진수, %x:16진수
print("지금은 %d시 입니다." %3)

#형변환
n1 = 1239.7
n2 = 131
s = 'Python'
print(int(n1)) #정수형으로 형변환
print(float(n2)) #실수형으로 형변환
print(str(n1)) #문자열으로 형변환
'''
##파이썬 문자열 ----------/


##파이썬 순서형 ----------@
'''
# list와 tuple (문자열도 순서형 sequential type(문자열 요소는 immutable))
# 순서형에서 사용하는 연산으로 인덱스(L[0]), 슬라이싱(L[0:]), 길이반환(len()), 연결(+), 반복(*), 멤버검사 (in 순서형)이 있다.

#list (리스트 요소 가변:mutable)
L1 = [1,2,3, 4]
L2 = [1, 2, 3, '4']
L3 = ["one", "two", 'three']
L4 = list()
L5 = []
print(L1)
print(L2[3])
print(L3[0])
print(L4)
print(L5)  

#다중리스트
L = [1, 2, 3, [4, 5, 6]]
L[3][0] = 6
print(L[3][0])
print(L)

#리스트 관련 함수들: 정렬(리스트.sort()), 뒤집기(리스트.reverse()), 위치(리스트.index(값), 요소추가(리스트.append(값),
#삭제(del 리스트[인덱스] etc(insert, remove, pop, extend, sorted)
L = [6, 1, 3, 2, 4, 5]
L2 = sorted(L)
print("L2: ", L2)
print("L: ", L)
L2 = L.sort()
print("L: ", L)

#tuple (리스트 요소 불변:immutable)
T = (1, 2, 3, 4, 5, 6)
print(T)
T = (1,)
print(T)
T = (1, 2,)
print(T)
T = 1, 2, 3,4,5,6
print(T)
T = tuple()
print(T)
T = ()
print(T)
T = (1, 2, '3')
print(T[2])
T = ('one', "two", 'three')
print(T[0])
'''
##파이썬 순서형 ---------/


##파이썬 set자료형 ----------@
'''
#set (순서형x: 순서가 없습니다. 중복허용x)
S = {1,2,3,3 }
print(S)
S = set()
print(S)
S = set("Hello, WorldWWWWWWWWWw")
print(S)
S = set(['one', 'two', 'three'])
print(S)

#set의 주요 연산자
#값 추가(set.add(값), 합집합(set.union(set2)), 교집합(set.intersection(set2)),
#차집합(set.difference(set2), 전체제거(set.clear())
#etc(copy, discard, remove, pop, update, intersection_update, difference_update)
S1 = {1,2,3,4,5}
S2= {3,4,5,6,7}
print(S1.union(S2))
print(S1.intersection(S2))
print(S1.difference(S2))
S1.clear()
print("set(S1): ", S1)
S1.add(1)
print("set(S1): ",S1)

#형변환 (list(), tuple(), set())
A = [1,2,3,'4',5,5]
print("list A: ", A, "\ntuple A: ", tuple(A), "\nset A: ", set(A), "\nlist A: ", A)
'''
##파이썬 set자료형 ----------/

##파이썬의 매핑(dictionary) ---------@
'''
#key:value 형태의 자료형 (key에는 immutable 값만 사용가능 합니다. -> list사용불가)
d = {}
print(d)
d = dict()
print(d)
d[5] = 3 #d[key] = key 대응 value
d[3] = 2
print(d)
print(d[5])

#dictionary 주요 함수들: 길이반환(len(dict)), 데이터 삭제(del dict[key]), 전체키반환(dict.keys())
#전체벨류반환(dict.values()), etc(clear, create, get(key), update, pop,item)
d = {1:2, 'sun':'shinny', '3':'look', '4':7}
print(d.values())
print(d.keys())
del d['4']
d.clear()
print(d)
'''
##파이썬의 매핑(dictionary) ---------/
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
