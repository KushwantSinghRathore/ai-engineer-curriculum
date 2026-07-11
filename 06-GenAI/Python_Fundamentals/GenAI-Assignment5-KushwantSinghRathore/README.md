# Python Fundamentals: Modules, Packages, and File I/O

Welcome to my Python repository! This collection represents my foundational work in Python, focusing on writing clean, modular code and handling data operations efficiently.

## Project Overview

This project is structured into logical components to demonstrate professional code organization:

* **Utility Modules:** Standalone files for math and string operations.
* **Custom Package:** A modularized `shop_package` for e-commerce logic.
* **Core Logic (`main.py`):** The driver script that integrates all modules and packages.

---

## Repository Structure

```text
project_folder/
│   main.py               # Main execution script
│   math_utils.py         # Math utility module
│   string_utils.py       # String manipulation module
└───shop_package/         # Custom package for shop logic
        __init__.py       # Package initialization
        billing.py        # Tax and total calculations
        discount.py       # Discount logic

```

---

## Task Details

### 1. Math Utility Module (`math_utils.py`)

Provides basic arithmetic functions including `add()`, `subtract()`, and `square()`. Demonstrates how to import modules using both full names and specific function imports.

### 2. String Utility Module (`string_utils.py`)

Contains tools for text processing:

* `capitalize_words()`: Uses `.title()` to format strings.
* `reverse_string()`: Uses slice notation `[::-1]` for efficient reversal.
* `word_count()`: Uses `.split()` to determine the number of words.

### 3. Shopping Package (`shop_package/`)

A structured approach to project organization.

* **`billing.py`**: Handles `calculate_total()` and `apply_tax()`.
* **`discount.py`**: Manages `apply_discount()` and `flat_discount()`.
* **`__init__.py`**: Exposes package functions directly, allowing for clean imports like `from shop_package import ...`.

---

## Key Concepts Applied

* **Modular Programming:** Breaking code into small, reusable files to keep the main logic clean.
* **Package Architecture:** Converting directories into importable packages using `__init__.py`.
* **Namespace Management:** Utilizing aliases (`import ... as ...`) to prevent name collisions in complex projects.
* **DRY Principle (Don't Repeat Yourself):** Creating shared utility modules that can be imported into any future project.

## How to Run

1. Ensure all files are in the same folder as shown in the structure above.
2. Open your terminal or command prompt.
3. Run the main script:
```bash
python main.py

```



---

*This assignment was a fantastic exercise in moving beyond single-script programming into building scalable, organized software architectures.*