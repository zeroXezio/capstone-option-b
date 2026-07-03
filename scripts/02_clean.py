import pandas as pd
import os

# Definir rutas de archivos
raw_path = "data/latam_finanzas_2025.csv"
clean_path = "data/latam_finanzas_clean.csv"
log_path = "data_quality_log.txt"

# Cargar el dataset original
df = pd.read_csv(raw_path)

# Preparar las líneas del reporte de calidad
log_lines = [
    "========================================================================",
    "DATA QUALITY & CLEANING LOG — FUTURO DIGITAL LATAM",
    "========================================================================\n"
]

# --- 1. MANEJO DE VALORES NULOS (SALUD) ---
null_salud_count = df['gasto_salud_usd'].isnull().sum()
mediana_salud = df['gasto_salud_usd'].median()
df['gasto_salud_usd'] = df['gasto_salud_usd'].fillna(mediana_salud)

log_lines.append(f"[MISSING VALUES] Found {null_salud_count} null rows in 'gasto_salud_usd'.")
log_lines.append(f"   -> Strategy: Imputed missing values with column median: ${mediana_salud:.2f} USD.\n")


# --- 2. NORMALIZACIÓN DE CATEGORÍAS (TECNOLOGÍA) ---
mapeo_industria = {
    'Tecnologia': 'Tecnología',
    'tech': 'Tecnología',
    'TECNOLOGÍA': 'Tecnología'
}
dirty_tech_count = df['industria'].isin(mapeo_industria.keys()).sum()
df['industria'] = df['industria'].replace(mapeo_industria)

# Quitar espacios en blanco invisibles al inicio o final de los textos
for col in df.select_dtypes(include=['object']).columns:
    df[col] = df[col].str.strip()

log_lines.append(f"[CATEGORICAL TEXT] Found {dirty_tech_count} inconsistent records in 'industria'.")
log_lines.append("   -> Strategy: Standardized variants to 'Tecnología' and applied str.strip() to all text columns.\n")


# --- 3. ANÁLISIS DE AHORRO NEGATIVO ---
negative_savings_count = (df['ahorro_mensual_usd'] < 0).sum()
log_lines.append(f"[NUMERIC ANOMALIES] Detected {negative_savings_count} rows with negative values in 'ahorro_mensual_usd'.")
log_lines.append("   -> Strategy: Preserved values intact because negative savings represent a real financial deficit (spending exceeds income).\n")


# --- 4. EXPORTAR RESULTADOS ---
df.to_csv(clean_path, index=False)
log_lines.append(f"[OUTPUT] Clean dataset successfully exported to: '{clean_path}' ({df.shape[0]} rows).")
log_lines.append("========================================================================")

# Escribir el archivo final de log
with open(log_path, "w", encoding="utf-8") as f:
    f.write("\n".join(log_lines))

print("✔ ¡Fase 2 Completada! Se generaron 'data/latam_finanzas_clean.csv' y 'data_quality_log.txt'.")