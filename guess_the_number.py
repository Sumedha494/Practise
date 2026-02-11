#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

# Random number generate (1 se 100)
secret_number = random.randint(1, 100)
attempts = 0

print("🎮 GUESS THE NUMBER GAME")
print("=" * 30)
print("Maine 1 se 100 ke beech ek number socha hai!")
print("Kya aap guess kar sakte ho?\n")

while True:
    guess = int(input("Apna guess enter karo: "))
    attempts += 1

    if guess < secret_number:
        print("📈 Too LOW! Thoda bada number try karo.\n")
    elif guess > secret_number:
        print("📉 Too HIGH! Thoda chhota number try karo.\n")
    else:
        print(f"\n🎉 CONGRATULATIONS! Sahi guess kiya!")
        print(f"🔢 Number tha: {secret_number}")
        print(f"📊 Attempts: {attempts}")
        break


# In[ ]:


import random

secret_number = random.randint(1, 100)
max_attempts = 7
attempts = 0

print("🎮 GUESS THE NUMBER GAME")
print("=" * 35)
print(f"🎯 Number: 1 se 100 ke beech")
print(f"⏰ Attempts: Sirf {max_attempts} chances!\n")

while attempts < max_attempts:
    remaining = max_attempts - attempts
    print(f"💡 Remaining attempts: {remaining}")

    guess = int(input("Apna guess enter karo: "))
    attempts += 1

    if guess < secret_number:
        print("📈 Too LOW!\n")
    elif guess > secret_number:
        print("📉 Too HIGH!\n")
    else:
        print(f"\n🎉 WINNER! {attempts} attempts mein guess kar liya!")
        print(f"🔢 Number tha: {secret_number}")
        break
else:
    print(f"\n😢 GAME OVER! Attempts khatam!")
    print(f"🔢 Sahi number tha: {secret_number}")


# In[ ]:


import random

def get_difficulty():
    print("🎮 GUESS THE NUMBER GAME")
    print("=" * 35)
    print("\n📊 Select Difficulty Level:")
    print("1. 😊 Easy   (1-50,  10 attempts)")
    print("2. 😐 Medium (1-100, 7 attempts)")
    print("3. 😈 Hard   (1-200, 5 attempts)")
    print("4. 💀 Expert (1-500, 8 attempts)")

    choice = input("\nChoice (1-4): ")

    if choice == '1':
        return 50, 10, "Easy"
    elif choice == '2':
        return 100, 7, "Medium"
    elif choice == '3':
        return 200, 5, "Hard"
    elif choice == '4':
        return 500, 8, "Expert"
    else:
        return 100, 7, "Medium"

def play_game():
    max_num, max_attempts, level = get_difficulty()
    secret_number = random.randint(1, max_num)
    attempts = 0

    print(f"\n🎯 Level: {level}")
    print(f"📊 Range: 1 to {max_num}")
    print(f"⏰ Attempts: {max_attempts}")
    print("-" * 30)

    while attempts < max_attempts:
        remaining = max_attempts - attempts

        try:
            guess = int(input(f"\n[{remaining} left] Your guess: "))
        except ValueError:
            print("❌ Please enter a valid number!")
            continue

        attempts += 1

        if guess < secret_number:
            diff = secret_number - guess
            if diff > 20:
                print("📈 Way too LOW!")
            else:
                print("📈 Too LOW, but close!")
        elif guess > secret_number:
            diff = guess - secret_number
            if diff > 20:
                print("📉 Way too HIGH!")
            else:
                print("📉 Too HIGH, but close!")
        else:
            print(f"\n🎉🎉🎉 CONGRATULATIONS! 🎉🎉🎉")
            print(f"🔢 Number was: {secret_number}")
            print(f"📊 Attempts used: {attempts}/{max_attempts}")

            # Score calculation
            score = (max_attempts - attempts + 1) * 100
            print(f"⭐ Score: {score} points!")
            return True

    print(f"\n😢 GAME OVER!")
    print(f"🔢 The number was: {secret_number}")
    return False

# Play the game
play_game()


# In[ ]:


import random

