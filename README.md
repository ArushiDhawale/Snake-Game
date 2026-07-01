# Classic Snake Game

A sleek, retro-inspired Snake Game built using **Python** and the **Turtle** graphics library. This project demonstrates fundamental programming concepts such as object-oriented design, collision detection, and game state management.

---

## Features

* **Smooth Controls:** Responsive arrow key movements.
* **Dynamic Scoring:** Keeps track of your current score and updates your **High Score** persistently.
* **Clean UI:** Simple, retro scoreboard and a classic dark-mode game board.
* **Increasing Difficulty:** (Optional, if implemented) The snake speeds up as it eats more food.

---

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **Graphics Library:** Turtle (Built-in Python module)

---

## 📦 Installation & Setup

Follow these steps to get the game running on your local machine.

### Prerequisites

Make sure you have Python installed. You can check by running:

```bash
python --version

```

### 1. Clone the Repository

```bash
git clone https://github.com/ArushiDhawale/Snake-Game.git
cd Snake-Game

```

### 2. Run the Game

Since the project relies entirely on Python's built-in `turtle` and `time` modules, there are **no external dependencies** to install! Just run the main script:

```bash
python main.py

```

*(Note: If your entry file is named differently, e.g., `snake.py`, replace `main.py` with that filename).*

---

## 🎮 How to Play

* **Up Arrow:** Move Up
* **Down Arrow:** Move Down
* **Left Arrow:** Move Left
* **Right Arrow:** Move Right

### Rules:

1. Eat the **food** (represented by a colored circle/square) to grow longer and increase your score.
2. Avoid hitting the **walls**.
3. Avoid biting your own **tail**.
4. If you crash, the game resets, and your highest score is saved!

---

## 📂 Project Structure

```text
├── main.py          # The entry point of the game (sets up the screen and game loop)
├── snake.py         # Contains the Snake class (handles movement and segment creation)
├── food.py          # Contains the Food class (handles random spawning of food)
├── scoreboard.py    # Contains the Scoreboard class (tracks score, high score, and game over)
└── README.md        # Project documentation

```

---
