def func():
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    # 读取输入
    first_line = data[0].split()
    N, M = int(first_line[0]), int(first_line[1])
    positions = list(map(int, data[1].split()))

    # 辅助函数：判断给定距离下是否可以放置M个上车点
    def can_place_buses(max_distance):
        count = 1  # 起始已有一个上车点
        last_position = positions[0]  # 第一个上车点的位置从第一个小区开始

        for i in range(1, N):
            # 如果当前小区和最后放置的上车点的距离超过 max_distance，则放置新上车点
            if positions[i] - last_position > max_distance:
                count += 1
                last_position = positions[i]  # 更新最后一个上车点的位置
                # 如果上车点数量超过 M，则该距离不可行
                if count > M:
                    return False
        return True

    # 二分搜索确定最小的最大距离
    left, right = 0, positions[-1] - positions[0]
    while left < right:
        mid = (left + right) // 2
        if can_place_buses(mid):
            right = mid  # 如果当前距离可行，尝试更小的距离
        else:
            left = mid + 1  # 如果当前距离不可行，增大距离

    # 输出最小的最大距离
    print(left)

if __name__ == "__main__":
    func()

"""
```python
def min_max_distance(n, m, arr):
    arr.sort()
    
    # 二分查找最小的最大距离
    def is_valid(d):
        count, last = 1, arr[0]
        for i in range(1, n):
            if arr[i] - last >= d:
                count += 1
                last = arr[i]
                if count == m:
                    return True
        return False
    
    left, right = 0, arr[-1] - arr[0]
    while left < right:
        mid = (left + right + 1) // 2
        if is_valid(mid):
            left = mid
        else:
            right = mid - 1
    
    return left

# 示例输入
n, m = map(int, input("输入N和M，用空格隔开: ").split())
arr = list(map(int, input("输入包含N个值的一维数组: ").split()))

# 输出结果
print("最小差值绝对值的最大值:", min_max_distance(n, m, arr))
```

可以通过动态规划的思想来解决这个问题，将问题转化为在一个数组中选择 
𝑀 个值，使得每个未选中的元素到最近选中的元素的距离之和最小。具体实现如下：

```python

def min_difference(N, M, arr):
    arr.sort()
    
    # 初始化dp数组，其中dp[i][j]表示在前i个元素中选j个值的最小绝对差值和
    dp = [[float('inf')] * (M + 1) for _ in range(N + 1)]
    for i in range(N + 1):
        dp[i][0] = 0  # 不选取任何值时，差值和为0
    
    # 填充dp数组
    for i in range(1, N + 1):
        for j in range(1, min(i, M) + 1):
            for k in range(j - 1, i):
                dp[i][j] = min(dp[i][j], dp[k][j - 1] + abs(arr[i - 1] - arr[k]))
    
    # 最小差值和
    min_difference_sum = dp[N][M]
    return min_difference_sum

# 输入处理
N, M = map(int, input().split())
arr = list(map(int, input().split()))

# 计算最小差值的绝对值和并输出
result = min_difference(N, M, arr)
print(result)
```

排序：首先对输入的数组进行排序，以便在后续处理差值时，能够快速得到相邻元素的最小差值。
动态规划：定义 dp[i][j] 表示在前 i 个元素中选择 j 个元素时，能够得到的最小差值和。
状态转移：在 dp[i][j] 中，遍历前面所有可能选取的元素，将它们和当前元素的绝对差值加到结果中，更新 dp[i][j]。
结果输出：最终 dp[N][M] 即为所求最小差值和。

```python
def min_max_absolute_difference(N, M, arr):
    min_diff = arr[-1] - arr[0]
    
    for i in range(N - M + 1):
        max_diff = arr[-1] - arr[0]
        for j in range(N):
            if j < i:
                max_diff = max(max_diff, abs(arr[j] - arr[i]))
            elif j >= i + M:
                max_diff = max(max_diff, abs(arr[j] - arr[i + M - 1]))
        min_diff = max(min_diff, max_diff)
    
    return min_diff

def func():
    first_line = input().strip()
    second_line = input().strip()

    N, M = map(int, first_line.split())
    positions = list(map(int, second_line.split()))
        
    left = min_max_absolute_difference(N, M, positions)
    print(left)

if __name__ == "__main__":
    func()
```
"""