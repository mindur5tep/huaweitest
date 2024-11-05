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
