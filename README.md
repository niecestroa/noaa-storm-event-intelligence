# NOAA Storm Event Intelligence

> [!WARNING]
> This project is currently under active development. Data acquisition, assessment, and initial data cleaning have been completed. Feature engineering, modeling, deep learning, and MLOps workflows remain in progress. Methods, project structure, and results may change throughout development.

Analysis of National Oceanic and Atmospheric Administration (NOAA) Storm Events data from 2000–2026 to develop storm profiles, impact categories, and machine learning workflows.

---

## Data Source

National Oceanic and Atmospheric Administration (NOAA) Storm Events Database

Source:

[NOAA Storm Events Database](https://www.ncdc.noaa.gov/stormevents/)

Coverage:

- 2000–2026

---

## Project Status

- [x] Data Acquisition
- [x] Data Assessment
- [x] Initial Data Cleaning
- [ ] Damage Variable Conversion
- [ ] Feature Engineering
- [ ] Exploratory Data Analysis
- [ ] Storm Profiles
- [ ] Impact Categories
- [ ] Classification
- [ ] Deep Learning
- [ ] MLOps

---

## Project Motivation

Storm events vary widely in their impacts on communities, infrastructure, agriculture, and public safety. While event types such as tornadoes, floods, and winter storms are well documented, less attention is often given to identifying broader patterns that exist across storm events.

This project uses NOAA Storm Events data from 2000–2026 to explore two fundamental questions:

### Research Question 1

Can storm events be grouped into meaningful storm profiles based on their characteristics and impacts?

### Research Question 2

Can storm impacts be categorized into distinct levels of severity using measures such as property damage, crop damage, injuries, and fatalities?

To answer these questions, the project combines exploratory data analysis, unsupervised learning, classification, deep learning, and future MLOps workflows using more than 1.6 million storm-event records collected across the United States and its territories.

---

## Dataset

### Raw NOAA Dataset

- 1,643,337 storm events
- 52 variables
- 57 event types
- 69 NOAA reporting regions
- 27 years of data (2000–2026)

Includes:

- States
- Territories
- Marine Regions
- Great Lakes Regions

### Land-Based Analytical Dataset

Current cleaned analytical dataset:

- 1,590,430 storm events
- 36 variables
- 57 event types
- 55 geographic regions
- 27 years of data (2000–2026)

Includes:

- States
- District of Columbia
- Territories

Excludes:

- Marine Regions
- Great Lakes Regions

This dataset serves as the primary dataset for all subsequent analysis and modeling.

---

## Why 2000–2026?

The study period begins in 2000 to focus on modern storm reporting practices while maintaining more than two decades of observations. This period provides a balance between reporting consistency, geographic coverage, data availability, and dataset size.

The resulting dataset contains more than 1.6 million storm events spanning 27 years of NOAA Storm Events records.

---

## Initial Cleaning Results

The first cleaning phase focused on missing-value reduction and removal of low-value variables.

| Metric | Before | After |
|----------|----------|----------|
| Rows | 1,590,430 | 1,590,430 |
| Columns | 52 | 36 |
| Variables Removed | - | 16 |
| Reduction | - | 30.77% |

No storm-event records were removed during cleaning.

Variables removed included:

- Variables containing more than 50% missing values
- Tornado-specific variables with limited coverage
- Low-value location descriptor variables
- Redundant reporting fields

Remaining variables preserve storm characteristics, geographic information, temporal information, injuries, fatalities, and damage measures.

---

## Research Questions

### Storm Profiles

- Do natural storm groups emerge from the data?
- What characteristics define different storm profiles?
- Can storm profiles be predicted accurately using machine learning?

### Impact Categories

- How should storm impacts be categorized?
- Which factors contribute most to storm severity?
- Can storm impact categories be predicted accurately using machine learning and deep learning models?

---

# Data Pipeline

## Phase 1: Data Acquisition & Assessment

### Raw NOAA Storm Events (2000–2026)

- Download NOAA Storm Events records
- Combine yearly datasets
- Create all-regions dataset
- Create land-based analytical dataset
- Assess data quality
- Review missing values
- Review event distributions

---

## Phase 2: Data Cleaning

Completed:

- Missing-value assessment
- Removal of variables with more than 50% missing data
- Removal of low-value location descriptor variables
- Date variable conversion and validation

In Progress:

- Damage variable standardization
- Additional data validation
- Final dataset preparation

Output:

- Cleaned land-based analytical dataset

---

## Phase 3: Feature Engineering

Planned features include:

- Property Damage
- Crop Damage
- Injuries
- Fatalities
- Storm Magnitude
- Event Duration
- Geographic Variables
- Temporal Variables

Output:

- Feature-engineered modeling dataset

---

# Outcome A: Storm Profiles

## Exploratory Data Analysis

- Event distributions
- Geographic patterns
- Temporal trends
- Storm-impact patterns

## Unsupervised Learning

- PCA
- K-Means
- Hierarchical Clustering
- DBSCAN

## Storm Profiles

Storm profile categories will be discovered through clustering methods and may evolve as the feature set develops.

Potential examples include:

- High-Damage Storms
- High-Fatality Storms
- Agricultural Impact Storms
- Severe Wind Events
- Low-Impact Common Storms

## Classification

Predict storm profile membership using machine learning models.

## Deep Learning

Predict storm profile membership using neural networks.

---

# Outcome B: Impact Categories

## Impact Engineering

Impact categories will be developed using event-level measures such as:

- Property Damage
- Crop Damage
- Injuries
- Fatalities

Planned categories include:

- Low Impact
- Moderate Impact
- High Impact
- Extreme Impact

## Unsupervised Learning

Explore and validate impact-category structure.

## Classification

Predict impact-category membership using traditional machine learning models.

## Deep Learning

Predict impact-category membership using neural networks.

---

## Expected Deliverables

This project is expected to produce:

- A cleaned NOAA Storm Events database (2000–2026)
- A land-based analytical dataset
- Storm profile categories discovered through clustering methods
- Impact categories derived from storm-impact measures
- Classification models for storm-profile prediction
- Classification models for impact-category prediction
- Deep-learning models for comparison with traditional approaches
- Reproducible data workflows supporting future MLOps development

---

## Future Development

Planned enhancements include:

### Data Engineering

- Automated NOAA data ingestion
- Scheduled data updates
- Data validation pipelines

### Machine Learning

- Feature pipelines
- Hyperparameter optimization
- Model evaluation workflows
- Explainability dashboards

### MLOps

- Experiment tracking
- Model versioning
- Automated retraining workflows
- CI/CD pipelines
- Model deployment
- Monitoring and observability

---

## Alignment with MLOps

This project is designed to evolve from exploratory analysis into a complete MLOps workflow.

Future enhancements will focus on:

- Automated data ingestion
- Data validation
- Feature pipelines
- Experiment tracking
- Model versioning
- Deployment
- Model monitoring

The repository serves as a long-term applied learning project supporting concepts covered in the Duke University MLOps Specialization.

Specialization:

[Duke University MLOps Specialization](https://www.coursera.org/specializations/mlops-duke)
