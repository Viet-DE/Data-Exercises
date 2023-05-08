import pandas as pd
import matplotlib.pyplot as plt


# Load data từ DataFrame
titanic = pd.read_csv('https://raw.githubusercontent.com/thieu1995/csv-files/main/data/pandas/titanic_train.csv')

# Đặt PasbahId làm chỉ mục
titanic.set_index('PassengerId', inplace=True)

# Tạo biểu đồ hình tròn thể hiện tỷ lệ nam/nữ
gender_counts = titanic['Sex'].value_counts()

plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%')
plt.title('Gender Proportion')
plt.show()

# Tạo biểu đồ phân tán với Giá vé đã thanh toán và Độ tuổi, phân biệt màu biểu đồ theo giới tính
colors = {'male': 'blue', 'female': 'red'}

fig, ax = plt.subplots()

for gender in titanic['Sex'].unique():
    subset = titanic[titanic['Sex'] == gender]
    ax.scatter(subset['Fare'], subset['Age'], c=colors[gender], label=gender)

ax.legend()
ax.set_xlabel('Fare')
ax.set_ylabel('Age')
plt.show()

# Có bao nhiêu người sống sót?
survival_counts = titanic['Survived'].value_counts()
print(f'So nguoi song sot: {survival_counts[1]}')

# Tạo biểu đồ với Giá vé đã thanh toán
plt.hist(titanic['Fare'], bins=20)
plt.xlabel('Fare')
plt.ylabel('Count')
plt.show()

# 
