###################
# 조건문의 기본 사용
###################

# 값을 입력 받음
number = input("정수 입력> ")   # 결과값은 '문자열'로 반환됨
number = int(number)

# 양수 조건
if number > 0:
    print("양수입니다.")

# 음수 조건
if number < 0:
    print("음수입니다.")

# 0 조건
if number == 0:
    print("0입니다.")
