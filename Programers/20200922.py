# n에 학생수, lost에 잃어버린 사람, reserve에 여벌옷이 있는 사람이 배열로 들어옴
# 바로 앞번호 혹은 뒷번호인 사람만 빌려줄 수 있고 잃어버린 사람이 여벌옷이 있으면 빌려줄 수 없음
# 최대한 많은 사람이 체육복을 입을 수 있는 학생수를 return함



def solution(n, lost, reserve):
    a=[]
    answer = n - len(lost)
    for i in lost:
        if reserve.count(i) > 0:
            answer += 1
            a.append(i)
            reserve.remove(i)
    for i in a:
        lost.remove(i)
    for i in lost:
        if reserve.count(i-1) > 0:
            answer += 1
            reserve.remove(i-1)
        elif reserve.count(i+1) > 0:
            answer += 1
            reserve.remove(i+1)
    return answer
