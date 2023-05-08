import pandas as pd
import matplotlib.pyplot as plt

# Load data từ link github
url = "https://github.com/thieu1995/csv-files/raw/main/data/matplotlib/company_sales_data.csv"
data = pd.read_csv(url)

# Thiết lập cột
total_profit = data["total_profit"]

# Xây dựng histogram
plt.hist(total_profit, bins=10, edgecolor='black')
plt.title('Total Profit Histogram')
plt.xlabel('Profit Range')
plt.ylabel('Frequency')
plt.show()