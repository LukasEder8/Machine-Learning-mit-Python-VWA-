# -*- coding: utf-8 -*-
#!/urs/bin/python

import numpy as np


# Arithmetische  Operationen mit ndarray:
x = np.array([[1, 2, 3, 4]], dtype="int64")
y = np.array([[5, 6, 7, 8]], dtype="int64")
print(f"NumPy Arrays addiert: {x+y}")

# Konkatenation zweier Python Listen:
x = [1, 2, 3, 4]
y = [5, 6, 7, 8]
print(f"Python Listen addiert: {x+y}")

# Arithmetische Operationen mit Python Listen (Schleife wird benoetigt):
x = [1, 2, 3, 4]
y = [5, 6, 7, 8]
ausgabe  = []
for i, j in zip(x, y):
    ausgabe.append(i+j)
print(f"Python Listen mit Schleife addiert: {ausgabe}")