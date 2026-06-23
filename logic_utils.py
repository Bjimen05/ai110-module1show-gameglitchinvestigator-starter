import json
import os

HIGHSCORE_FILE = os.path.join(os.path.dirname(__file__), "highscores.json")


def load_high_scores() -> dict:
    """Load per-difficulty high scores from disk.

    Reads ``highscores.json`` from the project root and returns a dictionary
    keyed by difficulty name.  If the file does not exist or contains invalid
    JSON, a fresh dictionary with all scores set to zero is returned so the
    caller never has to handle a missing-file case.

    Returns:
        dict: Mapping of difficulty name to integer high score, e.g.
            ``{"Easy": 0, "Normal": 50, "Hard": 90}``.
    """
    try:
        with open(HIGHSCORE_FILE, "r") as f:
            data = json.load(f)
        return {d: data.get(d, 0) for d in ("Easy", "Normal", "Hard")}
    except (FileNotFoundError, json.JSONDecodeError):
        return {"Easy": 0, "Normal": 0, "Hard": 0}


def save_high_score(difficulty: str, score: int) -> bool:
    """Persist a new high score for the given difficulty if it beats the record.

    Loads the current scores, compares ``score`` against the stored value for
    ``difficulty``, and writes the updated file only when a new record is set.
    This avoids unnecessary disk writes on non-record runs.

    Args:
        difficulty (str): One of ``"Easy"``, ``"Normal"``, or ``"Hard"``.
        score (int): The player's final score for this game.

    Returns:
        bool: ``True`` if ``score`` beat the previous record and was saved,
            ``False`` otherwise.
    """
    scores = load_high_scores()
    if score > scores.get(difficulty, 0):
        scores[difficulty] = score
        with open(HIGHSCORE_FILE, "w") as f:
            json.dump(scores, f)
        return True
    return False


def get_range_for_difficulty(difficulty: str):
    """Return the inclusive (low, high) number range for a given difficulty.

    Args:
        difficulty (str): One of ``"Easy"``, ``"Normal"``, or ``"Hard"``.

    Returns:
        tuple[int, int]: A ``(low, high)`` pair defining the valid guess range.

    Raises:
        NotImplementedError: This stub must be refactored from ``app.py``.
    """
    raise NotImplementedError(
        "Refactor this function from app.py into logic_utils.py"
    )


# FIX: Moved from app.py and extended with low/high range validation in agent
# mode. AI identified that the original silently accepted negatives, decimals,
# and out-of-range values.
def parse_guess(raw: str, low: int, high: int) -> tuple:
    """Parse and validate raw text input into an integer guess.

    Rejects empty input, decimal values, non-numeric strings, and integers
    that fall outside the ``[low, high]`` range for the current difficulty.

    Args:
        raw (str): The raw string entered by the player.
        low (int): The minimum valid guess (inclusive).
        high (int): The maximum valid guess (inclusive).

    Returns:
        tuple: A three-element tuple ``(ok, guess_int, error_message)`` where:

            - ``ok`` (bool) — ``True`` if the input is valid.
            - ``guess_int`` (int | None) — The parsed integer, or ``None`` on
              failure.
            - ``error_message`` (str | None) — A human-readable error string,
              or ``None`` on success.
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


# FIX: Moved check_guess from app.py into logic_utils.py using agent mode.
# AI identified that the hint messages were inverted and corrected them.
def check_guess(guess: int, secret) -> tuple:
    """Compare a player's guess to the secret number and return the outcome.

    Handles the case where ``secret`` is a string (the app intentionally
    converts it on even-numbered attempts) by falling back to string
    comparison inside the ``TypeError`` handler.

    Args:
        guess (int): The player's parsed integer guess.
        secret (int | str): The target value.  May be an ``int`` or a ``str``
            representation of the same integer.

    Returns:
        tuple[str, str]: A two-element tuple ``(outcome, message)`` where:

            - ``outcome`` is one of ``"Win"``, ``"Too High"``, or ``"Too Low"``.
            - ``message`` is the emoji-prefixed hint shown to the player.
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

    try:
        # FIX: Original directions were swapped — "Go HIGHER!" fired when the
        # guess was too high. Corrected so each message matches the needed
        # adjustment direction.
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


def update_score(current_score: int, outcome: str, attempt_number: int) -> int:
    """Update the running score based on the outcome of a single guess.

    Args:
        current_score (int): The player's score before this guess.
        outcome (str): One of ``"Win"``, ``"Too High"``, or ``"Too Low"``.
        attempt_number (int): The 1-based index of the current attempt.

    Returns:
        int: The updated score.

    Raises:
        NotImplementedError: This stub must be refactored from ``app.py``.
    """
    raise NotImplementedError(
        "Refactor this function from app.py into logic_utils.py"
    )
