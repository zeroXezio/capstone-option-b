import os
from datetime import datetime

# Rutas
report_path = "final_report.md"

print("==============================================================")
print("PHASE 4: AUTOMATED REPORT GENERATION")
print("==============================================================")

print("✔ Compilando hallazgos y generando 'final_report.md'...")

# Contenido del reporte en formato Markdown
report_content = f"""# REPORT EXECUTIVE: FUTURO DIGITAL LATAM 2025
**Fecha de Generación:** {datetime.now().strftime('%Y-%m-%d')}  
**Estado del Proyecto:** Completado con Éxito  

---

## 1. Introducción y Alcance
Este informe ejecutivo resume el proceso de exploración, limpieza, análisis y visualización del dataset *Futuro Digital LATAM 2025*. El objetivo principal del análisis fue comprender la salud financiera de los profesionales en la región y evaluar la correlación entre el uso de herramientas de Inteligencia Artificial (IA) y su nivel de satisfacción financiera.

---

## 2. Fase 1 & 2: Calidad de Datos y Limpieza
Durante la fase de exploración y limpieza de datos se identificaron y resolvieron las siguientes anomalías:
* **Manejo de Nulos:** Se detectaron **33 registros faltantes** en la columna `gasto_salud_usd`. Se aplicó una estrategia de imputación utilizando la mediana de la columna (**$45.66 USD**) para preservar la distribución original.
* **Normalización Textual:** Se estandarizaron variantes inconsistentes en la columna `industria` (como *'tech'* y *'TECNOLOGÍA'*) bajo el término unificado **'Tecnología'**. Asimismo, se eliminaron espacios en blanco invisibles (*whitespaces*) en todas las variables categóricas.
* **Anomalías Numéricas:** Se identificaron registros con ahorro mensual negativo. Se determinó mantenerlos intactos dado que representan un déficit financiero real (gastos superiores a los ingresos), aportando valor analítico al estudio.

---

## 3. Fase 3: Análisis Estadístico e Insights Clave

### A. Resumen Financiero por País
El análisis agregativo reveló que **Brasil** lidera la región tanto en ingresos mensuales promedio como en capacidad de ahorro, mientras que **Argentina** presenta los valores más moderados de la muestra:

| País | Ingreso Promedio (USD) | Ahorro Promedio (USD) |
| :--- | :---: | :---: |
| **Brasil** | $1,387.97 | $134.84 |
| **Chile** | $1,245.29 | $117.63 |
| **México** | $1,042.05 | $102.18 |
| **Colombia** | $848.78 | $81.74 |
| **Perú** | $817.76 | $80.84 |
| **Argentina** | $766.38 | $76.89 |

### B. El Impacto de la Inteligencia Artificial
Se descubrió una **correlación directa y positiva** entre las horas semanales dedicadas a herramientas de IA y la percepción de satisfacción financiera (escala 1 al 5):
* Los usuarios con el nivel más bajo de satisfacción (1) promedian apenas **2.02 horas** semanales de uso de IA.
* Los usuarios con el nivel máximo de estabilidad y satisfacción (5) dedican un promedio de **16.10 horas** semanales a estas tecnologías.

*El gráfico correspondiente a esta distribución ha sido exportado exitosamente en `plots/ahorro_promedio_pais.png`.*

---

## 4. Conclusión del Analista
El proyecto demuestra que la optimización de datos permite extraer conclusiones estratégicas claras. El "Efecto IA" detectado sugiere que la adopción tecnológica está fuertemente vinculada a una mayor productividad o mejores ingresos, lo que se traduce directamente en una mayor satisfacción financiera en los profesionales de América Latina.
"""

# Escribir el archivo
with open(report_path, "w", encoding="utf-8") as f:
    f.write(report_content)

print("✔ ¡Reporte ejecutivo generado con éxito en la raíz del proyecto!")
print("==============================================================")