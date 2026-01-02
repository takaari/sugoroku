import streamlit as st
import random

st.set_page_config(layout="wide")

st.title("🎲 すごろくゲーム（2人プレイ）")

# --------------------
# 初期設定
# --------------------
BOARD_SIZE = 20
DICE = [1, 2, 3, 4, 5, 6]

if "pos_a" not in st.session_state:
    st.session_state.pos_a = 0
if "pos_b" not in st.session_state:
    st.session_state.pos_b = 0
if "turn" not in st.session_state:
    st.session_state.turn = "A"
if "finished" not in st.session_state:
    st.session_state.finished = False
    
# --------------------
# サイコロ処理
# --------------------
if not st.session_state.finished:
    if st.button("🎲 サイコロを振る"):
        roll = random.choice(DICE)

        if st.session_state.turn == "A":
            st.session_state.pos_a = min(
                st.session_state.pos_a + roll, BOARD_SIZE
            )
            st.session_state.turn = "B"
        else:
            st.session_state.pos_b = min(
                st.session_state.pos_b + roll, BOARD_SIZE
            )
            st.session_state.turn = "A"

        st.session_state.last_roll = roll

# --------------------
# 盤面描画
# --------------------
board = ["□"] * (BOARD_SIZE + 1)

# 同じマスにいる場合
if st.session_state.pos_a == st.session_state.pos_b:
    board[st.session_state.pos_a] = "★"
else:
    board[st.session_state.pos_a] = "●"
    board[st.session_state.pos_b] = "▲"

st.markdown("### 🧭 盤面")
st.markdown("".join(board))

# --------------------
# 情報表示
# --------------------
st.markdown("### 📊 状態")
st.write(f"🔵 プレイヤーA：{st.session_state.pos_a}")
st.write(f"🟢 プレイヤーB：{st.session_state.pos_b}")

if "last_roll" in st.session_state:
    st.info(f"🎲 出目：{st.session_state.last_roll}")

st.write(f"👉 次の番：プレイヤー {st.session_state.turn}")

# --------------------
# 勝利判定
# --------------------
if st.session_state.pos_a >= BOARD_SIZE:
    st.success("🎉 プレイヤーAの勝ち！")
    st.session_state.finished = True

elif st.session_state.pos_b >= BOARD_SIZE:
    st.success("🎉 プレイヤーBの勝ち！")
    st.session_state.finished = True

# --------------------
# リセット
# --------------------
if st.button("🔄 リスタート"):
    st.session_state.clear()
    st.rerun()
