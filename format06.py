# 소수점 아래 자릿수 지정하기
output_a = "{:15.3f}".format(52.273)    # 전체 15자리로 잡고, 소수점을 3자리 출력
output_b = "{:15.2f}".format(52.273)    # 전체 15자리로 잡고, 소수점을 2자리 출력
output_c = "{:15.1f}".format(52.273)    # 전체 15자리로 잡고, 소수점을 1자리 출력

print(output_a)
print(output_b)
print(output_c)
