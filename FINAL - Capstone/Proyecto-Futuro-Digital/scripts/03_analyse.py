import os
import pandas as pd
from scipy import stats

def realizar_analisis_avanzado():
    ruta_limpio = os.path.join("data", "latam_finanzas_clean.csv")
    
    print("=== INICIANDO ENTORNO DE ANÁLISIS ESTADÍSTICO AVANZADO ===")
    df = pd.read_csv(ruta_limpio)
    
    # 1. Comparativa de Ingresos por País
    print("\n--- 1. Ingreso Mensual Promedio por País ---")
    ingreso_pais = df.groupby('pais')['ingreso_mensual_usd'].mean().sort_values(ascending=False)
    print(ingreso_pais)
    
    # 2. Correlación de Edad vs Tasa de Ahorro
    print("\n--- 2. Correlación de Pearson: Edad vs Ahorro Mensual ---")
    corr_edad_ahorro, p_val1 = stats.pearsonr(df['edad'], df['ahorro_mensual_usd'])
    print(f"Coeficiente de Correlación: {corr_edad_ahorro:.4f} (p-valor: {p_val1:.4e})")
    
    # 3. Desglose de Gastos Promedio a Nivel Regional
    print("\n--- 3. Desglose de Canasta de Gastos Promedio Regional (USD) ---")
    columnas_gastos = [c for c in df.columns if 'gasto_' in c]
    gastos_promedio = df[columnas_gastos].mean().sort_values(ascending=False)
    print(gastos_promedio)
    
    # 4. Impacto del Uso de Tarjetas de Crédito en las Deudas
    print("\n--- 4. Deuda Promedio: Usuarios con Tarjeta vs Sin Tarjeta ---")
    deuda_tarjeta = df.groupby('tiene_tarjeta_credito')['deuda_total_usd'].mean()
    print(deuda_tarjeta)
    
    # 5. Correlación: Horas de IA a la semana vs Satisfacción Financiera
    print("\n--- 5. Correlación de Pearson: Horas de IA vs Satisfacción Financiera ---")
    corr_ia_sat, p_val2 = stats.pearsonr(df['horas_herramientas_ia_semana'], df['satisfaccion_financiera'])
    print(f"Coeficiente de Correlación: {corr_ia_sat:.4f} (p-valor: {p_val2:.4e})")
    
    # 6. Carga de Vivienda Relativa por País (Gasto Vivienda / Ingreso)
    print("\n--- 6. Carga Financiera de Vivienda Promedio por País ---")
    df['carga_vivienda'] = df['gasto_vivienda_usd'] / df['ingreso_mensual_usd']
    carga_vivienda_pais = df.groupby('pais')['carga_vivienda'].mean().sort_values(ascending=False)
    print(carga_vivienda_pais)
    
    print("\n✅ ¡Fase 3 Completada! Todos los cálculos matemáticos requeridos están listos.")

if __name__ == "__main__":
    realizar_analisis_avanzado()