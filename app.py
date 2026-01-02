import random

dice = [1, 2, 3, 4, 5, 6]
board_size = 20

pos_a = 0
pos_b = 0

players = ["A", "B"]

for turn in range(10):  # 10ターン
    player = players[turn % 2]

    roll = random.choice(dice)

    if player == "A":
        pos_a += roll
        pos_a = min(pos_a, board_size)
    else:
        pos_b += roll
        pos_b = min(pos_b, board_size)

    # 盤面作成
    board = ["□"] * (board_size + 1)

    board[pos_a] = "●"
    board[pos_b] = "▲"   # Bが後なら上書きされる

    print(f"{turn+1}手目：プレイヤー{player} が {roll}")
    print("".join(board))
    print()

if pos_a >= board_size:
    print("🎉 プレイヤーAの勝ち！")
    break

if pos_b >= board_size:
    print("🎉 プレイヤーBの勝ち！")
    break
