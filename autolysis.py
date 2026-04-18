import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import sys

output_dir = "output"
os.makedirs(output_dir, exist_ok=True)
print("Output folder created...")

if len(sys.argv) < 2:
    print("Please provide a CSV file")
    print("Example: uv run autolysis.py data.csv")
    sys.exit()

file_path = sys.argv[1]

try:
    data = pd.read_csv(file_path, encoding='latin1')
    print(f"Dataset '{file_path}' loaded successfully!")
except Exception as e:
    print("Error loading file:", e)
    sys.exit()


numeric_cols = data.select_dtypes(include=np.number).columns

print(f"Numeric columns: {list(numeric_cols)}")

if len(numeric_cols) == 0:
    print("No numeric columns found.")
    sys.exit()


print(f"Numeric columns: {list(numeric_cols)}")

def save_histogram(column):
    plt.figure()
    sns.histplot(data[column].dropna(), kde=True)
    plt.title(f"{column} Histogram")
    
    filename = os.path.join(output_dir, f"{column}_hist.png")
    plt.savefig(filename)
    plt.close()
    
    print(f"Histogram saved: {filename}")

def save_boxplot(column):
    plt.figure()
    sns.boxplot(x=data[column])
    plt.title(f"{column} Boxplot")
    
    filename = os.path.join(output_dir, f"{column}_boxplot.png")
    plt.savefig(filename)
    plt.close()
    
    print(f"Boxplot saved: {filename}")

try:
    for col in numeric_cols:
        save_histogram(col)
        save_boxplot(col)

    print("All histograms and boxplots saved!")
except Exception as e:
    print("Error during plotting:", e)

try:
    plt.figure(figsize=(10, 8))
    corr = data.corr(numeric_only=True)
    
    sns.heatmap(corr, annot=True)
    plt.title("Correlation Matrix")
    
    filename = os.path.join(output_dir, "correlation_matrix.png")
    plt.savefig(filename)
    plt.close()
    
    print(f"Correlation matrix saved: {filename}")
except Exception as e:
    print("Error generating correlation matrix:", e)

print("\nAnalysis Completed Successfully!")
print("All outputs are saved in the 'output' folder")