import collections
import math


def solution(fees, records):
    record_dict = collections.defaultdict(str)
    fee_dict = collections.defaultdict(int)

    def each_parking_time(instr, outstr):
        H = int(outstr[0:2]) - int(instr[0:2])
        M = int(outstr[3:5]) - int(instr[3:5])
        return 60 * H + M

    for rec in records:
        r = list(rec.split())  # 시간, 차량번호, 입출차
        if r[2] == 'IN':
            record_dict[r[1]] = r[0]
        else:  # 출차시 계산
            fee_dict[r[1]] += each_parking_time(record_dict[r[1]], r[0])
            record_dict[r[1]] = ''
    for key, val in record_dict.items():
        if val != '':
            fee_dict[key] += each_parking_time(val, '23:59')

    answer = []
    for carnum, time in fee_dict.items():
        # 기본시간, 기본요금, 단위 시간, 단위 요금
        if time <= fees[0]:
            fee_dict[carnum] = fees[1]
            continue
        time -= fees[0]
        fee_dict[carnum] = fees[1] + math.ceil(time / fees[2]) * fees[3]
    for k, v in sorted(fee_dict.items(), key=lambda item: item[0]):
        answer.append(v)
    print(answer)
    return answer


solution([180, 5000, 10, 600],
         ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN",
          "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])
