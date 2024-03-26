import numpy as np
import matplotlib.pyplot as plt

# np.random.seed(15)

N = 100

X = np.linspace(1, 5, N) + 5*np.random.rand(N)  # -1 1
Y = 2*X + 3 + 5*np.random.rand(N)

plt.scatter(X, Y, color='r')

# standardisasi X dan Y

X_ave = np.mean(X)
Y_ave = np.mean(Y)

X_ = X - X_ave
Y_ = Y - Y_ave

#plt.plot(X_, Y_, '*b')

# Menentukan B0 dan B1

B1 = np.sum( X_ * Y_) / np.sum (X_ * X_)
B0 = Y_ave - B1 * X_ave

# plot regresi linier

x = np.linspace(np.min(X), np.max(X), N)
y = B0 + B1*x

plt.plot(x, y, 'b')

# akurasi dari model

MSE = np.mean( ( Y - (B0 + B1*X) )**2 ) # Mean Square Error
R2 = 1 - np.sum( ( Y - (B0 + B1*X) )**2 ) / np.sum( (Y-Y_ave)**2 )

print("MSE: {}, R2: {}".format(MSE, R2))

"""
X = luas tanah (m2)
Y = harga tanah (juta rupiah)
"""

luas = 5
harga = B0 + B1*luas

print("Perkiraan harga tanah dengan luas: {} = {}".format(luas, harga))

plt.plot(x, y, 'b')
plt.plot(luas, harga, 'og')

plt.show()
