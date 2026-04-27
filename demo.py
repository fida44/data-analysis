# ============================================================
#  WEEK 2 — DATA ANALYSIS WITH PANDAS
#  Always run this cell first before anything else!
# ============================================================

import pandas as pd        # pandas  → for data tables
import numpy as np         # numpy   → for numbers/math

# Check pandas is working
print("✅ Pandas version:", pd.__version__)
print("✅ NumPy  version:", np.__version__)
print("✅ Ready to start!")


# ============================================================
#  DEMO 1: PANDAS SERIES — Creating in 3 different ways
# ============================================================
# A Series = one column of data with labels (like Excel column)
# Structure:  Index (label)  →  Value
# ============================================================

# ── WAY 1: From a simple Python list ──────────────────────
# When you don't give labels, pandas uses 0, 1, 2, 3...
s1 = pd.Series([10, 20, 30, 40, 50])
print("📦 Basic Series (no custom labels):")
print(s1)

# ── WAY 2: List + custom index (labels) ───────────────────
# Now each value has a meaningful name instead of 0,1,2...
s2 = pd.Series(
    [85, 92, 78, 95, 88],            # ← the values (scores)
    index=['Ali', 'Sara', 'John', 'Mia', 'Leo'],  # ← the labels
    name='Exam Scores'               # ← name of the whole Series
)
print("\n📦 Series with custom labels (student scores):")
print(s2)

# ── WAY 3: From a Dictionary ──────────────────────────────
# Dictionary keys automatically become the index labels
grades_dict = {
    'Math':    90,
    'Science': 85,
    'English': 78,
    'History': 92
}
s3 = pd.Series(grades_dict)
print("\n📦 Series from Dictionary (subject grades):")
print(s3)

# ── NOTICE ────────────────────────────────────────────────
# All 3 Series look similar when printed:
#   Label   Value
#   -----   -----
print("\n✅ DEMO 1 done! All 3 ways create the same structure.")



# ============================================================
#  DEMO 2: SERIES ATTRIBUTES — Learning about your data
# ============================================================
# After creating a Series, these are the things you can check
# Think of them as "questions you can ask your data"
# ============================================================

# We use s2 from DEMO 1 (student exam scores)
# s2 = Ali:85, Sara:92, John:78, Mia:95, Leo:88

print("📊 Our Series (s2):")
print(s2)
print()

# ── .values → What numbers are inside? ────────────────────
print("1️⃣  s2.values  →", s2.values)
#    Returns a NumPy array of just the numbers

# ── .index → What are the labels? ─────────────────────────
print("2️⃣  s2.index   →", list(s2.index))
#    Returns all the row labels

# ── .dtype → What type of data? ───────────────────────────
print("3️⃣  s2.dtype   →", s2.dtype)
#    int64 = whole numbers, float64 = decimals, object = text

# ── .shape → How big is it? ───────────────────────────────
print("4️⃣  s2.shape   →", s2.shape)
#    (5,) means 5 rows, 1 column (it's 1D so no second number)

# ── .size → How many elements? ────────────────────────────
print("5️⃣  s2.size    →", s2.size)

print()
print("─"*40)
print("📐 MATH operations:")
print("─"*40)

# ── Math operations ────────────────────────────────────────
print("Mean  (average) :", s2.mean())   # sum ÷ count
print("Max   (highest) :", s2.max())    # biggest number
print("Min   (lowest)  :", s2.min())    # smallest number
print("Sum   (total)   :", s2.sum())    # all added together
print("Count (how many):", s2.count())  # number of values

print()
print("─"*40)
print("🏆 Finding WHO has the highest/lowest:")
print("─"*40)

# ── idxmax / idxmin → returns the LABEL of max/min ────────
print("Top student   :", s2.idxmax(), "with score", s2.max())
print("Lowest student:", s2.idxmin(), "with score", s2.min())

print()
# ── .describe() → gives ALL stats at once ─────────────────
print("📋 describe() — Full Summary:")
print(s2.describe())

print("\n✅ DEMO 2 done! Now you know how to explore a Series.")




# ============================================================
#  DEMO 3: SERIES SELECTION — Getting values you want
# ============================================================
# 3 ways to select data from a Series:
#   1. By label name  → s['Ali']
#   2. By position    → s.iloc[0]
#   3. By condition   → s[s > 88]
# ============================================================

print("📊 Our Series (s2):")
print(s2)
print()

