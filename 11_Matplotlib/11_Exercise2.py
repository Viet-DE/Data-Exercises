import pandas as pd
import matplotlib.pyplot as plt

# Load data từ link github
url = "https://raw.githubusercontent.com/thieu1995/csv-files/main/data/matplotlib/company_sales_data.csv"
df = pd.read_csv(url)
# Thiết lập các cột,các hàng
month_numbers = df["month_number"]
total_profits = df["total_profit"]

# Tạo biểu đồ đường của tổng lợi nhuận theo time
plt.plot(month_numbers, total_profits, color='red', linewidth=2, linestyle='--', marker='o', markersize=8, label="Profits data of last year")
plt.title("Company Sales data of the last year")
plt.xlabel("Month Number")
plt.ylabel("Total Profit ($)")
plt.legend(loc="lower right")
plt.grid(True)
plt.show()