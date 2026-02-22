# Install if needed (usually only once; pandas 2.0+ has built-in support)
#pip install pyreadstat  # or pandas if not already good

import pandas as pd

# Path to your uploaded file (change if you renamed it)
sav_path = 'Lassa Fever_Dataset_NCDC.sav'  # or whatever name it has after upload

# Read the .sav file
df = pd.read_spss(sav_path)

# Quick check: see the first few rows and columns
print(df.head())
print(df.columns.tolist())  # List of columns (symptoms, etc.)

# Save as CSV (no index column)
csv_path = 'lassa_real_data.csv'
df.to_csv(csv_path, index=False)

print(f"Converted! CSV saved as: {csv_path}")
# Now download it from the Colab files panel (right-click → Download)