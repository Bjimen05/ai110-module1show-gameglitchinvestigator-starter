import json
import os

HIGHSCORE_FILE = os.path.join(os.path.dirname(__file__), "highscores.json")

def load_high_scores() -> dict:
    """Load per-difficulty high scores from disk. Returns zeros if file missing or corrupt."""
    try:
        with open(HIGHSCORE_FILE, "r") as f:
            data = json.load(f)
        return {d: data.get(d, 0) for d in ("Easy", "Normal", "Hard")}
    except (FileNotFoundError, json.JSONDecodeError):
        return {"Easy": 0, "Normal": 0, "Hard": 0}

def save_high_score(difficulty: str, score: int) -> bool:
    """Save score for difficulty if it beats the current record. Returns True if a new record was set."""
    scores = load_high_scores()
    if score > scores.get(difficulty, 0):
        scores[difficulty] = score
        with open(HIGHSCORE_FILE, "w") as f:
            json.dump(scores, f)
        return True
    return False

def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


# FIX: Moved from app.py and extended with low/high range validation in agent mode.
# AI identified that the original accepted negatives, decimals, and out-of-range values silently.
def parse_guess(raw: str, low: int, high: int):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None or raw == "":
        return False, None, "Enter a guess."

    if "." in raw:
        return False, None, "Enter a whole number, not a decimal."

    try:
        value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    if value < low or value > high:
        return False, None, f"Enter a number between {low} and {high}."

    return True, value, None


# FIX: Moved check_guess from app.py into logic_utils.py using agent mode; AI identified the inverted hint messages and corrected them.
def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

    try:
        # FIX: Original code had "Go HIGHER!" when guess was too high and "Go LOWER!" when too low — directions were swapped. AI caught this by tracing the comparison logic.
        if guess > secret:
            return "Too High", "📉 Go LOWER!"
        else:
            return "Too Low", "📈 Go HIGHER!"
    except TypeError:
        g = str(guess)
        if g == secret:
            return "Win", "🎉 Correct!"
        if g > secret:
            return "Too High", "📉 Go LOWER!"
        return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")
