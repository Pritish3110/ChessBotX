♟️ Smart Chessboard - Physical to Virtual Sync










An embedded hardware + Python project that syncs a physical chessboard with a virtual board in real time using ESP32, electromagnets, and Pygame.





🎯 Overview


Hardware: ESP32 scans an 8x8 matrix with sensors/electromagnets to detect piece presence.


Software: Python + Pygame GUI renders the board, updates piece positions via serial data.



🛠️ Tech Stack

<table>
<tr>
<td align="center"><b>🔧 Hardware</b></td>
<td align="center"><b>💻 Software</b></td>
</tr>
<tr>
<td>ESP32 (C++)</td>
<td>Python 3 + PySerial + NumPy</td>
</tr>
<tr>
<td>Arduino IDE</td>
<td>Pygame (for GUI)</td>
</tr>
</table>


✨ Features


🎮 Real-time board state sync
🎨 Visual GUI with chess pieces
🔍 Detects pick-up and drop positions
🏗️ Modular, easy to expand



🔧 How It Works


ESP32 scans the chessboard grid and detects presence using GPIO
Converts the 8x8 board to a 64-bit matrix and sends via serial
Python reads matrix, detects movement, updates the GUI



📁 Project Structure


smart-chessboard/
├── 🔧 hardware/          # ESP32 firmware (Arduino)
│   ├── chessboard.ino    # Main ESP32 sketch
│   └── config.h          # Hardware configuration
├── 💻 software/          # Python GUI + assets
│   ├── virtual_chess.py  # Main GUI application
│   └── assets/           # Chess piece sprites
├── 📚 docs/              # Documentation
├── README.md             # This file
└── requirements.txt      # Python dependencies




🚀 Setup


Hardware Setup


Flash ESP32 using Arduino IDE
Connect ESP32 via USB


Software Setup


# Install dependencies
pip install pygame pyserial numpy

# Run GUI
python3 software/virtual_chess.py




🔮 Future Ideas


🤖 AI integration (e.g., Stockfish)
📝 Move logging & highlighting
🌐 Online multiplayer support
🎵 Audio feedback for moves



🤝 Contributing


Contributions are welcome! Feel free to:


🐛 Report bugs
💡 Suggest features
🔧 Submit pull requests



🆘 Troubleshooting


Common Issues


🔌 ESP32 not detected → Check USB connection & drivers
📡 Serial timeout → Verify baud rate (115200)  
🎯 Detection issues → Run calibration wizard




📄 License


This project is open source and available under the MIT License.


<div align="center">

🎉 Thank you for checking out Smart Chessboard! 🎉


Made with ♟️ by Pritish Bhatasana







Connect with me:

Email: pritishbhatasana68@gmail.com
LinkedIn: www.linkedin.com/in/pritish3110

</div>
