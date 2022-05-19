import collections
import math


def solution(progresses, speeds):
    """
    제출 코드입니다!
    밑의 solution_queue도 작동하지만 이쪽에 주석을 더 달았습니다
    """

    # speed update필요
    time_q = collections.deque() # FIFO이므로 큐! deque 사용
    for i in range(len(speeds)): # 수행시간을 계산해 큐에 더해준다(올림 필수)
        time_q.append(math.ceil((100 - progresses[i]) / speeds[i]))
    # print(time)
    longtime = 0 # 오래걸리는 시간을 저장하는 변수
    dict = collections.OrderedDict() # 순서가 섞일 수 있으므로 ordereddict
    while len(time_q) > 0: # pop할게 있을 때 까지 진행
        temp = time_q.popleft() # 맨 앞의 것을 꺼내온다! 반복수행될 수 있으므로 변수에 저장
        if longtime >= temp:  # 최장시간보다 짧은 경우 최장시간에 더해줘야 한다
            if longtime in dict: # [생략가능 - 초기에 else가 무조건 수행됨..]
                dict[longtime] = dict.get(longtime) + 1
        else:  # 최장 시간인 경우 - dict에 존재하지 않는다
            longtime = temp # 최장 시간 업데이트
            dict[longtime] = 1 # 최장시간을 key로 갖는 튜플 생성
    # print(dict)
    return list(dict.values()) # K,V 중 V만 쓰므로 values 뽑아서 리스트화


def solution_queue(progresses, speeds):
    answer = []
    # speed update필요
    time_q = collections.deque()  # 큐를 위해 deque 사용
    for i in range(len(speeds)):
        time_q.append(math.ceil((100 - progresses[i]) / speeds[i]))  # 무조건 올림 해줘야 된다
    # print(time) #time 출력 테스트
    while len(time_q) > 0:  # pop할게 있을 때까지
        temp = time_q.popleft() # pop한값 저장
        count = 1
        while time_q and temp >= time_q[0]:  # 다음 peek 값이 클때까지 진행한다!!
            time_q.popleft()
            count += 1
        answer.append(count)
    # print('answer', answer)
    return answer


p1 = [93, 30, 55]
s1 = [1, 30, 5]
p2 = [95, 90, 99, 99, 80, 99]
s2 = [1, 1, 1, 1, 1, 1]
print("------------")
print(solution(p1, s1))
print(solution(p2, s2))
print(solution([1], [1]))
