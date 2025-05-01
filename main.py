#!/usr/bin/env python3

import serial
import pygame
from pygame import transform
import numpy as np
import threading
import random


def clip(surface, x, y, x_size, y_size):  #Get a part of the image
    handle_surface = surface.copy()  #Sprite that will get process later
    clipRect = pygame.Rect(x, y, x_size, y_size)  #Part of the image
    handle_surface.set_clip(clipRect)  #Clip or you can call cropped
    image = surface.subsurface(handle_surface.get_clip())  #Get subsurface
    return image.copy()  #Return


# yapf: disable

NONE = 0

BLACK   = 1 << 0
WHITE   = 1 << 1

PAWN    = 1 << 2
BISHOP  = 1 << 3
KNIGHT  = 1 << 4
ROOK    = 1 << 5
KING    = 1 << 6
QUEEN   = 1 << 7

board = [
    WHITE | ROOK, WHITE | KNIGHT, WHITE | BISHOP, WHITE | QUEEN, WHITE | KING, WHITE | BISHOP, WHITE | KNIGHT, WHITE | ROOK,
    WHITE | PAWN, WHITE | PAWN, WHITE | PAWN, WHITE | PAWN, WHITE | PAWN, WHITE | PAWN, WHITE | PAWN, WHITE | PAWN,
    NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE,
    NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE,
    NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE,
    NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE,
    BLACK | PAWN, BLACK | PAWN,   BLACK | PAWN, BLACK | PAWN, BLACK | PAWN, BLACK | PAWN, BLACK | PAWN, BLACK | PAWN,
    BLACK | ROOK, BLACK | KNIGHT, BLACK | BISHOP, BLACK | QUEEN, BLACK | KING, BLACK | BISHOP, BLACK | KNIGHT, BLACK | ROOK,
];


# yapf: enable

ser = serial.Serial(port="/dev/ttyUSB0", baudrate=9600)


def serial_comms():
    global board
    prev_board_data = np.array([[0] * 8] * 8)
    place = False
    row, col = 0, 0
    from_row, from_col = 0, 0
    p = None

    while ser.isOpen():
        board_data = []
        data_bytes = ser.readline()
        data = None
        try:
            data = data_bytes.decode('utf-8')
        except:
            pass

        if data:
            board_data = []
            for i in range(0, 64, 8):
                board_data.append(
                    [int(i) for i in data[i:i + 8] if i.isdigit()])

            if all(len(row) == 8 for row in board_data):
                board_data = np.array(board_data)

                if board_data.shape == prev_board_data.shape:
                    if (prev_board_data != board_data).any():
                        found = False
                        for j in range(0, 8):
                            for k in range(0, 8):
                                if prev_board_data[j][k] == board_data[j][k]:
                                    continue
                                else:
                                    found = True
                                    if prev_board_data[j][k] == 1:
                                        p = board[j * 8 + k]
                                        board[j * 8 + k] = NONE
                                        from_row = j
                                        from_col = k
                                    elif prev_board_data[j][k] == 0:
                                        row = j
                                        col = k
                                        place = True
                                    break
                            if found:
                                break

                        prev_board_data = board_data

        if place:
            if p:
                board[row * 8 + col] = p
            place = False


if __name__ == "__main__":
    t1 = threading.Thread(target=serial_comms, args=())
    t1.start()

    pygame.init()
    screen = pygame.display.set_mode((800, 800))

    running = True

    while running:
        screen.fill((0, 0, 0))
        pieces_img = pygame.image.load("pieces.svg")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        for i in range(0, 8):
            for j in range(0, 8):
                if (i + j) % 2 == 0:
                    pygame.draw.rect(
                        screen, (200, 100, 100),
                        pygame.Rect((j * 100, i * 100), (100, 100)))
                else:
                    pygame.draw.rect(
                        screen, (150, 50, 50),
                        pygame.Rect((j * 100, i * 100), (100, 100)))

        for i in range(0, 8):
            for j in range(0, 8):
                piece = board[i * 8 + j]

                if piece == NONE:
                    continue
                else:
                    cx, cy, cw, ch = 0, 0, 540, 540
                    if piece & BLACK == 1:
                        cy = 540

                    if piece & (KING) != 0:
                        cx = 0 * 540
                    elif piece & (QUEEN) != 0:
                        cx = 1 * 540
                    elif piece & (BISHOP) != 0:
                        cx = 2 * 540
                    elif piece & (KNIGHT) != 0:
                        cx = 3 * 540
                    elif piece & (ROOK) != 0:
                        cx = 4 * 540
                    elif piece & (PAWN) != 0:
                        cx = 5 * 540

                    screen.blit(
                        transform.scale(clip(pieces_img, cx, cy, cw, ch),
                                        (100, 100)), (j * 100, i * 100))

        pygame.display.flip()

pygame.quit()

# print(board_data)
