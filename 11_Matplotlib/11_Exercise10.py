import matplotlib.pyplot as plt
import pandas as pd

# Đọc bộ dữ liệu
data = pd.read_csv('https://raw.githubusercontent.com/thieu1995/csv-files/main/data/matplotlib/company_sales_data.csv')

# Lọc các cột liên quan đến các sản phẩm
products = ['bathingsoap', 'facewash', 'facecream', 'shampoo', 'toothpaste', 'moisturizer']
data = data[['month_number'] + products].set_index('month_number')

# Tạo biểu đồ stack plot
plt.figure(figsize=(10, 6))
plt.stackplot(data.index, data.values.T, labels=products)

# Cấu hình biểu đồ
plt.xlabel('Month')
plt.ylabel('Sales')
plt.title('Product Sales Data')
plt.xticks(data.index)
plt.legend()

# Hiển thị biểu đồ
plt.show()
