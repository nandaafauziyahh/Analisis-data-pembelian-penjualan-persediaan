import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Tahap 1: Pengumpulan Data
data = pd.read_csv('data_penjualan.csv')

# Menampilkan beberapa baris pertama untuk memverifikasi data
print(data.head())

# Menampilkan nama kolom untuk memastikan semuanya sudah benar
print(data.columns)

# Statistik deskriptif
print("Statistik deskriptif:\n", data.describe())

# Visualisasi penjualan total per produk
plt.figure(figsize=(10, 6))
sns.barplot(data=data, x='Produk', y='Total Penjualan', estimator=sum, ci=None)
plt.title('Total Penjualan per Produk')
plt.show()

# Tren penjualan dari waktu ke waktu
plt.figure(figsize=(10, 6))
data.groupby('Tanggal')['Total Penjualan'].sum().plot()
plt.title('Tren Penjualan Harian')
plt.xlabel('Tanggal')
plt.ylabel('Total Penjualan')
plt.show()

# Pie Chart dari Total Penjualan berdasarkan Produk
plt.figure(figsize=(8, 8))
data.groupby('Produk')['Total Penjualan'].sum().plot(kind='pie', autopct='%1.1f%%')
plt.title('Distribusi Penjualan per Produk')
plt.ylabel('')
plt.show()

# Scatter Plot untuk melihat hubungan antara Jumlah Terjual dan Total Penjualan
plt.figure(figsize=(10, 6))
sns.scatterplot(data=data, x='Jumlah Terjual', y='Total Penjualan')
plt.title('Jumlah Terjual vs Total Penjualan')
plt.xlabel('Jumlah Terjual')
plt.ylabel('Total Penjualan')
plt.show()

# Menyiapkan data untuk modeling
X = data[['Jumlah Terjual']]
y = data['Total Penjualan']

# Membagi data menjadi data latih dan data uji
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Membuat dan melatih model regresi linear
model = LinearRegression()
model.fit(X_train, y_train)

# Memprediksi data uji
y_pred = model.predict(X_test)

# Evaluasi model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error:", mse)
print("R^2 Score:", r2)

# Visualisasi hasil prediksi vs aktual
plt.figure(figsize=(10, 6))
plt.scatter(X_test, y_test, color='blue', label='Actual')
plt.scatter(X_test, y_pred, color='red', label='Predicted')
plt.title('Prediksi vs Aktual')
plt.xlabel('Jumlah Terjual')
plt.ylabel('Total Penjualan')
plt.legend()
plt.show()


