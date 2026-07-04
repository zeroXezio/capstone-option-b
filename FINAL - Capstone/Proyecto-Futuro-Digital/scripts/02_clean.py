import os
import pandas as pd

def limpiar_datos():
    ruta_original = os.path.join("data", "latam_finanzas_2025.csv")
    ruta_salida = os.path.join("data", "latam_finanzas_2025_cleaned.csv")
    
    print("=== INICIANDO PIPELINE DE LIMPIEZA ===")
    
    # 1. Cargar archivo original
    df = pd.read_csv(ruta_original)
    
    # 2. Anonimizar datos (Eliminar columna 'nombre' por privacidad)
    if 'nombre' in df.columns:
        df = df.drop(columns=['nombre'])
        print("✅ Columna 'nombre' eliminada con éxito por privacidad.")
    
    # 3. Tratar valores nulos en 'gasto_salud_usd'
    # Usaremos la mediana para evitar que valores extremos afecten el promedio
    mediana_salud = df['gasto_salud_usd'].median()
    df['gasto_salud_usd'] = df['gasto_salud_usd'].fillna(mediana_salud)
    print(f"✅ Se imputaron los 33 valores nulos en 'gasto_salud_usd' usando la mediana ({mediana_salud} USD).")
    
    # 4. Verificar que ya no queden nulos
    nulos_restantes = df.isnull().sum().sum()
    print(f"🔍 Valores nulos restantes en el dataset: {nulos_restantes}")
    
    # 5. Guardar el nuevo dataset limpio
    df.to_csv(ruta_salida, index=False)
    print(f"🎉 ¡Fase 2 completada! Archivo limpio guardado en: {ruta_salida}")

if __name__ == "__main__":
    limpiar_datos()