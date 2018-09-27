#! /usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np

# Hinweis: Jede Zeile, welche mit einem Raute Zeichen beginnt wird   
# vom Programm ignoriert und dient ausschließlich als Kommentar

x = np.array([[1, 2, 3, 4], [5, 6, 7, 8]], dtype="int64")
print(f"Array: {x}")
print(f"Form: {x.shape}")
print(f"Typ: {x.dtype}")
