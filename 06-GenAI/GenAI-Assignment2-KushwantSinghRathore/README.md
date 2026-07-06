Python Sales & Management System
This project contains a collection of Python scripts designed to handle sales data, inventory processing, and interactive menu-driven applications.

Table of Contents
Task 1: Basic Input Validation

Task 2: Sales Discount Engine

Task 3: Interactive Menu System

Task 4: Data Sanitization & Flow Control

Task 1: Basic Input Validation
Objective: Ensure user inputs are numeric and valid.

Key Concept: isdigit() validation to prevent program crashes.

Task 2: Sales Discount Engine
Objective: Apply tiered discounts based on order volume.

Logic: * >= 2000: 15% discount

>= 1500: 10% discount

>= 1000: 7% discount

Key Concept: for loops and conditional (if/elif/else) branching.

Task 3: Interactive Menu System
Objective: Create a persistent, running-list application.

Key Concept: while True loop, list.append(), and break/continue control.

How to run: Run the script and follow the menu prompts to add orders or view the summary table.

Task 4: Data Sanitization & Flow Control
Objective: Process a list of sales while handling corrupt or missing data.

Logic:

-1: Treated as corrupted data; the process stops immediately (break).

0: No sales recorded; the process skips to the next item (continue).

Positive Values: Added to the running total.

Key Concept: Error handling via flow control.