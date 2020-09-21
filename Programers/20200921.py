# 3명이 답을 일정한 규칙을 가지고 찍음
# 정답이 순서대로 들어있는 배열과 비교해서 가장 답을 많이 맞춘사람을 return
# 여러명이면 오름차순으로 정렬 후 return



def solution(answers):
    answer = []
    count = [0, 0, 0]
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for idx, ans in enumerate(answers):
        if first[idx%5] == ans:
            count[0] +=1
        if second[idx%8] == ans:
            count[1] +=1
        if third[idx%10] == ans:
            count[2] +=1
    return [i+1 for i in range(len(count)) if count[i] == max(count)]
