# 8-PuzzleSolver
AI 8-Puzzle Solver

## Simple README for the 8-Puzzle Solver Code

### Purpose:
This script solves the classic 8-Puzzle game, where the player has to move tiles in a 3x3 board to achieve a target configuration. The user provides the initial state of the puzzle, and the script determines whether it's solvable and, if so, provides the solution.

### Description:

1. **Import Libraries**: 
   - Functions from `simpleai.search` to implement the A* search algorithm.
   - `re` (regular expressions) for pattern matching to validate user input.

2. **Input Validation**:
   - The `validate_input` function ensures the user provides correctly formatted puzzle rows using regular expressions.

3. **Get User Input**:
   - The user is prompted to input the initial state of the 8-Puzzle, row by row, using 'e' to represent the empty space.

4. **Utility Functions**:
   - `convert_list_to_str` and `convert_str_to_list` are helper functions that convert between the puzzle's string representation and a list of lists format.
   - `locate` function finds the position of a specific tile in the puzzle.

5. **Puzzle Logic**: The `PuzzleProblem` class defines:
   - `actions`: Lists the possible tiles that can be moved into the empty space.
   - `result`: Returns the state resulting from moving a specific tile.
   - `is_goal`: Checks if the current state matches the goal state.
   - `cost`: Defines the cost of making a move (constant in this case).
   - `heuristic`: Estimates the "distance" from the current state to the goal state, based on tile positions.

6. **Solvability Check**: 
   - The `is_solvable` function determines if the given puzzle state can be solved. This is a mathematical property of permutation inversions in the 8-Puzzle. The script checks this to avoid attempting to solve unsolvable configurations.

7. **Solve the Puzzle**:
   - If the puzzle is solvable, the A* search algorithm (`astar`) is used to find the solution.
   - The solution steps are printed, showing each move that leads to the goal state.

### How to Use:
1. Run the script.
2. When prompted, enter the three rows of your 8-Puzzle state one by one, using 'e' for the empty tile and dashes as separators.
3. The script will notify you if your puzzle is unsolvable. If solvable, it will display the steps to solve the puzzle.
