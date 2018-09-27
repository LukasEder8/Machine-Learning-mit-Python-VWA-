# -*- coding: utf-8 -*-
#!/urs/bin/python

# Bibliothek einbinden
import pandas as pd

# CSV-Datei einbinden
df = pd.read_csv("iris.csv")



# Ausgabe der ersten fünf Einträge des Dataframe-Objekts
print(df.head())

# die Reihen "sepal length" in eine eigene Variable speichern
sepal_length = df["sepal length"]

# Ausgabe der ersten fünf Einträge des Series-Objekts
print(sepal_length.head())

# Ausgabe der Typen
print(f"Typ der ganzen Tabelle: {type(df)}")
print(f"Typ der Reihe: {type(sepal_length)}")