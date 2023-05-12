import chess


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

king_black_heat_map = [
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -20, -30, -30, -40, -40, -30, -30, -20,
    -10, -20, -20, -20, -20, -20, -20, -10,
    20, 20, 0, 0, 0, 0, 20, 20,
    20, 30, 10, 0, 0, 10, 30, 20
]

king_white_heat_map = list(reversed(king_black_heat_map))

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
best = 0
after_move = 0

def main():
    global level
    while True:
        try:
            difficulty = input("What difficulty would you like? (Hard / Easy ): ").lower().strip()
            if difficulty == "hard":
                print("Hard Selected!")
                level = 5
                break
            elif difficulty == "easy":
                print("Easy Selected!")
                level = 3
                break
            else:
                print("Not a valid option")
        except:
            print("Error")
    while not board.is_checkmate():
        if board.turn:
            result = evaluate(board, board.turn)

        else:
            result = evaluate(board.turn)

        legalMoves = [board.legal_moves]
        playerMove(legalMoves)
        if board.is_game_over():
            print("Good Game!")
            break
        print(f'{board}\n')
        if board.turn:
            result = evaluate(board, board.turn)

        else:
            result = evaluate(board, board.turn)

        computerMove()
        print(f'{board}\n')


def alphaBeta(board, depth, alpha, beta, maximizingPlayer):
    if depth == 0 or board.is_game_over():
        return evaluate(board, not board.turn), None

    if maximizingPlayer:
        maxEval = float('-inf')
        bestMove = None
        for move in board.legal_moves:
            board.push(move)
            eval, _ = alphaBeta(board, depth-1, alpha, beta, False)
            board.pop()
            if eval > maxEval:
                maxEval = eval
                bestMove = move
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return maxEval, bestMove
    else:
        minEval = float('inf')
        bestMove = None
        for move in board.legal_moves:
            board.push(move)
            eval, _ = alphaBeta(board, depth-1, alpha, beta, True)
            board.pop()
            if eval < minEval:
                minEval = eval
                bestMove = move
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return minEval, bestMove



def playerMove(legal):
    print(f'Some possible moves for you: {legal}')
    checkMaterial()
    while True:
        try:
            move = input("What is your move: ")
            board.push_san(move)
            break
        except:
            print("illegal move")


def computerMove():
    print('Thinking...')
    print('===========================')

    best_score, best_move = alphaBeta(board, level, float('-inf'), float('inf'), True)
    print(board.turn)
    board.push(best_move)

    print(best_move)

def evaluate(board, color):
    evals = 0
    for squares in chess.SQUARES:
        piece = board.piece_type_at(squares)
        checkPawn = chess.Piece(1, color)
        checkKnight = chess.Piece(2, color)
        checkBishop = chess.Piece(3, color)
        checkRook = chess.Piece(4, color)
        checkQueen = chess.Piece(5, color)
        checkKing = chess.Piece(6, color)
        check = chess.Piece(piece, board.color_at(squares))

        if checkPawn.color and check.color and checkPawn.piece_type == check.piece_type:
            evals = evals + pawn_white_heat_map[squares]
        elif not checkPawn.color and not check.color and checkPawn.piece_type == check.piece_type:
            evals = evals + pawn_black_heat_map[squares]

        if checkKing.color and check.color and checkKing.piece_type == check.piece_type:
            evals = evals + king_white_heat_map[squares]
        elif not checkKing.color and not check.color and checkKing.piece_type == check.piece_type:
            evals = evals + king_black_heat_map[squares]

        if checkKnight.color == check.color and checkKnight.piece_type == check.piece_type:
            evals = evals + knight_heat_map[squares]

        if checkBishop.color == check.color and checkBishop.piece_type == check.piece_type:
            evals = evals + bishop_heat_map[squares]

        if checkRook.color == check.color and checkRook.piece_type == check.piece_type:
            evals = evals + rook_heat_map[squares]

        if checkQueen.color == check.color and checkQueen.piece_type == check.piece_type:
            evals = evals + queen_heat_map[squares]
    # if checkKing.color == check.color and checkPawn.piece_type == check.piece_type:
    # print(f'This is squaresKingLate: {squares} {board.piece_type_at(squares)}')
    # evals = evals + king_endgame_heat_map[squares]
    material = checkMaterial()
    evals = evals + material
   # attacking(board, board.turn)
    # print("---------------------------------------------------------------------------")
    if color:
        return evals
    else:
        return evals * -1

#def attacking(board, turn):
   # starting_material = checkMaterial()
   # if turn:

   # else:
       # board.attacks()


def checkMaterial():
    global white_material, black_material, amount_attacked, attackers
    white_material = 0
    black_material = 0
    for squares in chess.SQUARES:
        piece = board.piece_at(squares)
        #amount_attacked = board.attacks(squares)
       # attackers = board.attackers(board.turn, squares)
        if not piece:
            continue
        if piece.color == chess.WHITE:

            white_material += piece_values[piece.piece_type]
        elif piece.color == chess.BLACK:
            black_material += piece_values[piece.piece_type]
  #  print(f'Attacked:\n{amount_attacked} \n Attackers: \n{attackers}')
    if board.turn:
        return white_material
    else:
        return black_material


if __name__ == "__main__":
    main()
