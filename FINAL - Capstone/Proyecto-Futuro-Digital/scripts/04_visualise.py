import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def generar_visualizaciones_estrictas():
    ruta_limpio = os.path.join("data", "latam_finanzas_clean.csv")
    carpeta_charts = "charts"
    
    print("=== INICIANDO PIPELINE DE VISUALIZACIÓN PROFESIONAL ===")
    if not os.path.exists(carpeta_charts):
        os.makedirs(carpeta_charts)
        
    df = pd.read_csv(ruta_limpio)
    sns.set_theme(style="whitegrid")
    
    # --- CHART 1: Box Plot de Ingresos por País ---
    plt.figure(figsize=(9, 5))
    sns.boxplot(data=df, x='pais', y='ingreso_mensual_usd', hue='pais', palette='Blues_r', legend=False)
    plt.title('Distribución de Ingresos Mensuales por País', fontsize=12, fontweight='bold')
    plt.savefig(os.path.join(carpeta_charts, "01_income_by_country.png"), bbox_inches='tight')
    plt.close()
    print("Chart saved: 01_income_by_country.png 1/5 charts complete")

    # --- CHART 2: Scatter Plot Edad vs Ahorro con Línea de Tendencia ---
    plt.figure(figsize=(8, 5))
    sns.regplot(data=df, x='edad', y='ahorro_mensual_usd', scatter_kws={'alpha':0.5, 'color':'teal'}, line_kws={'color':'red', 'linewidth':2})
    plt.title('Edad vs. Ahorro Mensual (Con Línea de Tendencia)', fontsize=12, fontweight='bold')
    plt.savefig(os.path.join(carpeta_charts, "02_age_vs_savings.png"), bbox_inches='tight')
    plt.close()
    print("Chart saved: 02_age_vs_savings.png 2/5 charts complete")

    # --- CHART 3: Bar Chart Horizontal de Desglose de Gastos ---
    plt.figure(figsize=(9, 5))
    columnas_gastos = [c for c in df.columns if 'gasto_' in c]
    gastos_promedio = df[columnas_gastos].mean().sort_values(ascending=False).reset_index()
    gastos_promedio['index'] = gastos_promedio['index'].str.replace('_usd', '').str.replace('gasto_', '').str.capitalize()
    sns.barplot(data=gastos_promedio, x=0, y='index', hue='index', palette='Purples_r', legend=False)
    plt.title('Desglose de la Canasta de Gastos Promedio Regional', fontsize=12, fontweight='bold')
    plt.xlabel('Gasto Promedio (USD)')
    plt.savefig(os.path.join(carpeta_charts, "03_spending_breakdown.png"), bbox_inches='tight')
    plt.close()
    print("Chart saved: 03_spending_breakdown.png 3/5 charts complete")

    # --- CHART 4: Bar Chart de Satisfacción según Horas de IA ---
    plt.figure(figsize=(8, 5))
    sns.barplot(data=df, x='satisfaccion_financiera', y='horas_herramientas_ia_semana', hue='satisfaccion_financiera', palette='coolwarm', legend=False)
    plt.title('Uso Semanal de IA por Nivel de Satisfacción Financiera', fontsize=12, fontweight='bold')
    plt.savefig(os.path.join(carpeta_charts, "04_satisfaction_by_ia.png"), bbox_inches='tight')
    plt.close()
    print("Chart saved: 04_satisfaction_by_ia.png 4/5 charts complete")

    # --- CHART 5: Horizontal Bar Chart con Gradiente de Carga de Vivienda por País ---
    plt.figure(figsize=(9, 5))
    df['carga_vivienda'] = df['gasto_vivienda_usd'] / df['ingreso_mensual_usd']
    carga_pais = df.groupby('pais')['carga_vivienda'].mean().sort_values(ascending=False).reset_index()
    
    # Crear un gradiente de color de Rojo (Alta carga) a Verde (Baja carga)
    colores_gradient = plt.cm.RdYlGn_r(np.linspace(0.1, 0.8, len(carga_pais)))
    
    plt.barh(carga_pais['pais'], carga_pais['carga_vivienda'], color=colores_gradient, edgecolor='gray')
    plt.gca().invert_yaxis()  # El más alto arriba
    plt.title('Carga Financiera Destinada a Vivienda por País (Proporción del Ingreso)', fontsize=12, fontweight='bold')
    plt.xlabel('Proporción del Gasto en Vivienda vs Ingreso Total')
    plt.savefig(os.path.join(carpeta_charts, "05_housing_burden_by_country.png"), bbox_inches='tight')
    plt.close()
    print("Chart saved: 05_housing_burden_by_country.png 5/5 charts complete")

    print("\n🎉 ¡Fase 4 Completada! Los 5 gráficos estructurales han sido generados exitosamente.")

if __name__ == "__main__":
    generar_visualizaciones_estrictas()