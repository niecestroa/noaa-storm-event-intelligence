# -*- coding: utf-8 -*-
"""
NOAA Storm Events
Phase 1: Data Acquisition & Assessment

Author: Aaron Niecestro

Description
-----------
This script downloads NOAA Storm Events data from 2000-2026, combines all 
years into a single dataset, and performs an initial assessment of data 
quality, missing values, event types, and geographic coverage.

Datasets Created
----------------
df_all_regions
    Complete NOAA dataset including:
    - States
    - Territories
    - Marine Regions
    - Great Lakes Regions

df_land_regions
    Primary analytical dataset including:
    - States
    - District of Columbia
    - Territories

    Excludes:
    - Marine Regions
    - Great Lakes Regions

Outputs
-------
- All-regions dataset
- Land-regions dataset
- Dataset dimensions
- Missing-value assessment
- Event-type assessment
- Geographic-region assessment
- Injury and fatality assessment
- Damage-field assessment
- Candidate columns for removal

Future Phases
-------------
02_data_cleaning.py
03_feature_engineering.py

Outcome A:
Storm Profiles

Outcome B:
Impact Categories
"""

# ==========================================
# IMPORTS
# ==========================================

import pandas as pd
import re

# ==========================================
# NOAA FILE LIST
# ==========================================

base_url =(
    "https://www.ncei.noaa.gov/pub/data/swdi/stormevents/csvfiles/"
    )

files = [
    "StormEvents_details-ftp_v1.0_d2000_c20260323.csv.gz",
    "StormEvents_details-ftp_v1.0_d2001_c20260323.csv.gz",
    "StormEvents_details-ftp_v1.0_d2002_c20260323.csv.gz",
    "StormEvents_details-ftp_v1.0_d2003_c20260323.csv.gz",
    "StormEvents_details-ftp_v1.0_d2004_c20260323.csv.gz",
    "StormEvents_details-ftp_v1.0_d2005_c20260323.csv.gz",
    "StormEvents_details-ftp_v1.0_d2006_c20260323.csv.gz",
    "StormEvents_details-ftp_v1.0_d2007_c20260323.csv.gz",
    "StormEvents_details-ftp_v1.0_d2008_c20260323.csv.gz",
    "StormEvents_details-ftp_v1.0_d2009_c20260323.csv.gz",
    "StormEvents_details-ftp_v1.0_d2010_c20260323.csv.gz",
    "StormEvents_details-ftp_v1.0_d2011_c20260323.csv.gz",
    "StormEvents_details-ftp_v1.0_d2012_c20261026.csv.gz",
    "StormEvents_details-ftp_v1.0_d2013_c20260323.csv.gz",
    "StormEvents_details-ftp_v1.0_d2014_c20260323.csv.gz",
    "StormEvents_details-ftp_v1.0_d2015_c20260323.csv.gz",
    "StormEvents_details-ftp_v1.0_d2016_c20260323.csv.gz",
    "StormEvents_details-ftp_v1.0_d2017_c20260519.csv.gz",
    "StormEvents_details-ftp_v1.0_d2018_c20260323.csv.gz",
    "StormEvents_details-ftp_v1.0_d2019_c20260323.csv.gz",
    "StormEvents_details-ftp_v1.0_d2020_c20260323.csv.gz",
    "StormEvents_details-ftp_v1.0_d2021_c20260323.csv.gz",
    "StormEvents_details-ftp_v1.0_d2022_c20260625.csv.gz",
    "StormEvents_details-ftp_v1.0_d2023_c20260323.csv.gz",
    "StormEvents_details-ftp_v1.0_d2024_c20260728.csv.gz",
    "StormEvents_details-ftp_v1.0_d2025_c20260819.csv.gz",
    "StormEvents_details-ftp_v1.0_d2026_c20261026.csv.gz"
]

# ==========================================
# LOAD DATA
# ==========================================

dfs = []

for file in files:

    # Extract source year from filename

    year = re.search(
        r"_d(\d{4})_",
        file
    ).group(1)

    print(f"Loading {year}")

    # Read NOAA file

    temp = pd.read_csv(
        base_url + file,
        compression="gzip",
        low_memory=False
    )

    # Track source file year

    temp["SOURCE_YEAR"] = int(year)

    # Store dataset

    dfs.append(temp)

print("\nAll files loaded successfully.")
print(f"Files Loaded: {len(dfs)}")

# ==========================================
# CREATE ALL REGIONS DATASET
# ==========================================

df_all_regions = pd.concat(
    dfs,
    ignore_index=True
)

print("\nALL REGIONS DATASET")
print("=" * 60)

print(
    f"Rows: {df_all_regions.shape[0]:,}"
)

