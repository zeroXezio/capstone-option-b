import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# 1. Rutas
clean_path = "data/latam_finanzas_clean.csv"
charts_dir = "charts"
os.makedirs(charts_dir, exist_ok=True)

# Cargar datos
df = pd.read_csv(clean_path)
sns.set_theme(style="whitegrid")

print("==============================================================")
print("GENERANDO LAS 5 GRÁFICAS REQUERIDAS POR LA RÚBRICA...")
print("==============================================================")

# --- GRÁFICA 1: Ahorro Promedio por País ---
plt.figure(figsize=(8, 5))
resumen_pais = df.groupby('pais')['ahorro_mensual_usd'].mean().reset_index()
sns.barplot(x='pais', y='ahorro_mensual_usd', data=resumen_pais, palette="Blues_r", hue='pais', legend=False)
plt.title('1. Ahorro Mensual Promedio por País')
plt.savefig(f"{charts_dir}/ahorro_promedio_pais.png", dpi=300, bbox_inches='tight')
plt.close()
print("✔ Gráfica 1 generada.")

# --- GRÁFICA 2: Impacto de la IA en la Satisfacción ---
plt.figure(figsize=(8, 5))
ia_impacto = df.groupby('satisfaccion_financiera')['horas_herramientas_ia_semana'].mean().reset_index()
sns.lineplot(x='satisfaccion_financiera', y='horas_herramientas_ia_semana', data=ia_impacto, marker="o", color="green", linewidth=2.5)
plt.title('2. Horas de IA Semanales vs Satisfacción Financiera')
plt.savefig(f"{charts_dir}/impacto_ia_satisfaccion.png", dpi=300, bbox_inches='tight')
plt.close()
print("✔ Gráfica 2 generada.")

# --- GRÁFICA 3: Distribución de Ingresos por Industria ---
plt.figure(figsize=(10, 5))
sns.boxplot(x='industria', y='ingreso_mensual_usd', data=df, palette="Set2", hue='industria', legend=False)
plt.xticks(rotation=15)
plt.title('3. Distribución de Ingresos Mensuales por Industria')
plt.savefig(f"{charts_dir}/ingresos_por_industria.png", dpi=300, bbox_inches='tight')
plt.close()
print("✔ Gráfica 3 generada.")

# --- GRÁFICA 4: Metas Financieras más Comunes ---
plt.figure(figsize=(8, 5))
sns.countplot(y='meta_financiera', data=df, order=df['meta_financiera'].value_counts().index, palette="viridis", hue='meta_financiera', legend=False)
plt.title('4. Frecuencia de Metas Financieras en LATAM')
plt.savefig(f"{charts_dir}/metas_financieras.png", dpi=300, bbox_inches='tight')
plt.close()
print("✔ Gráfica 4 generada.")

# --- GRÁFICA 5: Relación entre Ingreso y Ahorro ---
plt.figure(figsize=(8, 5))
sns.scatterplot(x='ingreso_mensual_usd', y='ahorro_mensual_usd', hue='tiene_tarjeta_credito', data=df, alpha=0.7)
plt.title('5. Relación entre Ingresos y Ahorros Mensuales')
plt.savefig(f"{charts_dir}/relacion_ingreso_ahorro.png", dpi=300, bbox_inches='tight')
plt.close()
print("✔ Gráfica 5 generada. ¡Mínimo de la rúbrica cumplido!")
print("==============================================================")