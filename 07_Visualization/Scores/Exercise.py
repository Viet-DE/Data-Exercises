import pandas as pd
import matplotlib.pyplot as plt

#Hởi tạo DataFrame
records = [('Jason', 'Miller', 42, 0 ,4, 25), 
           ('Molly','Jacobson', 52, 1, 24, 94), 
           ('Tina', 'Ali', 36, 1, 31, 57), 
           ('Jake', 'Milner', 24, 0 ,2, 62),
           ('Amy', 'Cooze', 73, 1, 3, 70)]         
df = pd.DataFrame(data = records, columns = ['first_name', 'last_name', 'Age', 'Female', 'preTestScore', 'postTestScore'])
df.to_csv("data.csv")

# step 3
# Đọc dữ liệu từ file CSV và lưu vào DataFrame
df = pd.read_csv('data.csv')

# Tạo biểu đồ tán xạ với kích thước của mỗi điểm dựa trên cột "Age"
plt.scatter(x=df['preTestScore'], y=df['postTestScore'], s=df['Age'])

# Đặt nhãn cho trục x, trục y và tiêu đề
plt.xlabel('preTestScore')
plt.ylabel('postTestScore')
plt.title('Scatter plot of preTestScore vs postTestScore')




#Step 4
# Đọc dữ liệu từ file CSV và lưu vào DataFrame
df = pd.read_csv('data.csv')

# Tạo biến colors để lưu trữ màu sắc tương ứng với mỗi giới tính
colors = {'Male': 'blue', 'Female': 'red'}

# Tạo biểu đồ tán xạ với kích thước của mỗi điểm dựa trên cột "postTestScore" nhân với 4.5,
# màu sắc được xác định bởi giới tính

preTestScore = df['preTestScore']
postTestScore = df['postTestScore']*4.5
Female = df['Female']

# Đặt nhãn cho trục x, trục y và tiêu đề
plt.scatter(preTestScore, postTestScore, Female)
plt.xlabel('preTestScore')
plt.ylabel('postTestScore')
plt.title('Scatter plot of preTestScore vs postTestScore (size by 4.5*postTestScore, color by gender)')

# Hiển thị biểu đồ
plt.show()
plt.show()

