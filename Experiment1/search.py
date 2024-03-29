"""Implementation of the A* algorithm.

This file contains a skeleton implementation of the A* algorithm. It is a single
method that accepts the root node and runs the A* algorithm
using that node's methods to generate children, evaluate heuristics, etc.
This way, plugging in root nodes of different types, we can run this A* to
solve different problems.

"""
import heapq

def Astar(root):
    """Runs the A* algorithm given the root node. The class of the root node
    defines the problem that's being solved. The algorithm either returns the solution
    as a path from the start node to the goal node or returns None if there's no solution.

    Parameters
    ----------
    root: Node
        The start node of the problem to be solved.

    Returns
    -------
        path: list of Nodes or None
            The solution, a path from the initial node to the goal node.
            If there is no solution it should return None
    """

    # TODO: add your code here
    # Some helper pseudo-code:
    # 1. Create an empty fringe and add your root node (you can use lists, sets, heaps, ... )
    # 2. While the container is not empty:
    # 3.      Pop the best? node (Use the attribute `node.f` in comparison)
    # 4.      If that's a goal node, return node.get_path()
    # 5.      Otherwise, add the children of the node to the fringe
    # 6. Return None
    #
    # Some notes:
    # You can access the state of a node by `node.state`. (You may also want to store evaluated states)
    # You should consider the states evaluated and the ones in the fringe to avoid repeated calculation in 5. above.
    # You can compare two node states by node1.state == node2.state
    res_path = []
    OPEN = [] # 堆
    open_set = set() # 开集合 判断是否出现该状态
    close_set = set() # 闭集合 判断是否出现该状态
    OPEN.append(root)
    heapq.heapify(OPEN) # 使用heap, 加快计算速度
    open_set.add(root.state)
    while len(OPEN) > 0:
        node = heapq.heappop(OPEN) # 找到优先级最高的节点
        if node.is_goal(): # 到达目标
            res_path = node.get_path()
            break
        else: # 不是目标
            open_set.remove(node.state)
            close_set.add(node.state)
            childrens = node.generate_children()
            for children in childrens: # 遍历所有子节点
                if children.state in close_set:
                    continue
                elif children.state not in open_set:
                    open_set.add(children.state)
                    heapq.heappush(OPEN, children)

    return res_path
