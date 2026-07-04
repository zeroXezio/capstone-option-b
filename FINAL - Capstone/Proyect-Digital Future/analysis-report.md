# Reporte de Análisis Ejecutivo: Encuesta de Bienestar Financiero LATAM 2025

**Proyecto Capstone Avanzado – Arquitectura de Pipeline Automatizado
Institución:** Cardiff University / Universidad Anáhuac Mayab
**Fecha:** Julio 2026

\---

## 1\. Resumen Ejecutivo

Este informe presenta un diagnóstico integral sobre la salud financiera de jóvenes profesionales en América Latina, fundamentado en una muestra representativa de 500 encuestados distribuidos en 6 países clave de la región. El análisis se ejecutó mediante un pipeline automatizado, reproducible y auditable que garantiza la integridad de los datos mediante la eliminación de variables sensibles y la imputación estadística de valores nulos. Los hallazgos revelan marcadas asimetrías en la distribución del ingreso mensual promedio por país y una relación crítica entre los niveles de endeudamiento y la capacidad de reserva de capital. Asimismo, se identificó que el uso de herramientas de inteligencia artificial guarda una correspondencia notable con la percepción de control y satisfacción financiera individual. A partir de estas métricas, se proponen intervenciones de educación financiera altamente personalizadas que abandonan el enfoque homogéneo tradicional para adoptar soluciones adaptadas a la volatilidad económica y los marcos laborales locales, garantizando resiliencia e inclusión financiera escalable a largo plazo para la organización.

\---

## 2\. Metodología

El análisis se estructuró como un ecosistema automatizado dentro del entorno de desarrollo para asegurar la reproducibilidad continua ante futuras encuestas anuales. La ingesta inicial validó 500 registros y 21 variables. El proceso de limpieza ejecutó la anonimización de la base mediante la remoción de la columna de identificación de nombres. Posteriormente, se aislaron 33 registros nulos en la variable de salud, aplicando un algoritmo de imputación basado en la mediana regional ($45.66 USD) para prevenir distorsiones por valores atípicos. Las fases de cómputo estadístico implementaron correlaciones de Pearson a través de la librería `scipy` y las regresiones visuales se procesaron con `seaborn`.

\---

## 3\. Perfil de la Muestra

La muestra está compuesta por 500 jóvenes profesionales de América Latina pertenecientes a sectores dinámicos de la economía. La distribución por edades se concentra principalmente entre los 22 y los 35 años, reflejando una población en etapas tempranas y medias de consolidación profesional. El perfil laboral incluye un balance entre trabajadores corporativos asalariados y un segmento representativo de profesionales independientes o emprendedores, permitiendo contrastar la estabilidad de ingresos frente a entornos de alta variabilidad financiera.

\---

## 4\. Hallazgos Financieros (Formato Estricto de Skill /interpret)

### Hallazgo 1: Comparativa de Ingresos por País (Ref: charts/01\_income\_by\_country.png)

Los encuestados muestran una disparidad notable en sus ingresos mensuales promedios según su ubicación geográfica en la región. Esta brecha subraya la necesidad de diseñar programas de educación financiera con canastas de presupuesto y metas de ahorro adaptadas al costo de vida local de cada nación. Por lo tanto, la plataforma debe segmentar sus módulos formativos automáticamente según el país de residencia del usuario.

\## 4. Hallazgos Financieros



\### Hallazgo 1: Comparativa de Ingresos por País

Los encuestados muestran una disparidad notable en sus ingresos mensuales promedios según su ubicación geográfica en la región. Esta brecha subraya la necesidad de diseñar programas de educación financiera con canastas de presupuesto y metas de ahorro adaptadas al costo de vida local de cada nación. Por lo tanto, la plataforma debe segmentar sus módulos formativos automáticamente según el país de residencia del usuario.



!\[Comparativa de Ingresos por País](charts/bar\_ingresos\_paises.png)



\### Hallazgo 2: Relación Edad vs. Tasa de Ahorro

