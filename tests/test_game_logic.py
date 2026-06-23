from logic_utils import check_guess, parse_guess

# Existing starter tests — fixed to unpack the (outcome, message) tuple check_guess returns.
def test_winning_guess():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"

# FIX: Targets the inverted hint message bug — original code returned "Go HIGHER!" when guess was
# too high and "Go LOWER!" when too low. AI identified the swap by tracing the comparison logic.
def test_hint_message_too_high_says_go_lower():
    outcome, message = check_guess(70, 50)
    assert outcome == "Too High"
    assert "LOWER" in message, f"Expected 'Go LOWER!' hint when guess is too high, got: {message}"

def test_hint_message_too_low_says_go_higher():
    outcome, message = check_guess(30, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message, f"Expected 'Go HIGHER!' hint when guess is too low, got: {message}"

# Edge case 1: Negative number — the minimum valid guess is 1, so -5 is out of range.
# parse_guess should reject it and return ok=False rather than passing it to check_guess.
def test_negative_number_is_rejected():
    ok, value, error = parse_guess("-5", 1, 100)
    assert ok is False
    assert value is None
    assert error is not None

# Edge case 2: Decimal input — the game only accepts whole numbers.
# parse_guess should reject 3.7 (or any non-integer) with an error instead of silently truncating.
def test_decimal_is_rejected():
    ok, value, error = parse_guess("3.7", 1, 100)
    assert ok is False
    assert value is None
    assert error is not None

# Edge case 3: Extremely large value — numbers above the difficulty max are out of range.
# parse_guess should reject 99999 with an error rather than forwarding it to check_guess.
def test_extremely_large_value_is_rejected():
    ok, value, error = parse_guess("99999", 1, 100)
    assert ok is False
    assert value is None
    assert error is not None
