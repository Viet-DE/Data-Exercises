import pandas as pd
import matplotlib.pyplot as plt

# Load data từ link github
url = "https://github.com/thieu1995/csv-files/raw/main/data/matplotlib/company_sales_data.csv"
data = pd.read_csv(url)

# Thiết lập toothpaste Sales data cho mỗi tháng
months = data["month_number"]
toothpaste_sales = data["toothpaste"]

# Tạo biểu đồ Scatter
plt.scatter(months, toothpaste_sales, label="Tooth paste Sales data")
plt.title("Toothpaste Sales Data")
plt.xlabel("Month Number")
plt.ylabel("Number of units Sold")
plt.legend(loc ="upper left")
plt.show()