import pandas as pd
import matplotlib.pyplot as plt

# Load data từ link Github:
url = 'https://raw.githubusercontent.com/thieu1995/csv-files/main/data/pandas/chipotle.tsv'
chipo = pd.read_csv(url, delimiter = '\t') # \t: Định dạng dấu phân cách dưới dạng tab

# Xem 10 mục đầu tiên
print(chipo.head(10))

# Tạo biểu đồ của 5 mặt hàng được mua nhiều nhất
# Tạo Series chứa số lượng của mỗi mặt hàng
top_items = chipo['item_name'].value_counts().head(5)

# Vẽ biểu đồ cột
top_items.plot(kind='bar')

# Thiết lập tiêu đề và nhãn trục
plt.title('5 mặt hàng được mua nhiều nhất')
plt.xlabel('Mặt hàng')
plt.ylabel('Số lượng')




# Tạo một biểu đồ phân tán với số lượng mặt hàng được đặt hàng trên mỗi giá đặt hàng
# Nhóm các hàng theo giá đặt hàng và tính số lượng hàng được đặt hàng cho mỗi giá
orders = chipo.groupby('item_price')['quantity'].size()

# Vẽ biểu đồ phân tán
plt.scatter(x=orders.index, y=orders.values)

# Thiết lập tiêu đề và nhãn trục
plt.title('Số lượng mặt hàng được đặt hàng trên mỗi giá đặt hàng')
plt.xlabel('Giá đặt hàng')
plt.ylabel('Số lượng mặt hàng')

# Hiển thị biểu đồ
plt.show()
plt.show()
