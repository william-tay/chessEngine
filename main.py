from chess import Board, Move, STARTING_FEN, polyglot
import chess
import random


evals = 0

piece_values = {
    chess.PAWN: 100,
    chess.ROOK: 500,
    chess.KNIGHT: 320,
    chess.BISHOP: 330,
    chess.QUEEN: 900,
    chess.KING: 20000
}

pawn_black_heat_map = [
    1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000,
    200, 200, 200, 200, 200, 200, 200, 200,
    30, 30, 40, 40, 40, 40, 30, 30,
    30, 30, 40, 60, 60, 40, 30, 30,
    30, 30, 40, 60, 60, 40, 30, 30,
    30, 30, 30, 30, 30, 30, 30, 30,
    20, 20, 20, 20, 20, 20, 20, 20,
    0, 0, 0, 0, 0, 0, 0, 0
]

pawn_white_heat_map = list(reversed(pawn_black_heat_map))

knight_heat_map = [
    -50, -40, -30, -30, -30, -30, -40, -50,
    -40, -20, 0, 0, 0, 0, -20, -40,
    -30, 0, 10, 15, 15, 10, 0, -30,
    -30, 5, 15, 20, 20, 15, 5, -30,
    -30, 0, 15, 20, 20, 15, 0, -30,
    -30, 5, 10, 15, 15, 10, 5, -30,
    -40, -20, 0, 5, 5, 0, -20, -40,
    -50, -40, -30, -30, -30, -30, -40, -50
]

bishop_heat_map = [
    -20, -10, -10, -10, -10, -10, -10, -20,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -10, 0, 5, 10, 10, 5, 0, -10,
    -10, 5, 5, 10, 10, 5, 5, -10,
    -10, 0, 10, 10, 10, 10, 0, -10,
    -10, 10, 10, 10, 10, 10, 10, -10,
    -10, 5, 0, 0, 0, 0, 5, -10,
    -20, -10, -10, -10, -10, -10, -10, -20
]

rook_heat_map = [
    0, 0, 0, 0, 0, 0, 0, 0,
    5, 10, 10, 10, 10, 10, 10, 5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    0, 0, 0, 5, 5, 0, 0, 0
]

king_heat_map = [
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -20, -30, -30, -40, -40, -30, -30, -20,
    -10, -20, -20, -20, -20, -20, -20, -10,
    20, 20, 0, 0, 0, 0, 20, 20,
    20, 30, 10, 0, 0, 10, 30, 20
]

king_endgame_heat_map = [
    -50, -40, -30, -20, -20, -30, -40, -50,
    -30, -20, -10, 0, 0, -10, -20, -30,
    -30, -10, 20, 30, 30, 20, -10, -30,
    -30, -10, 30, 40, 40, 30, -10, -30,
    -30, -10, 30, 40, 40, 30, -10, -30,
    -30, -10, 20, 30, 30, 20, -10, -30,
    -30, -30, 0, 0, 0, 0, -30, -30,
    -50, -30, -30, -30, -30, -30, -30, -50
]

queen_heat_map = [
    -20, -10, -10, -5, -5, -10, -10, -20,
    -10, 0, 5, 0, 0, 0, 0, -10,
    -10, 5, 5, 5, 5, 5, 0, -10,
    0, 0, 5, 5, 5, 5, 0, -5,
    -5, 0, 5, 5, 5, 5, 0, -5,
    -10, 0, 5, 5, 5, 5, 0, -10,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -20, -10, -10, -5, -5, -10, -10, -20
]

# Starting Materials

black_material = 0
white_material = 0
who2move = 0
board = chess.Board(chess.STARTING_FEN)


def main():
    # with chess.polyglot.open_reader("baron30.bin") as reader:
    # for entry in reader.find_all(board):
    # print(entry.move, entry.weight, entry.learn)
    while not board.is_checkmate():
        if board.turn:
            result = eval() * 1
        elif not board.turn:
            result = eval() * -1
        print(board.turn)
        print(result)
        print(f'{board}\n')
        legalMoves = [board.legal_moves]
        playerMove(legalMoves)
        if board.turn:
            result = eval() * 1
        elif not board.turn:
            result = eval() * -1
        print(board.turn)
        print(result)
        computerMove()


