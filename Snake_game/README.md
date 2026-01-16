# 🐍 Python Snake Game

A classic arcade Snake game implementation using Python's Turtle graphics library. This project features Object-Oriented Programming (OOP) principles and a persistent high-score system.

## 📂 Project Structure

* **`main.py`**: The entry point of the game. It controls the game loop, screen setup, and event listeners.
* **`snake.py`**: Contains the `Snake` class, managing the snake's body segments, movement, and direction.
* **`food.py`**: Contains the `Food` class, which handles rendering food at random coordinates on the screen.
* **`scoreboard.py`**: Contains the `Scoreboard` class. It handles writing the score to the screen and reading/saving the high score to `data.txt`.
* **`data.txt`**: A simple text file that stores the all-time highest score.

## 🚀 How to Run

1.  Ensure you have Python installed.
2.  Navigate to the project directory in your terminal/command prompt.
3.  Run the game using:

```bash
python main.py
