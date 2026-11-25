import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 1. Ask for file name with validation (Test Case 3)
filename = input("Enter CSV file name: ")
while not os.path.exists(filename):
    print(f"Error: File '{filename}' not found. Please enter a valid file name.")
    filename = input("Enter CSV file name: ")

# 2. Load file and safely convert numeric columns
df = pd.read_csv(filename)
df["Temp"] = pd.to_numeric(df["Temp"], errors="coerce")
df["Rainfall"] = pd.to_numeric(df["Rainfall"], errors="coerce")

# 3. CLI Menu
print("\n1. Summary Statistics")
print("2. Clean Data & Plot Charts")
choice = input("Enter choice (1/2): ")

# Option 1: Summary Statistics (Test Cases 1 & 2)
if choice == "1":
    temps = df["Temp"].dropna().to_numpy()
    rain = df["Rainfall"].dropna().to_numpy()

    avg_t = np.mean(temps)
    max_t = int(np.max(temps))
    min_t = int(np.min(temps))

    # Test Case 2: Boundary / Minimum Input (1 row)
    if len(temps) == 1:
        std_t = np.std(temps)
        print(f"Average Temp: {avg_t:.2f} C | Max: {max_t} | Min: {min_t} | Std Dev: {std_t:.2f}")

    # Test Case 1: Normal Input
    else:
        max_date = df.loc[df["Temp"] == max_t, "Date"].values[0]
        min_date = df.loc[df["Temp"] == min_t, "Date"].values[0]
        total_rain = int(np.sum(rain))
        print(f"Average Temp: {avg_t:.2f} C | Max: {max_t} ({max_date}) | Min: {min_t} ({min_date}) | Total Rainfall: {total_rain} mm")

# Option 2: Clean & Plot (Test Case 4)
elif choice == "2":
    initial_count = len(df)
    df = df.drop_duplicates()
    dups_removed = initial_count - len(df)

    mean_val = df["Temp"].mean()
    df["Temp"] = df["Temp"].fillna(mean_val)

    print(f"Duplicates removed: {dups_removed} | Missing Temp filled with mean: {mean_val:.2f}")
    print(f"Cleaned rows: {len(df)} | Line chart 'Temperature Trend' displayed")

    # Line Chart
    plt.plot(df["Date"].astype(str), df["Temp"], marker="o", color="red")
    plt.title("Temperature Trend")
    plt.xlabel("Date")
    plt.ylabel("Temperature")
    plt.show()

    # Bar Chart
    plt.bar(df["Date"].astype(str), df["Rainfall"].fillna(0), color="blue")
    plt.title("Rainfall")
    plt.xlabel("Date")
    plt.ylabel("Rainfall")
    plt.show()