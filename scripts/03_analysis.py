import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# 1. Definir rutas de archivos
clean_path = "data/latam_finanzas_clean.csv"
plots_dir = "plots"
os.makedirs(plots_dir, exist_ok=True)

# 2. Cargar el dataset limpio
df = pd.read_csv(clean_path)

print("==============================================================")
print("PHASE 3: DATA ANALYSIS & VISUALIZATION")
print("==============================================================")

# 3. Métrica Clave 1: Promedio de ingresos y ahorros por país
print("\n[1] Resumen Financiero Promedio por País:")
resumen_pais = df.groupby('pais')[['ingreso_mensual_usd', 'ahorro_mensual_usd']].mean()
print(resumen_pais.round(2).to_string())

# 4. Métrica Clave 2: ¿Quienes usan más IA tienen más satisfacción financiera?
print("\n[2] Impacto del Uso de IA en la Satisfacción Financiera:")
ia_impacto = df.groupby('satisfaccion_financiera')['horas_herramientas_ia_semana'].mean()
print(ia_impacto.round(2).to_string())

# 5. GENERAR Y GUARDAR GRÁFICA PROFESIONAL
print("\n[3] Generando gráfico de barras: Ahorro Mensual Promedio por País...")

# Configurar el estilo visual del gráfico
sns.set_theme(style="whitegrid")
plt.figure(figsize=(10, 6))

# Crear la gráfica de barras
grafica = sns.barplot(
    x=resumen_pais.index, 
    y='ahorro_mensual_usd', 
    data=resumen_pais, 
    palette="Blues_r",
    hue=resumen_pais.index,
    legend=False
)

# Añadir títulos y etiquetas limpias
plt.title('Ahorro Mensual Promedio por País en LATAM (2025)', fontsize=14, pad=15, weight='bold')
plt.xlabel('País', fontsize=12, labelpad=10)
plt.ylabel('Ahorro Promedio (USD)', fontsize=12, labelpad=10)

# Guardar la gráfica en la carpeta 'plots'
plot_output_path = os.path.join(plots_dir, "ahorro_promedio_pais.png")
plt.savefig(plot_output_path, dpi=300, bbox_inches='tight')
plt.close()

print(f"✔ ¡Gráfico exportado con éxito a: '{plot_output_path}'!")
print("==============================================================")