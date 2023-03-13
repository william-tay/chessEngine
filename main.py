from chess import Board, Move, STARTING_FEN, polyglot
import chess

board = chess.Board(chess.STARTING_FEN)

print(board)

with chess.polyglot.open_reader("baron30.bin") as reader:
    for entry in reader.find_all(board):
        print(entry.move, entry.weight, entry.learn)


print(board.legal_moves)

print(chess.Move.from_uci("g1f3") in board.legal_moves)
print(board)
board.san(chess.Move(chess.E2, chess.E4))
board.parse_san('Nf3')
print(board.variation_san([chess.Move.from_uci(m) for m in ["e2e4", "e7e5", "g1f3"]]))