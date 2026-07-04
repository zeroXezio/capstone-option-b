import os
import pandas as pd

def ejecutar_country_profiler():
    ruta_limpio = os.path.join("data", "latam_finanzas_clean.csv")
    print("=== INICIANDO AGENTE: COUNTRY PROFILER (FASE 2.5) ===")
    
    if not os.path.exists(ruta_limpio):
        print("❌ Error: No se encuentra el dataset limpio.")
        return
        
    df = pd.read_csv(ruta_limpio)
    paises = df['pais'].unique()
    
    print(f"🌍 Identificados {len(paises)} países en la muestra. Procesando perfiles...")
    
    # Simular la extracción estructurada del agente por cada país
    for pais in paises:
        df_sub = df[df['pais'] == pais]
        muestra = int(len(df_sub))
        ingreso_mediano = float(df_sub['ingreso_mensual_usd'].median())
        
        # Calcular carga de vivienda promedio
        carga_viv = (df_sub['gasto_vivienda_usd'] / df_sub['ingreso_mensual_usd']).mean()
        
        print(f"\n📌 Perfil Estructurado para [ {pais} ]:")
        print(f"   - Muestra: {muestra} encuestados")
        print(f"   - Ingreso Mediano: ${ingreso_mediano:.2f} USD")
        print(f"   - Carga Vivienda Promedio: {carga_viv:.4f} ({carga_viv*100:.1f}%)")
        
    print("\n🎉 ¡Fase 2.5 Completada! Datos listos para sincronizar en la base de datos 'Country Profiles' de Notion.")

if __name__ == "__main__":
    ejecutar_country_profiler()