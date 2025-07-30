import heapq
import itertools
from puzzle import Puzzle

def weighted_astar(start_puzzle, heuristic, weight=2, search_mode=None):
    heuristic_functions = {
        1: lambda p: p.manhattan(),
        2: lambda p: p.hamming(),
        3: lambda p: p.manhattan_linear()
    }
    heuristic_func = heuristic_functions[heuristic]
    open_list = []
    counter = itertools.count()

    # Choose f(x) formula based on search_mode
    def f_score(g, h):
        if search_mode == '-u':      # Uniform-cost: ignore heuristic
            return g
        elif search_mode == '-g':    # Greedy: ignore path cost
            return h
        else:                        # Regular Weighted A*
            return g + weight * h
        
    heapq.heappush(open_list, (f_score(0, heuristic_func(start_puzzle)), 0, next(counter), start_puzzle, []))
    closed_set = set()

    # Stats
    states_selected = 0
    max_states_in_memory = 1  # open_list + closed_set

    while open_list:
        _, g, _, node, path = heapq.heappop(open_list)
        states_selected += 1
        state_tuple = tuple(node.flat_puzzle)
        if state_tuple in closed_set:
            continue
        closed_set.add(state_tuple)
        new_path = path + [node]
        # Update max memory usage
        current_states = len(open_list) + len(closed_set)
        if current_states > max_states_in_memory:
            max_states_in_memory = current_states
        if node.is_goal():
            return new_path, (states_selected, max_states_in_memory)
        for succ in node.successors():
            succ_tuple = tuple(succ.flat_puzzle)
            if succ_tuple in closed_set:
                continue
            h = heuristic_func(succ)
            heapq.heappush(open_list, (f_score(g + 1, h), g + 1, next(counter), succ, new_path))
            # Update max memory usage after push
            current_states = len(open_list) + len(closed_set)
            if current_states > max_states_in_memory:
                max_states_in_memory = current_states
    return None, (0, 0)