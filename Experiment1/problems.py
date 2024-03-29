from node import Node
import copy

class FifteensNode(Node):
    """Extends the Node class to solve the 15 puzzle.

    Parameters
    ----------
    parent : Node, optional
        The parent node. It is optional only if the input_str is provided. Default is None.

    g : int or float, optional
        The cost to reach this node from the start node : g(n).
        In this puzzle it is the number of moves to reach this node from the initial configuration.
        It is optional only if the input_str is provided. Default is 0.

    board : list of lists
        The two-dimensional list that describes the state. It is a 4x4 array of values 0, ..., 15.
        It is optional only if the input_str is provided. Default is None.

    input_str : str
        The input string to be parsed to create the board.
        The argument 'board' will be ignored, if input_str is provided.
        Example: input_str = '1 2 3 4\n5 6 7 8\n9 10 0 11\n13 14 15 12' # 0 represents the empty cell

    Examples
    ----------
    Initialization with an input string (Only the first/root construction call should be formatted like this):
    >>> n = FifteensNode(input_str=initial_state_str)
    >>> print(n)
      5  1  4  8
      7     2 11
      9  3 14 10
      6 13 15 12

    Generating a child node (All the child construction calls should be formatted like this) ::
    >>> n = FifteensNode(parent=p, g=p.g+c, board=updated_board)
    >>> print(n)
      5  1  4  8
      7  2    11
      9  3 14 10
      6 13 15 12

    """

    def __init__(self, parent=None, g=0, board=None, input_str=None):
        # NOTE: You shouldn't modify the constructor
        if input_str:
            self.board = []
            for i, line in enumerate(filter(None, input_str.splitlines())):
                self.board.append([int(n) for n in line.split()])
        else:
            self.board = board

        super(FifteensNode, self).__init__(parent, g)

    def generate_children(self):
        """Generates children by trying all 4 possible moves of the empty cell.

        Returns
        -------
            children : list of Nodes
                The list of child nodes.
        """

        # TODO: add your code here
        # You should use self.board to produce children. Don't forget to create a new board for each child
        # e.g you can use copy.deepcopy function from the standard library.
        childrens = []
        row = -1; col = -1;
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == 0:
                    row = i;
                    col = j;
                    break
        if row == -1 or col == -1:
            return childrens
        if row - 1 >= 0:
            child_board = copy.deepcopy(self.board)
            child_board[row][col], child_board[row - 1][col] = child_board[row - 1][col], child_board[row][col]
            children = FifteensNode(parent=self, g=self.g+1, board=child_board, input_str=None)
            childrens.append(children)
        if row + 1 <= 3:
            child_board = copy.deepcopy(self.board)
            child_board[row][col], child_board[row + 1][col] = child_board[row + 1][col], child_board[row][col]
            children = FifteensNode(parent=self, g=self.g+1, board=child_board, input_str=None)
            childrens.append(children)
        if col - 1 >= 0:
            child_board = copy.deepcopy(self.board)
            child_board[row][col], child_board[row][col - 1] = child_board[row][col - 1], child_board[row][col]
            children = FifteensNode(parent=self, g=self.g+1, board=child_board, input_str=None)
            childrens.append(children)
        if col + 1 <= 3:
            child_board = copy.deepcopy(self.board)
            child_board[row][col], child_board[row][col + 1] = child_board[row][col + 1], child_board[row][col]
            children = FifteensNode(parent=self, g=self.g+1, board=child_board, input_str=None)
            childrens.append(children)
        return childrens

    def is_goal(self):
        """Decides whether this search state is the final state of the puzzle.

        Returns
        -------
            is_goal : bool
                True if this search state is the goal state, False otherwise.
        """

        # TODO: add your code here
        # You should use self.board to decide.
        flag = True
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if i == 3 and j == 3:
                    if self.board[i][j] != 0:
                        flag = False
                else:
                    if self.board[i][j] != i * 4 + j + 1:
                        flag = False

        return flag

    def evaluate_heuristic(self):
        """Heuristic function h(n) that estimates the minimum number of moves
        required to reach the goal state from this node.

        Returns
        -------
            h : int or float
                The heuristic value for this state.
        """

        # TODO: add your code here
        # You may want to use self.board here.
        h = 0;
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if i == 3 and j == 3:
                    target = 0
                else:
                    target = i * 4 + j + 1
                num = self.board[i][j]
                if num != target:
                    x = num / 4
                    y = num - 4 * x - 1
                    h += (abs(x - i) + abs(y - j)) # 计算曼哈顿距离

        return h

    def _get_state(self):
        """Returns an hashable representation of this search state.

        Returns
        -------
            state: tuple
                The hashable representation of the search state
        """
        # NOTE: You shouldn't modify this method.
        return tuple([n for row in self.board for n in row])

    def __str__(self):
        """Returns the string representation of this node.

        Returns
        -------
            state_str : str
                The string representation of the node.
        """
        # NOTE: You shouldn't modify this method.
        sb = []  # String builder
        for row in self.board:
            for i in row:
                sb.append(' ')
                if i == 0:
                    sb.append('  ')
                else:
                    if i < 10:
                        sb.append(' ')
                    sb.append(str(i))
            sb.append('\n')
        return ''.join(sb)

    def __lt__(self, other):
        return self.f < other.f

    

