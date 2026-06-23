# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

<!-- Describe the goal you asked the agent to accomplish -->
*I told the agent to create a new feature which is a High Score Tracker.

**What did the agent do?**

<!-- List the steps the agent took (files edited, commands run, etc.) -->
*The agent add new functions and json files to the logic_utils.py, them exported to app.py, which then we created a section in the game which display the current high score of each difficulty of the user.

**What did you have to verify or fix manually?**

<!-- Describe anything the agent got wrong or that required human review -->
*The new functions and section required human review to make sure that the new highest get upated until the newest highest score came, as well how it was display which came great.

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

| Edge Case | Prompt Used |    AI-Suggested Test             | Did It Pass? | Your Reasoning |
|-----------|-------------|----------------------------------|--------------|----------------|

| Negative number (`-5`) | "identify edge case inputs that might break the game and generate pytest cases" | `test_negative_number_is_rejected` | Yes | Min valid guess is 1; negatives are out of range and must be rejected by `parse_guess` |

| Decimal input (`3.7`) | "identify edge case inputs that might break the game and generate pytest cases" | `test_decimal_is_rejected` | Yes | Original code silently truncated decimals; game only accepts whole numbers so this should be an explicit error |

| Extremely large value (`99999`) | "identify edge case inputs that might break the game and generate pytest cases" | `test_extremely_large_value_is_rejected` | Yes | Values above the difficulty maximum are out of range and must be caught at input time |


---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**

```
add professional-grade docstrings to every function in logic_utils.py,
review my code for PEP 8 style compliance and apply its suggestions to
resolve any formatting or naming issues it identifies
```

**Linting output before:**

```
Note: flake8 and pycodestyle were not installed in the environment.
The AI performed a manual PEP 8 audit and identified the following issues:

E302  logic_utils.py:6   expected 2 blank lines before load_high_scores(), found 1
E302  logic_utils.py:15  expected 2 blank lines before save_high_score(), found 1
E302  logic_utils.py:25  expected 2 blank lines before get_range_for_difficulty(), found 1
E501  logic_utils.py:55  line too long (134 > 79 characters) — FIX comment
E501  logic_utils.py:66  line too long (107 > 79 characters) — inline FIX comment
W291  logic_utils.py     missing type annotations on check_guess() and update_score()
```

**Changes applied:**

- Added 2 blank lines between every top-level function definition (E302 fix)
- Wrapped long FIX comment lines to stay within 79 characters (E501 fix)
- Added `-> tuple` and `-> int` return type annotations to `check_guess` and `update_score`
- Replaced single-line docstrings with full Google-style docstrings on all six functions, including `Args:`, `Returns:`, and `Raises:` sections where applicable

---

## Model Comparison (SF11)

> Compare two AI models on the same task.

**Task given to both models:**

<!-- Describe what you asked each model to do -->

| | Model A | Model B |
|-|---------|---------|
| **Model name** | | |
| **Response summary** | | |
| **More Pythonic?** | | |
| **Clearer explanation?** | | |

**Which did you prefer and why?**

<!-- Your conclusion -->