El análisis de regresión lineal indica una correlación positiva moderada entre la edad de los profesionales y su capacidad de acumulación de ahorro mensual. Este comportamiento demuestra que los usuarios más jóvenes enfrentan mayores barreras de liquidez inicial o falta de hábitos de retención de capital. En consecuencia, se recomienda priorizar micro-módulos de ahorro automático dirigidos específicamente al segmento de menor edad de la muestra.



!\[Regresión Edad vs Ahorro](charts/scatter\_edad\_ahorro.png)



\### Hallazgo 3: Desglose General de Gastos Regionales

La estructura de gastos promedio regional evidencia que la vivienda y la alimentación representan los mayores drenajes de capital de los encuestados, superando por amplio margen a educación y salud. Esta fuerte concentración limita de forma severa el margen de maniobra de los jóvenes profesionales para afrontar imprevistos económicos. Por ello, el programa educativo debe incorporar simuladores avanzados de optimización de gastos fijos y negociación de contratos de arrendamiento.



!\[Distribución de Gastos Regionales](charts/pie\_gastos\_regionales.png)



\### Hallazgo 4: Impacto de Tarjetas de Crédito y Deuda

Los usuarios que poseen tarjetas de crédito activas reportan niveles de deuda total promedio significativamente más elevados en comparación con aquellos que no operan con dinero plástico. Este patrón revela que el acceso al crédito desregulado actúa como un catalizador del sobreendeudamiento debido a una baja comprensión de las tasas de interés compuestas. Por consiguiente, se debe establecer un taller obligatorio de salud crediticia antes de otorgar insignias de progreso en la plataforma.



!\[Impacto de Tarjetas de Crédito](charts/box\_deuda\_tarjetas.png)



\### Hallazgo 5: Uso de IA vs. Satisfacción Financiera

Existe una correlación positiva medible entre el número de horas semanales dedicadas a herramientas de Inteligencia Artificial y el índice de satisfacción financiera declarado. Este fenómeno sugiere que la adopción tecnológica optimiza la productividad laboral de los jóvenes, permitiéndoles acceder a mejores ingresos o gestionar sus finanzas con mayor eficiencia. En consecuencia, el programa debe integrar tutoriales prácticos sobre el uso de agentes de IA para finanzas personales.



!\[Uso de IA vs Satisfacción](charts/correlation\_ia\_satisfaccion.png)



\### Hallazgo 6: Análisis de Carga de Vivienda Relativa

La carga financiera destinada a la vivienda supera el umbral crítico recomendado del 30% del ingreso mensual neto en ciertos países evaluados, mostrando un gradiente de estrés financiero asimétrico. Esta sobrecarga sofoca la resiliencia económica de los profesionales independientes, incrementando el riesgo de impago ante crisis de volatilidad laboral. Por lo tanto, es imperativo estructurar fondos de contingencia específicos equivalentes a tres meses de renta para los países del extremo rojo del gradiente.



!\[Carga de Vivienda por País](charts/heatmap\_carga\_vivienda.png)
**Fuente:** Análisis de distribución agrupado por variable 'pais' e 'ingreso\_mensual\_usd'.

### Hallazgo 2: Relación Edad vs. Tasa de Ahorro (Ref: charts/02\_age\_vs\_savings.png)

El análisis de regresión lineal indica una correlación positiva moderada entre la edad de los profesionales y su capacidad de acumulación de ahorro mensual. Este comportamiento demuestra que los usuarios más jóvenes enfrentan mayores barreras de liquidez inicial o falta de hábitos de retención de capital. En consecuencia, se recomienda priorizar micro-módulos de ahorro automático dirigidos específicamente al segmento de menor edad de la muestra.
**Fuente:** Coeficiente de correlación de Pearson calculado entre 'edad' y 'ahorro\_mensual\_usd'.

### Hallazgo 3: Desglose General de Gastos Regionales (Ref: charts/03\_spending\_breakdown.png)

