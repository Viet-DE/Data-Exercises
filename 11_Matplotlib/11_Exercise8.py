import pandas as pd
import matplotlib.pyplot as plt

# Load data từ link Github
url = 'https://github.com/thieu1995/csv-files/raw/main/data/matplotlib/company_sales_data.csv'
df = pd.read_csv(url)

# Lọc các cột chúng ta muốn giữ lại
cols_to_keep = ['facecream', 'facewash', 'bathingsoap', 'toothpaste', 'shampoo', 'moisturizer', 'month_number']
df = df[cols_to_keep]

# Tính tổng doanh số cho mỗi sản phẩm trong năm
sales = df.groupby('month_number').sum().transpose()

# Vẽ biểu đồ hình tròn của dữ liệu
labels = sales.index.values
sizes = sales.sum(axis=1).values
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.axis('equal')
plt.title('Sales Data')
plt.show()