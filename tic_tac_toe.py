#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Simple Tic Tac Toe
board = [' ' for _ in range(9)]

def print_board():
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()

def check_winner(player):
    # Winning combinations
    wins = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]

    for combo in wins:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

def is_board_full():
    return ' ' not in board

# Game Start
print("🎮 TIC TAC TOE")
print("=" * 20)
print("Positions: 1-9")
print()
print(" 1 | 2 | 3 ")
print("-----------")
print(" 4 | 5 | 6 ")
print("-----------")
print(" 7 | 8 | 9 ")

current_player = 'X'

while True:
    print_board()

    # Get move
    try:
        move = int(input(f"Player {current_player}, enter position (1-9): ")) - 1
    except ValueError:
        print("❌ Enter a number!")
        continue

    # Validate move
    if move < 0 or move > 8:
        print("❌ Enter 1-9 only!")
        continue

    if board[move] != ' ':
        print("❌ Position already taken!")
        continue

    # Make move
    board[move] = current_player

    # Check winner
    if check_winner(current_player):
        print_board()
        print(f"🎉 Player {current_player} WINS! 🎉")
        break

    # Check draw
    if is_board_full():
        print_board()
        print("🤝 It's a DRAW!")
        break

    # Switch player
    current_player = 'O' if current_player == 'X' else 'X'


# In[ ]:


def print_fancy_board(board):
    print()
    print("┌───┬───┬───┐")
    print(f"│ {board[0]} │ {board[1]} │ {board[2]} │")
    print("├───┼───┼───┤")
    print(f"│ {board[3]} │ {board[4]} │ {board[5]} │")
    print("├───┼───┼───┤")
    print(f"│ {board[6]} │ {board[7]} │ {board[8]} │")
    print("└───┴───┴───┘")
    print()

# Example
board = ['X', 'O', 'X', ' ', 'O', ' ', 'X', ' ', 'O']
print_fancy_board(board)


# In[ ]:


def tic_tac_toe_2player():
    board = [' ' for _ in range(9)]

    def print_board():
        print()
        print("┌───┬───┬───┐")
        print(f"│ {board[0]} │ {board[1]} │ {board[2]} │")
        print("├───┼───┼───┤")
        print(f"│ {board[3]} │ {board[4]} │ {board[5]} │")
        print("├───┼───┼───┤")
        print(f"│ {board[6]} │ {board[7]} │ {board[8]} │")
        print("└───┴───┴───┘")

    def print_positions():
        print()
        print("┌───┬───┬───┐")
        print("│ 1 │ 2 │ 3 │")
        print("├───┼───┼───┤")
        print("│ 4 │ 5 │ 6 │")
        print("├───┼───┼───┤")
        print("│ 7 │ 8 │ 9 │")
        print("└───┴───┴───┘")

    def check_winner(player):
        wins = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for combo in wins:
            if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
                return True
        return False

    def is_full():
        return ' ' not in board

    # Game setup
    print("🎮 TIC TAC TOE - 2 PLAYER")
    print("=" * 35)

    player1 = input("👤 Player 1 (X) name: ") or "Player 1"
    player2 = input("👤 Player 2 (O) name: ") or "Player 2"

    players = {
        'X': player1,
        'O': player2
    }

    print(f"\n{player1} = X")
    print(f"{player2} = O")
    print("\n📍 Position Guide:")
    print_positions()

    current = 'X'
    moves = 0

    while True:
        print_board()
        name = players[current]

        try:
            move = int(input(f"🎯 {name} ({current}), enter position: ")) - 1
        except ValueError:
            print("❌ Invalid input!")
            continue

        if move < 0 or move > 8:
            print("❌ Enter 1-9!")
            continue

        if board[move] != ' ':
            print("❌ Already taken!")
            continue

        board[move] = current
        moves += 1

        if check_winner(current):
            print_board()
            print(f"\n🎉🎉🎉 {name} WINS! 🎉🎉🎉")
            print(f"📊 Total moves: {moves}")
            break

        if is_full():
            print_board()
            print("\n🤝 It's a DRAW!")
            break

        current = 'O' if current == 'X' else 'X'

