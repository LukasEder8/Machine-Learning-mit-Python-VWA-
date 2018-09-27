#! /usr/bin/python
# -*- coding: utf-8 -*-

# Datensatz importieren
from sklearn.datasets import load_iris
iris = load_iris()

# Größe des Datensatzes Anzeigen
print(f"Feature Form: {iris.data.shape}")
print(f"Feature Namen: {iris.feature_names}")
print(f"Labels Form: {iris.target.shape}")
print(f"Labels Namen: {iris.target_names}")

"""
# Ausgabe von 3 Datenpunkte jeder Klasse (3 Klassen)
for i in [0,50,100]:
    print(f"{iris.data[i]} = Klasse: {iris.target[i]}")
"""


# In Trainings- und Testdaten aufteilen
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target,
                                                test_size=0.3, random_state=42,
                                                stratify=iris.target)

# Einbindung/Verwendung eines LernAlgorithmus
from sklearn.neighbors import KNeighborsClassifier

#KNN-Classifier mit 4 Nachbarn (Anzahl der Klassen + 1)
Clf = KNeighborsClassifier(n_neighbors=4)

# Trainingsdaten dem Klassifikator füttern
Clf.fit(X_train, y_train)

#Genauigkeit Vorhersagen
print(f"Genauigkeit auf Trainingsdaten: {Clf.score(X_train, y_train)}")
print(f"Genauigkeit auf Testdaten: {Clf.score(X_test, y_test)}")


# Vorhersage mittels der predict Methode

vorhersage = Clf.predict(X_test)
#print(f"Vorhersagen fuer den X_test: {vorhersage}")
#print(f"y_test: \n{y_test}")


from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, vorhersage)
print(cm)

# Normalisierung

import numpy as np

matrix_15_15_15 = cm.sum(axis=1)[:, np.newaxis]
norm_matrix = cm.astype('float') / matrix_15_15_15
print(norm_matrix)
