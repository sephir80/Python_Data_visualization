import matplotlib.pyplot as plt
from matplotlib.axes import Axes  # IDE doesn't understand subplots return type.
ax: Axes

squares = [1, 4, 9, 16, 25]

fig, ax = plt.subplots() # The variable <<fig>> represents the entire figure or collection of plots that are generated
ax.plot(squares, linewidth=3)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels
ax.tick_params(axis='both', labelsize=8)

plt.show()