# ── METHOD 1: Select by LABEL name ────────────────────────
print("─"*40)
print("METHOD 1: Select by label name")
print("─"*40)

print("s2['Ali']        =", s2['Ali'])        # single value
print("s2['Mia']        =", s2['Mia'])        # single value

# Select multiple labels at once using a list
print("\nMultiple labels at once:")
print(s2[['Ali', 'Mia', 'Leo']])              # returns a Series

# ── METHOD 2: Select by POSITION (iloc) ───────────────────
print("\n─"*40)
print("METHOD 2: Select by position using .iloc")
print("─"*40)
# iloc = integer location (position number, starts from 0)

print("s2.iloc[0]  = first  item →", s2.iloc[0])   # Ali=85
print("s2.iloc[1]  = second item →", s2.iloc[1])   # Sara=92
print("s2.iloc[-1] = last   item →", s2.iloc[-1])  # Leo=88

# Slice: from position 0 up to (NOT including) position 3
print("\nFirst 3 students (iloc[0:3]):")
print(s2.iloc[0:3])

# ── IMPORTANT DIFFERENCE ──────────────────────────────────
print("\n⚠️  KEY DIFFERENCE — memorize this!")
print("  s2['Ali':'John']  → label slice → INCLUDES John")
print(s2['Ali':'John'])    # includes 'John' ✅

print("\n  s2.iloc[0:3]      → position slice → EXCLUDES position 3")
print(s2.iloc[0:3])        # excludes position 3 ✅

# ── METHOD 3: Filter by CONDITION ─────────────────────────
print("\n─"*40)
print("METHOD 3: Filter by condition (Boolean Masking)")
print("─"*40)
# This is like asking: "show me only rows where score > 88"

print("Students with score > 88:")
print(s2[s2 > 88])

print("\nStudents with score between 80 and 92:")
print(s2[(s2 >= 80) & (s2 <= 92)])   # & means AND

print("\nStudents with score < 80 OR score > 93:")
print(s2[(s2 < 80) | (s2 > 93)])     # | means OR

print("\n✅ DEMO 3 done! 3 ways to select: label, position, condition.")




# ============================================================
#  DEMO 4: PANDAS DATAFRAME — The main data structure
# ============================================================
# DataFrame = a full TABLE (like an Excel spreadsheet)
# Think of it as:  many Series stuck together side by side
#
#   Name      Age    City        Score
#   ──────────────────────────────────
#   Alice      24    Karachi      88.5   ← each row = one record
#   Bob        27    Lahore       92.0
#   ...
#   ↑ each column = one Series
# ============================================================

# ── CREATING a DataFrame from a Dictionary ─────────────────
# Keys   = column names
# Values = lists of data (all lists must be same length!)

data = {
    'Name':  ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'Age':   [24,      27,    22,        32,      29],
    'City':  ['Karachi','Lahore','Islamabad','Karachi','Quetta'],
    'Score': [88.5,    92.0,  75.5,      95.0,    83.5]
}

# Create the DataFrame
df = pd.DataFrame(data)

print("📊 Our DataFrame:")
print(df)
print()

# ── EXPLORING the DataFrame ────────────────────────────────
print("─"*40)
print("Basic information about our table:")
print("─"*40)

# Shape → (rows, columns)
print("Shape (rows, cols) :", df.shape)
#   (5, 4) = 5 students, 4 columns

# Column names
print("Column names       :", list(df.columns))

# Index (row labels — default is 0,1,2...)
print("Row index          :", list(df.index))

print()
print("─"*40)
print("Data types of each column:")
print("─"*40)
print(df.dtypes)
# object  = text (strings)
# int64   = whole numbers
# float64 = decimal numbers

print()
print("─"*40)
print("Statistical summary (.describe()):")
print("─"*40)
print(df.describe())
# Only shows NUMBER columns automatically
# count = how many, mean = average, std = spread, min/max etc.

print()
print("─"*40)
print("Quick peek — first 3 rows (.head(3)):")
print("─"*40)
print(df.head(3))   # default is 5, but we use 3 here

print()
print("─"*40)
print("Check for missing values (.isnull()):")
print("─"*40)
print(df.isnull().sum())
# 0 means no missing values in that column — good!

print("\n✅ DEMO 4 done! You created and explored your first DataFrame!")
print("   Next: selecting columns, filtering rows, .loc vs .iloc")