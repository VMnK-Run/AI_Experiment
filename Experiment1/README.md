## Experiment1

使用A*搜索算法解决15谜图问题和超级皇后问题

### A* 搜索算法介绍

+ 每一个节点有一个优先级，计算方式：`f(n)=g(n)+h(n)`

  + `f(n)`是节点n的综合优先级，每次选取优先级最高（值最小）
  + `g(n)`是节点n到起点的代价
  + `h(n)`是节点n到终点的代价，即启发式函数
+ 每个节点要知道自己的parent是谁
+ 维护两个集合：`open_set`为待遍历的节点，`close_set`为已遍历的节点
+ 伪代码描述：
+ ```python
  初始化open_set和close_set;
  将起点加入open_set,设置优先级为0；
  if not open_set.isEmpty():
      n = open_set中优先级最高的节点;
      if n 是终点:
          从终点开始回溯parent节点，一直到起点;
          返回找到的路径，结束算法;
      else:
          将n从open_set中删除, 加入close_set;
          for m in n的所有邻近节点:
              if m in close_set:
                  pass;
              else if m not in open_set:
                  m.parent = n;
                  计算m的启发式函数，设置优先级
                  将m加入open_set;
  ```
+ 启发式函数计算：

  + 简单的预测即可，可采用曼哈顿距离，对角距离，欧几里得距离
