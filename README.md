# Conway's Game of Life

This project implements Conway's Game of Life using Python and Pygame. The simulation supports user interaction, pattern saving/loading, and customizable board size and speed via command-line arguments.

## Features

- Interactive grid with mouse and keyboard control
- Toggle play/pause, step forward, randomize, clear, save/load pattern
- Display of generation count, live cells, and FPS
- Uses Pygame for graphical interface
- Pattern persistence via `patterns.txt`

## How to Run

```bash
python life.py --width 60 --height 30 --fps 10
```

Optional arguments:
- `--width` : number of cells horizontally (default: 60)
- `--height` : number of cells vertically (default: 30)
- `--fps` : simulation speed in frames per second (default: 10)

## Controls

- `Space` : Play / Pause
- `N` : Advance one generation
- `R` : Randomize board
- `C` : Clear board
- `S` : Save pattern to `patterns.txt`
- `L` : Load pattern from `patterns.txt`
- `Q` : Quit

Click on cells to toggle them on/off.

## Testing

To run the test cases:

```bash
pytest -q
```

All tests must pass (you should see green output). Test cases include classic patterns like **blinker** and **glider** to validate behavior.

## Demo Video

- Shows simulation controls, loading/saving pattern, and custom pattern creation
- Demonstrates correct behavior and error handling
- Discusses:
  - Use of a 2D list to represent the board
  - Toroidal wrapping for neighbor calculation
  - Modular structure and file I/O for pattern saving
  - Challenges with real-time Pygame rendering
  - Coolest extension: pattern save/load + status bar display


## GitHub Repository

https://github.com/saketjndl/Conway-s-game-of-life-Project---1

## Sample Files

- `patterns.txt` – Used for saving/loading live cell coordinates

## Author

NAME: SAKET JINDAL  
STUDENT_ID: IITMCS_24093071  
DATE: 17/05/2025
