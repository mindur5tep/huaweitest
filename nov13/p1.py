def func():
    m = int(input().strip())
    # 读取每位游客的游玩时段
    intervals = []
    for i in range(1, m + 1):
        start, end = map(int, input().strip().split())
        intervals.append((start, end))
    
    # 按开始时间排序，若开始时间相同则按结束时间排序
    intervals.sort()
    
    # 变量初始化
    total_duration = 0
    current_start, current_end = intervals[0]
    
    # 遍历所有时段，合并重叠时段并计算总时长
    for i in range(1, m):
        start, end = intervals[i]
        if start <= current_end:  # 区间重叠
            current_end = max(current_end, end)  # 合并区间
        else:  # 区间不重叠，计算前一区间长度并移动到下一区间
            total_duration += current_end - current_start
            current_start, current_end = start, end
    
    # 加上最后一个区间的长度
    total_duration += current_end - current_start
    
    # 输出结果
    print(total_duration)

if __name__ == "__main__":
    func()
