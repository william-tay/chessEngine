from chess import Board, Move, STARTING_FEN, polyglot
import chess

board = chess.Board(chess.STARTING_FEN)

def main():




    with chess.polyglot.open_reader("baron30.bin") as reader:
        for entry in reader.find_all(board):
            print(entry.move, entry.weight, entry.learn)

    while not board.is_checkmate():
        print(board)
        legalMoves = [board.legal_moves]
        playerMove(legalMoves)



# print(board.legal_moves)

# print(chess.Move.from_uci("g1f3") in board.legal_moves)
# print(board)
# board.san(chess.Move(chess.E2, chess.E4))
# board.parse_san('Nf3')
# print(board.variation_san([chess.Move.from_uci(m) for m in ["e2e4", "e7e5", "g1f3"]]))




def playerMove(legal):
    print(legal)
    while True:
        try:
            move = input("What is your move: ")
            board.push_san(move)
            break
        except:
            print("illegal move")

def computerMove():
    pass


if __name__ == "__main__":
    main()