class SuperqueensNode(Node):
    """Extends the Node class to solve the Superqueens problem.

    Parameters
    ----------
    parent : Node, optional
        The parent node. Default is None.

    g : int or float, optional
        The cost to reach this node from the start node : g(n).
        In this problem it is the number of pairs of superqueens that can attack each other in this state configuration.
        Default is 1.

    queen_positions : list of pairs
        The list that stores the x and y positions of the queens in this state configuration.
        Example: [(q1_y,q1_x),(q2_y,q2_x)]. Note that the upper left corner is the origin and y increases downward
        Default is the empty list [].
        ------> x
        |
        |
        v
        y

    n : int
        The size of the board (n x n)

    Examples
    ----------
    Initialization with a board size (Only the first/root construction call should be formatted like this):
    >>> n = SuperqueensNode(n=4)
    >>> print(n)
         .  .  .  .
         .  .  .  .
         .  .  .  .
         .  .  .  .

    Generating a child node (All the child construction calls should be formatted like this):
    >>> n = SuperqueensNode(parent=p, g=p.g+c, queen_positions=updated_queen_positions, n=p.n)
    >>> print(n)
         Q  .  .  .
         .  .  .  .
         .  .  .  .
         .  .  .  .

    """

    def __init__(self, parent=None, g=0, queen_positions=[], n=1):
        # NOTE: You shouldn't modify the constructor
        self.queen_positions = queen_positions
        self.n = n
        super(SuperqueensNode, self).__init__(parent, g)

    def generate_children(self):
        """Generates children by adding a new queen.

        Returns
        -------
            children : list of Nodes
                The list of child nodes.
        """
        # TODO: add your code here
        # You should use self.queen_positions and self.n to produce children.
        # Don't forget to create a new queen_positions list for each child.
        # You can use copy.deepcopy function from the standard library.
        childrens = []
        x_flag = [False for x in range(self.n)]
        y_flag = [False for y in range(self.n)]
        if len(self.queen_positions) == self.n:
            return childrens
        for tuple in self.queen_positions:
            x_flag[tuple[1]] = True
            y_flag[tuple[0]] = True
        # 计算下一个要摆放的行号
        next_y = 0
        if len(self.queen_positions) == 0:
            next_y = 0
        else:
            tuple = self.queen_positions[-1]
            next_y = tuple[0] + 1
        directions = [(-2, 1), (-1, 2), (1, 2), (2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1)] # 马的移动方向
        for i in range(self.n):
            if x_flag[i] == False:
                new_positions = copy.deepcopy(self.queen_positions)
                new_positions.append((next_y, i))
                cost = 0 # 计算新产生的耗费
                for j in range(min(next_y, i)):
                    if (next_y - j - 1, i - j - 1) in new_positions:
                        cost += 1
                for j in range(min(next_y, self.n - i - 1)):
                    if (next_y - j - 1, i + j + 1) in new_positions:
                        cost += 1
                for j in directions: # knight的攻击方式
                    if (next_y + j[0], i + j[1]) in new_positions:
                        cost += 1
                children = SuperqueensNode(parent=self, g=self.g+cost, queen_positions=new_positions,n=self.n)
                childrens.append(children)
        return childrens

    def is_goal(self):
        """Decides whether all the queens are placed on the board.

        Returns
        -------
            is_goal : bool
                True if all the queens are placed on the board, False otherwise.
        """
        # You should use self.queen_positions and self.n to decide.
        # TODO: add your code here
        x_flag = [False for i in range(self.n)]
        y_flag = [False for i in range(self.n)]
        flag = True
        for tuple in self.queen_positions:
            if x_flag[tuple[1]] == False:
                x_flag[tuple[1]] = True
            else:
                flag = False
                break
            
            if y_flag[tuple[0]] == False:
                y_flag[tuple[0]] = True
            else:
                flag = False
                break
        # 要先保证放了足够的皇后
        if len(self.queen_positions) != self.n:
            flag = False
        return flag

    def evaluate_heuristic(self):
        """Heuristic function h(n) that estimates the minimum number of conflicts required to reach the final state.

        Returns
        -------
            h : int or float
                The heuristic value for this state.
        """
        # If you want to design a heuristic for this problem, you should use self.queen_positions and self.n.
        # TODO: add your code here (optional)
        h = 0
        
        return h

    def _get_state(self):
        """Returns an hashable representation of this search state.

        Returns
        -------
            state: tuple
                The hashable representation of the search state
        """
        # NOTE: You shouldn't modify this method.
        return tuple(self.queen_positions)

    def __str__(self):
        """Returns the string representation of this node.

        Returns
        -------
            state_str : str
                The string representation of the node.
        """
        # NOTE: You shouldn't modify this method.
        sb = [[' . '] * self.n for i in range(self.n)]  # String builder
        for i, j in self.queen_positions:
            sb[i][j] = ' Q '
        return '\n'.join([''.join(row) for row in sb])

    def __lt__(self, other):
        return self.f < other.f
