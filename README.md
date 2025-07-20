Smart Chessboard - Physical to Virtual Sync


An embedded hardware + Python project that creates a smart chessboard system, syncing a physical board with a virtual interface in real-time using ESP32 microcontrollers, electromagnetic sensors, and a Python GUI.


🎯 Overview


This project bridges the gap between traditional chess and digital gaming by creating a smart chessboard that automatically detects piece movements and mirrors them on a virtual board display.


Hardware: ESP32 microcontroller scans an 8×8 sensor matrix to detect chess piece presence and positioning using GPIO pins and electromagnetic detection.


Software: Python application with Pygame creates an intuitive GUI that renders the chess board, processes piece movements, and updates positions based on real-time serial communication from the hardware.


🛠️ Tech Stack


ESP32 (C++ with Arduino IDE)
Python 3 + PySerial + NumPy
Pygame (GUI framework)
Serial Communication (USB connection)


✨ Features


Real-time synchronization between physical and virtual boards
Interactive GUI with visual chess piece representation
Movement detection - automatically detects piece pick-up and drop positions
Modular architecture - easy to extend and customize
Low latency communication via serial interface


🔧 How It Works


Detection: ESP32 continuously scans the 8×8 chessboard grid using GPIO pins to detect piece presence through electromagnetic sensors
Processing: The microcontroller converts the board state into a 64-bit binary matrix representing occupied/vacant squares
Communication: Board data is transmitted to the computer via USB serial connection
Visualization: Python application reads the matrix data, detects piece movements, and updates the GUI in real-time


📁 Project Structure


smart-chessboard/
├── hardware/          # ESP32 firmware and Arduino code
│   ├── chessboard.ino  # Main ESP32 sketch
│   └── config.h        # Hardware configuration
├── software/           # Python application and assets
│   ├── virtual_chess.py    # Main GUI application
│   ├── chess_pieces/       # Chess piece sprites/assets
│   └── utils/             # Helper modules
├── docs/              # Documentation and schematics
├── README.md          # This file
└── requirements.txt   # Python dependencies



🚀 Setup Instructions


Prerequisites


Arduino IDE with ESP32 board support
Python 3.7+
ESP32 development board
USB cable for ESP32 connection


Hardware Setup




Flash the ESP32 firmware using Arduino IDE:


# Open hardware/chessboard.ino in Arduino IDE
# Select your ESP32 board and COM port
# Click Upload





Connect the ESP32 to your computer via USB




Software Setup




Install Python dependencies:


pip install pygame pyserial numpy





Run the virtual chess application:


python3 software/virtual_chess.py





The application will automatically detect the ESP32 serial connection and begin syncing




🎮 Usage


Power on the ESP32 and ensure it's connected via USB
Launch the Python GUI application
Place chess pieces on the physical board - they'll appear on the virtual display
Move pieces physically - watch them update on screen in real-time
The system automatically detects piece pickups and placements


🔮 Future Enhancements


AI Integration: Connect with chess engines like Stockfish for computer opponents
Move Validation: Implement chess rule checking and legal move validation
Game Logging: Record complete games with move history and timestamps
Move Highlighting: Visual indicators for possible moves and captures
Multi-player Support: Network connectivity for remote chess games
Voice Commands: Audio interface for hands-free operation


🤝 Contributing


Contributions are welcome! Please feel free to submit pull requests, report bugs, or suggest new features.


📄 License


This project is open source and available under the MIT License.


🔗 Links


Hardware Documentation: See /docs folder for circuit diagrams and assembly instructions
API Reference: Check /software/docs for detailed code documentation



Made with ♟️ by [Pritish Bhatasana]
