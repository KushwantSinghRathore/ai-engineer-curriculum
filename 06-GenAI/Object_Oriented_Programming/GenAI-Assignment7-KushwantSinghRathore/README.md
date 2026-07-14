# Python OOP & Exception Handling Assignments

Hi! This is the repository for my Python assignments. These tasks were a great way for me to move from writing simple scripts to building more structured, reliable programs. I focused on two main areas: making code "unbreakable" using error handling, and organizing complex logic using Object-Oriented Programming (OOP).

---

## 📁 Project Overview

### Section 1: Exception Handling

I learned that good code anticipates when things might go wrong. Instead of letting the program crash, I used `try-except` blocks to handle errors gracefully and keep the program running.

* **Key Skills:** Using `try-except` for user input, handling file errors, and using `raise` to enforce my own rules (like preventing negative prices).

### Section 2: Object-Oriented Programming (OOP)

This was all about grouping data and behavior together to make code easier to manage and reuse.

* **Key Concepts:**
* **Encapsulation:** Keeping data private (using `__price`) so it can't be changed accidentally.
* **Inheritance:** Creating new classes that "inherit" features from a parent, which saved me from repeating code.
* **Polymorphism:** Writing code that can interact with different types of objects using the same method names.
* **Abstraction:** Creating a "blueprint" for other classes to follow, ensuring consistency.
* **Magic Methods:** Customizing how objects behave, like making `+` work between two products.



---

## 🛠 Tasks Breakdown

| Task | Topic | Description |
| --- | --- | --- |
| **Task 1** | Basic Class | Defining simple `Product` classes with attributes and methods. |
| **Task 2** | Encapsulation | Using getters and setters to protect sensitive data like price. |
| **Task 3** | Inheritance | Creating `ElectronicProduct` to inherit and override base class methods. |
| **Task 4** | Polymorphism | Demonstrating how different objects respond to the same method call. |
| **Task 5** | Abstraction | Enforcing a payment structure using Abstract Base Classes (`ABC`). |
| **Task 6** | Magic Methods | Adding `__str__` and `__add__` to make classes act like built-in types. |
| **Task 7** | Mini Project | Building an `Inventory` system to manage products and demonstrate OOP in action. |

---

## 🚀 How to Run

These scripts are written in standard Python 3 and don't require any external libraries. Just download the files and run them in your terminal. For example, to test the final inventory system:

```bash
python Task7.py

```

---

*Overall, these assignments helped me realize that "good code" isn't just code that works—it's code that is easy to read, test, and maintain. Thanks for taking the time to check out my work!*