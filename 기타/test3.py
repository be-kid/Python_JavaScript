def solution(tri):
    for i in range(len(tri)):
        tri[i] = list(tri[i])
    tri.reverse()
    for i in range(1, len(tri)):
        tri[i] = find_num(tri[i], i-1 , tri)

    return tri
        
def find_num(arr, row, tri):
    num_idx = 0
    for i in range(len(arr)):
        if arr[i] != '?':
            num_idx = i
    
    for i in range(num_idx, 0, -1):
        arr[i-1] = find_side_num(arr[i], tri[row][i-1])
        
    for i in range(num_idx + 1, len(arr)):
        arr[i] = find_side_num(arr[i-1], tri[row][i-1])
    return arr
        
def find_side_num(x, y):
    x = int(x)
    y = int(y)
    print(x,y)
    if y - x < 0:
        return y-x+10
    else:
        return y-x
    
print(solution(["4??","?2","1"]))