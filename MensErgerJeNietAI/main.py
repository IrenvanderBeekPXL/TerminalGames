# line 81 to change the ai priorities
from secrets import randbelow
def dice():
    return randbelow(6) + 1

def max_index(numberlist):
    max_element = 0
    for i in range(len(numberlist)):
        if numberlist[max_element] < numberlist[i]:
            max_element = i
    return max_element

def count_items(list, item):
    index = -1
    number = 0
    try:
        while True:
            index = list.index(item, index + 1)
            number += 1
    except:
        return number

def print_board(board, need_to_start):
    print("   ", end=" ")
    for i in need_to_start:
        print(i, end="  ")
        for j in range(int(len(board) / len(need_to_start)-1)):
            print("  ", end=" ")
    print("", end="\n ")
    for i in board:
        print(i, end="  ")
    print()

def move(player, pawn, needs_to_start, board, moves_to_move):
    # Make a system to get the correct pawn, and move it moves_to_move places towards index -inf
    # Also store the last number in the variable last_number. You can use print_board for debugging
    # If moves_to_move is 6, you should get a new pawn on the board
    # the place to let it start is player * 10 - 8
    def moving(moves_to_move, player, pawn, board):
        for i in range(pawn + 1):
            try:
                pawn_index = board.index(player, pawn_index + 1)
            except:
                if player in board:
                    pawn_index = 0
                else:
                    break
        try:
            last_number = board[pawn_index - moves_to_move]
            if not ((pawn_index - moves_to_move <= player * 10 + 2) and (pawn_index > player * 10 + 2)):
                board[pawn_index - moves_to_move] = player
            board[pawn_index] = "."
            if (pawn_index - moves_to_move < player * 10 + 2):
                last_number = "."
        except:
            last_number = "."
        return last_number

    if moves_to_move == 6 and needs_to_start[player] != 0:
        needs_to_start[player] -= 1
        last_number = board[player * 10 + 2]
        board[player * 10 + 2] = player
    else:
        last_number = moving(moves_to_move, player, pawn, board)

    if last_number != ".":
        needs_to_start[last_number] += 1

def get_winner(board, needs_to_start):
    for i in range(4):
        if needs_to_start[i] == 0 and not i in board:
            return i
    return -1

def aimove(board, moves_to_move, needs_to_start, player):
    def ai(board, moves_to_move, needs_to_start, player):
        pawn_score = [0, 0, 0, 0]
        enemies = [0, 1, 2, 3]
        enemies.pop(player)
        # change these numbers to make it more or less intelligent
        priority = {"attacked": 2,
                    "can_chapture": 10,
                    "can_get_home": 5,
                    "can_get_home_and_attacked": 1,
                    "can_chapture_one_that_can_get_home": 3,
                    "can_chapture_one_that_attackes": 1,
                    "can_chapture_player_that_has_few_pawns": 2
                    }
        if moves_to_move == 6:
            return 1
        for i in range(count_items(board, player)):
            for j in range(i + 2):
                try:
                    pawn_index = board.index(player, pawn_index + 1)
                except:
                    if player in board:
                        pawn_index = 0
                    else:
                        break
            pawn_score[i] = 1
            if board[pawn_index - moves_to_move] in enemies:
                pawn_score[i] += priority.get("can_chapture")
                player_can_chapture = board[pawn_index - moves_to_move]
                if count_items(board, player_can_chapture) + needs_to_start[player] <= 2:
                    pawn_score[i] += priority.get("can_chapture_player_that_has_few_pawns")
                if player in board[(pawn_index - moves_to_move):(pawn_index - moves_to_move-6)]:
                    pawn_score[i] += priority.get("can_chapture_one_that_attackes")
            for j in enemies:
                if j in board[(pawn_index - len(board)):(pawn_index - len(board) + 6)]:
                    pawn_score[i] += priority.get("attacked")
                    if pawn_index - moves_to_move <= player * 10 + 2:
                        pawn_score[i] += priority.get("can_get_home_and_attacked")
            if pawn_index - moves_to_move <= player * 10 + 2:
                pawn_score[i] += priority.get("can_get_home")
        return max_index(pawn_score) + 1

    move(player, ai(board, moves_to_move, needs_to_start, player), needs_to_start, board, moves_to_move)

def main():
    needs_to_start = [4] * 4
    board = ["."] * 40
    while get_winner(board, needs_to_start) == -1:
        for i in range(4):
            moves_to_move = dice()
            print_board(board, needs_to_start)
            print("jij hebt", moves_to_move, "gegooid met de dobbelsteen")
            print("commando ai is dat de computer zet")
            pawn = input("Welke pion wil je zetten? (jij bent speler " + str(i) + ") ")
            if pawn == "ai":
                aimove(board, moves_to_move, needs_to_start, i)
            else:
                move(i, int(pawn), needs_to_start, board, moves_to_move)

    print("Spel afgelopen. Speler", get_winner(board, needs_to_start), "heeft gewonnen")

if __name__ == "__main__":
    main()