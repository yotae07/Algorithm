# scoville배열에 음식의 맵기들이 들어있음
# 가장 덜 매운맛 + 그 다음 덜 매운맛 * 2 한 값이 K보다 큰지 확인해야됨
# 계산을 몇번했는지 횟수를 return


import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while(1):
        if scoville[0] >= K:
            return answer
        if len(scoville) == 1:
            return -1
        heapq.heappush(scoville, heapq.heappop(scoville) + (heapq.heappop(scoville) * 2))
        answer += 1
    return answer
