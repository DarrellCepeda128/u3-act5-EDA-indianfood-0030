import pandas as pd
import matplotlib.pyplot as plt
# Cepeda Darrell NC 0030
# 1. Leer el archivo CSV comida pais India
df_food_india = pd.read_csv('indian_food.csv')
print("\n--- DATOS LEIDOS DESDE CSV, comida India 0030---")
print(df_food_india)
print("\n--- Mostrar nombre comida + Ingredientes 0030---")
recetas = df_food_india[['name', 'ingredients']]
print(recetas)
print("\n--- Tiempo de cocinado mostrar 10 registros con head 0030---")
nombre_y_hora = df_food_india[['name', 'cook_time']].head(10)
print(nombre_y_hora)