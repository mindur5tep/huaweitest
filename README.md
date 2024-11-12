# huaweitest

Algorithm machine test of Huawei Recruitment on Oct.30

## 第1题-历史行为信任计算

[problem1.md](problem1.md)

[problem1_sol.py](problem1_sol.py)

云计算环境下用户访问行为多样并且复杂，项目组决定根据用户一定时间周期内的最低信任分，控制用户的授权等级。需要设计一个程序，通过分析用户历史信任分序列，输出最小信任分序列。

其中最小信任分为时间周期内的最低信任分。假设历史信任分序列为 $\{x_i\}$ ，时间周期大小为，那么最小信任分 $m_i = \min[x_i,\ x_{i+1}]$ .

已知长度为 $N$ 的用户历史信任分序列和时间周期 $W$，请输出长度为 $N - W + 1$ 的最小信任分序列。

### 输入描述

第一行:用户历史信任分序列的长度 $N[1,10^6]$，时间周期 $W[1,N]$，并使用空格隔开。

第二行:用户历史信任分序列，依次使用空格隔开。其中每个历史信任分为 $[0，10^9]$。

### 输出描述

第一行:输出最小信任分序列，并依次使用空格隔开。

> Tips: 滑动窗口 双端队列 优化算法

```python
from collections import deque

def func():
    # Read input values
    first_line = input().strip()
    second_line = input().strip()

    # Parse the input
    n, w = map(int, first_line.split())
    trust_sequence = list(map(int, second_line.split()))

    # Deque to store indexes of useful elements for each window
    deq = deque()
    result = []

    for i in range(n):
        # Remove elements not within the window
        if deq and deq[0] < i - w + 1:
            deq.popleft()

        # Remove elements that are larger than the current element as they are not useful
        while deq and trust_sequence[deq[-1]] > trust_sequence[i]:
            deq.pop()

        # Add the current element index
        deq.append(i)

        # Append the minimum value for the current window to the result list
        if i >= w - 1:
            result.append(trust_sequence[deq[0]])

    # Print the result as space-separated values
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    func()

```

## 第2题-序列化热点调用栈树

[problem2.md](problem2.md)

[problem2_sol.py](problem2_sol.py)

调用栈指从主函数执行到某个函数的调用路径，

如 $A \rightarrow B$ ，经过这条调用栈到达的其他调用栈称为其子调用栈，如 $A \rightarrow B \rightarrow D$ 是 $A \rightarrow B$ 的子调用栈；

使用某性能分析工具对软件运行过程中的调用栈进行采样分析，得到的热点调用栈数据为树形结构。

树的每个节点代表一条调用栈，子节点为父节点的子调用栈，每个节点有一个数值为采样到该调用栈的样本数量。

现需要刷新各节点的数值为包含其子调用栈的总样本数量，请编码实现。

数的层序遍历，指的是从上到下遍历每层，每层从左到右遍历各节点；为了标识子节点关系，对于 $N$ 个节点的树的层序遍历，插入 $N$ 个 $-1$ 个  ，第 $i$ 个 $-1$ 和第 $i+1$ 个 $-1$ 中间的节点序列为 $i$ 个节点的子节点序列，根节点为第 $1$ 个节点;

### 输入描述

第一行为树的总节点数量 $N$，取值范围 $[1,1000]$;
第二行为树的序列化输入，采用层序遍历，共 $2N$ 个数据，包括 $N$ 个节点的样本数和 $N$ 个节点的子节点序列的分隔符(参见示例)；各节点样本数取值范围 $[0,10000]$

### 输出描述

输出刷新各节点数值后的树，与输入格式保持一致。

> Tips：树的递归求和，dfs一遍
>
> - 数据结构定义：
>   - 使用 `sampleCount` 数组存储每个节点的样本数量
>   - `tree` 是一个邻接表，用于储存树的结构，以便进行深度优先搜索
>   - `visited` 数组用于标记节点是否被访问，以避免重复访问
> - 输入输出处理：
>   - 读取节点总数 n
>   - 循环读取 $2*n$ 个值，即节点样本数 和 分隔符 `-1`；当读到 `-1` 时表示当前节点子序列结束，进入下一个节点
>   - 输出时使用 `visted` 确保每个节点只输出一次
> - DFS深度优先搜索计算样本数量：
>   - DFS 从根节点开始遍历整棵树；美访问一个子节点时，将样本数量累加到父节点的样本数中
> - 复杂度分析
>   - 时间复杂度 $O(N)$， $N$ 为节点数， 每个节点和边仅访问一次
>   - 空间复杂度 $O(N)$，存储树结构和样本量的数组

```python
MAX_NODES = 1000
sample_count = [0] * MAX_NODES
n = 0
tree = [[] for _ in range(MAX_NODES)]
visited = [False] * MAX_NODES

def dfs(curr_node, parent_node):
    for child_node in tree[curr_node]:
        if child_node == parent_node:
            continue
        dfs(child_node, curr_node)
        sample_count[curr_node] += sample_count[child_node]

def func():
    global n
    n = int(input())
    curr_node_idx = 1
    child_node_idx = 1

    values = list(map(int, input().strip().split()))

    for value in values:
        if value == -1:
            curr_node_idx += 1
        else:
            sample_count[child_node_idx] = value
            child_node_idx += 1
            if child_node_idx > 2:
                tree[curr_node_idx -1].append(child_node_idx - 1)
                tree[child_node_idx - 1].append(curr_node_idx - 1)
  
    dfs(1,-1)

    result = []
    result.append(sample_count[1])
    result.append(-1)
    visited[1] = True

    for i in range(1, n + 1):
        size = len(tree[i])
        if size > 1:
            for j in range(size):
                child_node = tree[i][j]
                if not visited[child_node]:
                    visited[child_node] = True
                    result.append(sample_count[child_node])
        if i != n:
            result.append(-1)

    print(" ".join(map(str, result)))

if __name__ == "__main__":
    func()

```

## 第3题-公司班车上车点规划-让最远的员工少走点路

[problem3.md](problem3.md)

[problem3_sol.py](problem3_sol.py)

云某公司基地搬迁到新地点之后，新规划了一条班车路线，在这条路线上会经过 $N$ 个小区，计划在这些小区中挑选出 $M$ 个作为上车点，小区的位置可以用一维坐标上的点来表示，小区到上车点的距离为两个坐标点差值的绝对值。

现在给定个 $N$ 小区的位置，即一维坐标上的整数点: $x_1, x_2,...,x_n$ ，我们希望所有小区到最近上车点的距离的最大值尽可能小，请计算这个最大值的最小值能够是多少?当该小区被作为上车点，该小区到上车点的距离为 $0$。

### 输入描述

第一行有两个整数，用空格隔开:`N M`,   $(1\le M\le N\le  100000)$,
第二行有个没有重复的递增的整数，用空格隔开，表示依次经过个小区的位置， $(1\le  x_i \le 1000000)$

### 输出描述

一个整数，表示所有小区到上车点距离的最大值的最小值

> Tips: 二分搜索 最小中值mid，每个车站的覆盖范围是 $[x - mid, x + mid]$ , 超出范围则加一个车站。遍历时，保持二分 $mid$ 所以需要的车站数不超过 $M$。

```python
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
```
