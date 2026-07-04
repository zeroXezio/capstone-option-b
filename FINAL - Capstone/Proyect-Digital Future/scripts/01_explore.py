import os
import pandas as pd

def explorar_datos():
    # Definir la ruta del dataset
    ruta_data = os.path.join("data", "latam_finanzas_2025.csv")
    
    print("=== INICIANDO EXPLORACIÓN DE DATOS ===")
    
    # Verificar si el archivo existe
    if not os.path.exists(ruta_data):
        print(f"❌ Error: No se encontró el archivo en la ruta: {ruta_data}")
        print("Por favor, asegúrate de colocar el archivo .csv dentro de una carpeta llamada 'data'.")
        return

    # Cargar el dataset
    df = pd.read_csv(ruta_data)
    
    # 1. Dimensiones del dataset
    filas, columnas = df.shape
    print(f"✅ Dataset cargado correctamente.")
    print(f"📊 Dimensiones: {filas} filas y {columnas} columnas.\n")
    
    # 2. Mostrar las primeras filas
    print("👀 Primeras 5 filas del dataset:")
    print(df.head())
    print("\n" + "="*40 + "\n")
    
    # 3. Tipos de datos e información general
    print("ℹ️ Información de las columnas y tipos de datos:")
    print(df.info())
    
    # 4. Detectar valores nulos iniciales
    print("\n🔍 Conteo de valores nulos por columna:")
    print(df.isnull().sum())

if __name__ == "__main__":
    explorar_datos()