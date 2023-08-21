date2list = lambda s: list(map(int, s.split('.')))
def privacy2list(s):
    l = s.split()
    date = date2list(l[0])
    return {
        'date': date,
        'term': l[1]
    }

def solution(today, terms, privacies):
    answer = []
    
    today = date2list(today)
    privacies = list(map(privacy2list, privacies))
    
    termsdict = {}
    for term in terms:
        term = term.split()
        termsdict[term[0]] = int(term[1])
    
    for i, privacy in enumerate(privacies):
        due = privacy['date'][:]
        due[1] += termsdict[privacy['term']]
        while due[1] > 12:
            due[1] -= 12
            due[0] += 1
        
        if due[0] < today[0] or due[0] == today[0] and (
                due[1] < today[1] or due[1] == today[1] and (
                    due[2] <= today[2]
                )
            ):
                answer.append(i + 1)
    
    return answer