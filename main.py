import sys

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

        
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

    puzzle_input = sys.argv[1]
    # Process the puzzle_input and implement the N-Puzzle solver logic here

if __name__ == "__main__" :
    main()