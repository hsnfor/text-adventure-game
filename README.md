# The Python Labyrinth

A classic text-based adventure game built in Python as a beginner project to learn core programming concepts.

## How to Play
1.  Navigate between rooms using commands like `go north`, `go south`, etc.
2.  Collect items with `get [item]`.
3.  Use items to solve puzzles and progress.
4.  Your goal is to escape to the Garden!

## Game Commands
*   `go [direction]`
*   `get [item]`
*   `inventory`
*   `look`

## What This Project Demonstrates
This was my first project to apply the fundamentals of Python:
*   **Data Structures:** Using dictionaries to model the game world and lists to track inventory.
*   **Control Flow:** Using `if/elif/else` statements to handle all possible player commands.
*   **Functions:** Breaking down the game logic into reusable functions like `move_player()` and `show_status()`.
*   **Input/Output:** Taking user input and providing text output to create an interactive experience.

## How to Run
1.  Make sure you have Python 3 installed.
2.  Clone this repository.
3.  Navigate to the `src` directory in your terminal.
4.  Run the game: `python game.py`

## Future Improvements
*   Add more rooms and a more complex story.
*   Implement a ‘health’ points system with challenges.
*   Add a simple combat system using random numbers.
*   Load the room data from a separate JSON file instead of hard-coding it.
