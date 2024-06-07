# Analisis-data-pembelian-penjualan-persediaan
terdiri dari 3 tabel (tabel pembelian, persediaan, dan penjualan). langkah"nya install vscode dan python lalu searching di chat GPT bagaimana kode pythonnya dengan selengkap-lengkapnya. 
# DATA PEMBELIAN
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Tahap 1: Pengumpulan Data
data = pd.read_csv('data_pembelian.csv')

# Menampilkan beberapa baris pertama untuk memverifikasi data
print(data.head())

# Menampilkan nama kolom untuk memastikan semuanya sudah benar
print(data.columns)

# Menghitung persentase total biaya pembelian per produk
produk = data['produk']
total_biaya = data['total_biaya']

plt.figure(figsize=(10, 8))
plt.pie(total_biaya, labels=produk, autopct='%1.1f%%', startangle=140)
plt.title('Persentase Total Biaya Pembelian per Produk pada 2023')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()

# Membuat Bar Chart
produk = data['produk']
jumlah_dibeli = data['jumlah_dibeli']

plt.figure(figsize=(12, 6))
plt.bar(produk, jumlah_dibeli, color='skyblue')
plt.xlabel('Produk')
plt.ylabel('Jumlah Dibeli')
plt.title('Jumlah Barang Dibeli per Produk pada 2023')
plt.xticks(rotation=45)
plt.show()

# Mengidentifikasi produk dengan jumlah pembelian terbanyak dan paling sedikit
max_jumlah_dibeli = data['jumlah_dibeli'].max()
min_jumlah_dibeli = data['jumlah_dibeli'].min()
colors = ['red' if val == max_jumlah_dibeli else 'blue' if val == min_jumlah_dibeli else 'gray' for val in data['jumlah_dibeli']]

# Membuat Bar Chart
produk = data['produk']
jumlah_dibeli = data['jumlah_dibeli']

plt.figure(figsize=(12, 6))
plt.bar(produk, jumlah_dibeli, color=colors)
plt.xlabel('Produk')
plt.ylabel('Jumlah Dibeli')
plt.title('Jumlah Pembelian Produk Terbanyak dan Tersedikit pada 2023')
plt.xticks(rotation=45)
plt.show()

# Tahap 1: Pengumpulan Data
data = pd.read_csv('data_persediaan_barang.csv')

# DATA PERSEDIAAN
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Tahap 1: Pengumpulan Data
data = pd.read_csv('data_persediaan_barang.csv')

# Menampilkan beberapa baris pertama untuk memverifikasi data
print(data.head())

# Menampilkan nama kolom untuk memastikan semuanya sudah benar
print(data.columns)

# Membuat Bar Chart
produk = data['produk']
stok = data['stok']

plt.figure(figsize=(12, 6))
plt.bar(produk, stok, color='skyblue')
plt.xlabel('Produk')
plt.ylabel('Jumlah Stok')
plt.title('Jumlah Stok per Produk pada 2023')
plt.xticks(rotation=45)
plt.show()

# Mengidentifikasi produk dengan penjualan tertinggi dan terendah
max_terjual = data['terjual'].max()
min_terjual = data['terjual'].min()
colors = ['red' if val == max_terjual else 'blue' if val == min_terjual else 'gray' for val in data['terjual']]

# Membuat Bar Chart
produk = data['produk']
terjual = data['terjual']

plt.figure(figsize=(12, 6))
plt.bar(produk, terjual, color=colors)
plt.xlabel('Produk')
plt.ylabel('Jumlah Terjual')
plt.title('Penjualan Produk Tertinggi dan Terendah pada 2023')
plt.xticks(rotation=45)
plt.show()

# Mengidentifikasi produk dengan jumlah pembelian terbanyak dan paling sedikit
max_jumlah_harga = data['harga'].max()
min_jumlah_harga = data['harga'].min()
colors = ['red' if val == max_jumlah_harga else 'blue' if val == min_jumlah_harga else 'b' for val in data['harga']]

# Membuat Bar Chart
produk = data['produk']
harga = data['harga']

plt.figure(figsize=(10, 6))
sns.scatterplot(x='stok', y='total_penjualan', data=data)
plt.title('Hubungan antara Stok dan Total Penjualan')
plt.xlabel('Stok')
plt.ylabel('Total Penjualan')
plt.show()

# DATA PENJUALAN
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
