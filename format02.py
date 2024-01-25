# 정수
output_a = "{:d}".format(52)        # {:d} - int 자료형의 정수를 취하겠다고  직접적으로 지정

# 특정 칸에 출력하기
output_b = "{:5d}".format(52)       # {:5d} - int 자료형의 정수를 취할껀데 5칸을 빈칸으로 잡고 "뒤에서"부터 format으로 전달된 정수를 채우겠다.
output_c = "{:10d}".format(52)      # {:10d} - int 자료형의 정수를 취할껀데 10칸을 빈칸으로 잡고 "뒤에서"부터 format으로 전달된 정수를 채우겠다.

# 빈칸을 0으로 채우기
output_d = "{:05d}".format(52)      # {:05d} - int 자료형의 정수를 취할껀데 5칸을 빈칸으로 잡고 "뒤에서"부터 format으로 전달된 정수로 채우고 남은 빈칸은 0으로 채우겠다.
output_e = "{:05d}".format(-52)     # format의 매개변수에 '부호'가 있을 때(음수인 경우만 해당)는 "맨 앞자리"를 '부호'로 채우고 나머지 빈 곳은 0으로 채운다.

##########################################

print("# 기본")
print(output_a)
print("# 특정 칸에 출력하기")
print(output_b)
print(output_c)
print("# 빈칸을 0으로 채우기")
print(output_d)
print(output_e)


