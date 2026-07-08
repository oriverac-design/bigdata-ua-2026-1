# S6 — Predicción de Churn en Movistar Perú

**Curso:** Big Data DD283 | Universidad Autónoma del Perú | 2026-1

## Resultados del modelo

| Modelo | Accuracy | F1-Churn | AUC-ROC |
|--------|----------|----------|---------|
| Regresión Logística | ~0.76 | ~0.48 | ~0.84 |
| Árbol de Decisión | ~0.91 | ~0.38 | ~0.80 |
| **Random Forest** | ~0.91 | ~0.52 | **~0.87** |

**Modelo seleccionado:** Random Forest (mayor AUC-ROC y F1-Churn equilibrado).

## Región con mayor sesgo geográfico

Las regiones con menor cantidad de datos en el dataset histórico (como **Iquitos** y **Tacna**) presentaron el F1-Score más bajo, lo que indica que el modelo predice peor el churn para clientes fuera de Lima.

## Estrategia de mitigación del sesgo

Se aplicó **ajuste de threshold de decisión** (de 0.50 a 0.35) para la región con peor F1. Esto incrementa el Recall — el modelo identifica más churners reales — a costa de una ligera reducción en Precision. En el contexto de retención de clientes, este trade-off es favorable: es mejor contactar a algunos clientes que no iban a irse (falso positivo) que perder clientes reales por no detectarlos (falso negativo).
