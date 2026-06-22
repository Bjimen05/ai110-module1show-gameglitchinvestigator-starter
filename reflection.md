# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

 The first time I ran the game, it was buggy, the show hint didn't show when I guessed wrong, the hint was wrong, as it say to go lower even though the right number was higher (ex. secret is 29, I guess 20, hint say to go lower), when you change the difficulty, the game didn't update to the right range (ex. if I change the difficulty from normal to easy, the game will display "1 - 100" instead of "1 - 20") and the history will also not update when changing difficulty.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input       | Expected Behavior | Actual Behavior | Console Output / Error |
|-------------|-------------------|-----------------|------------------------|
| 65          | Go Higher         | Go Lower        | None                   |
|-------------|-------------------|-----------------|------------------------|
|-5           | Incorrect Number  | Go Lower        | None                   |
|-------------|-------------------|-----------------|------------------------|
|Nothing      | "Enter a guess"   | "Enter a guess" | Attempts left: -56     |
|-------------|-------------------|-----------------|------------------------|
|Click "Easy" | Have more attempts|Less attempts    |                        |
|             | than normal &     |than normal &    |                        |
|             | hard              |hard             |                        |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

*I use ChatGPT and Claude on this project.
*One of an AI suggestion that was correct is suggesting refactoring the logic into the logic_utils.py correctly, and I verified the result by manually testing it
*One of an AI suggestion that was incorrect is it didn't include the incorrect attempt limits for each difficulty. Which I have to manually look at logic_utilis.py and the AI chat.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

*I first run pytest by having it create cases that test whether the secret number matches the guess number, it show me that one case the guess was greater than the secret, one case where the guess is the same as the secret, one case the guess was less than the secret and display the hints. The AI help me understand how to create edge-cases and how to focus on specific bugs.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
