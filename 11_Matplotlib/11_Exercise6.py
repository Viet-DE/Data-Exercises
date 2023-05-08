import pandas as pd
import matplotlib.pyplot as plt

# Load data từ link github
url = "https://github.com/thieu1995/csv-files/raw/main/data/matplotlib/company_sales_data.csv"
data = pd.read_csv(url)

# Thiết lập bathingsoap sales data cho mỗi tháng
months = data["month_number"]
bathing_soap_sales = data["bathingsoap"]

# Xây dựng bar chart
plt.bar(months, bathing_soap_sales)
plt.title('BathingSoap Sales Data')
plt.xlabel('Month Number')
plt.ylabel('Sales units in number')
# Lưu chart vào disk
plt.savefig('bathing_soap_sales.png')
plt.show()