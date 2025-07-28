import sys

class Puzzle():
    def __init__(self, size, puzzle):
        self.size = size
        self.puzzle = puzzle
        self.flat_puzzle = [num for row in puzzle for num in row]

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

    def solve(self):
        pass
    
    # Why doesn't this work?
    # def is_solvable(self): 
    #     """Check if the puzzle is solvable (generalized for any size)."""
    #     def getInvCount(puzzle):
    #         arr = self.flat_puzzle
    #         print("Flat puzzle:", arr)
    #         inv_count = 0
    #         for i in range(self.size * self.size - 1):
    #             for j in range(i + 1, self.size * self.size):
    #                 if arr[j] and arr[i] and arr[i] > arr[j]:
    #                     inv_count += 1
    #         return inv_count

    #     def findXPosition(puzzle):
    #         # Find the row of the blank (0) from the bottom
    #         for i in range(self.size - 1, -1, -1):
    #             for j in range(self.size - 1, -1, -1):
    #                 if puzzle[i][j] == 0:
    #                     return self.size - i

    #     invCount = getInvCount(puzzle)
    #     print("Inversion count:", invCount)
    #     # If grid is odd, return true if inversion
    #     # count is even.
    #     if (self.size & 1):
    #         return ~(invCount & 1)

    #     else:    # grid is even
    #         pos = findXPosition(self.puzzle)
    #         if (pos & 1):
    #             return ~(invCount & 1)
    #         else:
    #             return invCount & 1

def main():
    try: 
        if len(sys.argv) != 2:
            raise ValueError("Usage: python n_puzzle.py <input_file.txt>")
        
        arg = sys.argv[1] 
        if not arg.endswith('.txt'):
            raise ValueError("Error: The input file must have a .txt extension.")
        
        with open(arg, 'r') as file:
            lines = file.readlines()

        data_lines = [line.strip() for line in lines if line.strip() and not line.strip().startswith('#')]
        if not data_lines:
            raise ValueError("Error: The input file is empty or contains only comments.")
        
        puzzle = []
        size = int(data_lines[0])
        for line in data_lines[1:]:
            row = list(map(int, line.split()))
            if len(row) != size:
                raise ValueError(f"Error: Each row must have exactly {size} elements.")
            puzzle.append(row)

        if len(puzzle) != size:
            raise ValueError("Error: The puzzle does not match the specified size.")
        
        # Check if a number is repeated or out of range
        flat_puzzle = [num for row in puzzle for num in row]
        if len(flat_puzzle) != len(set(flat_puzzle)):
            raise ValueError("Error: The puzzle contains duplicate numbers.")
        if any(num < 0 or num >= size * size for num in flat_puzzle):
            raise ValueError("Error: The puzzle contains numbers out of the valid range (0 to size*size-1).")

        print("Puzzle loaded successfully:")
        for row in puzzle:
            print(row)
            
        return puzzle, size

        
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

    puzzle_input = sys.argv[1]
    # Process the puzzle_input and implement the N-Puzzle solver logic here

if __name__ == "__main__" :

    ui_puzzle, size = main()
    puzzle = Puzzle(size, ui_puzzle)
    print("Size of the puzzle:", size)
    print("Manhattan/Taxicab distance:", puzzle.manhattan())
    print("Hamming distance:", puzzle.hamming())
    print("Manhattan distance with linear conflict:", puzzle.manhattan_linear())