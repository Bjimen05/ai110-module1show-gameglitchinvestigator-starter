# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] Describe the game's purpose.
*The game's purpose is correctly guess the secret number in an range with limited guesses

- [x] Detail which bugs you found.
*The hints give the wrong direction, the score was updated when given a negative number/nothing.

- [x] Explain what fixes you applied.
*Refactor the logic into logic_uttils.py, 

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. The user enter a guess of 36 and press "Enter"
2. The game returns "Go Higher"
3. The user enter a guess of 93 and press "Enter"
4. The game returns "Go Lower"
5. User enter correct guess and the game ends

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
============================= test session starts =============================
platform win32 -- Python 3.14.5, pytest-9.0.3, pluggy-1.6.0 -- C:\Python314\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\Brandon\Documents\GitHub\ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.13.0
collecting ... collected 8 items

tests/test_game_logic.py::test_winning_guess PASSED                      [ 12%]
tests/test_game_logic.py::test_guess_too_high PASSED                     [ 25%]
tests/test_game_logic.py::test_guess_too_low PASSED                      [ 37%]
tests/test_game_logic.py::test_hint_message_too_high_says_go_lower PASSED [ 50%]
tests/test_game_logic.py::test_hint_message_too_low_says_go_higher PASSED [ 62%]
tests/test_game_logic.py::test_negative_number_is_rejected PASSED        [ 75%]
tests/test_game_logic.py::test_decimal_is_rejected PASSED                [ 87%]
tests/test_game_logic.py::test_extremely_large_value_is_rejected PASSED  [100%]

============================== 8 passed in 0.02s ==============================

## 🚀 Stretch Features

- [x] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
*By adding the Guess History, I also included a closeness bar which show how close a user's guess was to the secret using three colors, green meaning it was the correct guess, yellow mean it was close, and red mean it was too far from the secret