def alphaBeta(alpha, beta, leftbranch):
    pass


# print(board.legal_moves)
# print(chess.Move.from_uci("g1f3") in board.legal_moves)
# print(board)
# board.san(chess.Move(chess.E2, chess.E4))
# board.parse_san('Nf3')
# print(board.variation_san([chess.Move.from_uci(m) for m in ["e2e4", "e7e5", "g1f3"]]))
def playerMove(legal):
    print(legal)
    checkMaterial()
    while True:
        try:
            move = input("What is your move: ")
            board.push_san(move)
            break
        except:
            print("illegal move")

def computerMove():
    real = list(board.legal_moves)

    print(real)
    listRand = real

    test = random.choice(listRand)

    test1 = str(test)
    board.push_uci(test1)



def eval():
    global evals
    for squares in chess.SQUARES:
        piece = board.piece_type_at(squares)
        checkPawn = chess.Piece(1, board.turn)
        checkKnight = chess.Piece(2, board.turn)
        checkBishop = chess.Piece(3, board.turn)
        checkRook = chess.Piece(4, board.turn)
        checkQueen = chess.Piece(5, board.turn)
        checkKing = chess.Piece(6, board.turn)
        check = chess.Piece(piece, board.color_at(squares))

        print(squares)
        print(board.piece_type_at(squares))

        if checkPawn.color and checkPawn.piece_type == check.piece_type:
            print(f'This is squaresPawn: {squares} {board.piece_type_at(squares)}')
            evals = evals + pawn_white_heat_map[squares]
            print(pawn_white_heat_map[squares])
        elif not checkPawn.color and checkPawn.piece_type == check.piece_type:
            print(f'This is squaresPawn: {squares} {board.piece_type_at(squares)}')
            evals = evals + pawn_black_heat_map[squares]
        elif checkKnight.color == check.color and checkKnight.piece_type == check.piece_type:
            print(f'This is squaresKnight: {squares} {board.piece_type_at(squares)}')
            evals = evals + knight_heat_map[squares]
            print(knight_heat_map[squares])
        elif checkBishop.color == check.color and checkBishop.piece_type == check.piece_type:
            print(f'This is squaresBishop: {squares} {board.piece_type_at(squares)}')
            evals = evals + bishop_heat_map[squares]
            print(bishop_heat_map[squares])
        elif checkRook.color == check.color and checkRook.piece_type == check.piece_type:
            print(f'This is squaresRook: {squares} {board.piece_type_at(squares)}')
            evals = evals + rook_heat_map[squares]
            print(rook_heat_map[squares])
        elif checkQueen.color == check.color and checkQueen.piece_type == check.piece_type:
            print(f'This is squaresQueen: {squares} {board.piece_type_at(squares)}')
            evals = evals + queen_heat_map[squares]
            print(queen_heat_map[squares])
        elif checkKing.color == check.color and checkKing.piece_type == check.piece_type:
            print(f'This is squaresKing: {squares} {board.piece_type_at(squares)}')
            evals = evals + king_heat_map[squares]
            print(king_heat_map[squares])
       # if checkKing.color == check.color and checkPawn.piece_type == check.piece_type:
           # print(f'This is squaresKingLate: {squares} {board.piece_type_at(squares)}')
           # evals = evals + king_endgame_heat_map[squares]

    print(f'This is {evals}')
    return evals






def checkMaterial():
    global white_material
    global black_material
    white_material = 0
    black_material = 0
    for squares in chess.SQUARES:
        if board.piece_at(chess.D4):
            continue
        piece = board.piece_at(squares)
        if not piece:
            continue
        if piece.color == chess.WHITE:
            white_material += piece_values[piece.piece_type]
        elif piece.color == chess.BLACK:
            black_material += piece_values[piece.piece_type]
    print(white_material)
    print(black_material)


if __name__ == "__main__":
    main()
