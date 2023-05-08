import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data từ DataFrame
tips = pd.read_csv('https://raw.githubusercontent.com/thieu1995/csv-files/main/data/pandas/tips.csv')

# Xoas cột Unnamed 0
tips = tips.drop('Unnamed: 0', axis=1)

# Vẽ biểu đồ cột total bill
tips['total_bill'].plot(kind='bar')
plt.show()

# Tạo biểu đồ phân tán thể hiện mối quan hệ giữa tổng_bill và tiền boa
plt.scatter(tips['total_bill'], tips['tip'])
plt.xlabel('Total Bill')
plt.ylabel('Tip')
plt.show()

# Tạo một hình ảnh có mối quan hệ về tổng số hóa đơn, tiền boa và kích thước
sns.pairplot(tips, vars=['total_bill', 'tip', 'size'])
plt.show()

# Trình bày mối quan hệ giữa số ngày và tổng giá trị hóa đơn
plt.scatter(tips['day'], tips['total_bill'])
plt.xlabel('Day')
plt.ylabel('Total Bill')
plt.show()

# Tạo biểu đồ phân tán với ngày là trục y và đỉnh là trục x, phân biệt các dấu chấm theo giới tính
sns.scatterplot(data=tips, x='tip', y='day', hue='sex')
plt.show()

# Tạo biểu đồ hộp trình bày tổng_hóa đơn mỗi ngày với sự khác biệt về thời gian (Bữa tối hoặc Bữa trưa)
sns.boxplot(data=tips, x='day', y='total_bill', hue='time')
plt.show()

# Tạo hai biểu đồ giá trị tiền boa dựa trên Bữa tối và Bữa trưa. Họ phải ở cạnh nhau.
fig, (ax1, ax2) = plt.subplots(ncols=2, sharey=True)
sns.histplot(data=tips.query("time == 'Lunch'"), x='tip', kde=True, ax=ax1)
ax1.set(title='Lunch')

sns.histplot(data=tips.query("time == 'Dinner'"), x='tip', kde=True, ax=ax2)
ax2.set(title='Dinner')
plt.show()


