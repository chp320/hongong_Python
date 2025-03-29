########################
# 기호 조합해 보기
########################

# 조합하기
output_h = "{:+5d}".format(52)      # 양수: 기호를 뒤로 밀기
output_h2 = "{:5d}".format(52)      # 양수: 뒤에서부터 채워짐
output_i = "{:+5d}".format(-52)     # 음수: 기호를 뒤로 밀기
output_i2 = "{:5d}".format(-52)     # 음수: 뒤에서부터 채워짐
output_j = "{:=+5d}".format(52)     # 양수: 기호를 '앞으로' 밀기
# output_j2 = "{:=0+5d}".format(52)   # ValueError: Invalid format specifier
output_k = "{:=+5d}".format(-52)    # 음수: 기호를 '앞으로' 밀기
output_l = "{:+05d}".format(52)     # 양수: 0으로 채우기
output_m = "{:+05d}".format(-52)    # 음수: 0으로 채우기

print("# 조합하기")
print(output_h)
print(output_h2)
print(output_i)
print(output_i2)
print(output_j)
print(output_k)
print(output_l)
print(output_m)
# print("# 조합순서 오입력한 경우")
# print(output_j2)
