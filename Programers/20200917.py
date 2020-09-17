# 초 단위로 기록된 주식가격이 prices배열로 들어옴
# 가격이 떨어지지 않는 시간을 배열에 담아 return해야됨
# prices는 1이상 10000이하 길이는 2이상 10000이하



def solution(prices):
    answer = []
    count = 0
    for i in range(len(prices)-1):
        for j in range(i+1, len(prices)):
            if prices[i] > prices[j] or j == len(prices)-1:
                count += 1
                answer.append(count)
                count = 0
                break
            else:
                count += 1
    answer.append(0)
    return answer
