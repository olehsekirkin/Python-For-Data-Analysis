import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('C:\\Users\\olehs\\Desktop\\dataset\\jobs_in_data.csv')

# Check the first few rows of the DataFrame
print(df.head())

# Salary distribution
# Create a histogram to visualize the distribution of salaries
plt.figure(figsize=(10, 6))
plt.hist(df['salary_in_usd'], bins=20, color='skyblue', edgecolor='black')
plt.title('Salary Distribution')
plt.xlabel('Salary (USD)')
plt.ylabel('Frequency')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Group by job category and visualize the salary distribution
plt.figure(figsize=(12, 8))
df.groupby('job_category')['salary_in_usd'].plot(kind='hist', alpha=0.5, legend=True)
plt.title('Salary Distribution by Job Category')
plt.xlabel('Salary (USD)')
plt.ylabel('Frequency')
plt.legend(title='Job Category')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Experience level analysis
# Bar chart for the distribution of jobs based on experience levels
plt.figure(figsize=(12, 6))
df['experience_level'].value_counts().sort_index().plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Distribution of Jobs Based on Experience Levels')
plt.xlabel('Experience Level')
plt.ylabel('Number of Jobs')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Bar chart for the average salary for each experience level
plt.figure(figsize=(12, 6))
df.groupby('experience_level')['salary_in_usd'].mean().plot(kind='bar', color='orange', edgecolor='black')
plt.title('Average Salary for Each Experience Level')
plt.xlabel('Experience Level')
plt.ylabel('Average Salary (USD)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Job category breakdown
# Calculate the percentage distribution of jobs across job categories
job_category_distribution = df['job_category'].value_counts(normalize=True)
# Group job categories with less than 5% into an "Other" category
threshold = 0.055
other_categories = job_category_distribution[job_category_distribution < threshold].index
df['job_category'] = df['job_category'].apply(lambda x: 'Other' if x in other_categories else x)
# Pie chart for the distribution of jobs across job categories
plt.figure(figsize=(12, 6))
df['job_category'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
plt.title('Distribution of Jobs Across Job Categories')
plt.ylabel('')
plt.show()

# Bar chart for the average salary within each job category
plt.figure(figsize=(12, 6))
df.groupby('job_category')['salary_in_usd'].mean().sort_values().plot(kind='bar', color='green', edgecolor='black')
plt.title('Average Salary Within Each Job Category')
plt.xlabel('Job Category')
plt.ylabel('Average Salary (USD)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Company size/analysis
# Bar chart for the average salary within each employment type
plt.figure(figsize=(12, 6))
df.groupby('employment_type')['salary_in_usd'].mean().sort_values().plot(kind='bar', color='lightblue', edgecolor='black')
plt.title('Average Salary Within Each Employment Type')
plt.xlabel('Employment Type')
plt.ylabel('Average Salary (USD)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Geographical distribution
# Bar chart for the distribution of top 15 companies based on their locations
plt.figure(figsize=(12, 6))
df['company_location'].value_counts().nlargest(5).sort_values().plot(kind='barh', color='skyblue', edgecolor='black')
plt.title('Top 15 Companies Based on Their Locations')
plt.xlabel('Number of Companies')
plt.ylabel('Company Location')
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.show()

# Bar chart for the average salary across top 15 regions
plt.figure(figsize=(12, 6))
df.groupby('company_location')['salary_in_usd'].mean().nlargest(15).sort_values().plot(kind='barh', color='orange', edgecolor='black')
plt.title('Top 15 Regions with the Highest Average Salary')
plt.xlabel('Average Salary (USD)')
plt.ylabel('Company Location')
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.show()

# Pie chart for the distribution of employment types
plt.figure(figsize=(12, 6))
df['employment_type'].value_counts().plot(kind='barh', color='skyblue')
plt.title('Distribution of Employment Types')
plt.ylabel('')
plt.show()

# Bar chart for the average salary within each employment type
plt.figure(figsize=(12, 6))
df.groupby('employment_type')['salary_in_usd'].mean().sort_values().plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Average Salary Within Each Employment Type')
plt.xlabel('Employment Type')
plt.ylabel('Average Salary (USD)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Bar chart for the distribution of jobs across different work settings
plt.figure(figsize=(12, 6))
df['work_setting'].value_counts().sort_values().plot(kind='barh', color='skyblue', edgecolor='black')
plt.title('Distribution of Jobs Across Work Settings')
plt.xlabel('Number of Jobs')
plt.ylabel('Work Setting')
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.show()