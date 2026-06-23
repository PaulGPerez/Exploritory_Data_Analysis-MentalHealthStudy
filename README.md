# Mental Health & Lifestyle Data Study

This project focuses on auditing and analyzing 2,000 survey records to see how lifestyle affects mental health.

You can find the dataset here on Kaggle:
[https://www.kaggle.com/datasets/jajidhasan/mental-health](https://www.kaggle.com/datasets/jajidhasan/mental-health)

**Important: How to View Documentation**
Please open the Microsoft Word versions of the documentation instead of the PDFs. The Word files are structured in an outline format, which makes the project much easier to read and navigate.

---

## Deliverables and steps taken:

1.  **Data Cleanup:** Performed a full audit of the dataset to ensure data integrity.
2.  **Quality Assurance:** Confirmed there were 0 duplicates, 0 missing values, and 0 outliers in key fields like Sleep Hours and Stress Levels.

<p align="center">
  <!-- replace [[INSERT YOUR IMAGE FILENAME HERE]] with your actual file name -->
  <img src="[[INSERT YOUR IMAGE FILENAME HERE]]" alt="Data Distribution Visualization" width="600px" />
  <br>
  <em>Visualization: Overview of key variable distributions after cleaning.</em>
</p>

## Statistical Analysis

**Testing:** Ran hypothesis tests to determine if "Gender" or "Occupation" actually influence "Sleep" or "Stress".

### 1. Sleep vs. Gender
A T-Test showed that males and females have nearly identical sleep averages. The difference was not statistically significant.

*   **P-value:** 0.84 (higher than 0.05 alpha)
*   **T-statistic:** -0.19 (too close to zero)

<p align="center">
  <!-- replace [[INSERT YOUR IMAGE FILENAME HERE]] with your actual file name -->
  <img src="[[INSERT YOUR IMAGE FILENAME HERE]]" alt="T-Test Results for Sleep vs Gender" width="600px" />
  <br>
  <em>Visualization: Comparing average sleep hours by gender.</em>
</p>

### 2. Stress vs. Job
A Mann-Whitney test showed that being a "Student" vs "Employed" didn't show significant change in stress levels in this group.

*   **P-value:** 0.44 (higher than the standard alpha of 0.05)

<p align="center">
  <!-- replace [[INSERT YOUR IMAGE FILENAME HERE]] with your actual file name -->
  <img src="[[INSERT YOUR IMAGE FILENAME HERE]]" alt="Mann-Whitney Results for Stress vs Job" width="600px" />
  <br>
  <em>Visualization: Stress level distribution across occupations.</em>
</p>
