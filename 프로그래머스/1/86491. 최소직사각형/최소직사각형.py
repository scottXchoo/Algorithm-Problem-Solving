def solution(sizes):
    width, height = 0, 0
    for size in sizes:
        if size[0] < size[1]:
            temp = size[0]
            size[0] = size[1]
            size[1] = temp
        width = max(width, size[0])
        height = max(height, size[1])
    
    answer = width * height
    return answer