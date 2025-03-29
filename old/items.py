# 딕셔너리에 items() 함수 사용하기

# 변수 선언
dictionary = {
    "키A": "값A",
    "키B": "값B",
    "키C": "값C"
}

# 딕셔너리의 items() 함수 결과 출력하기
print("# 딕셔너리의 items() 함수")
print("items(): ", dictionary.items())
print()

# for 반복문과 items() 함수 조합해서 사용하기
print("# 딕셔너리의 items() 함수와 반복문 조합하기")

for key, element in dictionary.items():
    print("dictionary[{}] = {}".format(key, element))
