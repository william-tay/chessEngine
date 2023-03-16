import random

from chess import Board, Move, STARTING_FEN, polyglot
import chess

board = chess.Board(chess.STARTING_FEN)

print(board)

with chess.polyglot.open_reader("baron30.bin") as reader:
    for entry in reader.find_all(board):
        print(entry.move, entry.weight, entry.learn)

board.push_san("Nh3")

print(board)

real = list(board.legal_moves)

print(real)
listRand = real

print(listRand)
test = random.choice(listRand)
test1 = str(test)
print(type(test1))

print(board)
#board.push_uci(test)
board.push_uci(test1)
print(board)
print(f'Hey this is a {test1}')
