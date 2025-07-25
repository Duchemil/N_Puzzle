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
        """Calculate the Manhattan distance using linear conflict."""
        pass

    def solve(self):
        pass
    
    def is_solvable(self):
        """Check if the puzzle is solvable."""
        # https://www.geeksforgeeks.org/dsa/check-instance-8-puzzle-solvable/

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
    print("Manhattan distance:", puzzle.manhattan())
    print("Hamming distance:", puzzle.hamming())