# array배열에 값이 들어오고 commands 이중배열 형태로 값이 3개 담겨 들어옴
# 첫번째와 두번째는 길이를 정해주고 마지막값이 인덱스를 정해줌
# 그 값들을 담아서 배열형태로 return 하면됨


def solution(array, commands):
    return list(map(lambda x: sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
