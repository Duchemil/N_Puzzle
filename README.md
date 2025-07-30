# N-Puzzle Solver

This project solves the N-Puzzle (also known as "Taquin" in French) using primarily the informed search algorithms **Weighted A\***, it also includes **Uniform-Cost Search** and **Greedy Search** for the bonus part. The solver supports different heuristics (Manhattan, Hamming and Manhattan with Linear Conflict) and provides statistics about the search process.

---

## Features

- **Weighted A\***: Fast, heuristic-driven search (not always optimal).
- **Uniform-Cost Search**: Finds the shortest solution, ignores heuristics (slow).
- **Greedy Search**: Uses only the heuristic, very fast but not always optimal.
- **Heuristics**:
  - Manhattan Distance
  - Hamming Distance
  - Manhattan Distance with Linear Conflict
- **Solvability Check**: Automatically checks if a puzzle is solvable before searching.
- **Statistics**: Prints the number of states selected (time complexity) and the maximum number of states in memory (space complexity).
- **Readable Output**: Prints each step of the solution as a grid.

---

## Usage

The program can currently handle random puzzle up to 5*5 in size.
With a 6*6 generated randomly it starts to take a lot of time to solve, easy 6`*`6 can be solved without problems.
```bash
python [main.py](http://_vscodecontentref_/0) <input_file.txt> <heuristic_type> [search_mode]

Input_file example :
```
`#` This is a comment, next line is the size, puzzle afterwards.
3 
4 6 3
5 1 2
8 7 0
```
Heuristic type : 
-m -> Manhattan Distance
-h -> Hamming Distance
-l -> Manhattan Distance with Linear Conflict

Search mode (bonuses) : 
-u -> Uniform-Cost Search (Keep in mind that this one is very slow)
-g -> Greedy Search

## Output :
```
44 Previous steps...
----------
 1  2  3
 4  5  0
 7  8  6
----------
 1  2  3
 4  5  6
 7  8  0
----------
Done in 46 steps.
Total states selected (time complexity): 137
Maximum states in memory (space complexity): 234
```
