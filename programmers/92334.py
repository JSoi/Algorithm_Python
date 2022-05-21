import collections


def solution(id_list, report, k):
    answer = [0] * len(id_list)

    report_log = collections.defaultdict(list)
    report_count = {}
    reporter_index = {}
    for i in range(len(id_list)):
        reporter_index[id_list[i]] = i

    for r in report:
        er, ed = r.split()
        # print(er, ed)
        if ed in report_log[er]:
            continue
        report_log[er].append(ed)
        if ed not in report_count:
            report_count[ed] = 1
        else:
            report_count[ed] = report_count.get(ed) + 1
    # print(report_count)
    # print(reporter_index)
    for re in report_count:
        if int(report_count[re]) >= k:
            for d in report_log:
                if re in report_log[d]:
                    answer[reporter_index[d]] += 1
    # print(answer)
    return answer


a = ["muzi", "frodo", "apeach", "neo"]
b = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
a1 = 	["con", "ryan"]
b1= ["ryan con", "ryan con", "ryan con", "ryan con"]

# solution(a, b, 2)

solution(a1, b1, 3)