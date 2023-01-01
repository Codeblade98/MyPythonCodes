import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [1,3,4,2]

fig,ax = plt.subplots()
ax.plot(x,y)
print('The graph is being plotted \n')
plt.show()