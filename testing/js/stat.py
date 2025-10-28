



import matplotlib.pyplot as plt

karakterer = [1, 2, 3, 4, 5, 6]
frekvenser = [2, 3, 5, 7, 4, 1]

plt.bar(karakterer, frekvenser)
plt.title("Frekvensfordeling")
plt.xlabel("Karakter")
plt.ylabel("Frekvens")
plt.show()
