import matplotlib.pyplot as plt
import numpy as np

x  = np.linspace(-2* np.pi, 2* np.pi, 100)
plt.figure()
plt.plot(x, np.sin(x), label="$sin(x)$")
plt.plot(x, np.cos(x), label="$cos(x)$")
plt.axis([-2* np.pi, 2* np.pi, -1, 1])
plt.legend(loc="upper right")

plt.show()
