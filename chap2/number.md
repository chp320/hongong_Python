# 자료형

## 숫자
- 소수점이 없는 숫자 (정수형, integer)
- 소수점이 있는 숫자 (실수형, float)
``` python
>>> type(1)
<class 'int'>
>>> type(1.1)
<class 'float'>
```

### 사칙 연산자
- 일반적으로 알고 있는 +(덧셈) , -(뺄셈) , *(곱셈) , /(나눗셈)
##### 정수 나누기 연산자: //
- 나눗셈할 때 '정수'만 남기기 위해 사용
##### 나머지 연산자: %
- 나눗셈할 때 '나머지' 만 구하기 위해 사용
##### 제곱 연산자: **
- xx 승 표현할 때 사용
``` python
>>> print(3/2)
1.5
>>> print(3//2)
1
>>> print(3%2)
1
>>> print(2**3)
8
```

#### TypeError
- 자료형이 다른 항목끼리 연산자 수행 시 발생
``` python
>>> print("hello" + 1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
```

[go to chapter2's main](./README.md)