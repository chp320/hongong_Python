########################
# 기호 붙여 출력하기
########################

# 기호와 함께 출력하기
output_f = "{:+d}".format(52)       # 양수
output_g = "{:+d}".format(-52)      # 음수
output_h = "{: d}".format(52)       # 양수: 기호 부분 공백
output_i = "{: d}".format(-52)      # 음수: 기호 부분 공백

# 기호가 표시된 경우만 출력하기
output_hh = "{:d}".format(52)       # 양수
output_ii = "{:d}".format(-52)      # 음수

print("# 기호와 함께 출력하기")
print(output_f)
print(output_g)
print(output_h)
print(output_i)
print("# 기호가 표시된 경우만 출력하기")
print(output_hh)
print(output_ii)
