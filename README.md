# ♟️ ChessBotX - Physical to Virtual Sync

An embedded hardware + Python project that syncs a physical chessboard with a virtual board in real time using **ESP32**, **electromagnets**, and **Pygame**.

---

## 🎯 Overview

**Hardware:** ESP32 scans an 8x8 matrix with sensors/electromagnets to detect piece presence.  
**Software:** Python + Pygame GUI renders the board and updates piece positions via serial data.

---

## 🛠️ Tech Stack

### 🔌 Hardware Components

- **ESP32 (C++)** – Main microcontroller  
- **Acrylic Sheet** – Board base and structure  
- **4148 Diodes** – Signal protection and isolation  
- **Motion Sensors** – PIR/ultrasonic sensors for piece detection  
- **Electromagnets** – Piece positioning feedback  
- **GPIO Matrix** – 8x8 sensor array  

### 💻 Software Stack

- **Python 3** + **PySerial** + **NumPy**  
- **Pygame** – For GUI  
- **Arduino IDE** – For ESP32 programming  

---

## ✨ Features

- 🎮 Real-time board state sync  
- 🎨 Visual GUI with chess pieces  
- 🔍 Detects pick-up and drop positions  
- 🏗️ Modular, easy to expand  

---

## 📁 Project Structure

ChessBotX/

├── hardware/
│   └── chessboard_scanner.ino     # ESP32 code for board scanning
├── software/
│   ├── virtual_chess.py           # Main GUI application
│   └── chess_simulator.py         # Chess game simulator
├── requirements.txt
├── LICENSE
└── README.md


---

## 🔧 Hardware Setup

1. Flash ESP32 using Arduino IDE with  
   `hardware/chessboard_scanner.ino`
2. Connect ESP32 via USB

---

## 💻 Software Setup

```bash
# Clone repository
git clone https://github.com/Pritish3110/ChessBotX.git
cd ChessBotX

# Install dependencies
pip install pygame pyserial numpy

# Run main application
python3 software/virtual_chess.py

# Or run chess simulator (software only)
python3 software/chess_simulator.py
```
## 🔮 Future Ideas

🤖 AI integration (e.g., Stockfish)

📝 Move logging & highlighting

🌐 Online multiplayer support

🎵 Audio feedback for moves

## 🤝 Contributing

Contributions are welcome! Feel free to:

🐛 Report bugs

💡 Suggest features

🔧 Submit pull requests


## 🆘 Troubleshooting

### Common Issues

🔌 ESP32 not detected → Check USB connection & drivers

📡 Serial timeout → Verify baud rate (115200)

🎯 Detection issues → Run calibration wizard


## 📄 License


This project is open source and available under the MIT License.


<div align="center">

🎉 Thank you for checking out ChessBotX! 🎉

## Made with ♟️ by Pritish Bhatasana


## 📬 Connect with me:

GitHub: @Pritish3110

LinkedIn: Pritish Bhatasana

Email: pritishbhatasana68@gmail.com
