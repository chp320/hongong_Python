# pass 키워드는 '곧 개발하겠음' 정도로 이해하면 될듯
# 그러나 pass만 입력하고 실제 구현하지 않을 수 있으니, 미구현 코드 호출 시 강제로 오류 발생시킬 수 있음

# 입력을 받습니다.
number = input("정수 입력> ")
number = int(number)

# 조건문 사용
if number > 0:
    # 양수일 때: 아직 미구현 상태입니다.
    raise NotImplementedError
else:
    # 음수일 때: 아직 미구현 상태입니다.
    raise NotImplementedError
