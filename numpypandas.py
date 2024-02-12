import pandas as pd
import numpy as np
import os

# Load the dataset
df = pd.read_csv("C:\\whereveryouhaveit\\jobs_in_data.csv")

# Display the first few rows of the dataset
print("First few rows of the dataset:")
print(df.head())

# Show basic information about the dataset
print("\nBasic information about the dataset:")
print(df.info())

# Summary statistics of numeric columns
print("\nSummary statistics of numeric columns:")
print(df.describe())

# Extract information based on conditions
# For example, extracting jobs with a salary greater than 50000 USD
high_salary_jobs = df[df["salary_in_usd"] > 50000]
print("\nJobs with a salary greater than 50000 USD:")
print(high_salary_jobs)

# Grouping and summarizing data
# For example, finding the average salary for each job category
average_salary_by_category = df.groupby("job_category")["salary_in_usd"].mean()
print("\nAverage salary for each job category:")
print(average_salary_by_category)

# Modify the dataset
# For example, add a new column "adjusted_salary" by increasing the salary by 10%
df["adjusted_salary"] = df["salary_in_usd"] * 1.1
print("\nDataset with adjusted salary:")
print(df.head())

# Save the modified dataset to a new CSV file on the desktop
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
modified_file_path = os.path.join(desktop_path, "modified_jobs_data.csv")
df.to_csv(modified_file_path, index=False)
print(f"\nModified dataset saved to {modified_file_path}")

# Drop the "adjusted_salary" column
df = df.drop(columns=["adjusted_salary"])

# Display the modified dataset
print("\nDataset after dropping "adjusted_salary" column:")
print(df.head())
