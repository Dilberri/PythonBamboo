#%%
import pandas as pd


#crear dataframe
db = {
    'Nombre': ['Ana', 'Luis', 'Carlos', 'Bea'],
    'Edad': [23, 34, 28, 30],
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Sevilla']
}

df = pd.read_csv('C:/Users/Dilan/Documents/Data analyst Contenido/Bamboo docs/Bamboo Tec Python/Ventas+Videojuegos.csv', sep=';')
#print(df.head(10)) #ver las primeras 10 filas del DF

# Eliminar comas y convertir a numérico
df['Valor'] = df['Valor'].replace({',': '.'}, regex=True)

# Convertir la columna a tipo numérico
df['Valor'] = pd.to_numeric(df['Valor'])


# Ventas por plataforma
ventas_por_plataforma = df.groupby('Plataforma')['Valor'].sum()
print(ventas_por_plataforma)

# Ventas por género
ventas_por_genero = df.groupby('Genero')['Valor'].sum()
print(ventas_por_genero)

# Ventas por año
ventas_por_año = df.groupby('Año')['Valor'].sum()
print(ventas_por_año)






# %%
