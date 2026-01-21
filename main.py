import pandas as pd
import matplotlib.pyplot as plt
import os 

#TAREA 1 -  Carga y análisis de datos (Pandas

#1) Leer archivo CSV
df = pd.read_csv('datos_ventas.csv')

#2) Mostrar las filas y columnas 
print( df.head())

#Tarea 2 — Tabla resumen de datos

#3) Crear una tabla para imprimir el DataFrame
tabla_estetica = df.to_html()

#4) Montar un HTML completo (con título + estilo básico)
html_completo = f"""
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>GRUPO DAM</title>
<style>
    body {{
      font-family: Arial, sans-serif;
      margin: 30px;
    }}
    h1 {{
      margin-bottom: 5px;
    }}
    p {{
      color: #555;
      margin-top: 0;
    }}
    table {{
      border-collapse: collapse;
      width: 100%;
      margin-top: 15px;
    }}
    th, td {{
      border: 1px solid #ddd;
      padding: 10px;
      text-align: left;
    }}
    th {{
      background: #f2f2f2;
    }}
    tr:nth-child(even) {{
      background: #fafafa;
    }}
</style>
</head>
<body>
<h1>Grupo DAM</h1>
<p>Generado con Pandas (sin Datapane)</p>
 
  <h2>Tabla de datos</h2>
  {tabla_estetica}
</body>
</html>
"""

# 5) Guardar el HTML en un archivo
# Crear la carpeta 'salida' si no existe
if not os.path.exists('salida'):
    os.makedirs('salida')

with open('salida/tabla_datos.html', 'w', encoding='utf-8') as f:
    f.write(html_completo)
    
#Tarea 3 — Cálculo de valores agregados
  
# 6) Total de unidades vendidas
total_unidades_vendidas = df['Unidades'].sum()
print(f'Total de unidades vendidas: {total_unidades_vendidas}')

#7) Total importe de ventas
total_importe_ventas = df['Importe'].sum()   
print(f'Total importe de ventas: {total_importe_ventas}')

#8) Media de unidades por venta
media_unidades_por_venta = df['Unidades'].mean()
print(f'Media de unidades por venta: {media_unidades_por_venta}')

#9) Comercial con mayor importe total
comercial_mayor_importe = df.groupby('Nombre')['Importe'].sum().idxmax()
print(f'Comercial con mayor importe total: {comercial_mayor_importe}')
  
#Tarea 4 — Visualización de datos (Matplotlib)

#Gráfico 1 — Líneas. Evolución de unidades vendidas por mes

ax = df.groupby('Mes')['Unidades'].sum().plot(kind='line', marker='o', title='Evolución de Unidades Vendidas por Mes')
ax.set_xlabel('Mes')    
ax.set_ylabel('Unidades Vendidas')
plt.grid()
plt.savefig('salida/grafico_lineas_unidades.png')
plt.close()

#Gráfico 2 — Barras Importe total por comercial

ax2 = df.groupby('Nombre')['Importe'].sum().plot(kind='bar', title='Importe Total por Comercial', color='skyblue')
ax2.set_xlabel('Comercial')
ax2.set_ylabel('Importe Total')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.savefig('salida/grafico_barras_importe_comercial.png')
plt.close()

#Gráfico 3 — Sector Reparto de unidades por comercial

ax3 = df.groupby('Nombre')['Unidades'].sum().plot(kind='pie', title='Reparto de Unidades por Comercial', autopct='%1.1f%%', startangle=140)
ax3.set_ylabel('')  
plt.savefig('salida/grafico_sector_unidades.png')
plt.close()

#Tarea 5 - Informe final en HTML (CLAVE)

# Tarea 5 - Informe final en HTML (CLAVE)

# 10) Definir las rutas de las imágenes (relativas al archivo HTML)
grafico_1 = 'grafico_lineas_unidades.png'
grafico_2 = 'grafico_barras_importe_comercial.png'
grafico_3 = 'grafico_sector_unidades.png'

# 11) Montar el HTML final del informe
informe_html = f"""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="utf-8">
    <title>Informe Final de Ventas - Grupo DAM</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 40px;
            background-color: #f4f4f9;
            color: #333;
            line-height: 1.6;
        }}
        .container {{
            max-width: 900px;
            margin: auto;
            background: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }}
        h1 {{
            color: #2c3e50;
            border-bottom: 2px solid #3498db;
            padding-bottom: 10px;
        }}
        h2 {{
            color: #2980b9;
            margin-top: 30px;
        }}
        .resumen {{
            background: #e8f4fd;
            padding: 15px;
            border-left: 5px solid #3498db;
            margin: 20px 0;
        }}
        .grafico-container {{
            text-align: center;
            margin-top: 20px;
            padding: 20px;
            border: 1px solid #eee;
            border-radius: 5px;
        }}
        img {{
            max-width: 100%;
            height: auto;
            border-radius: 4px;
        }}
        footer {{
            margin-top: 40px;
            font-size: 0.8em;
            color: #888;
            text-align: center;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Informe Final de Rendimiento de Ventas</h1>
        <p>Este informe presenta el análisis visual de los datos de ventas procesados, incluyendo la evolución mensual, el rendimiento por comercial y la cuota de mercado en unidades.</p>
        
        <div class="resumen">
            <strong>Resumen Ejecutivo:</strong><br>
            • Unidades totales: {total_unidades_vendidas}<br>
            • Importe total: {total_importe_ventas} €<br>
            • Mejor comercial: {comercial_mayor_importe}
        </div>

        <h2>1. Evolución Temporal</h2>
        <p>Tendencia de las unidades vendidas a lo largo de los meses analizados.</p>
        <div class="grafico-container">
            <img src="{grafico_1}" alt="Evolución de Unidades">
        </div>

        <h2>2. Rendimiento Económico por Comercial</h2>
        <p>Comparativa del importe total generado por cada miembro del equipo.</p>
        <div class="grafico-container">
            <img src="{grafico_2}" alt="Importe por Comercial">
        </div>

        <h2>3. Distribución de Unidades</h2>
        <p>Porcentaje de unidades totales vendidas por cada comercial.</p>
        <div class="grafico-container">
            <img src="{grafico_3}" alt="Reparto de Unidades">
        </div>

        <footer>
            Generado automáticamente por el sistema de análisis Grupo DAM - {pd.Timestamp.now().strftime('%d/%m/%Y')}
        </footer>
    </div>
</body>
</html>
"""

# 12) Guardar el informe final en la carpeta 'salida'
with open('salida/informe_final.html', 'w', encoding='utf-8') as f:
    f.write(informe_html)

print("¡Informe final generado con éxito en 'salida/informe_final.html'!")

# 13) Abrir el HTML en el navegador predeterminado
import webbrowser
import os
webbrowser.open('file://' + os.path.realpath('salida/informe_final.html'))