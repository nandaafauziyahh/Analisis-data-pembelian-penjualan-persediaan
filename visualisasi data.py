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