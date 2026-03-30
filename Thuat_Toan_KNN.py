import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler

# 1. Đọc dữ liệu
data = pd.read_csv("khach_hang.csv")

X = data[['thunhap', 'sono']]
Y = data['nhan']

# 2. Chuẩn hóa Min-Max
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# 3. Train model
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_scaled, Y)

# 4. Dữ liệu mới cũng phải scale
new_fruit = [[38,90]]
new_fruit_scaled = scaler.transform(new_fruit)

prediction = model.predict(new_fruit_scaled)

print("Kết quả dự đoán:", prediction[0])