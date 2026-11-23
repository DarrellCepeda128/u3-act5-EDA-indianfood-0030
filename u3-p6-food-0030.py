import pandas as pd
import matplotlib.pyplot as plt
# Cepeda Darrell NC 0030
# 1. Leer el archivo CSV comida pais India
df_food_india = pd.read_csv('indian_food.csv')
print("\n--- DATOS LEIDOS DESDE CSV, comida India 0030---")
print(df_food_india)

print("\n--- Mostrar Nombre + Ingredientes de comida 0030---")
recetas = df_food_india[['name', 'ingredients']]
print(recetas)

print("\n--- Tiempo de Cocinado mostrar 10 registros con head 0030---")
nombre_y_hora = df_food_india[['name', 'cook_time']].head(10)
print(nombre_y_hora)

print("\n--- Grafica comida (X) Tiempo de Cocinado (Y) 0030---")
print("\n--- Grafica comida (X) Texto a 30 grados 0030---")
nombre_y_hora.plot.bar(x='name',y='cook_time', rot=30)
plt.title('Comida tipica de India Darrell 0030')
plt.xlabel('Nombre de Platillo')
plt.ylabel('Tiempo de Cocinado')
plt.show()

print("\n--- Grafica multiple 0030---")
nombre_y_hora = df_food_india[['name', 'prep_time', 'cook_time']].head(10)
nombre_y_hora.plot.bar(x='name', rot=30)
plt.title('Grafica de 2 columnas Darrell 0030')
plt.xlabel('Nombre de platillo')
plt.ylabel('Tiempo de Cocinado prep y comida')
plt.show()

print("\n--- Graficas apiladas una tras otra verticalmente 0030---")
nombre_y_hora.plot.bar(x='name', stacked=True, rot=30)
plt.title('Graficas apiladas Darrell 0030')
plt.xlabel('Nombre del platillo')
plt.ylabel('Tiempo de Cocinado prep y comida')
plt.show()