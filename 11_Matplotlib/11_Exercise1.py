import pandas as pd
import matplotlib.pyplot as plt
# Load data từ link Github
url = "https://raw.githubusercontent.com/thieu1995/csv-files/main/data/matplotlib/company_sales_data.csv"
df = pd.read_csv(url)

month_numbers = df["month_number"]
total_profits = df["total_profit"]

plt.plot(month_numbers, total_profits)
plt.title("Company profit per Month")
plt.xlabel("Month Number")
plt.ylabel("Total Profit ($)")
plt.show()
