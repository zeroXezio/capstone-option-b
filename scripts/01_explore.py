import pandas as pd

# 1. Leer el archivo CSV original
csv_path = "data/latam_finanzas_2025.csv"
df = pd.read_csv(csv_path)

print("="*60)
print("PHASE 1: DATASET EXPLORATION")
print("="*60)

# 1. Número de filas y columnas
print(f"\n[1] Shape of Dataset:\nRows: {df.shape[0]} | Columns: {df.shape[1]}")

# 2. Listar columnas y tipos de datos
print("\n[2] Column Names and Data Types:")
print(df.dtypes)

# 3. Contar valores perdidos/nulos por columna
print("\n[3] Missing Values per Column (Sorted):")
missing_vals = df.isnull().sum().sort_values(ascending=False)
print(missing_vals[missing_vals > 0] if missing_vals.sum() > 0 else "No missing values found.")

# 4. Basic Statistics for Numeric Columns
print("--- ESTADÍSTICAS BÁSICAS (NUMÉRICAS) ---")
stats = df.describe().T
stats = stats.rename(columns={'50%': 'median'})  # Cambiamos '50%' por 'median'
print(stats[['min', 'max', 'mean', 'median', 'std']])
print()

# 5. Valores únicos para variables categóricas solicitadas
categorical_cols = ['pais', 'industria', 'ocupacion', 'meta_financiera', 'tiene_tarjeta_credito', 'tiene_cuenta_ahorro', 'tiene_deuda']
print("\n[5] Unique Value Counts for Categorical Columns:")
for col in categorical_cols:
    if col in df.columns:
        print(f"\n--- Column: {col} (Top 5 values) ---")
        print(df[col].value_counts().head(5))

print("\n"+"="*60)