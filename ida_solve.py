from puzzle import Puzzle

def ida_star(start_puzzle, heuristic):
    """Perform IDA* search on the puzzle."""
    # Check if heuristic is 1, 2, or 3
    heuristic_functions = {
        1: lambda p: p.manhattan(),
        2: lambda p: p.hamming(),
        3: lambda p: p.manhattan_linear()
    }
    heuristic_func = heuristic_functions[heuristic]
    threshold = heuristic_func(start_puzzle)
    path = [start_puzzle]
    visited = set()
    nodes_expanded = [0]
    while True:
        # print(f"Current threshold: {threshold}")
        temp = search(path, 0, threshold, heuristic_func, visited, nodes_expanded)
        if isinstance(temp, tuple) and isinstance(temp[0], list):
            print(f"Total nodes expanded: {temp[1][0]}")
            return temp[0] # Solution found
        if temp == float('inf'):
            return None # No solution found
        threshold = temp

def search(path, g, threshold, heuristic_func, visited, nodes_expanded):
    node = path[-1]
    f = g + heuristic_func(node)
    nodes_expanded[0] += 1
    if f > threshold:
        return f
    if node.is_goal():
        return path[:], nodes_expanded
    min_threshold = float('inf')
    state_tuple = tuple(node.flat_puzzle)
    visited.add(state_tuple)
    # Order successors by heuristic value
    succs = [(succ, heuristic_func(succ)) for succ in node.successors()]
    succs.sort(key=lambda x: x[1])
    for succ, _ in succs:
        succ_tuple = tuple(succ.flat_puzzle)
        if succ_tuple in visited:
            continue
        path.append(succ)
        temp = search(path, g + 1, threshold, heuristic_func, visited, nodes_expanded)
        if isinstance(temp, tuple) and isinstance(temp[0], list):
            return temp
        if temp < min_threshold:
            min_threshold = temp
        path.pop()
    visited.remove(state_tuple)
    return min_threshold