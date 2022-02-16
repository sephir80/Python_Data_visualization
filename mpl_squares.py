import matplotlib.pyplot as plt
from matplotlib.axes import Axes  # IDE doesn't understand subplots return type.
ax: Axes


x_values = range(1, 1001)
y_values = [x**2 for x in x_values]   # [x**2] -> [x^2]

# input_values = [1, 2, 3, 4, 5]
# squares = [1, 4, 9, 16, 25]

plt.style.use('seaborn')
fig, ax = plt.subplots()  # The variable <<fig>> represents the entire figure or collection of plots that are generated
# ax.plot(x_values, y_values, linewidth=3)  # Disegna una linea che passa per i punti
ax.scatter(x_values, y_values, c='red', s=10)     # Disegna un punto di size=s e di colore c(rosso)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set the range for each axis.
ax.axis([0, 1100, 0, 1100000])

# Set size of tick labels
ax.tick_params(axis='both', labelsize=8)

plt.show()
