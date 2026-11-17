# -*- coding: utf-8 -*-
"""
NOAA Storm Events
Phase 2: Data Cleaning

Author: Aaron Niecestro

Description
-----------
Cleans the land-based NOAA Storm Events dataset
created during Phase 1 and prepares the data
for feature engineering and modeling.

Input Dataset
-------------
df_land_regions

Output Dataset
--------------
clean_land_regions

Workflow
--------
1. Assess Missing Values
2. Remove Variables with >50% Missing Data
3. Remove Low-Value Location Variables
4. Convert Date Variables
5. Review Damage Variables
6. Validate Results
7. Review Cleaned Dataset

Cleaning Summary
----------------
Variables removed during cleaning are documented
within the script output along with dataset size,
remaining missing values, and data type validation.

Future Phase
------------
03_feature_engineering.py

Outcome A
---------
Storm Profiles

Outcome B
---------
Impact Categories
"""

# ==========================================
# IMPORTS
# ==========================================

import pandas as pd

# ==========================================
# CREATE CLEAN DATASET
# ==========================================

clean_land_regions = df_land_regions.copy()

print("=" * 60)
print("CREATE CLEAN DATASET")
print("=" * 60)

print(
    f"Rows: {clean_land_regions.shape[0]:,}"
)

print(
    f"Columns: {clean_land_regions.shape[1]}"
)

print()

# ==========================================
# ASSESS MISSING VALUES
# ==========================================

missing_summary = pd.DataFrame({
    "Missing Count": clean_land_regions.isnull().sum(),
    "Missing Percent": (
        clean_land_regions.isnull().mean() * 100
    ).round(2)
})

missing_summary = (
    missing_summary
    .sort_values(
        "Missing Percent",
        ascending=False
    )
)

print("=" * 60)
print("TOP MISSING VARIABLES")
print("=" * 60)

print(missing_summary.head(25))

print()


# ==========================================
# DROP COLUMNS >50% MISSING
# ==========================================

drop_cols = (
    missing_summary[
        missing_summary["Missing Percent"] > 50
    ]
    .index
    .tolist()
)

print("=" * 60)
print("COLUMNS TO DROP (>50% MISSING)")
print("=" * 60)

for col in drop_cols:
    print(col)

print()

pre_drop_cols = clean_land_regions.shape[1]

clean_land_regions.drop(
    columns=drop_cols,
    inplace=True,
    errors="ignore"
)

post_drop_cols = clean_land_regions.shape[1]

print("=" * 60)
print("POST-DROP DATASET")
print("=" * 60)

print(
    f"Rows: {clean_land_regions.shape[0]:,}"
)

print(
    f"Columns Before: {pre_drop_cols}"
)

print(
    f"Columns After: {post_drop_cols}"
)

print(
    f"Columns Removed: "
    f"{pre_drop_cols - post_drop_cols}"
)

print()


# ==========================================
# REVIEW 25%+ MISSING VARIABLES
# ==========================================

review_cols = (
    missing_summary[
        missing_summary["Missing Percent"] >= 25
    ]
    .index
    .tolist()
)

print("=" * 60)
print("REVIEW VARIABLES (25%+ MISSING)")
print("=" * 60)

for col in review_cols:
    print(col)

print()


# ==========================================
# DROP LOW-VALUE LOCATION VARIABLES
# ==========================================

print("=" * 60)
print("MISSING VALUES AFTER LOCATION REMOVAL")
print("=" * 60)

print(
    missing_summary.head(20)
)

print()

pre_drop_cols = clean_land_regions.shape[1]

drop_cols = [
    "BEGIN_RANGE",
    "BEGIN_AZIMUTH",
    "BEGIN_LOCATION",
    "END_RANGE",
    "END_AZIMUTH",
    "END_LOCATION"
]

clean_land_regions.drop(
    columns=drop_cols,
    inplace=True,
    errors="ignore"
)

post_drop_cols = clean_land_regions.shape[1]

print("=" * 60)
print("LOCATION VARIABLES REMOVED")
print("=" * 60)

for col in drop_cols:
    print(col)

print()

print(
    f"Columns Before: {pre_drop_cols}"
)

print(
    f"Columns After: {post_drop_cols}"
)

print(
    f"Columns Removed: "
    f"{pre_drop_cols - post_drop_cols}"
)

print()


# ==========================================
# MISSING VALUES AFTER LOCATION REMOVAL
# ==========================================

missing_summary = pd.DataFrame({
    "Missing Count":
        clean_land_regions.isnull().sum(),

    "Missing Percent":
        (
            clean_land_regions.isnull().mean()
            * 100
        ).round(2)
})

missing_summary = (
    missing_summary
    .sort_values(
        "Missing Percent",
        ascending=False
    )
)

print(
    missing_summary.head(20)
)

print()