# Play
tic_tac_toe_2player()


# In[ ]:


import random

def tic_tac_toe_vs_computer():
    board = [' ' for _ in range(9)]

    def print_board():
        print()
        print("┌───┬───┬───┐")
        print(f"│ {board[0]} │ {board[1]} │ {board[2]} │")
        print("├───┼───┼───┤")
        print(f"│ {board[3]} │ {board[4]} │ {board[5]} │")
        print("├───┼───┼───┤")
        print(f"│ {board[6]} │ {board[7]} │ {board[8]} │")
        print("└───┴───┴───┘")

    def check_winner(player):
        wins = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for combo in wins:
            if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
                return True
        return False

    def is_full():
        return ' ' not in board

    def get_empty_positions():
        return [i for i, x in enumerate(board) if x == ' ']

    def computer_move():
        empty = get_empty_positions()
        return random.choice(empty)

    # Game setup
    print("🎮 TIC TAC TOE - VS COMPUTER")
    print("=" * 35)
    print("You = X, Computer = O")
    print("\n📍 Positions:")
    print(" 1 | 2 | 3 ")
    print(" 4 | 5 | 6 ")
    print(" 7 | 8 | 9 ")

    while True:
        # Player's turn
        print_board()

        try:
            move = int(input("🎯 Your turn (1-9): ")) - 1
        except ValueError:
            print("❌ Enter a number!")
            continue

        if move < 0 or move > 8 or board[move] != ' ':
            print("❌ Invalid move!")
            continue

        board[move] = 'X'

        if check_winner('X'):
            print_board()
            print("\n🎉 YOU WIN! 🎉")
            break

        if is_full():
            print_board()
            print("\n🤝 DRAW!")
            break

        # Computer's turn
        print("\n🤖 Computer thinking...")
        import time
        time.sleep(1)

        comp_move = computer_move()
        board[comp_move] = 'O'
        print(f"🤖 Computer chose position {comp_move + 1}")

        if check_winner('O'):
            print_board()
            print("\n😢 Computer WINS!")
            break

        if is_full():
            print_board()
            print("\n🤝 DRAW!")
            break

# Play
tic_tac_toe_vs_computer()


# In[ ]:


import math

def tic_tac_toe_smart_ai():
    board = [' ' for _ in range(9)]

    def print_board():
        print()
        print("┌───┬───┬───┐")
        print(f"│ {board[0]} │ {board[1]} │ {board[2]} │")
        print("├───┼───┼───┤")
        print(f"│ {board[3]} │ {board[4]} │ {board[5]} │")
        print("├───┼───┼───┤")
        print(f"│ {board[6]} │ {board[7]} │ {board[8]} │")
        print("└───┴───┴───┘")

    def check_winner(b, player):
        wins = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for combo in wins:
            if b[combo[0]] == b[combo[1]] == b[combo[2]] == player:
                return True
        return False

    def is_full(b):
        return ' ' not in b

    def get_empty(b):
        return [i for i, x in enumerate(b) if x == ' ']

    def minimax(b, depth, is_maximizing):
        """
        Minimax Algorithm - Unbeatable AI!
        Computer = O (Maximizing)
        Player = X (Minimizing)
        """
        # Base cases
        if check_winner(b, 'O'):
            return 10 - depth
        if check_winner(b, 'X'):
            return depth - 10
        if is_full(b):
            return 0

        if is_maximizing:
            best_score = -math.inf
            for i in get_empty(b):
                b[i] = 'O'
                score = minimax(b, depth + 1, False)
                b[i] = ' '
                best_score = max(score, best_score)
            return best_score
        else:
            best_score = math.inf
            for i in get_empty(b):
                b[i] = 'X'
                score = minimax(b, depth + 1, True)
                b[i] = ' '
                best_score = min(score, best_score)
            return best_score

    def computer_move():
        best_score = -math.inf
        best_move = None

        for i in get_empty(board):
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ' '

            if score > best_score:
                best_score = score
                best_move = i

        return best_move

    # Game
    print("🎮 TIC TAC TOE - SMART AI")
    print("=" * 35)
    print("⚠️  Warning: AI is UNBEATABLE!")
    print("You = X, Computer = O")
    print("\n📍 Positions: 1-9")

    # Who goes first?
    first = input("\nGo first? (y/n): ").lower()

    if first != 'y':
        # Computer first move (center or corner)
        board[4] = 'O'
        print("🤖 Computer starts at center!")

    while True:
        print_board()

        # Player's turn
        try:
            move = int(input("🎯 Your move (1-9): ")) - 1
        except ValueError:
            print("❌ Invalid!")
            continue

        if move < 0 or move > 8 or board[move] != ' ':
            print("❌ Invalid move!")
            continue

        board[move] = 'X'

        if check_winner(board, 'X'):
            print_board()
            print("\n🎉 YOU WIN! (Impossible... 🤔)")
            break

        if is_full(board):
            print_board()
            print("\n🤝 DRAW! (Best you can do!)")
            break

        # Computer's turn
        print("\n🤖 AI thinking...")
        import time
        time.sleep(0.5)

        comp_move = computer_move()
        board[comp_move] = 'O'
        print(f"🤖 AI chose position {comp_move + 1}")

        if check_winner(board, 'O'):
            print_board()
            print("\n🤖 AI WINS! Better luck next time!")
            break

        if is_full(board):
            print_board()
            print("\n🤝 DRAW!")
            break

