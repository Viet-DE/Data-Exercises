import pandas as pd
import matplotlib.pyplot as plt

# Load data từ link github
url = "https://raw.githubusercontent.com/thieu1995/csv-files/main/data/matplotlib/company_sales_data.csv"
df = pd.read_csv(url)

# Thiết lập các cột,các hàng
facecream_sales = df["facecream"]
facewash_sales = df["facewash"]
toothpaste_sales = df["toothpaste"]

# Tạo biểu đồ đường
plt.plot(df["month_number"], facecream_sales, color='blue', linewidth=2, marker='o', markersize=8, label="Face Cream")
plt.plot(df["month_number"], facewash_sales, color='red', linewidth=2, marker='o', markersize=8, label="Face Wash")
plt.plot(df["month_number"], toothpaste_sales, color='green', linewidth=2, marker='o', markersize=8, label="Toothpaste")

plt.xlim(1, 12)
plt.ylim(0, 18000)
plt.title("Sales Data")
plt.xlabel("Month Number")
plt.ylabel("Sales units in number")
plt.legend()
plt.show()