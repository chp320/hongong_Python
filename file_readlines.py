# 앞서 생성한 info.txt 파일에서 한 줄씩 읽기
with open("info.txt", "r") as file:
    for line in file:
        # 변수 선언
        (name, weight, height) = line.strip().split(", ")

        # 데이터 검증: 문제 있는 경우 skip~
        if (not name) or (not weight) or (not height):
            continue

        # 결과를 계산
        bmi = int(weight) / ((int(height) / 100) ** 2)
        result = ""
        if 25 <= bmi:
            result = "과체중"
        elif 18.5 <= bmi:
            result = "정상 체중"
        else:
            result = "저체중"

        print('\n'.join([
            "이름: {}",
            "몸무게: {}",
            "키: {}",
            "BMI: {}",
            "결과: {}"
        ]).format(name, weight, height, bmi, result))
        print()
