# 자료형


## 문자열의 format() 함수
- format() 함수는 문자열의 기본 함수
- 사용법: 중괄호{} 포함한 문자열 뒤에 마침표(.)를 찍고 format() 함수 사용
          중괄호 개수와 format() 함수의 매개변수 개수가 일치해야 함
## format() 함수의 다양한 기능
- {} 와 format() 함수를 조합해서 다양하게 출력 가능하다.
##### 정수를 특정 칸에 출력하기
``` python
# 5칸을 빈칸으로 잡고 뒤에서부터 format 의 매개변수를 뒤에서부터 채워서 입력. 정수 only (d)
>>> print("{:5d}".format(52))
   52
# 5칸을 0으로 채우고 뒤에서부터 format 의 매개변수를 뒤에서부터 채워서 입력. 정수 only (d)
>>> print("{:05d}".format(52))
00052   
```
- 참고) 실수(부동 소수점) 표현은 {:f} 로 진행한다.
##### '기호' 붙혀서 출력
- d 앞에 '+' 기호를 붙혀서 format() 의 매개변수 값을 + 혹은 - 붙혀서 표현
``` python
>>> print("{:+d}".format(52))
+52
>>> print("{:+d}".format(-52))
-52
```

## 대문자, 소문자 바꾸기
- upper(): 문자열의 알파벳을 대문자로 생성
- lower(): 문자열의 알파멧을 소문자로 생성
  - upper(), lower() 함수를 사용해도 원본 문자열은 변경이 없음 (비파괴적 함수)
``` python
>>> a = "Hello Python Programming...!"
>>> print(a)
Hello Python Programming...!
>>> a.upper()
'HELLO PYTHON PROGRAMMING...!'
>>> a.lower()
'hello python programming...!'
>>> print(a)
Hello Python Programming...!
```

## 문자열 양옆 공백 제거: strip()
- lstrip(): 왼쪽 공백 제거
- rstrip(): 오른쪽 공백 제거
  - '공백'은 띄어쓰기, 탭, 줄바꿈을 모두 포함
``` python
>>> a = """
...       안녕하세요
... 문자열의 함수를 알아봅니다
... """
>>> print(a)

      안녕하세요
문자열의 함수를 알아봅니다

>>> print(a.strip())
안녕하세요
문자열의 함수를 알아봅니다
```

## 문자열 구성 여부 확인: isXXX()
- 문자열에 마침표(.) 후 isXXX() 함수를 통해 알파벳으로만 구성되어 있는지, 정수 형태인지 등을 확인
- 결과: True/False

## 문자열 찾기
- find(): 매개변수로 전달된 값을 문자열 왼쪽부터 찾아서 처음 등장하는 위치 인덱스를 반환
``` python
>>> a = "안녕안녕안녕하세요"
>>> a.find("안녕")
0
>>> a.find("하")
6
```

## 문자열 존재여부 확인
- 'in' 연산자: A in B (B 문자열 내에 A 가 존재하는지 확인)
- 결과: True/False
``` python
>>> print("안녕" in "안녕하세요")
True
>>> print("HI" in "안녕하세요")
False
```

## 문자열 자르기: split()
- split() 함수 매개변수로 전달된 문자열로 원본 문자열을 자름 (파괴적 함수)
- 결과: 리스트 형식
``` python
>>> a = "10 20 30 40 50".split(" ")
>>> a
['10', '20', '30', '40', '50']
```

## f-문자열
- 문자열 내부에 표현식을 {} 괄호로 감싸서 삽입
- 파이썬 3.6 이후 부터 가능