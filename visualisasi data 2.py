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

