
class Puzzle():
    def __str__(self):
        """Return a string representation of the puzzle grid."""
        lines = []
        for row in self.puzzle:
            lines.append(' '.join(f"{num:2d}" for num in row))
        return '\n'.join(lines)
    
    def __init__(self, size, puzzle):
        self.size = size
        self.puzzle = puzzle
        self.flat_puzzle = [num for row in puzzle for num in row]
        self.open_list = []
        self.closed_list = []
        self.g = 0  # Cost from start to current node
        self.h = 0  # Heuristic cost to goal
        self.f = 0  # Total cost (g + h)

    def manhattan(self):
        """Calculate the Manhattan (min movements) distance of the puzzle."""
        dist = 0
        for idx, value in enumerate(self.flat_puzzle):
            if value == 0:
                goal_idx = self.size * self.size - 1  # Solving from bottom-right
            else:
                goal_idx = value - 1
            x1, y1 = divmod(idx, self.size)
            x2, y2 = divmod(goal_idx, self.size)
            dist += abs(x1 - x2) + abs(y1 - y2)
        return dist

    def hamming(self):
        """Count the number of misplaced tiles."""
        dist = 0
        for idx, value in enumerate(self.flat_puzzle):
            if value != 0 and value != idx + 1:
                dist += 1
        return dist
    
    def manhattan_linear(self):
        """Calculate Manhattan distance with linear conflict."""
        manhattan = self.manhattan()
        linear_conflict = 0

        # Row conflicts
        for row in range(self.size):
            tiles_in_row = []
            for col in range(self.size):
                tile = self.puzzle[row][col]
                if tile == 0:
                    continue
                goal_row = (tile - 1) // self.size
                goal_col = (tile - 1) % self.size
                if goal_row == row:
                    tiles_in_row.append((col, goal_col))
            # Count conflicts in this row
            for i in range(len(tiles_in_row)):
                for j in range(i + 1, len(tiles_in_row)):
                    col_i, goal_col_i = tiles_in_row[i]
                    col_j, goal_col_j = tiles_in_row[j]
                    if goal_col_i > goal_col_j and col_i < col_j:
                        linear_conflict += 1

        # Column conflicts
        for col in range(self.size):
            tiles_in_col = []
            for row in range(self.size):
                tile = self.puzzle[row][col]
                if tile == 0:
                    continue
                goal_row = (tile - 1) // self.size
                goal_col = (tile - 1) % self.size
                if goal_col == col:
                    tiles_in_col.append((row, goal_row))
            # Count conflicts in this column
            for i in range(len(tiles_in_col)):
                for j in range(i + 1, len(tiles_in_col)):
                    row_i, goal_row_i = tiles_in_col[i]
                    row_j, goal_row_j = tiles_in_col[j]
                    if goal_row_i > goal_row_j and row_i < row_j:
                        linear_conflict += 1

        return manhattan + 2 * linear_conflict
    
    def findXPosition(self):
        """Find the position of the blank tile (0) from the bottom."""
        for i in range(self.size - 1, -1, -1):
            for j in range(self.size - 1, -1, -1):
                if self.puzzle[i][j] == 0:
                    return self.size - i
    def is_goal(self):
        """Check if the current puzzle state is the goal state."""
        goal = list(range(1, self.size * self.size)) + [0]
        return self.flat_puzzle == goal
    
    def successors(self):
        """Generate all possible successor states from the current puzzle state."""
        successors = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
        zero_pos = self.flat_puzzle.index(0)
        zero_row, zero_col = divmod(zero_pos, self.size)

        for dr, dc in directions:
            new_row, new_col = zero_row + dr, zero_col + dc
            if 0 <= new_row < self.size and 0 <= new_col < self.size:
                # Copy the current puzzle state
                new_puzzle = [row[:] for row in self.puzzle]
                # Swap blank with the adjacent tile
                new_puzzle[zero_row][zero_col], new_puzzle[new_row][new_col] = \
                    new_puzzle[new_row][new_col], new_puzzle[zero_row][zero_col]
                # Create a new Puzzle instance and add to successors
                successors.append(Puzzle(self.size, new_puzzle))
        return successors

    def is_solvable(self):
        """Check if the puzzle is solvable (generalized for any size)."""
        def getInvCount(puzzle):
            arr = self.flat_puzzle
            inv_count = 0
            for i in range(self.size * self.size - 1):
                for j in range(i + 1, self.size * self.size):
                    if arr[j] and arr[i] and arr[i] > arr[j]:
                        inv_count += 1
            return inv_count

        invCount = getInvCount(self.puzzle)
        print("Inversion count:", invCount)
        if self.size % 2 == 1:  # If grid is odd, return true if inversion count is even.
            return invCount % 2 == 0
        else:    # grid is even
            pos = self.findXPosition()
            print("Position of blank from bottom:", pos)
            if pos % 2 == 0:  # Blank on even row from bottom
                return invCount % 2 == 1 # Must be odd
            else:
                return invCount % 2 == 0 # Must be even
