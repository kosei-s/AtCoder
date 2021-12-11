N, Q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
questions = [int(input()) for _ in range(Q)]

def binary_search(target):
    left = 0
    right = N - 1
    while(left <= right):
        mid = (left + right) // 2
        # print(mid)  # debug
        if A[mid] == target:
            return mid
        elif A[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    
    return left

for i in range(Q):
    # print('#####')
    num = binary_search(questions[i])
    print(N - num)
