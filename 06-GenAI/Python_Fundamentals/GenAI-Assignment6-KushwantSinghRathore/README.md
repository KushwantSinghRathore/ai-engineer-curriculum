"""# Exception Handling & Data Validation Projects

Welcome to my repository! This collection of Python scripts demonstrates a deep dive into **Exception Handling** and **Data Validation** techniques. These tasks were designed to build robust, crash-proof programs that gracefully handle unexpected user input, file system errors, and data inconsistencies.

## 📁 Repository Contents

| Task | File Name | Description |
| :--- | :--- | :--- |
| **Task 1** | `Task1.py` | **Safe Division Utility:** Implements `try-except` blocks to handle non-integer inputs (`ValueError`) and division by zero (`ZeroDivisionError`). |
| **Task 2** | `Task2.py` | **Bill Calculator:** Iterates through a list of mixed data, skipping invalid types and negative values using custom exception raising. |
| **Task 3** | `Task3.py` | **Age Validator:** Uses a custom function to validate age ranges, demonstrating how to `raise` and catch custom `ValueError` exceptions. |
| **Task 4** | `Task4.py` | **Safe File Reader:** Reads the first three lines of a user-provided file while handling `FileNotFoundError` and `PermissionError` scenarios. |
| **Task 5** | `Task5.py` | **Safe Shopping Cart:** An interactive CLI tool that collects prices, validates input in real-time, and generates a final receipt summary. |

---

## 🛠 Key Concepts Applied

* **Graceful Degradation:** Ensuring programs stay running even when faced with bad data.
* **Granular Exception Handling:** Distinguishing between `ValueError`, `TypeError`, `FileNotFoundError`, and `PermissionError` to provide accurate user feedback.
* **Custom Validation Logic:** Using the `raise` keyword to enforce business rules (like "no negative prices").
* **Resource Cleanup:** Utilizing the `finally` block to ensure operations (like file access) are finalized regardless of success or failure.

## 🚀 How to Run
Each file is a self-contained program. You can run any task by executing it in your terminal:
```bash
python Task1.py