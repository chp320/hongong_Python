#######################################
# 사용자에게 숫자 두 개 입력받고
# 입력받은 두 수의 뎃셈, 뺄셈, 곱셈, 나눗셈 연산 기능
#######################################

# 데이터 입력
input_a = input("첫 번째 수를 입력하세요: ")
input_b = input("두 번째 수를 입력하세요: ")

# 덧셈
output_1 = int(input_a) + int(input_b)

# 뺄셈
output_2 = int(input_a) - int(input_b)

# 곱셈
output_3 = int(input_a) * int(input_b)

# 나눗셈
output_4 = float(input_a) / float(input_b)

print("덧셈: ", output_1)
print("뺄셈: ", output_2)
print("곱셈: ", output_3)
print("나눗셈: ", output_4)