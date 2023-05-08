import pandas as pd
import matplotlib.pyplot as plt


# Load data từ DataFrame
online_rt = pd.read_csv('https://raw.githubusercontent.com/thieu1995/csv-files/main/data/pandas/Online_Retail.csv', encoding='latin1')


# Loại bỏ các đơn hàng của Vương quốc Anh
online_rt_without_uk = online_rt[online_rt.Country != 'United Kingdom']

# Lấy 10 quốc gia có số lượng hàng đặt hàng nhiều nhất
top_10_countries = online_rt_without_uk.groupby('Country')['Quantity'].sum().sort_values(ascending=False).head(10)

# Vẽ biểu đồ
plt.figure(figsize=(10, 6))
plt.bar(top_10_countries.index, top_10_countries.values)
plt.title('Top 10 countries by Quantity (excluding UK)')
plt.xlabel('Country')
plt.ylabel('Quantity')
plt.show()

# Loại bỏ các mục có sóo lượng âm
online_rt_without_uk = online_rt_without_uk[online_rt_without_uk.Quantity > 0]

# Tạo biểu đồ phân tán với Số lượng trên mỗi Đơn giá theo ID khách hàng cho 3 quốc gia hàng đầu (ngoại trừ Vương quốc Anh)
# Lấy 3 quốc gia hàng đầu (ngoài Vương quốc Anh)
top_3_countries = online_rt_without_uk.groupby('Country')['Quantity'].sum().sort_values(ascending=False).head(3)

# Tạo biểu đồ phân tán
for country in top_3_countries.index:
    data = online_rt_without_uk[online_rt_without_uk.Country == country]
    plt.figure(figsize=(8, 5))
    plt.scatter(data.UnitPrice, data.Quantity)
    plt.title('Scatter plot of Quantity vs UnitPrice for ' + country)
    plt.xlabel('UnitPrice')
    plt.ylabel('Quantity')
    plt.show()

# Hiển thị một vài hàng đầu tiên của DataFrame đó
print(online_rt_without_uk.head())    

# hiển thị dtype của UnitPrice
print(online_rt_without_uk['UnitPrice'].dtype)

#Lấy dữ liệu từ online_rt cho ID khách hàng 12346.0 và 12347.0
data_12346 = online_rt[online_rt.CustomerID == 12346.0]
data_12347 = online_rt[online_rt.CustomerID == 12347.0]

# Tính doanh thu cho mỗi lần bán hàng
online_rt_without_uk['Revenue'] = online_rt_without_uk['Quantity'] * online_rt_without_uk['UnitPrice']

# Nhóm theo Quốc gia và tính tổng doanh số
sales_by_country = online_rt_without_uk.groupby('Country')['Revenue'].sum()

# Lấy ra 3 quốc gia hàng đầu
top_3_countries = sales_by_country.sort_values(ascending=False).head(3)

# Tính giá trung bình cho mỗi khách hàng
online_rt_without_uk['Revenue'] = online_rt_without_uk['Quantity'] * online_rt_without_uk['UnitPrice']
avg_price_by_customer = online_rt_without_uk.groupby(['CustomerID', 'Country'])['Revenue'].mean().reset_index()

# Lấy dữ liệu của top 3 quốc gia
data_top_3_countries = avg_price_by_customer[avg_price_by_customer.Country.isin(top_3_countries.index)]

# Thêm một cột vào online_rt có tên là Doanh thu tính toán doanh thu (Số lượng * Đơn giá) từ mỗi lần bán hàng
online_rt_without_uk['Revenue'] = online_rt_without_uk['Quantity'] * online_rt_without_uk['UnitPrice']

# Nhóm theo ID khách hàng và Quốc gia và tính giá trung bình
avg_price_by_customer = online_rt_without_uk.groupby(['CustomerID', 'Country'])['Revenue'].mean().reset_index()

# Vẽ biểu đồ phân tán
for country in top_3_countries.index:
    data = avg_price_by_customer[avg_price_by_customer.Country == country]
    plt.figure(figsize=(8, 5))
    plt.scatter(data.Revenue, data.CustomerID)
    plt.title('Scatter plot of Average Price vs Customer ID for ' + country)
    plt.xlabel('Average Price')
    plt.ylabel('Customer ID')
    plt.show()

# Vẽ dữ liệu cho từng ID khách hàng trên một biểu đồ
for customer_id in avg_price_by_customer.CustomerID.unique():
    data = avg_price_by_customer[avg_price_by_customer.CustomerID == customer_id]
    plt.plot(data.Country, data.Revenue, label=customer_id)
plt.legend()
plt.title('Revenue by Country for each Customer ID')
plt.xlabel('Country')
plt.ylabel('Revenue')
plt.show()

# Phóng to để chúng ta có thể nhìn rõ đường cong đó hơn
for customer_id in avg_price_by_customer.CustomerID.unique():
    data = avg_price_by_customer[avg_price_by_customer.CustomerID == customer_id]
    plt.plot(data.Country, data.Revenue, label=customer_id)
plt.legend()
plt.title('Revenue by Country for each Customer ID')
plt.xlabel('Country')
plt.ylabel('Revenue')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Nhóm theo khoảng cách giá và tính tổng Số lượng và Doanh thu
online_rt_without_uk['PriceRange'] = pd.cut(online_rt_without_uk['UnitPrice'], bins=range(0, 51))
sales_by_price_range = online_rt_without_uk.groupby('PriceRange')['Revenue', 'Quantity'].sum()

# Chuyển đổi đơn vị của trục y sang hàng triệu đồng
sales_by_price_range['Revenue'] = sales_by_price_range['Revenue'] / 1000000

# Vẽ biểu đồ đường
plt.plot(sales_by_price_range.index.astype(str), sales_by_price_range.Revenue)
plt.title('Revenue by Price Range')
plt.xlabel('Price Range')
plt.ylabel('Revenue (million VND)')
plt.show()