print(
    f"Columns: {df_all_regions.shape[1]}"
)

print(
    "\nMemory Usage (MB):"
)

print(
    round(
        df_all_regions.memory_usage(
            deep=True
        ).sum() / 1024**2,
        2
    )
)

print(
    "\nRows Per YEAR:"
)

print(
    df_all_regions["YEAR"]
      .value_counts()
      .sort_index()
)

print("\nGeographic Regions:")

print(
    df_all_regions["STATE"]
    .nunique()
)

print(
    "\nRows Per SOURCE_YEAR:"
)

print(
    df_all_regions["SOURCE_YEAR"]
      .value_counts()
      .sort_index()
)

# ==========================================
# CREATE LAND REGIONS DATASET
# ==========================================

exclude_regions = [
    "ATLANTIC NORTH",
    "ATLANTIC SOUTH",
    "E PACIFIC",
    "GULF OF ALASKA",
    "GULF OF MEXICO",
    "HAWAII WATERS",
    "GUAM WATERS",
    "LAKE ERIE",
    "LAKE HURON",
    "LAKE MICHIGAN",
    "LAKE ONTARIO",
    "LAKE ST CLAIR",
    "LAKE SUPERIOR",
    "ST LAWRENCE R"
]

df_land_regions = df_all_regions[
    ~df_all_regions["STATE"].isin(
        exclude_regions
    )
].copy()

print("\nLAND REGIONS DATASET")
print("=" * 60)

print(
    f"Rows: {df_land_regions.shape[0]:,}"
)

print(
    f"Columns: {df_land_regions.shape[1]}"
)

print(
    "\nGeographic Regions:"
)

print(
    df_land_regions["STATE"]
    .nunique()
)

states = sorted(
    df_land_regions["STATE"]
    .dropna()
    .unique()
)

print(
    f"\nUnique Regions: "
    f"{len(states)}"
)

for state in states:
    print(state)

# ==========================================
# DATA ASSESSMENT
# ==========================================

# ------------------------------------------
# DATASET OVERVIEW
# ------------------------------------------

print("=" * 60)
print("DATASET OVERVIEW")
print("=" * 60)

print(
    f"Rows: {df_land_regions.shape[0]:,}"
)

print(
    f"Columns: {df_land_regions.shape[1]}"
)

print()

print("=" * 60)
print("DATA TYPES")
print("=" * 60)

print(
    df_land_regions.dtypes.value_counts()
)

print()


# ------------------------------------------
# MISSING VALUES
# ------------------------------------------

missing_summary = pd.DataFrame({
    "Missing Count":
        df_land_regions.isnull().sum(),

    "Missing Percent":
        (
            df_land_regions.isnull().mean()
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

print("=" * 60)
print("TOP 25 MISSING VARIABLES")
print("=" * 60)

print(
    missing_summary.head(25)
)

print()


# ------------------------------------------
# EVENT TYPES
# ------------------------------------------

print("=" * 60)
print("EVENT TYPES")
print("=" * 60)

print(
    f"Unique Event Types: "
    f"{df_land_regions['EVENT_TYPE'].nunique()}"
)

print()

print(
    df_land_regions["EVENT_TYPE"]
    .value_counts()
    .head(20)
)

print()


# ------------------------------------------
# GEOGRAPHIC REGIONS
# ------------------------------------------

print("=" * 60)
print("GEOGRAPHIC REGIONS")
print("=" * 60)

print(
    f"Unique Regions: "
    f"{df_land_regions['STATE'].nunique()}"
)

print()


# ------------------------------------------
# INJURIES & DEATHS
# ------------------------------------------

print("=" * 60)
print("INJURIES & DEATHS")
print("=" * 60)

print(
    df_land_regions[
        [
            "INJURIES_DIRECT",
            "DEATHS_DIRECT"
        ]
    ].describe()
)

print()


# ------------------------------------------
# PROPERTY DAMAGE
# ------------------------------------------

print("=" * 60)
print("PROPERTY DAMAGE EXAMPLES")
print("=" * 60)

print(
    df_land_regions["DAMAGE_PROPERTY"]
    .dropna()
    .value_counts()
    .head(20)
)

print()


# ------------------------------------------
# CROP DAMAGE
# ------------------------------------------

print("=" * 60)
print("CROP DAMAGE EXAMPLES")
print("=" * 60)

print(
    df_land_regions["DAMAGE_CROPS"]
    .dropna()
    .value_counts()
    .head(20)
)

print()

# ------------------------------------------
# SCRIPT COMPLETE
# ------------------------------------------

print("=" * 60)
print("SCRIPT COMPLETE")
print("=" * 60)