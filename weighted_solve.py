import heapq
import itertools
from puzzle import Puzzle

def weighted_astar(start_puzzle, heuristic, weight=2):
    heuristic_functions = {
        1: lambda p: p.manhattan(),
        2: lambda p: p.hamming(),
        3: lambda p: p.manhattan_linear()
    }
    heuristic_func = heuristic_functions[heuristic]
    open_list = []
    counter = itertools.count()
    heapq.heappush(open_list, (heuristic_func(start_puzzle) * weight, 0, next(counter), start_puzzle, []))
    closed_set = set()

    while open_list:
        _, g, _, node, path = heapq.heappop(open_list)
        state_tuple = tuple(node.flat_puzzle)
        if state_tuple in closed_set:
            continue
        closed_set.add(state_tuple)
        new_path = path + [node]
        if node.is_goal():
            return new_path
        for succ in node.successors():
            succ_tuple = tuple(succ.flat_puzzle)
            if succ_tuple in closed_set:
                continue
            h = heuristic_func(succ)
            heapq.heappush(open_list, (g + 1 + weight * h, g + 1, next(counter), succ, new_path))
    return None