# Play
tic_tac_toe_smart_ai()


# In[ ]:


import random
import math

def tic_tac_toe_difficulty():
    board = [' ' for _ in range(9)]

    def print_board():
        print()
        print("┌───┬───┬───┐")
        print(f"│ {board[0]} │ {board[1]} │ {board[2]} │")
        print("├───┼───┼───┤")
        print(f"│ {board[3]} │ {board[4]} │ {board[5]} │")
        print("├───┼───┼───┤")
        print(f"│ {board[6]} │ {board[7]} │ {board[8]} │")
        print("└───┴───┴───┘")

    def check_winner(b, player):
        wins = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for combo in wins:
            if b[combo[0]] == b[combo[1]] == b[combo[2]] == player:
                return True
        return False

    def is_full(b):
        return ' ' not in b

    def get_empty(b):
        return [i for i, x in enumerate(b) if x == ' ']

    def minimax(b, depth, is_maximizing):
        if check_winner(b, 'O'):
            return 10 - depth
        if check_winner(b, 'X'):
            return depth - 10
        if is_full(b):
            return 0

        if is_maximizing:
            best = -math.inf
            for i in get_empty(b):
                b[i] = 'O'
                score = minimax(b, depth + 1, False)
                b[i] = ' '
                best = max(score, best)
            return best
        else:
            best = math.inf
            for i in get_empty(b):
                b[i] = 'X'
                score = minimax(b, depth + 1, True)
                b[i] = ' '
                best = min(score, best)
            return best

    def easy_move():
        """Random move"""
        return random.choice(get_empty(board))

    def medium_move():
        """50% smart, 50% random"""
        if random.random() < 0.5:
            return smart_move()
        return easy_move()

    def smart_move():
        """Minimax - unbeatable"""
        best_score = -math.inf
        best_move = None

        for i in get_empty(board):
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ' '

            if score > best_score:
                best_score = score
                best_move = i

        return best_move

    # Select difficulty
    print("🎮 TIC TAC TOE")
    print("=" * 30)
    print("\n📊 Select Difficulty:")
    print("1. 😊 Easy   (Random moves)")
    print("2. 😐 Medium (Sometimes smart)")
    print("3. 😈 Hard   (Unbeatable AI)")

    diff = input("\nChoice (1-3): ")

    if diff == '1':
        ai_move = easy_move
        level = "Easy"
    elif diff == '2':
        ai_move = medium_move
        level = "Medium"
    else:
        ai_move = smart_move
        level = "Hard"

    print(f"\n🎯 Level: {level}")
    print("You = X, Computer = O")

    while True:
        print_board()

        # Player
        try:
            move = int(input("🎯 Your move (1-9): ")) - 1
        except:
            continue

        if move < 0 or move > 8 or board[move] != ' ':
            print("❌ Invalid!")
            continue

        board[move] = 'X'

        if check_winner(board, 'X'):
            print_board()
            print("\n🎉 YOU WIN!")
            break

        if is_full(board):
            print_board()
            print("\n🤝 DRAW!")
            break

        # Computer
        comp = ai_move()
        board[comp] = 'O'
        print(f"\n🤖 Computer: position {comp + 1}")

        if check_winner(board, 'O'):
            print_board()
            print("\n🤖 Computer WINS!")
            break

        if is_full(board):
            print_board()
            print("\n🤝 DRAW!")
            break

