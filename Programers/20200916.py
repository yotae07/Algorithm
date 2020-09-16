# 마라톤 참가자와 완주자가 있는 배열이 2개가 주어짐
# 완주하지 못한 사람의 이름을 return하는 문제
# 동명이인이 있으며, 최대 100000명, completion이 participant보다 1이 작다.



def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i, j in zip(participant, completion):
        if i != j:
            return i
    return participant[-1]
