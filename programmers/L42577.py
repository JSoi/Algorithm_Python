def solution(phone_book):  # 해시맵
    my_map = {}
    phone_book.sort(key=len)  # 짧은 값부터 비교하도록 정렬 (119,1111...)
    for number in phone_book:  # 전번 하나하나씩 돌면서
        my_map[number] = 1  # 맵에 '번호 전체'를 저장한다
        tempchar = ''  # 한글자씩 누적해서 더해줄 변수
        for char in number:
            tempchar += char  # 1,11,119 식으로 저장됨
            if tempchar == number:
                # [중요] 전체가 저장 될시 무조건 map에 들어있기 때문에 코드를 진행하지 X
                continue
            if tempchar in my_map:
                # 앞부터 더해나간 누적글자가 map에 존재한다면 접두사가 맞으므로 false반환
                return False  # 탈출
    # print(my_map)
    return True  # 모두 마쳤다면 접두사가 없으므로 TRUE


test = ["119", "1195524421"]
print(solution(test))