def number_guessing_with_hints():
    secret_number = random.randint(1, 100)
    attempts = 0
    hints_used = 0
    max_hints = 3

    print("🎮 GUESS THE NUMBER (With Hints!)")
    print("=" * 40)
    print("📊 Number: 1 to 100")
    print(f"💡 Hints available: {max_hints}")
    print("Type 'hint' for a hint, 'quit' to exit\n")

    while True:
        user_input = input("Your guess (or 'hint'): ").lower()

        if user_input == 'quit':
            print(f"\n👋 Bye! Number was: {secret_number}")
            break

        if user_input == 'hint':
            if hints_used < max_hints:
                hints_used += 1
                remaining_hints = max_hints - hints_used

                # Different hints
                if hints_used == 1:
                    if secret_number % 2 == 0:
                        print(f"💡 Hint: Number is EVEN ({remaining_hints} hints left)")
                    else:
                        print(f"💡 Hint: Number is ODD ({remaining_hints} hints left)")

                elif hints_used == 2:
                    if secret_number <= 50:
                        print(f"💡 Hint: Number is between 1-50 ({remaining_hints} hints left)")
                    else:
                        print(f"💡 Hint: Number is between 51-100 ({remaining_hints} hints left)")

                elif hints_used == 3:
                    lower = (secret_number // 10) * 10
                    upper = lower + 10
                    print(f"💡 Hint: Number is between {lower}-{upper} ({remaining_hints} hints left)")
            else:
                print("❌ No hints remaining!")
            continue

        try:
            guess = int(user_input)
        except ValueError:
            print("❌ Enter a valid number!")
            continue

        attempts += 1

        if guess < secret_number:
            print("📈 Too LOW!")
        elif guess > secret_number:
            print("📉 Too HIGH!")
        else:
            print(f"\n🎉 CORRECT! Number was {secret_number}")
            print(f"📊 Attempts: {attempts}")
            print(f"💡 Hints used: {hints_used}")

            # Bonus for not using hints
            bonus = (max_hints - hints_used) * 50
            base_score = max(100 - (attempts * 10), 10)
            total_score = base_score + bonus
            print(f"⭐ Score: {total_score} points!")
            break

# Play
number_guessing_with_hints()


# In[ ]:


import random

def play_round(round_num):
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7

    print(f"\n🎮 ROUND {round_num}")
    print("-" * 25)

    while attempts < max_attempts:
        remaining = max_attempts - attempts

        try:
            guess = int(input(f"[{remaining} left] Guess: "))
        except ValueError:
            print("❌ Invalid input!")
            continue

        attempts += 1

        if guess < secret_number:
            print("📈 Too LOW!")
        elif guess > secret_number:
            print("📉 Too HIGH!")
        else:
            score = (max_attempts - attempts + 1) * 100
            print(f"✅ Correct! Score: {score}")
            return score

    print(f"❌ Failed! Number was: {secret_number}")
    return 0

def main_game():
    print("🎮 GUESS THE NUMBER - CHAMPIONSHIP")
    print("=" * 40)

    player_name = input("Enter your name: ")
    total_rounds = 3
    total_score = 0
    round_scores = []

    for round_num in range(1, total_rounds + 1):
        score = play_round(round_num)
        round_scores.append(score)
        total_score += score

    # Final Results
    print("\n" + "=" * 40)
    print("🏆 FINAL RESULTS")
    print("=" * 40)
    print(f"👤 Player: {player_name}")
    print(f"\n📊 Round-wise Scores:")
    for i, score in enumerate(round_scores, 1):
        status = "✅" if score > 0 else "❌"
        print(f"   Round {i}: {score} points {status}")

    print(f"\n⭐ Total Score: {total_score}")

    # Rank
    if total_score >= 1500:
        rank = "🥇 GOLD"
    elif total_score >= 1000:
        rank = "🥈 SILVER"
    elif total_score >= 500:
        rank = "🥉 BRONZE"
    else:
        rank = "📜 Participant"

    print(f"🏅 Rank: {rank}")

# Play
main_game()


# In[ ]:


def computer_guesses():
    print("🤖 COMPUTER GUESSES YOUR NUMBER!")
    print("=" * 40)
    print("📊 Ek number socho 1 se 100 ke beech")
    print("💡 Computer guess karega, aap hints do:")
    print("   'h' = Too High")
    print("   'l' = Too Low")
    print("   'c' = Correct!\n")

    input("Number soch liya? Press Enter to start...")

    low = 1
    high = 100
    attempts = 0

    while low <= high:
        guess = (low + high) // 2
        attempts += 1

        print(f"\n🤖 Attempt {attempts}")
        print(f"   Computer's guess: {guess}")

        feedback = input("   Your feedback (h/l/c): ").lower()

        if feedback == 'c':
            print(f"\n🎉 Computer won in {attempts} attempts!")
            print("🤖 I'm smart, right? 😎")
            break
        elif feedback == 'h':
            high = guess - 1
            print(f"   📉 Okay, number is less than {guess}")
        elif feedback == 'l':
            low = guess + 1
            print(f"   📈 Okay, number is greater than {guess}")
        else:
            print("   ❌ Please enter 'h', 'l', or 'c'")
            attempts -= 1
    else:
        print("\n🤔 Something went wrong! Are you cheating? 😄")

# Play
computer_guesses()


# In[ ]:


import random

def two_player_game():
    print("👥 TWO PLAYER GUESSING GAME")
    print("=" * 40)

    player1 = input("Player 1 name: ")
    player2 = input("Player 2 name: ")

    rounds = 3
    scores = {player1: 0, player2: 0}

    for round_num in range(1, rounds + 1):
        print(f"\n{'='*40}")
        print(f"🎮 ROUND {round_num}")
        print(f"{'='*40}")

        for player in [player1, player2]:
            secret = random.randint(1, 50)
            attempts = 0
            max_attempts = 5

            print(f"\n👤 {player}'s turn!")
            print(f"📊 Guess number between 1-50")
            print(f"⏰ You have {max_attempts} attempts")

            while attempts < max_attempts:
                remaining = max_attempts - attempts

                try:
                    guess = int(input(f"[{remaining} left] Guess: "))
                except ValueError:
                    print("❌ Invalid!")
                    continue

                attempts += 1

                if guess < secret:
                    print("📈 Higher!")
                elif guess > secret:
                    print("📉 Lower!")
                else:
                    score = (max_attempts - attempts + 1) * 100
                    scores[player] += score
                    print(f"✅ Correct! +{score} points")
                    break
            else:
                print(f"❌ Time up! Number was {secret}")

        # Round summary
        print(f"\n📊 After Round {round_num}:")
        print(f"   {player1}: {scores[player1]} pts")
        print(f"   {player2}: {scores[player2]} pts")

    # Final results
    print("\n" + "=" * 40)
    print("🏆 FINAL RESULTS")
    print("=" * 40)
    print(f"   {player1}: {scores[player1]} points")
    print(f"   {player2}: {scores[player2]} points")

    if scores[player1] > scores[player2]:
        print(f"\n🎉 {player1} WINS! 🎉")
    elif scores[player2] > scores[player1]:
        print(f"\n🎉 {player2} WINS! 🎉")
    else:
        print("\n🤝 IT'S A TIE!")

# Play
two_player_game()


# In[ ]:


import random
from datetime import datetime

class NumberGuessingGame:
    def __init__(self):
        self.high_scores = []
        self.games_played = 0

    def show_menu(self):
        print("\n🎮 NUMBER GUESSING GAME")
        print("=" * 35)
        print("1. 🎯 Play Game")
        print("2. 🤖 Computer Guesses")
        print("3. 👥 Two Player Mode")
        print("4. 🏆 High Scores")
        print("5. 📊 Statistics")
        print("6. ❓ How to Play")
        print("7. 🚪 Exit")
        return input("\nChoice (1-7): ")

    def select_difficulty(self):
        print("\n📊 Select Difficulty:")
        print("1. 😊 Easy   (1-50)")
        print("2. 😐 Medium (1-100)")
        print("3. 😈 Hard   (1-200)")

        choice = input("Choice (1-3): ")

        difficulties = {
            '1': (50, 10, 'Easy'),
            '2': (100, 7, 'Medium'),
            '3': (200, 5, 'Hard')
        }
        return difficulties.get(choice, (100, 7, 'Medium'))

    def play_single(self):
        max_num, max_attempts, level = self.select_difficulty()
        secret = random.randint(1, max_num)
        attempts = 0

        print(f"\n🎯 Level: {level}")
        print(f"📊 Range: 1-{max_num}")
        print(f"⏰ Attempts: {max_attempts}\n")

        while attempts < max_attempts:
            remaining = max_attempts - attempts

            try:
                guess = int(input(f"[{remaining} left] Guess: "))
            except ValueError:
                print("❌ Enter a number!")
                continue

            if guess < 1 or guess > max_num:
                print(f"❌ Enter between 1-{max_num}!")
                continue

            attempts += 1
            diff = abs(secret - guess)

            if guess < secret:
                if diff > 20:
                    print("📈 Much higher!")
                elif diff > 10:
                    print("📈 Higher!")
                else:
                    print("📈 Slightly higher! 🔥")
            elif guess > secret:
                if diff > 20:
                    print("📉 Much lower!")
                elif diff > 10:
                    print("📉 Lower!")
                else:
                    print("📉 Slightly lower! 🔥")
            else:
                score = (max_attempts - attempts + 1) * 100 * (max_num // 50)
                print(f"\n🎉 CORRECT!")
                print(f"📊 Attempts: {attempts}")
                print(f"⭐ Score: {score}")

                self.save_score(score, level, attempts)
                self.games_played += 1
                return

        print(f"\n😢 Game Over! Number was: {secret}")
        self.games_played += 1

    def computer_guess(self):
        print("\n🤖 Think of a number (1-100)")
        input("Press Enter when ready...")

        low, high = 1, 100
        attempts = 0

        while low <= high:
            guess = (low + high) // 2
            attempts += 1

            print(f"\n🤖 Is it {guess}?")
            feedback = input("(h)igh, (l)ow, (c)orrect: ").lower()

            if feedback == 'c':
                print(f"🎉 Got it in {attempts} tries!")
                return
            elif feedback == 'h':
                high = guess - 1
            elif feedback == 'l':
                low = guess + 1

        print("🤔 Are you cheating?")

    def save_score(self, score, level, attempts):
        self.high_scores.append({
            'score': score,
            'level': level,
            'attempts': attempts,
            'date': datetime.now().strftime("%Y-%m-%d %H:%M")
        })
        self.high_scores.sort(key=lambda x: x['score'], reverse=True)
        self.high_scores = self.high_scores[:10]  # Keep top 10

    def show_high_scores(self):
        print("\n🏆 HIGH SCORES")
        print("=" * 45)

        if not self.high_scores:
            print("No scores yet! Play a game first.")
            return

        print(f"{'Rank':<6}{'Score':<10}{'Level':<10}{'Attempts':<10}")
        print("-" * 45)

        for i, entry in enumerate(self.high_scores, 1):
            print(f"{i:<6}{entry['score']:<10}{entry['level']:<10}{entry['attempts']:<10}")

    def show_stats(self):
        print("\n📊 GAME STATISTICS")
        print("=" * 35)
        print(f"🎮 Games Played: {self.games_played}")
        print(f"🏆 High Scores: {len(self.high_scores)}")

        if self.high_scores:
            best = self.high_scores[0]
            print(f"⭐ Best Score: {best['score']} ({best['level']})")

    def show_help(self):
        print("\n❓ HOW TO PLAY")
        print("=" * 40)
        print("1. Computer picks a random number")
        print("2. You try to guess it")
        print("3. Get hints: Too High / Too Low")
        print("4. Guess correctly to win!")
        print("\n💡 TIPS:")
        print("• Start with middle number")
        print("• Use binary search strategy")
        print("• Fewer attempts = Higher score")

    def run(self):
        print("\n🎮 Welcome to Number Guessing Game! 🎮")

        while True:
            choice = self.show_menu()

            if choice == '1':
                self.play_single()
            elif choice == '2':
                self.computer_guess()
            elif choice == '3':
                print("👥 Two player mode - Coming soon!")
            elif choice == '4':
                self.show_high_scores()
            elif choice == '5':
                self.show_stats()
            elif choice == '6':
                self.show_help()
            elif choice == '7':
                print("\n👋 Thanks for playing! Goodbye!")
                break
            else:
                print("❌ Invalid choice!")

# Run the game
game = NumberGuessingGame()
game.run()


# In[ ]:


import random

# Ultra compact version
secret = random.randint(1, 100)
print("Guess 1-100!")

while (g := int(input("Guess: "))) != secret:
    print("📈 Higher!" if g < secret else "📉 Lower!")

print("🎉 Correct!")


# In[ ]:




