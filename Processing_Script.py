import psychrolib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

# Configuración inicial de Psychrolib
psychrolib.SetUnitSystem(psychrolib.SI)
pressure = 101325  # Presión atmosférica en Pa

# Función para crear y guardar el gráfico psicrométrico
def create_psychrometric_chart(file_path):
    # Extraer los primeros 6 caracteres del nombre de archivo para el título
    title = os.path.basename(file_path)[:7]

    # Cargar datos desde CSV
    datos = pd.read_csv(file_path)
    datos.columns = datos.columns.str.strip()  # Elimina espacios adicionales en los nombres de columnas
    datos['humidity'] = datos['humidity'] / 100  # Convertir porcentaje a fracción
    datos['humidity_ratio'] = datos.apply(lambda row: psychrolib.GetHumRatioFromRelHum(row['temperature'], row['humidity'], pressure), axis=1)

    # Crear el gráfico
    f, ax = plt.subplots()

    # Líneas de humedad relativa y temperatura de bulbo húmedo constantes
    t_array = np.arange(5, 45, 0.1)
    rh_array = np.arange(0, 1.1, 0.1)
    for rh in rh_array:
        hr_array = [psychrolib.GetHumRatioFromRelHum(t, rh, pressure) for t in t_array]
        ax.plot(t_array, hr_array, 'k', linewidth=0.5)

    # Datos experimentales
    ax.scatter(datos['temperature'], datos['humidity_ratio'], color='red', marker='x', label='Datos Reales')

    # Zona de confort térmica
    temp_comfort_range = np.arange(18, 24.1, 0.1)
    hr_low = [psychrolib.GetHumRatioFromRelHum(t, 0.30, pressure) for t in temp_comfort_range]
    hr_high = [psychrolib.GetHumRatioFromRelHum(t, 0.60, pressure) for t in temp_comfort_range]
    ax.fill_between(temp_comfort_range, hr_low, hr_high, color='green', alpha=0.3, label='Zona de Confort')

    # Dibujar bordes sólidos de la zona de confort
    ax.plot(temp_comfort_range, hr_low, 'green', linewidth=2)
    ax.plot(temp_comfort_range, hr_high, 'green', linewidth=2)

    # Contar puntos dentro de la zona de confort
    comfort_data_count = datos[(datos['temperature'] >= temp_comfort_range[0]) & 
                               (datos['temperature'] <= temp_comfort_range[-1]) &
                               (datos['humidity_ratio'] >= min(hr_low)) & 
                               (datos['humidity_ratio'] <= max(hr_high))].shape[0]

    # Mostrar cantidad de datos en zona de confort
    ax.text(5, 0.025, f'Datos en zona de confort: {comfort_data_count}', fontsize=12, color='blue', horizontalalignment='left')

    # Configuraciones adicionales y visualización
    ax.set_ylim(0, 0.03)
    ax.set_xlim(5, 45)
    ax.set_xlabel("Temperatura de Bulbo Seco (°C)")
    ax.set_ylabel("Relación de Humedad (kg/kg de aire seco)")
    ax.legend()
    ax.set_title(title)  # Establecer el título

    plt.tight_layout()

    # Guardar el gráfico en formato PDF
    save_path = os.path.join(os.path.dirname(file_path), title + "_chart.pdf")
    plt.savefig(save_path)
    plt.close()
    print(f"Gráfico guardado en: {save_path}")

