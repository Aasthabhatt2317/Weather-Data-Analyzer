import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

print("=" * 60)
print("             AUTOMATED TEST CASES EXECUTION             ")
print("=" * 60)

# -----------------------------------------------------------
# TEST CASE 1: Normal Input (Menu Option 1)
# -----------------------------------------------------------
print("\n>>> RUNNING TEST CASE 1: Normal Input")
tc1_data = """Date,Temp,Humidity,Rainfall
2026-08-01,32,70,0
2026-08-02,34,65,0
2026-08-03,30,80,12"""

with open("test1.csv", "w") as f:
    f.write(tc1_data)

df1 = pd.read_csv("test1.csv")
df1["Temp"] = pd.to_numeric(df1["Temp"], errors="coerce")
df1["Rainfall"] = pd.to_numeric(df1["Rainfall"], errors="coerce")

temps1 = df1["Temp"].dropna().to_numpy()
rain1 = df1["Rainfall"].dropna().to_numpy()

avg_t = np.mean(temps1)
max_t = int(np.max(temps1))
min_t = int(np.min(temps1))
max_date = df1.loc[df1["Temp"] == max_t, "Date"].values[0]
min_date = df1.loc[df1["Temp"] == min_t, "Date"].values[0]
total_rain = int(np.sum(rain1))

print(f"Average Temp: {avg_t:.2f} C | Max: {max_t} ({max_date}) | Min: {min_t} ({min_date}) | Total Rainfall: {total_rain} mm")

# -----------------------------------------------------------
# TEST CASE 2: Boundary / Minimum Input (Menu Option 1)
# -----------------------------------------------------------
print("\n>>> RUNNING TEST CASE 2: Boundary / Minimum Input (1 row)")
tc2_data = """Date,Temp,Humidity,Rainfall
2026-08-01,31,60,0"""

with open("test2.csv", "w") as f:
    f.write(tc2_data)

df2 = pd.read_csv("test2.csv")
df2["Temp"] = pd.to_numeric(df2["Temp"], errors="coerce")
temps2 = df2["Temp"].dropna().to_numpy()

avg_t2 = np.mean(temps2)
max_t2 = int(np.max(temps2))
min_t2 = int(np.min(temps2))
std_t2 = np.std(temps2)

print(f"Average Temp: {avg_t2:.2f} C | Max: {max_t2} | Min: {min_t2} | Std Dev: {std_t2:.2f}")

# -----------------------------------------------------------
# TEST CASE 3: Invalid Input (File does not exist)
# -----------------------------------------------------------
print("\n>>> RUNNING TEST CASE 3: Invalid Input")
bad_filename = "wether.csv"
if not os.path.exists(bad_filename):
    print(f"Error: File '{bad_filename}' not found. Please enter a valid file name.")

# -----------------------------------------------------------
# TEST CASE 4: Different Valid Scenario (Menu Option 2)
# -----------------------------------------------------------
print("\n>>> RUNNING TEST CASE 4: Missing Values, Duplicates & Charts")
tc4_data = """Date,Temp,Humidity,Rainfall
2026-08-01,32,70,0
2026-08-02,,65,0
2026-08-02,,65,0
2026-08-03,30,80,12"""

with open("test4.csv", "w") as f:
    f.write(tc4_data)

df4 = pd.read_csv("test4.csv")
df4["Temp"] = pd.to_numeric(df4["Temp"], errors="coerce")
df4["Rainfall"] = pd.to_numeric(df4["Rainfall"], errors="coerce")

initial_rows = len(df4)
df4 = df4.drop_duplicates()
dups_removed = initial_rows - len(df4)

mean_temp = df4["Temp"].mean()
df4["Temp"] = df4["Temp"].fillna(mean_temp)

print(f"Duplicates removed: {dups_removed} | Missing Temp filled with mean: {mean_temp:.2f}")
print(f"Cleaned rows: {len(df4)} | Line chart 'Temperature Trend' displayed")

# Display Line and Bar charts side by side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
ax1.plot(df4["Date"].astype(str), df4["Temp"], marker="o", color="red")
ax1.set_title("Temperature Trend")
ax1.set_xlabel("Date")
ax1.set_ylabel("Temperature (°C)")

ax2.bar(df4["Date"].astype(str), df4["Rainfall"].fillna(0), color="blue")
ax2.set_title("Rainfall")
ax2.set_xlabel("Date")
ax2.set_ylabel("Rainfall (mm)")

plt.tight_layout()
plt.show()

# Clean up temporary test files
for temp_file in ["test1.csv", "test2.csv", "test4.csv"]:
    if os.path.exists(temp_file):
        os.remove(temp_file)

print("\nAll 4 test cases executed successfully!")