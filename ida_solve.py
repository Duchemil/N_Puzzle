from puzzle import Puzzle

def ida_star(start_puzzle, heuristic):
    """Perform IDA* search on the puzzle."""
    # Check if heuristic is 1, 2, or 3
    heuristic_functions = {
        1: start_puzzle.manhattan,
        2: start_puzzle.hamming,
        3: start_puzzle.manhattan_linear
    }
    heuristic_func = heuristic_functions[heuristic]
    threshold = heuristic_func()
    print("Picked Threshold:", threshold)

