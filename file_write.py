# 파일 한 줄씩 읽기 테스트를 위해서 랜덤하게 1,000명의 키와 몸무게 만들기
import random

# 간단한 한글 리스트 생성
hanguls = list("가나다라마바사아자차카타파하")

# 파일을 '쓰기(w)' 모드로 오픈
with open("info.txt", "w") as file:
    for i in range(1000):
        # 랜덤한 값으로 변수 생성
        name = random.choice(hanguls) + random.choice(hanguls)
        weight = random.randrange(40, 100)
        height = random.randrange(140, 200)
        # 텍스트 쓰기
        file.write("{}, {}, {}\n".format(name, weight, height))
