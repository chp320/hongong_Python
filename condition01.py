######################################
# 짝수와 홀수 구분하기
######################################

# 끝자리로 짝수/홀수 구분

# 입력을 받습니다.
number = input("정수 입력> ")   # input() 의 결과값은 '문자열'

# 끝자리 숫자가 2,4,6,8,0 인 경우 짝수로 판단한다.
# 문자열에서 끝자리 값은 -1 로 확인 가능함
last_character = number[-1]
print(last_character)

# 짝수 여부 확인
if last_character == '0' \
or last_character == '2' \
or last_character == '4' \
or last_character == '6' \
or last_character == '8' :
    print("짝수입니다.")

# 홀수 여부 확인
if last_character == '1' \
or last_character == '3' \
or last_character == '5' \
or last_character == '7' \
or last_character == '9' :
    print("홀수입니다.")
