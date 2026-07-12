Python Exception Handling Project
Hi! This repository contains my work on learning Exception Handling in Python. The goal of these assignments was to move beyond writing code that "just works" under perfect conditions and start building programs that can handle real-world errors—like bad user input, missing files, or incorrect data—without crashing.

📁 Tasks Overview
Task	Focus	What I Learned
Task 1	Safe Division	How to catch ZeroDivisionError and ValueError so the program stays alive.
Task 2	Bill Calculator	How to use a loop to process a list, skip bad data, and use raise for custom rules.
Task 3	Age Validator	How to separate validation logic into a function and handle custom ValueError exceptions.
Task 4	File Reader	How to manage file system errors like FileNotFoundError and PermissionError.
Task 5	Shopping Cart	How to build an interactive tool that validates price input in real-time.
🛠 Concepts I Practiced
Try-Except Blocks: Wrapping "dangerous" code to prevent crashes.

Specific Error Catching: Using different except blocks to give better feedback to the user (e.g., distinguishing between a file being missing vs. a file being locked).

Custom Exceptions: Using the raise keyword to define my own rules (like "no negative prices").

Resource Management: Using finally to ensure clean-up operations happen, even if something goes wrong.

🚀 How to Run
Each task is a standalone Python file. You can run any of them by opening your terminal and typing:

Bash
python Task1.py
This was a really helpful way to learn how to write "defensive" code. I feel much more confident now about building programs that are resilient and user-friendly!