# ==========================================
# REVIEW REMAINING HIGH-MISSING VARIABLES
# ==========================================

review_cols = [
    "MAGNITUDE",
    "BEGIN_LAT",
    "BEGIN_LON",
    "END_LAT",
    "END_LON",
    "DAMAGE_CROPS",
    "DAMAGE_PROPERTY",
    "EVENT_NARRATIVE",
    "EPISODE_NARRATIVE"
]

print("=" * 60)
print("REMAINING HIGH-MISSING VARIABLES")
print("=" * 60)

print(
    missing_summary.loc[
        review_cols
    ]
)

print()

# ==========================================
# CONVERT DATE VARIABLES
# ==========================================

date_cols = [
    "BEGIN_DATE_TIME",
    "END_DATE_TIME"
]

for col in date_cols:

    clean_land_regions[col] = pd.to_datetime(
        clean_land_regions[col],
        errors="coerce"
    )

print("=" * 60)
print("DATE VARIABLES CONVERTED")
print("=" * 60)

print(date_cols)

print()

print("Date Types")

print(
    clean_land_regions[
        date_cols
    ].dtypes
)

print()

print("Date Range")

print(
    clean_land_regions[
        date_cols
    ].agg(["min", "max"])
)

print()


# ==========================================
# REVIEW DAMAGE VARIABLES
# ==========================================

print("=" * 60)
print("PROPERTY DAMAGE VALUES")
print("=" * 60)

print(
    clean_land_regions["DAMAGE_PROPERTY"]
    .value_counts(dropna=False)
    .head(25)
)

print()

print(
    f"Unique Values: "
    f"{clean_land_regions['DAMAGE_PROPERTY'].nunique()}"
)

print()

print()

print("=" * 60)
print("CROP DAMAGE VALUES")
print("=" * 60)

print(
    clean_land_regions["DAMAGE_CROPS"]
    .value_counts(dropna=False)
    .head(25)
)

print()

print()

print(
    f"Unique Values: "
    f"{clean_land_regions['DAMAGE_CROPS'].nunique()}"
)

print()

# ==========================================
# VALIDATE RESULTS
# ==========================================

print("=" * 60)
print("VALIDATION")
print("=" * 60)

print(
    f"Rows: {clean_land_regions.shape[0]:,}"
)

print(
    f"Columns: {clean_land_regions.shape[1]}"
)

print()

print("Data Types")

print(
    clean_land_regions.dtypes.value_counts()
)

print()

print("=" * 60)
print("TOP REMAINING MISSING VARIABLES")
print("=" * 60)

missing_summary = pd.DataFrame({
    "Missing Count":
        clean_land_regions.isnull().sum(),

    "Missing Percent":
        (
            clean_land_regions.isnull().mean()
            * 100
        ).round(2)
})

missing_summary = (
    missing_summary
    .sort_values(
        "Missing Percent",
        ascending=False
    )
)

print(
    missing_summary.head(15)
)

print()

print("Columns Remaining")

print(
    clean_land_regions.columns.tolist()
)

print()

# ==========================================
# REVIEW DATA
# ==========================================

print("=" * 60)
print("DATA REVIEW")
print("=" * 60)

print()

print("Dataset Preview")

print(
    clean_land_regions.head()
)

print()

print("Top Event Types")

print(
    clean_land_regions["EVENT_TYPE"]
    .value_counts()
    .head(10)
)

print()

print("Geographic Coverage")

print(
    f"States/Territories: "
    f"{clean_land_regions['STATE'].nunique()}"
)

print()

print("Date Coverage")

print(
    clean_land_regions[
        [
            "BEGIN_DATE_TIME",
            "END_DATE_TIME"
        ]
    ]
    .agg(["min", "max"])
)

print()

# ==========================================
# CLEANING SUMMARY
# ==========================================

original_cols = 52
final_cols = clean_land_regions.shape[1]

print("=" * 60)
print("CLEANING SUMMARY")
print("=" * 60)

print(
    f"Original Rows: "
    f"{df_land_regions.shape[0]:,}"
)

print(
    f"Final Rows: "
    f"{clean_land_regions.shape[0]:,}"
)

print()

print(
    f"Original Columns: "
    f"{original_cols}"
)

print(
    f"Final Columns: "
    f"{final_cols}"
)

print(
    f"Columns Removed: "
    f"{original_cols - final_cols}"
)

print(
    f"Percent Reduction: "
    f"{round((original_cols-final_cols)/original_cols*100,2)}%"
)

print()

# ==========================================
# SCRIPT COMPLETE
# ==========================================

print("=" * 60)
print("SCRIPT COMPLETE")
print("=" * 60)

print(
    f"Final Rows: "
    f"{clean_land_regions.shape[0]:,}"
)

print(
    f"Final Columns: "
    f"{clean_land_regions.shape[1]}"
)
