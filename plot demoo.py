import matplotlib.pyplot as plt

x = [2,4,1,5,3,2,7,6,7.5,3,1,0]
y = [3,4,1,3,5,7,8,9,6,7,8,4]

# plt.plot(x)
# plt.show()
# plt.plot(x,y)
plt.scatter(x,y, c="purple", marker="x")
plt.xlabel("Xs")
plt.ylabel("Ys")
plt.grid()
plt.show()