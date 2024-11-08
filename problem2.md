经过 $A \rightarrow B$ 这条调用栈达到的其他调用栈被称为其子调用栈
如 $A \rightarrow B \rightarrow D$ 是 $A \rightarrow B$ 的子调用栈
通过分析工具对调用栈进行采样分析，得到树形结构，每个节点代表一条调用栈，子节点为父节点的子调用栈，每个节点有一个数值为采样到该调用栈的样本数量。
现在需要刷新个节点的数值为包含其子调用栈的总样本数量，请编码实现：

树的层序遍历，指的是从上到下遍历每层，每层从左到右遍历个节点，为了标识子节点关系，对于 $N$ 个节点的树的层遍历，插入 $N$ 个 $-1$.第 $i$ 个 $-1$ 和第 $i+1$ 个 $-1$ 中间的节点序列为第i个节点的子节点序列，根节点为第一个节点。

输入：
第一行为树的总节点数量 $N$，取值范围 $[1,1000]$;
第二行为树的序列化输入，采用层序遍历，共 $2N$ 个数据，包括$N$个节点的样本数和 $N$ 个节点的子节点序列的分隔符（参见示例）；各节点样本数取值范围 $[0,10000]$

输出：
输出刷新各节点数值后的树，与输入格式保持一致

样例1
输入：

```
6
5 -1 2 3 8 -1 -1 1 7 -1 -1 -1
```

输出：

```
26 -1 2 11 8 -1 -1 1 7 -1 -1 -1
```

解释：
第一行表示树一共有 $6$ 个节点;
第二行为按章层序遍历的序列化输入，共 $12$ 个数据（包含 $6$ 个节点的样本数和 $6$ 个节点的子节点序列的分隔符），含义分别为：

```
 5： 第一个节点 （即根节点），样本数为5；
-1：分隔第一个节点（即根节点）的子节点序列；
 2： 第二个节点的样本数为2，它是根节点的第一个子节点；
 3：第三个节点的样本数为3，它是根节点的第二个子节点；
 8：第四个节点的样本数为8，它是根节点的第三个子节点；
-1：分隔第二个节点的子节点序列，后续无有效值，表示该节点无子节点；
-1：分隔第三个节点的子节点序列；
 1：第五个节点的样本数为1，它是第三个节点的第一个子节点；
 7：第六个节点的样本数为7，它是第三个节点的第二个子节点；
-1：分隔第四个节点的子节点序列，后续无有效值，表示该节点无子节点；
-1：分隔第五个节点的子节点序列，后续无有效值，表示该节点无子节点；
-1：分隔第六个节点的子节点序列，后续无有效值，表示该节点无子节点；
```

构造输入树形结构：

$$ 
5(A)\rightarrow 
 \begin{cases} 2(A\rightarrow B),\\ 
 3(A\rightarrow C)\rightarrow 
  \begin{cases} 1 (A\rightarrow C\rightarrow E)\\ 
   7(A\rightarrow C\rightarrow F)
  \end{cases} ,\\ 
  8(A\rightarrow D)
 \end{cases} 
$$

根据树形结构计算各节点包含子节点的样本数:
调用栈 $A\rightarrow C$ 有子调用栈 $A\rightarrow C\rightarrow E$ 和 $A\rightarrow C\rightarrow F$ ，所以其包含子调用栈的样本数为 $3+1+7 =1$ ：第五个节点的样本数为 $1$，它是第三个节点的第一个子节点；
根节点调用栈 $A$ 包含的子调用栈 $A\rightarrow B,A\rightarrow C,A\rightarrow D$ ，其包含子调用栈的样本数为 5+2+11+8=26.
刷新后的调用栈树按照层序遍历序列化输出为 `26 -1 2 11 8 -1 -1 1 7 -1 -1 -1`

---
树的递归求和，dfs一遍
- 数据结构定义：
    - 使用 `sampleCount` 数组存储每个节点的样本数量
    - `tree` 是一个邻接表，用于储存树的结构，以便进行深度优先搜索
    - `visited` 数组用于标记节点是否被访问，以避免重复访问
- 输入输出处理：
    - 读取节点总数 n
    - 循环读取 $2*n$ 个值，即节点样本数 和 分隔符 `-1`；当读到 `-1` 时表示当前节点子序列结束，进入下一个节点
    - 输出时使用 `visted` 确保每个节点只输出一次
- DFS深度优先搜索计算样本数量：
    - DFS 从根节点开始遍历整棵树；美访问一个子节点时，将样本数量累加到父节点的样本数中
- 复杂度分析
    - 时间复杂度 $O(N)$， $N$ 为节点数， 每个节点和边仅访问一次
    - 空间复杂度 $O(N)$，存储树结构和样本量的数组
