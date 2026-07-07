# Assignment 1: Python - Data Structures

## Overview
This repository contains my solution for the first Python Data Structures assignment. The goal of this project is to build a simple inventory management utility for an e-commerce store using only standard Python concepts (lists, tuples, sets, and dictionaries). 

There are no external libraries (like Pandas or NumPy) used in this script, keeping the logic clean and focused on core data structures.

## Breakdown of Tasks

The code is divided into four main sections:

* Task 1: Product Collections (Lists & Tuples)
  Sets up the basic inventory. It uses a list for product names and a tuple to structure a sample product. It also handles basic list operations like appending new items and grabbing specific items using zero-based and negative indexing.

* Task 2: Categories (Sets)
  Demonstrates how to handle unique values. It takes a parallel list of product categories and converts it into a set to automatically remove any duplicate entries. It also includes logic to add new categories and check if a specific category already exists.

* Task 3: Product Pricing (Dictionaries)
  Manages the pricing data. It links product names (keys) to their prices (values). This section includes operations to add new prices, update existing ones, and safely remove items using an `if/else` block to prevent the program from crashing if an item isn't found. It also calculates the average price of the entire inventory.

* Task 4: Combined Operations
  This ties everything together. It uses `zip()` to combine the isolated lists and dictionary into a master `catalog` (a list of tuples). It then loops through that catalog to dynamically generate a new dictionary that acts like a filing cabinet, sorting lists of products into their respective categories. Finally, it calculates and prints the category that contains the highest number of products.

## How to Run
1. Ensure you have Python installed on your machine.
2. Open the main `.py` file in your preferred IDE or terminal.
3. Run the script. The outputs for each task will print sequentially to the console.
