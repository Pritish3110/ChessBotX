An embedded + Python project that syncs a physical chessboard with a virtual board in real time using ESP32, electromagnets, and Pygame.
Overview

    Hardware: ESP32 scans an 8x8 matrix with sensors/electromagnets to detect piece presence.

    Software: Python + Pygame GUI renders the board, updates piece positions via serial data.

Tech Stack

    ESP32 (C++)

    Python 3 + PySerial + NumPy

    Pygame (for GUI)

Features

    Real-time board state sync

    Visual GUI with chess pieces

    Detects pick-up and drop positions

    Modular, easy to expand

How It Works

    ESP32 scans the chessboard grid and detects presence using GPIO.

    Converts the 8x8 board to a 64-bit matrix and sends via serial.

    Python reads matrix, detects movement, updates the GUI.


Structure:

    /hardware      → ESP32 firmware (Arduino)
    /software      → Python GUI + assets
    README.md      → This file


Setup:

    Flash ESP32 using Arduino IDE.
    Connect ESP32 via USB.
    Run GUI:

    pip install pygame pyserial numpy
    python3 virtual_chess.py


Future Ideas:

    AI integration (e.g., Stockfish)
    Move logging & highlighting
