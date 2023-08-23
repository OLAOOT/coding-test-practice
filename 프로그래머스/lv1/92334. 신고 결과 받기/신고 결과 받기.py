def solution(id_list, report, k):
    answer = [0] * len(id_list)
    
    report_list = {user: [] for user in id_list}
    reported_counts = {user: 0 for user in id_list}
    
    for r in report:
        user, reported = r.split()
        if reported not in report_list[user]:
            report_list[user].append(reported)
            reported_counts[reported] += 1
    
    for user, count in reported_counts.items():
        if count >= k:
            for idx, reports in enumerate(report_list.values()):
                if user in reports:
                    answer[idx] += 1
    
    return answer