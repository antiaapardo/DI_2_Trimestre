
import pandas as pd
import webbrowser
from pathlib import Path

# 1) Ruta del JSON
FICHERO_JSON = "datos.json"

# 2) Leer el JSON y cargarlo en DataFrame
df = pd.read_json(FICHERO_JSON)

#Ordenar por año 
df = df.sort_values(by="anio", ascending=True)

#Filtral albumes desde 2010
df = df[df["anio"] >= 2010]

#Crea una columna nueva “duracion_media_por_cancion”
df["duracion_media_por_cancion"] = df["duracion_min"] / df["canciones"]



# 3) Mostrar por consola (para comprobar)
print("=== DATAFRAME CARGADO DESDE JSON ===")
print(df)

# 4) Generar HTML bonito (tabla)
html = df.to_html(index=False)

# 5) Guardar el informe HTML
salida = Path("informe_json.html")
salida.write_text(html, encoding="utf-8")
print(f"\n✅ Informe guardado en: {salida.resolve()}")

# 6) Abrir en el navegador
webbrowser.open(salida.resolve().as_uri())