La estructura de gastos promedio regional evidencia que la vivienda y la alimentación representan los mayores drenajes de capital de los encuestados, superando por amplio margen a educación y salud. Esta fuerte concentración limita de forma severa el margen de maniobra de los jóvenes profesionales para afrontar imprevistos económicos. Por ello, el programa educativo debe incorporar simuladores avanzados de optimización de gastos fijos y negociación de contratos de arrendamiento.
**Fuente:** Media calculada de las variables 'gasto\_vivienda\_usd' y 'gasto\_alimentacion\_usd'.

### Hallazgo 4: Impacto de Tarjetas de Crédito y Deuda

Los usuarios que poseen tarjetas de crédito activas reportan niveles de deuda total promedio significativamente más elevados en comparación con aquellos que no operan con dinero plástico. Este patrón revela que el acceso al crédito desregulado actúa como un catalizador del sobreendeudamiento debido a una baja comprensión de las tasas de interés compuestas. Por consiguiente, se debe establecer un taller obligatorio de salud crediticia antes de otorgar insignias de progreso en la plataforma.
**Fuente:** Agrupación y promedio de 'deuda\_total\_usd' segmentado por 'tiene\_tarjeta\_credito'.

### Hallazgo 5: Uso de IA vs. Satisfacción Financiera (Ref: charts/04\_satisfaction\_by\_ia.png)

Existe una correlación positiva medible entre el número de horas semanales dedicadas a herramientas de Inteligencia Artificial y el índice de satisfacción financiera declarado. Este fenómeno sugiere que la adopción tecnológica optimiza la productividad laboral de los jóvenes, permitiéndoles acceder a mejores ingresos o gestionar sus finanzas con mayor eficiencia. En consecuencia, el programa debe integrar tutoriales prácticos sobre el uso de agentes de IA para finanzas personales.
**Fuente:** Coeficiente de Pearson entre 'horas\_herramientas\_ia\_semana' y 'satisfaccion\_financiera'.

### Hallazgo 6: Análisis de Carga de Vivienda Relativa (Ref: charts/05\_housing\_burden\_by\_country.png)

La carga financiera destinada a la vivienda supera el umbral crítico recomendado del 30% del ingreso mensual neto en ciertos países evaluados, mostrando un gradiente de estrés financiero asimétrico. Esta sobrecarga sofoca la resiliencia económica de los profesionales independientes, incrementando el riesgo de impago ante crisis de volatilidad laboral. Por lo tanto, es imperativo estructurar fondos de contingencia específicos equivalentes a tres meses de renta para los países del extremo rojo del gradiente.
**Fuente:** Ratio promedio de la relación entre 'gasto\_vivienda\_usd' e 'ingreso\_mensual\_usd' por país.

\---

## 5\. Recomendaciones

1. **Presupuestos Regionalizados:** Abandonar las plantillas únicas de presupuesto e implementar calculadoras dinámicas indexadas al salario mediano por país obtenido en la Fase 2.5.
2. **Priorización de Deuda:** Desplegar herramientas de consolidación de pasivos utilizando los métodos de "avalancha" o "bola de nieve" dirigidos a los usuarios de tarjetas de crédito con deudas críticas.
3. **Alfabetización Tecnológica:** Desarrollar un módulo de aprendizaje enfocado en herramientas digitales y automatización para ligar las habilidades tecnológicas directamente con la optimización de ingresos.

\---

## 6\. Conclusión

El despliegue del pipeline demostró que la transición de un análisis estático a una infraestructura automatizada asegura un monitoreo confiable y auditable del bienestar financiero en América Latina. Las marcadas diferencias en ingresos, cargas de vivienda y dinámicas de deuda halladas a lo largo de las 500 observaciones comprueban que el éxito de la estrategia educativa de Futuro Digital LatAm radica en la hiper-personalización contextualizada de sus contenidos. El sistema queda completamente preparado y robustecido para recibir y procesar de manera estandarizada las cargas de datos correspondientes a los próximos ciclos anuales de la organización.