# Play
tic_tac_toe_difficulty()


# In[ ]:


import random
import math

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.scores = {'Player': 0, 'Computer': 0, 'Draws': 0}
        self.games_played = 0

    def reset_board(self):
        self.board = [' ' for _ in range(9)]

    def print_board(self):
        print()
        print("┌───┬───┬───┐")
        print(f"│ {self.board[0]} │ {self.board[1]} │ {self.board[2]} │")
        print("├───┼───┼───┤")
        print(f"│ {self.board[3]} │ {self.board[4]} │ {self.board[5]} │")
        print("├───┼───┼───┤")
        print(f"│ {self.board[6]} │ {self.board[7]} │ {self.board[8]} │")
        print("└───┴───┴───┘")

    def print_positions(self):
        print()
        print("┌───┬───┬───┐")
        print("│ 1 │ 2 │ 3 │")
        print("├───┼───┼───┤")
        print("│ 4 │ 5 │ 6 │")
        print("├───┼───┼───┤")
        print("│ 7 │ 8 │ 9 │")
        print("└───┴───┴───┘")

    def check_winner(self, player):
        wins = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for combo in wins:
            if (self.board[combo[0]] == 
                self.board[combo[1]] == 
                self.board[combo[2]] == player):
                return True
        return False

    def is_full(self):
        return ' ' not in self.board

    def get_empty(self):
        return [i for i, x in enumerate(self.board) if x == ' ']

    def computer_move(self):
        # Simple AI: try to win, block, or random

        # 1. Try to win
        for i in self.get_empty():
            self.board[i] = 'O'
            if self.check_winner('O'):
                self.board[i] = ' '
                return i
            self.board[i] = ' '

        # 2. Block player
        for i in self.get_empty():
            self.board[i] = 'X'
            if self.check_winner('X'):
                self.board[i] = ' '
                return i
            self.board[i] = ' '

        # 3. Take center
        if self.board[4] == ' ':
            return 4

        # 4. Take corner
        corners = [0, 2, 6, 8]
        empty_corners = [c for c in corners if self.board[c] == ' ']
        if empty_corners:
            return random.choice(empty_corners)

        # 5. Random
        return random.choice(self.get_empty())

    def show_scores(self):
        print("\n🏆 SCOREBOARD")
        print("=" * 25)
        print(f"👤 Player:   {self.scores['Player']}")
        print(f"🤖 Computer: {self.scores['Computer']}")
        print(f"🤝 Draws:    {self.scores['Draws']}")
        print(f"📊 Games:    {self.games_played}")

    def play_round(self):
        self.reset_board()

        print("\n🎮 NEW GAME!")
        print("You = X, Computer = O")
        self.print_positions()

        while True:
            self.print_board()

            # Player's turn
            while True:
                try:
                    move = int(input("🎯 Your move (1-9): ")) - 1
                    if 0 <= move <= 8 and self.board[move] == ' ':
                        break
                    print("❌ Invalid!")
                except ValueError:
                    print("❌ Enter a number!")

            self.board[move] = 'X'

            if self.check_winner('X'):
                self.print_board()
                print("\n🎉 YOU WIN! 🎉")
                self.scores['Player'] += 1
                break

            if self.is_full():
                self.print_board()
                print("\n🤝 DRAW!")
                self.scores['Draws'] += 1
                break

            # Computer's turn
            print("\n🤖 Computer thinking...")
            import time
            time.sleep(0.5)

            comp_move = self.computer_move()
            self.board[comp_move] = 'O'
            print(f"🤖 Computer: position {comp_move + 1}")

            if self.check_winner('O'):
                self.print_board()
                print("\n🤖 Computer WINS!")
                self.scores['Computer'] += 1
                break

            if self.is_full():
                self.print_board()
                print("\n🤝 DRAW!")
                self.scores['Draws'] += 1
                break

        self.games_played += 1

    def run(self):
        print("🎮 TIC TAC TOE")
        print("=" * 30)

        while True:
            print("\n📋 MENU")
            print("1. 🎯 Play Game")
            print("2. 🏆 View Scores")
            print("3. 🔄 Reset Scores")
            print("4. 🚪 Exit")

            choice = input("\nChoice (1-4): ")

            if choice == '1':
                self.play_round()
            elif choice == '2':
                self.show_scores()
            elif choice == '3':
                self.scores = {'Player': 0, 'Computer': 0, 'Draws': 0}
                self.games_played = 0
                print("✅ Scores reset!")
            elif choice == '4':
                self.show_scores()
                print("\n👋 Thanks for playing!")
                break

