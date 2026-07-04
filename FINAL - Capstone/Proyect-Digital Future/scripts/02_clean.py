import os
import pandas as pd

def clean_dataset():
    # Asegurar rutas correctas
    input_path = "data/latam_finanzas_2025.csv"
    output_dir = "data"
    output_path = os.path.join(output_dir, "latam_finanzas_clean.csv")
    
    if not os.path.exists(input_path):
        print(f"Error: {input_path} not found.")
        return

    # 1. Cargar el dataset original
    df = pd.read_csv(input_path)
    print(f"Initial shape: {df.shape[0]} rows, {df.shape[1]} columns")

    # PROBLEM 1: Direct PII exposure (Participant names)
    # FIX: Drop the 'nombre' column entirely to guarantee data privacy.
    df_clean = df.drop(columns=['nombre'])
    print("- Problem 1 Fixed: Removed 'nombre' column for participant privacy.")

    # PROBLEM 2: 33 missing values identified in 'gasto_salud_usd'
    # FIX: Robust statistical imputation using the regional median ($45.66)
    regional_median_health = df_clean['gasto_salud_usd'].median() # Arroja 45.66
    missing_count = df_clean['gasto_salud_usd'].isna().sum()
    df_clean['gasto_salud_usd'] = df_clean['gasto_salud_usd'].fillna(regional_median_health)
    print(f"- Problem 2 Fixed: Imputed {missing_count} null rows in 'gasto_salud_usd' using regional median (${regional_median_health:.2f}).")

    # Guardar archivo limpio
    os.makedirs(output_dir, exist_ok=True)
    df_clean.to_csv(output_path, index=False)
    print(f"Cleaned dataset successfully saved to: {output_path}")
    print(f"Final shape: {df_clean.shape[0]} rows, {df_clean.shape[1]} columns")

if __name__ == "__main__":
    clean_dataset()