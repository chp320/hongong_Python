# 여러 줄 문자열과 if 구문을 조합했을 때의 문제 해결1

# 변수 선언
number = int(input("정수 입력> "))

# if 조건문으로 홀/짝수 구분
if number % 2 == 0:
    print((
        "입력한 문자열은 {}입니다. \n"
        "{}는(은) 짝수입니다. \n"
    ).format(number, number))
else:
    print((
        "입력한 문자열은 {}입니다. \n"
        "{}는(은) 홀수입니다. \n"
    ).format(number, number))
