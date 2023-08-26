import math

split_time = lambda s: list(map(int, s.split(':')))
def calc_time(t1, t2):
    h1, m1 = split_time(t1)
    h2, m2 = split_time(t2)
    m1 += h1 * 60
    m2 += h2 * 60
    return m2 - m1

def solution(fees, records):
    def calc_fee(time):
        if time > fees[0]:
            return fees[1] + math.ceil((time - fees[0]) / fees[2]) * fees[3]
        else:
            return fees[1]
    
    answer = []
    
    records_dict = {}
    for record in records:
        time, num, _ = record.split()
        
        if num not in records_dict:
            records_dict[num] = [time]
        else:
            records_dict[num].append(time)
            
    for record in records_dict.values():
        if len(record) % 2 != 0:
            record.append('23:59')
    
    records_dict = dict(sorted(records_dict.items()))
    
    for times in records_dict.values():
        times_sum = 0
        for idx in range(0, len(times), 2):
            times_sum += calc_time(times[idx], times[idx + 1])
        answer.append(times_sum)
    
    answer = [calc_fee(time) for time in answer]
    
    return answer