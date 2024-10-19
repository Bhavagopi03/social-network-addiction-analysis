# Social Media Addiction and Impact Analysis

This project is a **mini-project** for a Big Data assignment, where I conducted an analysis on how social media is addicting and affecting individuals. The data was collected from **friends and family (100+ people)**, and it underwent thorough cleaning and preprocessing before being analyzed using PySpark.

## Project Overview

Social media has become an integral part of our daily lives, but it also has significant effects on mental health, productivity, and behavior. In this project, I aim to analyze the level of social media addiction and its perceived impact based on self-reported data.

### Key Objectives:
- **Analyze Social Media Usage Patterns**: Understand how frequently and for how long people use social media.
- **Measure Perceived Addiction**: Evaluate how addicted individuals feel towards social media platforms.
- **Assess Impact**: Investigate the effects on productivity, mental well-being, and personal relationships.
  
## Data Collection

- The data was collected through personal surveys conducted with over **100 people**, including friends and family members.
- Participants provided insights into their social media habits, perceived addiction, and the effects of social media on various aspects of their lives.

### Data Fields:
- **Age, Gender, Occupation**: Basic demographic information.
- **Social Media Platforms Used**: Which platforms participants engage with most.
- **Time Spent on Social Media**: Average daily usage.
- **Perceived Addiction Level**: Self-reported addiction levels (scale of 1-10).
- **Impact Areas**: Productivity, mental health, social relationships, etc.

The raw data is available in the repository as a CSV file (`data/social_media_data.csv`).

## Preprocessing and Cleaning

Data preprocessing was a crucial step to ensure the accuracy of the analysis. The following steps were taken:
- **Handling Missing Data**: Removed or imputed missing values.
- **Normalization**: Standardized numerical values such as time spent on social media.
- **Categorization**: Grouped responses into relevant categories for better analysis.

## Analysis and Findings

Using **PySpark**, the analysis focused on:
- **Addiction Scores**: Correlating age, gender, and occupation with addiction levels.
- **Effect on Productivity**: Analyzing how social media impacts participants' work/study productivity.
- **Mental Health Impact**: Measuring the emotional effects such as stress, anxiety, and mood changes.

Detailed analysis results are available in the documentation provided.

## Repository Contents

- `main.py`: The main PySpark script for cleaning and analyzing the data.
- `data/social_media_data.csv`: The dataset collected from the survey.
- `docs/analysis_report.pdf`: Detailed documentation and results of the analysis.

## How to Run the Project

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/social-media-analysis-pyspark.git
