####################################################
# 리스트에 요소 추가하기 - append()/insert()
####################################################

# 리스트 선언
list_a = [1, 2, 3]

# 리스트 뒤에 요소 추가하기 - append()
print("# 리스트 뒤에 요소 추가하기")
list_a.append(4)
list_a.append(5)
print(list_a)
print()

# 리스트 중간에 요소 추가하기 - insert()
print("# 리스트 중간에 요소 추가하기")
list_a.insert(0, 10)
print(list_a)
print()

# 리스트 뒤에 새로운 '리스트의 요소'를 추가 - extend()
print("# 리스트 뒤에 새로운 리스트요소 추가하기")
list_a.extend([7, 8, 9])
print(list_a)
print()
