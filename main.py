import sys
from ida_solve import ida_star
from weighted_solve import weighted_astar
from puzzle import Puzzle

def main():
    try: 
        if len(sys.argv) < 3 or len(sys.argv) > 4:
            raise ValueError("Usage: python main.py <input_file.txt> <heuristic_type> (e.g. -l, -m, -h) [bonus_searches] [-u, -g]")
        
        arg = sys.argv[1] 
        if not arg.endswith('.txt'):
            raise ValueError("Error: The input file must have a .txt extension.")
        
        heuristic_type = sys.argv[2]
        if heuristic_type not in ['-l', '-m', '-h']:
            raise ValueError("Error: Invalid heuristic type. Use -l (linear conflict), -m (manhattan), or -h (hamming).")
        
        if len(sys.argv) == 4:
            bonus_searches = sys.argv[3]
            if bonus_searches not in ['-u', '-g']:
                raise ValueError("Error: Invalid bonus searches option. Use -u (uniform cost) or -g (greedy).")
        else:
            bonus_searches = None
            
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

        return puzzle, size
        
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

    # Process the puzzle_input and implement the N-Puzzle solver logic here

ui_puzzle, size = main()
puzzle = Puzzle(size, ui_puzzle)

# Perform IDA* search with the specified heuristic
heuristic_map = {'-l': 3, '-m': 1, '-h': 2}
heuristic = heuristic_map[sys.argv[2]]
search_mode = sys.argv[3] if len(sys.argv) == 4 else None
# print solution
# solution = ida_star(puzzle, heuristic)
if puzzle.is_solvable():
    print("Puzzle is solvable.")
else:
    print("Puzzle is not solvable.")
    sys.exit(0)
solution, (states_selected, max_states_in_memory) = weighted_astar(puzzle, heuristic, search_mode=search_mode)
if solution:
    print("Solution found:")
    for step in solution:
        print(step)
        print('-' * 10)
    print("Done in {} steps.".format(len(solution) - 1))
    print("Total states selected (time complexity): {}".format(states_selected))
    print("Maximum states in memory (space complexity): {}".format(max_states_in_memory))
else:
    print("No solution found.")