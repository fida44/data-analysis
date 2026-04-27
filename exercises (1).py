"""
=============================================================
  Week 2 — Data Analysis with Pandas
  Workshop Exercises — Starter File
=============================================================
  Instructions:
  - Fill in each section marked with  # YOUR CODE HERE
  - Run the file with:  python exercises.py
  - Uncomment test lines to check your answers
=============================================================
"""

import pandas as pd
import numpy as np

print("=" * 60)
print("  WEEK 2 PANDAS WORKSHOP EXERCISES")
print("=" * 60)


# ─────────────────────────────────────────────────────────────
# EXERCISE 1 — Series Basics
# ─────────────────────────────────────────────────────────────
print("\n--- Exercise 1: Series Basics ---\n")

# 1a. Create a Series of temperatures for 7 days
temps_data = [22, 25, 19, 28, 30, 24, 21]
days       = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

# YOUR CODE HERE — create the Series
temps = None  # Replace None with your code



# 1b. Find the hottest day, coldest day, average temperature
print("Hottest day:  ", None)   # YOUR CODE HERE
print("Coldest day:  ", None)   # YOUR CODE HERE
print("Average temp: ", None)   # YOUR CODE HERE

# 1c. Filter days where temp > 24
print("\nDays with temp > 24:")
# YOUR CODE HERE

# 1d. BONUS — Add 2 degrees to all temperatures
print("\nTemps + 2 degrees:")
# YOUR CODE HERE


# ─────────────────────────────────────────────────────────────
# EXERCISE 2 — DataFrame Creation
# ─────────────────────────────────────────────────────────────
print("\n--- Exercise 2: DataFrame Creation ---\n")

# 2a. Create a products DataFrame
products_data = {
    'Product':  ['Rice 5kg', 'Sugar 1kg', 'Tea 200g', 'Milk 1L', 'Bread'],
    'Category': ['Grocery', 'Grocery', 'Beverage', 'Dairy', 'Bakery'],
    'Price':    [850, 180, 320, 220, 120],
    'Stock':    [120, 45, 80, 30, 60],
    'Rating':   [4.5, 3.8, 4.2, 4.7, 3.5]
}

# YOUR CODE HERE — create the DataFrame
df_products = None  # Replace with pd.DataFrame(...)



# 2b. Display shape, dtypes, basic stats
print("Shape:  ", None)  # YOUR CODE HERE
print("\nData types:\n")
# YOUR CODE HERE — print dtypes
print("\nStatistics:\n")
# YOUR CODE HERE — print describe()

# 2c. Select only Product and Price columns
print("\nProduct & Price only:")
# YOUR CODE HERE

# 2d. Filter: Stock > 50 AND Rating >= 4
print("\nHigh-stock, high-rated products:")
# YOUR CODE HERE

# 2e. Add Discounted_Price column (15% off)
# YOUR CODE HERE

# 2f. Sort by Rating descending, then Price ascending
print("\nSorted products:")
# YOUR CODE HERE


# ─────────────────────────────────────────────────────────────
# EXERCISE 3 — Indexing & Selection (.loc / .iloc)
# ─────────────────────────────────────────────────────────────
print("\n--- Exercise 3: Indexing & Selection ---\n")

# Load the students dataset
df = pd.read_csv('data/students.csv')
print("Students dataset loaded:")
print(df.head())
print()

# 3a. Select first 3 students using .iloc
print("First 3 students (.iloc):")
# YOUR CODE HERE

# 3b. Select all students from 'Karachi' using .loc boolean
print("\nStudents from Karachi (.loc):")
# YOUR CODE HERE

# 3c. Set StudentID as index, then select row 'S003'
# YOUR CODE HERE — set_index
print("\nStudent S003:")
# YOUR CODE HERE — .loc['S003']

# 3d. Using .iloc — rows 2-4, columns Score and Grade
df_reset = df.reset_index(drop=True)
print("\nRows 2-4, Score & Grade (.iloc):")
# YOUR CODE HERE — hint: find column positions first with df.columns

# 3e. CHALLENGE — Highest scorer in each city
print("\nHighest scorer per city:")
# YOUR CODE HERE — hint: groupby + idxmax or nlargest


# ─────────────────────────────────────────────────────────────
# BONUS EXERCISE — Real Dataset
# ─────────────────────────────────────────────────────────────
print("\n--- BONUS: Real Dataset Exploration ---\n")

# Load Titanic or any CSV you have
# df_titanic = pd.read_csv('data/titanic.csv')

# 1. Passenger count per class
# print(df_titanic['Pclass'].value_counts())

# 2. Average age by class
# print(df_titanic.groupby('Pclass')['Age'].mean())

# 3. Female survivors
# survivors = df_titanic[(df_titanic['Sex'] == 'female') & (df_titanic['Survived'] == 1)]

# 4. AgeBucket column
# def age_bucket(age):
#     if age < 18: return 'Child'
#     elif age <= 60: return 'Adult'
#     else: return 'Senior'
# df_titanic['AgeBucket'] = df_titanic['Age'].apply(age_bucket)

# 5. Survival rate by AgeBucket
# print(df_titanic.groupby('AgeBucket')['Survived'].mean() * 100)

print("Great job! Check answers in solutions.py")