# Lista de archivos para procesar
file_paths = [
   r"C:\Users\andre\OneDrive - Universidad Católica de Chile\Construccion Civil\Fondecyt 11220965\4.- Datas\3.- datos general\154541 2022-11-30 2024-04-01 10-Minute Average_processed.csv",
r"C:\Users\andre\OneDrive - Universidad Católica de Chile\Construccion Civil\Fondecyt 11220965\4.- Datas\3.- datos general\153560 2022-11-30 2024-04-01 10-Minute Average_processed.csv",
r"C:\Users\andre\OneDrive - Universidad Católica de Chile\Construccion Civil\Fondecyt 11220965\4.- Datas\3.- datos general\154183 2022-11-30 2024-04-01 10-Minute Average_processed.csv",
r"C:\Users\andre\OneDrive - Universidad Católica de Chile\Construccion Civil\Fondecyt 11220965\4.- Datas\3.- datos general\154241 2022-11-30 2024-04-01 10-Minute Average_processed.csv",
r"C:\Users\andre\OneDrive - Universidad Católica de Chile\Construccion Civil\Fondecyt 11220965\4.- Datas\3.- datos general\154287 2022-11-30 2024-04-01 10-Minute Average_processed.csv",
r"C:\Users\andre\OneDrive - Universidad Católica de Chile\Construccion Civil\Fondecyt 11220965\4.- Datas\3.- datos general\154291 2022-11-30 2024-04-01 10-Minute Average_processed.csv",
r"C:\Users\andre\OneDrive - Universidad Católica de Chile\Construccion Civil\Fondecyt 11220965\4.- Datas\3.- datos general\154435 2022-11-30 2024-04-01 10-Minute Average_processed.csv",
r"C:\Users\andre\OneDrive - Universidad Católica de Chile\Construccion Civil\Fondecyt 11220965\4.- Datas\3.- datos general\151572 2022-11-30 2024-04-01 10-Minute Average_processed.csv",
r"C:\Users\andre\OneDrive - Universidad Católica de Chile\Construccion Civil\Fondecyt 11220965\4.- Datas\3.- datos general\154557 2022-11-30 2024-04-01 10-Minute Average_processed.csv",
r"C:\Users\andre\OneDrive - Universidad Católica de Chile\Construccion Civil\Fondecyt 11220965\4.- Datas\3.- datos general\154561 2022-11-30 2024-04-01 10-Minute Average_processed.csv",
r"C:\Users\andre\OneDrive - Universidad Católica de Chile\Construccion Civil\Fondecyt 11220965\4.- Datas\3.- datos general\154563 2022-11-30 2024-04-01 10-Minute Average_processed.csv",
r"C:\Users\andre\OneDrive - Universidad Católica de Chile\Construccion Civil\Fondecyt 11220965\4.- Datas\3.- datos general\154569 2022-11-30 2024-04-01 10-Minute Average_processed.csv",
r"C:\Users\andre\OneDrive - Universidad Católica de Chile\Construccion Civil\Fondecyt 11220965\4.- Datas\3.- datos general\154697 2022-11-30 2024-04-01 10-Minute Average_processed.csv",
r"C:\Users\andre\OneDrive - Universidad Católica de Chile\Construccion Civil\Fondecyt 11220965\4.- Datas\3.- datos general\154699 2022-11-30 2024-04-01 10-Minute Average_processed.csv",
r"C:\Users\andre\OneDrive - Universidad Católica de Chile\Construccion Civil\Fondecyt 11220965\4.- Datas\3.- datos general\154443 2022-11-30 2024-04-01 10-Minute Average_processed.csv",
r"C:\Users\andre\OneDrive - Universidad Católica de Chile\Construccion Civil\Fondecyt 11220965\4.- Datas\3.- datos general\154451 2022-11-30 2024-04-01 10-Minute Average_processed.csv",
r"C:\Users\andre\OneDrive - Universidad Católica de Chile\Construccion Civil\Fondecyt 11220965\4.- Datas\3.- datos general\154455 2022-11-30 2024-04-01 10-Minute Average_processed.csv",
r"C:\Users\andre\OneDrive - Universidad Católica de Chile\Construccion Civil\Fondecyt 11220965\4.- Datas\3.- datos general\154485 2022-11-30 2024-04-01 10-Minute Average_processed.csv",
r"C:\Users\andre\OneDrive - Universidad Católica de Chile\Construccion Civil\Fondecyt 11220965\4.- Datas\3.- datos general\154491 2022-11-30 2024-04-01 10-Minute Average_processed.csv",
r"C:\Users\andre\OneDrive - Universidad Católica de Chile\Construccion Civil\Fondecyt 11220965\4.- Datas\3.- datos general\154521 2022-11-30 2024-04-01 10-Minute Average_processed.csv",
r"C:\Users\andre\OneDrive - Universidad Católica de Chile\Construccion Civil\Fondecyt 11220965\4.- Datas\general_datos_transformadost.csv"
    # Lista tus archivos aquí
]

# Ejecutar la función para cada archivo
for file_path in file_paths:
    create_psychrometric_chart(file_path)
