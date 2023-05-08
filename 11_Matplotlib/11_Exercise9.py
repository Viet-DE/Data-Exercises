import pandas as pd
import matplotlib.pyplot as plt

# Load data từ link Github
url = 'https://github.com/thieu1995/csv-files/raw/main/data/matplotlib/company_sales_data.csv'
df = pd.read_csv(url)

# Lọc các cột liên quan đến Bathingsoap và facewash theo từng tháng
bathingsoap_data = df[['month_number', 'bathingsoap']].set_index('month_number')
facewash_df = df[['month_number', 'facewash']].set_index('month_number')

# Tạo hai đối tượng subplot
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))

# Vẽ biểu đồ cho Bathingsoap
ax1.plot(bathingsoap_data.index, bathingsoap_data.values, marker='o')
ax1.set_xlabel('Month')
ax1.set_ylabel('Sales')
ax1.set_title('Bathingsoap Sales data')

# Vẽ biểu đồ cho facewash
ax2.plot(facewash_df.index, facewash_df.values, marker='o')
ax2.set_xlabel('Month')
ax2.set_ylabel('Sales')
ax2.set_title('Facewash Sales data')

# Hiển thị biểu đồ
plt.show()
