import pandas as pd
import matplotlib.pyplot as plt

# Load data từ link github
url = "https://github.com/thieu1995/csv-files/raw/main/data/matplotlib/company_sales_data.csv"
data = pd.read_csv(url)

# Thiết lập facecream and facewash sales data cho mỗi tháng
months = data["month_number"]
facecream_sales = data["facecream"]
facewash_sales = data["facewash"]

# Thiết lập vị trí và độ rộng của các thanh bar
bar_width = 0.35
r1 = range(len(months))
r2 = [x + bar_width for x in r1]

# xây dựng bar chart
plt.bar(r1, facecream_sales, color='blue', width=bar_width, label='Face Cream Sales Data')
plt.bar(r2, facewash_sales, color='orange', width=bar_width, label='Face Wash Sales Data')
plt.title('Face Cream and Face Wash Sales data')
plt.xlabel('Month Number')
plt.ylabel('Sales units in number')
plt.xticks([r + bar_width/2 for r in range(len(months))], months)
plt.legend()
plt.show()