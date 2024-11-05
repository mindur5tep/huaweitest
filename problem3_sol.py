def can_placest(N, M, arr, mid):
    count = 1  # 选择的点数量
    last_position = arr[0]

    for i in range(1, N):
        if arr[i] - last_position > 2 * mid:
            count += 1
            last_position = arr[i]
            if count > M:
                return False
    return True

def func():
    first_line = input().strip()
    second_line = input().strip()

    N, M = map(int, first_line.split())
    positions = list(map(int, second_line.split()))
        
        # 二分查找最小的最大差值
    left, right = 0, positions[-1] - positions[0]
    ans = right
    while left <= right:
        mid = (left + right) // 2
        if can_placest(N, M, positions, mid):
            ans = mid 
            right = mid - 1
        else:
            left = mid + 1

    print(ans)

if __name__ == "__main__":
    func()