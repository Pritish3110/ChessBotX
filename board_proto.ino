#include <array>

constexpr uint32_t board_width_v{ 8 };
constexpr uint32_t board_height_v{ 8 };

constexpr std::array<int, board_height_v> row_pins{ 13, 12, 14, 27, 26, 25, 33, 32 };
constexpr std::array<int, board_width_v> column_pins{ 23, 22, 21, 19, 18, 4, 2, 15 };

using Board = std::array<std::array<bool, board_width_v>, board_height_v>;
Board board{};

void update_board(Board &board) {
  for (int i{}; i < board_width_v; ++i) {
    for (int j{}; j < board_height_v; ++j) {
      for (int k{}; k < board_height_v; ++k) {
        if (k == j) {
          digitalWrite(row_pins.at(k), HIGH);
        } else {
          digitalWrite(row_pins.at(k), LOW);
        }
      }

      int new_state = digitalRead(column_pins.at(i));

      if (new_state == 1) {
        board.at(j).at(i) = 1;
      }
    }
  }
}

void setup() {
  static_assert(column_pins.size() == board_width_v);
  static_assert(row_pins.size() == board_height_v);

  Serial.begin(9600);

  for (int i{}; i < board_height_v; ++i) {
    pinMode(row_pins.at(i), OUTPUT);
  }

  for (int i{}; i < board_width_v; ++i) {
    pinMode(column_pins.at(i), INPUT_PULLDOWN);
  }
}

void loop() {
  for (int i{}; i < board_height_v; ++i) {
    for (int j{}; j < board_width_v; ++j) {
      board.at(i).at(j) = 0;
    }
  }

  for (int i{}; i < board_height_v; ++i) {
    digitalWrite(row_pins.at(i), OUTPUT);
  }

  update_board(board);

  for (int i{}; i < board_height_v; ++i) {
    for (int j{}; j < board_width_v; ++j) {
      Serial.print(board.at(i).at(j));
    }
  }
  Serial.println();
}