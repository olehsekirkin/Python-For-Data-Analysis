import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

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

# 1. Find the top 5 job titles with the highest average salary
top_jobs_by_salary = df.groupby('job_title')['salary_in_usd'].mean().sort_values(ascending=False).head(5)
print("\nTop 5 job titles with the highest average salary:")
print(top_jobs_by_salary)

# 2. Determine the distribution of job categories among different experience levels
experience_category_distribution = df.groupby(['experience_level', 'job_category']).size().unstack(fill_value=0)
print("\nDistribution of job categories among different experience levels:")
print(experience_category_distribution)

# 3. Identify the average salary for each company size category
average_salary_by_company_size = df.groupby('company_size')['salary_in_usd'].mean()
print("\nAverage salary for each company size category:")
print(average_salary_by_company_size)

# 4. Visualize the distribution of salaries using a histogram
plt.figure(figsize=(10, 6))
plt.hist(df['salary_in_usd'], bins=20, color='orange', edgecolor='black')
plt.title('Distribution of Salaries')
plt.xlabel('Salary (USD)')
plt.ylabel('Frequency')
plt.show()