# Play
game = TicTacToe()
game.run()


# In[ ]:


import random
import math
import os
import time

class TicTacToeComplete:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.scores = {'Player': 0, 'Computer': 0, 'Draws': 0}
        self.player_name = "Player"
        self.player_symbol = 'X'
        self.computer_symbol = 'O'
        self.difficulty = 'Medium'
        self.games_played = 0

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def reset_board(self):
        self.board = [' ' for _ in range(9)]

    def print_header(self):
        print("╔═══════════════════════════════════╗")
        print("║       🎮 TIC TAC TOE 🎮           ║")
        print("╚═══════════════════════════════════╝")

    def print_board(self):
        # Color codes for terminal
        X_color = '\033[91m'  # Red
        O_color = '\033[94m'  # Blue
        reset = '\033[0m'

        def colorize(cell):
            if cell == 'X':
                return f"{X_color}X{reset}"
            elif cell == 'O':
                return f"{O_color}O{reset}"
            return cell

        print()
        print("     ┌───┬───┬───┐")
        print(f"     │ {colorize(self.board[0])} │ {colorize(self.board[1])} │ {colorize(self.board[2])} │")
        print("     ├───┼───┼───┤")
        print(f"     │ {colorize(self.board[3])} │ {colorize(self.board[4])} │ {colorize(self.board[5])} │")
        print("     ├───┼───┼───┤")
        print(f"     │ {colorize(self.board[6])} │ {colorize(self.board[7])} │ {colorize(self.board[8])} │")
        print("     └───┴───┴───┘")

    def print_positions(self):
        print()
        print("     ┌───┬───┬───┐")
        print("     │ 1 │ 2 │ 3 │")
        print("     ├───┼───┼───┤")
        print("     │ 4 │ 5 │ 6 │")
        print("     ├───┼───┼───┤")
        print("     │ 7 │ 8 │ 9 │")
        print("     └───┴───┴───┘")

    def check_winner(self, b, player):
        wins = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for combo in wins:
            if b[combo[0]] == b[combo[1]] == b[combo[2]] == player:
                return combo
        return None

    def is_full(self, b):
        return ' ' not in b

    def get_empty(self, b):
        return [i for i, x in enumerate(b) if x == ' ']

    def minimax(self, b, depth, is_maximizing, alpha, beta):
        """Minimax with Alpha-Beta Pruning"""
        if self.check_winner(b, self.computer_symbol):
            return 10 - depth
        if self.check_winner(b, self.player_symbol):
            return depth - 10
        if self.is_full(b):
            return 0

        if is_maximizing:
            best = -math.inf
            for i in self.get_empty(b):
                b[i] = self.computer_symbol
                score = self.minimax(b, depth + 1, False, alpha, beta)
                b[i] = ' '
                best = max(score, best)
                alpha = max(alpha, best)
                if beta <= alpha:
                    break
            return best
        else:
            best = math.inf
            for i in self.get_empty(b):
                b[i] = self.player_symbol
                score = self.minimax(b, depth + 1, True, alpha, beta)
                b[i] = ' '
                best = min(score, best)
                beta = min(beta, best)
                if beta <= alpha:
                    break
            return best

    def easy_move(self):
        return random.choice(self.get_empty(self.board))

    def medium_move(self):
        # Win if possible
        for i in self.get_empty(self.board):
            self.board[i] = self.computer_symbol
            if self.check_winner(self.board, self.computer_symbol):
                self.board[i] = ' '
                return i
            self.board[i] = ' '

        # Block player
        for i in self.get_empty(self.board):
            self.board[i] = self.player_symbol
            if self.check_winner(self.board, self.player_symbol):
                self.board[i] = ' '
                return i
            self.board[i] = ' '

        # Center, corners, or random
        if self.board[4] == ' ':
            return 4

        corners = [c for c in [0, 2, 6, 8] if self.board[c] == ' ']
        if corners:
            return random.choice(corners)

        return random.choice(self.get_empty(self.board))

    def hard_move(self):
        best_score = -math.inf
        best_move = None

        for i in self.get_empty(self.board):
            self.board[i] = self.computer_symbol
            score = self.minimax(self.board, 0, False, -math.inf, math.inf)
            self.board[i] = ' '

            if score > best_score:
                best_score = score
                best_move = i

        return best_move

    def computer_move(self):
        if self.difficulty == 'Easy':
            return self.easy_move()
        elif self.difficulty == 'Medium':
            return self.medium_move()
        else:
            return self.hard_move()

    def animate_thinking(self):
        print("\n🤖 Computer thinking", end="", flush=True)
        for _ in range(3):
            time.sleep(0.3)
            print(".", end="", flush=True)
        print()

    def show_scores(self):
        print("\n╔═══════════════════════════════════╗")
        print("║         🏆 SCOREBOARD 🏆          ║")
        print("╠═══════════════════════════════════╣")
        print(f"║  👤 {self.player_name:<15}: {self.scores['Player']:>5}   ║")
        print(f"║  🤖 Computer         : {self.scores['Computer']:>5}   ║")
        print(f"║  🤝 Draws            : {self.scores['Draws']:>5}   ║")
        print(f"║  📊 Total Games      : {self.games_played:>5}   ║")
        print("╚═══════════════════════════════════╝")

    def settings(self):
        print("\n⚙️  SETTINGS")
        print("=" * 30)
        print("1. 👤 Change Name")
        print("2. 🎯 Change Difficulty")
        print("3. 🔄 Swap Symbols (X/O)")
        print("4. ↩️  Back")

        choice = input("\nChoice: ")

        if choice == '1':
            self.player_name = input("Enter name: ") or "Player"
            print(f"✅ Name changed to {self.player_name}")
        elif choice == '2':
            print("\n📊 Difficulty:")
            print("1. 😊 Easy")
            print("2. 😐 Medium")
            print("3. 😈 Hard (Unbeatable)")
            d = input("Choice: ")
            if d == '1':
                self.difficulty = 'Easy'
            elif d == '2':
                self.difficulty = 'Medium'
            else:
                self.difficulty = 'Hard'
            print(f"✅ Difficulty: {self.difficulty}")
        elif choice == '3':
            self.player_symbol, self.computer_symbol = self.computer_symbol, self.player_symbol
            print(f"✅ You are now {self.player_symbol}")

    def play_round(self):
        self.reset_board()

        print(f"\n🎮 NEW GAME - {self.difficulty} Mode")
        print(f"👤 {self.player_name} = {self.player_symbol}")
        print(f"🤖 Computer = {self.computer_symbol}")
        self.print_positions()

        # Decide who goes first
        current = 'X'

        while True:
            self.print_board()

            if current == self.player_symbol:
                # Player's turn
                while True:
                    try:
                        move = int(input(f"\n🎯 {self.player_name}'s turn (1-9): ")) - 1
                        if 0 <= move <= 8 and self.board[move] == ' ':
                            break
                        print("❌ Invalid position!")
                    except ValueError:
                        print("❌ Enter a number 1-9!")

                self.board[move] = self.player_symbol

                winning_combo = self.check_winner(self.board, self.player_symbol)
                if winning_combo:
                    self.print_board()
                    print(f"\n🎉🎉🎉 {self.player_name} WINS! 🎉🎉🎉")
                    self.scores['Player'] += 1
                    break
            else:
                # Computer's turn
                self.animate_thinking()

                comp_move = self.computer_move()
                self.board[comp_move] = self.computer_symbol
                print(f"🤖 Computer chose position {comp_move + 1}")

                winning_combo = self.check_winner(self.board, self.computer_symbol)
                if winning_combo:
                    self.print_board()
                    print("\n🤖 Computer WINS! Better luck next time!")
                    self.scores['Computer'] += 1
                    break

            if self.is_full(self.board):
                self.print_board()
                print("\n🤝 It's a DRAW!")
                self.scores['Draws'] += 1
                break

            # Switch turns
            current = 'O' if current == 'X' else 'X'

        self.games_played += 1

    def how_to_play(self):
        print("\n📖 HOW TO PLAY")
        print("=" * 40)
        print("1. The game is played on a 3x3 grid")
        print("2. Players take turns placing X or O")
        print("3. First to get 3 in a row wins!")
        print("4. Rows can be horizontal, vertical,")
        print("   or diagonal")
        print()
        print("📍 Positions are numbered 1-9:")
        self.print_positions()
        print()
        print("💡 TIP: Try to control the center!")
        input("\nPress Enter to continue...")

    def main_menu(self):
        print("\n📋 MAIN MENU")
        print("=" * 30)
        print("1. 🎮 Play vs Computer")
        print("2. 👥 Play vs Friend")
        print("3. 🏆 View Scores")
        print("4. ⚙️  Settings")
        print("5. 📖 How to Play")
        print("6. 🔄 Reset Scores")
        print("7. 🚪 Exit")
        return input("\nChoice (1-7): ")

    def play_vs_friend(self):
        self.reset_board()

        player1 = input("👤 Player 1 name (X): ") or "Player 1"
        player2 = input("👤 Player 2 name (O): ") or "Player 2"

        players = {'X': player1, 'O': player2}
        current = 'X'

        print(f"\n{player1} = X")
        print(f"{player2} = O")
        self.print_positions()

        while True:
            self.print_board()
            name = players[current]

            while True:
                try:
                    move = int(input(f"\n🎯 {name} ({current}), enter position: ")) - 1
                    if 0 <= move <= 8 and self.board[move] == ' ':
                        break
                    print("❌ Invalid!")
                except ValueError:
                    print("❌ Enter 1-9!")

            self.board[move] = current

            if self.check_winner(self.board, current):
                self.print_board()
                print(f"\n🎉🎉🎉 {name} WINS! 🎉🎉🎉")
                break

            if self.is_full(self.board):
                self.print_board()
                print("\n🤝 It's a DRAW!")
                break

            current = 'O' if current == 'X' else 'X'

    def run(self):
        self.print_header()
        self.player_name = input("\n👤 Enter your name: ") or "Player"
        print(f"\n👋 Welcome, {self.player_name}!")

        while True:
            choice = self.main_menu()

            if choice == '1':
                self.play_round()
            elif choice == '2':
                self.play_vs_friend()
            elif choice == '3':
                self.show_scores()
            elif choice == '4':
                self.settings()
            elif choice == '5':
                self.how_to_play()
            elif choice == '6':
                self.scores = {'Player': 0, 'Computer': 0, 'Draws': 0}
                self.games_played = 0
                print("✅ Scores reset!")
            elif choice == '7':
                self.show_scores()
                print(f"\n👋 Goodbye, {self.player_name}! Thanks for playing!")
                break
            else:
                print("❌ Invalid choice!")

# Run the game
if __name__ == "__main__":
    game = TicTacToeComplete()
    game.run()

