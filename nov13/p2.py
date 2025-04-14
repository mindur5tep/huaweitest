def func():
# 读取输入数据
    n = int(input().strip())
    sets = []

    # 读取每个集合的信息
    for _ in range(n):
        a_i = int(input().strip())
        s_i = set(input().strip() for _ in range(a_i))
        sets.append(s_i)

    # 处理交集
    results = []
    for i in range(n):
        max_intersection_count = 0
        min_j = -1
        
        for j in range(n):
            if i != j:
                # 计算集合Si和Sj的交集大小
                intersection_count = len(sets[i] & sets[j])
                # 更新最大交集和最小j的逻辑
                if intersection_count > max_intersection_count or (intersection_count == max_intersection_count and (min_j == -1 or j < min_j)):
                    max_intersection_count = intersection_count
                    min_j = j + 1  # 序号输出要求从1开始，而不是0

        # 如果交集大小全为0，选择最小序号集合
        if max_intersection_count == 0:
            min_j = 1 if i != 0 else 2
        
        results.append(f"{min_j} {max_intersection_count}")

    # 输出结果
    print("\n".join(results))


if __name__ == "__main__":
    func()
