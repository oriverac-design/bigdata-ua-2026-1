---
**UNIVERSIDAD AUTÓNOMA DEL PERÚ**
**FACULTAD DE INGENIERÍA Y ARQUITECTURA**
**ESCUELA PROFESIONAL DE INGENIERÍA DE SISTEMAS COMPUTACIONALES**

---

# EVALUACIÓN PARCIAL — BIG DATA
## Código: DD283 | Ciclo VIII | Semestre 2026-1

---

| **CÓDIGO DEL ESTUDIANTE:** |2221896125 | **NÚMERO DE CLASE:** |6 - 202601 |
|---|---|---|---|
| **APELLIDOS Y NOMBRES:** |Tolentino Vargas, Jesus Antonio | **FECHA ENTREGA:** | 25/06/2026|
| **DOCENTE:** | **Mg. Rubén Quispe Llacctarimay** | **Modalidad:** | **Implementación + Video** |

---
REPOSITORIO
https://github.com/J3susTo/EXAMEN_PARCIAL_BIG_DATA_YAPE

VIDEO:
https://www.loom.com/share/114d199177b442a9a3e2b9e9c60c8d59

ARQUITECTURA:
https://drive.google.com/file/d/1QdAvU9IIQ2AxsCpqrxyEtEmcuJXMU5v8/view?usp=sharing


## INSTRUCCIONES GENERALES

| Ítem | Detalle |
|------|---------|
| **Duración** | 48 horas desde que el docente comparte este documento |
| **Modalidad** | Individual — implementación real en software + video de sustentación |
| **IA permitida** | **Sí** — puedes usar ChatGPT, Claude, Gemini, GitHub Copilot para asistirte en el código. Sin embargo, debes **entender, modificar y ejecutar** lo que el sistema genere. El video evidenciará tu comprensión. |
| **Entregable** | Enlace de repositorio GitHub (PR a la rama `semana_04`) + enlace de video |
| **Herramientas obligatorias** | Databricks Community Edition · MongoDB Atlas M0 · Docker Desktop |

---

> **Sobre el uso de IA:** Usar IA para generar código es válido y profesional. Lo que se evalúa es que:
> (a) el código funcione en las herramientas indicadas con **output real visible**,
> (b) puedas **explicar verbalmente** en el video cada decisión técnica, y
> (c) hayas **adaptado el código** al caso específico de este examen, no copiado una respuesta genérica.

---

## CASO BASE: YAPE — Sistema de Pagos Digitales

**Yape** (BCP) es la fintech más grande de Perú:

| Indicador | Dato 2025 |
|-----------|-----------|
| Usuarios activos | 15 millones |
| Transacciones diarias | 3.2 millones |
| Comerciantes afiliados | 1.3 millones |
| TPS en hora pico | 450 transacciones/segundo |
| Historial acumulado | ~18 TB/año |
| Tipos de comercio | Bodega, restaurante, farmacia, taxi, empresa, ONG |

**Problema:** El sistema Oracle actual demora 45 segundos en cargar el historial de un usuario. El equipo de Data Engineering necesita rediseñar la arquitectura con Big Data tools. Tú eres parte de ese equipo.

---

## PARTE A — DISEÑO Y ARQUITECTURA (4 puntos)
### *Puedes usar IA generativa en esta sección — cita qué herramienta usaste*

---

### PREGUNTA 1 — Arquitectura Big Data de Yape (4 puntos)

**1.1 (2 pts) — Tabla de arquitectura:**

Diseña la arquitectura completa de datos para Yape. Para cada componente del sistema, elige la tecnología adecuada y justifica. Puedes usar IA para explorar opciones, pero la justificación debe ser tuya.

| Componente del sistema | Tecnología elegida | Tipo BD/Herramienta | Por qué esta tecnología para Yape |
|---|---|---|---|
| Core de pagos (3.2M transacciones/día, no puede perder dinero) | CockroachDB | NewSQL distribuida | Permite transacciones ACID y consistencia fuerte, necesarias para débito y crédito de saldos. Además, escala horizontalmente mejor que una base relacional centralizada cuando crece el número de usuarios. |
| Sesiones de login activo (15M usuarios, expira en 30 min) | Redis Cluster | Base de datos en memoria / Key-Value | Las sesiones son datos temporales y de acceso muy rápido. Redis permite TTL de 30 minutos, baja latencia y escalabilidad para millones de usuarios activos. |
| Perfil del comerciante (bodega, restaurante, taxi - atributos distintos) | MongoDB Atlas | Base documental NoSQL | Cada tipo de comercio tiene atributos diferentes, como carta, vehículo, categorías o código DIGEMID. MongoDB permite guardar documentos flexibles sin crear muchas columnas nulas como en SQL. |
| Historial de transacciones para análisis (18 TB/año) | Databricks + Delta Lake / Parquet | Lakehouse / Big Data Analytics | El historial masivo se usa para análisis, reportes y dashboards, no para pagos en tiempo real. Databricks con Spark permite procesar grandes volúmenes mediante arquitectura Bronze, Silver y Gold. |
| Red de detección de fraude (ciclo A->B->C->A en < 5 min) | Neo4j | Base de datos de grafos | El fraude puede detectarse analizando relaciones entre usuarios y ciclos de transferencias. Una base de grafos identifica patrones de conexión mucho más rápido que consultas relacionales complejas. |
| Dashboard ejecutivo (top 10 distritos, actualización diaria) | Power BI conectado a Gold tables | BI / Dashboard ejecutivo | Los ejecutivos necesitan indicadores agregados como distritos, volumen y comisiones. Power BI permite visualizar métricas diarias a partir de datos Gold ya procesados. |

---

**1.2 (1 pt) — Teorema CAP:**

Para los siguientes 2 componentes de Yape, indica la combinación CAP correcta (CP, AP o CA) y explica qué propiedad sacrifica y por qué ese sacrificio es aceptable o inaceptable:

| Componente | Combinación CAP | Propiedad sacrificada | ¿Por qué ese sacrificio es correcto o incorrecto para este caso? |
|------------|-----------------|-----------------------|------------------------------------------------------------------|
| Core de pagos (débito/crédito de saldos) | CP | Disponibilidad | En pagos es más importante no perder dinero ni duplicar saldos. Si ocurre una partición de red, es aceptable rechazar temporalmente operaciones antes que confirmar pagos inconsistentes. |
| Historial "mis últimas 50 transacciones" | AP | Consistencia fuerte inmediata | El historial puede tolerar unos segundos de retraso. Es preferible mostrar rápido la lista al usuario aunque una transacción reciente tarde poco en aparecer, porque no afecta directamente el saldo contable. |

---

**1.3 (1 pt) — NewSQL:**

El equipo de Yape evalúa migrar el core de pagos a **CockroachDB** (NewSQL). Responde:

a) ¿Qué limitación de Oracle resuelve CockroachDB al escalar de 15M a 50M usuarios?

CockroachDB resuelve la limitación de escalamiento horizontal. En una arquitectura Oracle tradicional, el crecimiento suele depender de escalar verticalmente servidores más grandes o de configuraciones complejas. CockroachDB distribuye datos y carga entre nodos, permitiendo crecer agregando servidores sin perder transacciones ACID.

b) ¿Por qué MongoDB NO puede reemplazar a Oracle para el procesamiento de pagos aunque también escala horizontalmente?

MongoDB es adecuado para documentos flexibles, perfiles y catálogos, pero el core de pagos necesita transacciones financieras con consistencia fuerte, integridad, aislamiento y control estricto del débito/crédito. Aunque MongoDB soporta transacciones, no es la opción principal para un ledger financiero crítico donde no se puede permitir doble gasto, pérdida de saldo o inconsistencias entre cuentas.

c) ¿Qué mecanismo técnico usa CockroachDB para mantener ACID en múltiples nodos distribuidos? (1 término técnico es suficiente)
Raft consensus.
---

## PARTE B — DATABRICKS COMMUNITY EDITION (6 puntos)
### *Implementación obligatoria — evidencia en video y screenshot de outputs*

---

### PREGUNTA 2 — Pipeline de Transacciones Yape en Databricks (6 puntos)

**Contexto:** El equipo de Data Engineering de Yape necesita un pipeline que procese el historial de transacciones diarias. Debes implementarlo en **Databricks Community Edition** usando la arquitectura medallion (Bronze → Silver → Gold).

**Acceso:** [community.cloud.databricks.com](https://community.cloud.databricks.com) | Gratis | Sin tarjeta de crédito

---

**CELDA 1 — Generación del dataset (ya escrita, ejecutar tal cual):**

```python
# ============================================================
# CELDA 1: Dataset sintético — 2,000 transacciones Yape
# ============================================================
import numpy as np
import pandas as pd
from pyspark.sql import functions as F
from pyspark.sql.types import *
np.random.seed(42)

n = 2000
distritos = ["Miraflores", "San Isidro", "SJL", "Comas", "Villa El Salvador",
             "Los Olivos", "Surco", "Ate", "Callao", "Independencia"]
tipos     = ["persona_a_persona", "persona_a_comercio", "retiro_bcp", "recarga"]
estados   = ["completada", "completada", "completada", "rechazada", "pendiente"]

data = {
    "id_transaccion": [f"YP{i:07d}" for i in range(1, n+1)],
    "fecha":          pd.date_range("2025-01-01", periods=n, freq="1h").strftime("%Y-%m-%d").tolist(),
    "hora":           [f"{h:02d}:{m:02d}" for h, m in zip(np.random.randint(0,24,n), np.random.randint(0,60,n))],
    "monto_soles":    np.round(np.random.exponential(45, n), 2).tolist(),
    "tipo":           np.random.choice(tipos, n).tolist(),
    "distrito_origen":np.random.choice(distritos, n).tolist(),
    "estado":         np.random.choice(estados, n, p=[0.75, 0.1, 0.05, 0.07, 0.03]).tolist(),
    "id_usuario":     [f"USR{np.random.randint(1000,9999)}" for _ in range(n)],
    "es_comercio":    np.random.choice([True, False], n, p=[0.4, 0.6]).tolist()
}

df_pandas = pd.DataFrame(data)
df_bronze = spark.createDataFrame(df_pandas)
df_bronze.write.mode("overwrite").parquet("/FileStore/yape/bronze/transacciones")

print(f"✅ Bronze layer: {df_bronze.count()} transacciones guardadas")
df_bronze.show(5)
```
RESPUESTA:
✅ **Bronze Layer:** 2000 transacciones guardadas.

| id_transaccion | fecha | hora | monto_soles | tipo | distrito_origen | estado | id_usuario | es_comercio |
|---------------|--------|------|------------:|---------------------|----------------|------------|------------|:-----------:|
| YP0000001 | 2025-01-01 | 06:25 | 35.47 | persona_a_persona | Surco | completada | USR9055 | false |
| YP0000002 | 2025-01-01 | 19:07 | 4.16 | persona_a_comercio | Surco | completada | USR4216 | true |
| YP0000003 | 2025-01-01 | 14:35 | 42.01 | retiro_bcp | San Isidro | completada | USR6688 | false |
| YP0000004 | 2025-01-01 | 10:47 | 7.40 | retiro_bcp | Los Olivos | completada | USR5364 | false |
| YP0000005 | 2025-01-01 | 07:29 | 1.41 | recarga | San Isidro | completada | USR7042 | false |

> **Nota:** Solo se muestran las primeras 5 filas de un total de **2000 transacciones** almacenadas en la capa Bronze.
---

**CELDA 2 — Silver layer: limpiar y enriquecer (completar los `___`):**

```python
# ============================================================
# CELDA 2: Silver — limpiar y transformar
# COMPLETA los ___ según las instrucciones en los comentarios
# ============================================================
df_bronze = spark.read.parquet("/FileStore/yape/bronze/transacciones")

df_silver = df_bronze \
    .filter(df_bronze.estado == ___) \
    .filter(df_bronze.monto_soles > ___) \
    .withColumn("categoria_monto",
        F.when(F.col("monto_soles") < 20, "micro")
         .when(F.col("monto_soles") < 100, "medio")
         .otherwise(___)) \
    .withColumn("es_hora_pico",
        F.when(F.col("hora").between("12:00", "14:00"), True)
         .when(F.col("hora").between("18:00", ___), True)
         .otherwise(False)) \
    .withColumn("comision_yape",
        F.when(F.col("tipo") == "persona_a_comercio",
               F.round(F.col("monto_soles") * ___, 2))
         .otherwise(0.0))

df_silver.write.mode("overwrite").parquet("/FileStore/yape/silver/transacciones_limpias")

print(f"✅ Silver layer: {df_silver.count()} transacciones válidas")
print(f"   Eliminadas: {df_bronze.count() - df_silver.count()} (rechazadas/pendientes/monto cero)")
df_silver.groupBy("categoria_monto").count().show()
```

*Pistas para los `___`:*
- *`estado ==` → solo transacciones "completadas"*
- *`monto_soles >` → mayor a 0*
- *`otherwise` en categoría → "alto" (más de S/100)*
- *`between` hora tarde → "22:00"*
- *`comision_yape` → Yape cobra 1.5% a comercios: `0.015`*

RESPUESTA:
✅ **Silver Layer:** 1802 transacciones válidas.

- **Transacciones eliminadas:** 198 (rechazadas, pendientes o con monto igual a cero).

| Categoría de monto | Cantidad |
|--------------------|---------:|
| Alto | 202 |
| Micro | 634 |
| Medio | 966 |

> **Resumen:** A partir de las 2000 transacciones de la capa Bronze, se filtraron los registros inválidos (rechazados, pendientes o con monto cero), obteniendo **1802 transacciones válidas** para su análisis en la capa Silver.
---

**CELDA 3 — Gold layer: métricas de negocio (completar los `___`):**

```python
# ============================================================
# CELDA 3: Gold — agregaciones para el dashboard ejecutivo
# COMPLETA los ___ 
# ============================================================
df_silver = spark.read.parquet("/FileStore/yape/silver/transacciones_limpias")
df_silver.createOrReplaceTempView("transacciones")

# Gold 1: Top 5 distritos por volumen de transacciones
gold_distritos = spark.sql("""
    SELECT 
        distrito_origen,
        COUNT(*)                          AS total_transacciones,
        ROUND(SUM(monto_soles), 2)        AS volumen_total_soles,
        ROUND(AVG(monto_soles), 2)        AS ticket_promedio,
        SUM(CASE WHEN es_comercio THEN ___ ELSE 0 END) AS transacciones_comercio
    FROM transacciones
    GROUP BY ___
    ORDER BY ___ DESC
    LIMIT 5
""")

# Gold 2: Ingresos Yape por hora del día (comisiones de comercios)
gold_comisiones = spark.sql("""
    SELECT
        SUBSTRING(hora, 1, 2)             AS hora_dia,
        COUNT(*)                          AS num_transacciones,
        ROUND(SUM(comision_yape), 2)      AS ingresos_yape_soles
    FROM transacciones
    WHERE ___
    GROUP BY SUBSTRING(hora, 1, 2)
    ORDER BY ingresos_yape_soles DESC
""")

gold_distritos.write.mode("overwrite").parquet("/FileStore/yape/gold/top_distritos")
gold_comisiones.write.mode("overwrite").parquet("/FileStore/yape/gold/ingresos_por_hora")

print("📊 TOP 5 DISTRITOS POR VOLUMEN YAPE:")
gold_distritos.show()

print("💰 INGRESOS YAPE POR HORA (comisión comercios):")
gold_comisiones.show(5)
```

*Pistas para los `___`:*
- *`SUM(CASE WHEN es_comercio THEN ___ ELSE 0 END)` → contar con `1`*
- *`GROUP BY ___` → el campo de distrito*
- *`ORDER BY ___ DESC` → el campo de total de transacciones*
- *`WHERE ___` → solo donde la comisión es mayor a 0*


RESPUESTA:
## 📊 Gold Layer

### 📍 Resumen por distrito

| Distrito | Total transacciones | Volumen total (S/.) | Ticket promedio (S/.) | Transacciones a comercios |
|-----------|--------------------:|--------------------:|----------------------:|--------------------------:|
| Independencia | 204 | 8,968.04 | 43.96 | 75 |
| San Isidro | 197 | 8,194.34 | 41.60 | 71 |
| Los Olivos | 190 | 8,505.19 | 44.76 | 79 |
| Callao | 186 | 8,929.61 | 48.01 | 77 |
| Miraflores | 179 | 8,295.37 | 46.34 | 65 |

> **Nota:** Se muestran únicamente los **5 distritos principales** obtenidos del procesamiento de la capa Gold.

---

### 💰 Ingresos de Yape por hora (comisiones de comercios)

| Hora | Nº de transacciones | Ingresos Yape (S/.) |
|-----:|--------------------:|--------------------:|
| 01 | 30 | 21.56 |
| 04 | 17 | 20.75 |
| 03 | 24 | 19.47 |
| 22 | 23 | 18.65 |
| 11 | 25 | 16.47 |

> **Nota:** Se muestran las **5 primeras horas** con los ingresos generados por las comisiones cobradas en transacciones realizadas hacia comercios.
---

**CELDA 4 — Visualización (ya escrita, ejecutar tal cual):**

```python
# ============================================================
# CELDA 4: Visualización — gráfico de barras con matplotlib
# ============================================================
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

gold_distritos = spark.read.parquet("/FileStore/yape/gold/top_distritos").toPandas()
gold_comisiones = spark.read.parquet("/FileStore/yape/gold/ingresos_por_hora").toPandas()

fig, axes = plt.subplots(1, 2, figsize=(14, 5))
fig.suptitle("Dashboard Ejecutivo YAPE — Análisis de Transacciones", fontsize=14, fontweight='bold')

# Gráfico 1: Top 5 distritos
axes[0].barh(gold_distritos["distrito_origen"], gold_distritos["volumen_total_soles"],
             color=["#c41230","#e63950","#f47a8a","#f9b4bc","#fde8ea"])
axes[0].set_xlabel("Volumen total (S/)")
axes[0].set_title("Top 5 Distritos — Volumen de Pagos")
axes[0].xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"S/{x:,.0f}"))

# Gráfico 2: Ingresos Yape por hora
gold_comisiones_sorted = gold_comisiones.sort_values("hora_dia")
axes[1].plot(gold_comisiones_sorted["hora_dia"], gold_comisiones_sorted["ingresos_yape_soles"],
             marker='o', color='#c41230', linewidth=2)
axes[1].fill_between(gold_comisiones_sorted["hora_dia"], gold_comisiones_sorted["ingresos_yape_soles"],
                     alpha=0.15, color='#c41230')
axes[1].set_xlabel("Hora del día")
axes[1].set_ylabel("Comisión recaudada (S/)")
axes[1].set_title("Ingresos Yape por Hora")
axes[1].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.savefig("/dbfs/FileStore/yape/gold/dashboard_yape.png", dpi=150, bbox_inches='tight')
plt.show()

print("✅ Dashboard guardado en /FileStore/yape/gold/dashboard_yape.png")
```

---

**Entregable Parte B:**
- Screenshot del notebook completo con las 4 celdas ejecutadas (outputs visibles)
- En el video (P5): explicar qué hace la arquitectura Medallion y mostrar el dashboard generado

---

## PARTE C — MONGODB ATLAS (5 puntos)
### *Implementación obligatoria en Atlas M0 — evidencia en screenshot y video*
RESPUESTA: Las imagenes estan en el repositorio mio el cual usrted esta como colaborador.
---

### PREGUNTA 3 — Base de Datos NoSQL de Comerciantes Yape en Atlas (5 puntos)

**Acceso:** [mongodb.com/atlas](https://mongodb.com/atlas) → Create free account → M0 Free Tier (AWS São Paulo)

---

**PASO 1 — Conectar a Atlas desde Google Colab o tu local (ejecutar primero):**

```python
# ============================================================
# INSTALACIÓN (en Google Colab: ejecutar con !)
# ============================================================
# !pip install pymongo dnspython -q

from pymongo import MongoClient
import json

# REEMPLAZA con tu connection string de Atlas:
# Atlas → Connect → Drivers → Python → copia el string
CONNECTION_STRING = "mongodb+srv://<usuario>:<password>@<cluster>.mongodb.net/"

client = MongoClient(CONNECTION_STRING)
db = client["yape_db"]
comerciantes = db["comerciantes"]
print("✅ Conectado a MongoDB Atlas")
print(f"   DB: {db.name} | Colección: {comerciantes.name}")
```

---

**PASO 2 — Insertar 5 comerciantes con esquemas distintos (3.1 — 2 pts):**

Inserta los siguientes 5 documentos. Observa que **cada uno tiene campos únicos** — esto es imposible en SQL sin columnas NULL masivas.

```python
# ============================================================
# INSERTAR 5 COMERCIANTES CON ESTRUCTURA FLEXIBLE
# ============================================================

lista_comerciantes = [
    {
        "ruc": "10456789012",
        "nombre_comercio": "Bodega La Esquina de Don Mario",
        "tipo": "bodega",
        "propietario": "Mario Quispe Condori",
        "distrito": "San Juan de Lurigancho",
        "departamento": "Lima",
        "calificacion": 4.2,
        "yape_activo": True,
        "monto_mensual_soles": 4500.00,
        "categorias": ["abarrotes", "bebidas", "snacks"],   # Array
        "horario": {"apertura": "06:00", "cierre": "22:00"},# Objeto anidado
        "acepta_delivery": False
        # NO tiene: carta, capacidad_mesas, num_empleados
    },
    {
        "ruc": "20512345678",
        "nombre_comercio": "Cevichería El Muelle SAC",
        "tipo": "restaurante",
        "representante_legal": "Ana Flores Rojas",
        "distrito": "Miraflores",
        "departamento": "Lima",
        "calificacion": 4.8,
        "yape_activo": True,
        "monto_mensual_soles": 28000.00,
        "carta": [                                           # Array de objetos
            {"plato": "Ceviche clásico", "precio": 28.00},
            {"plato": "Leche de tigre",  "precio": 18.00},
            {"plato": "Tiradito",        "precio": 32.00}
        ],
        "capacidad_mesas": 45,
        "num_empleados": 12,
        "horario": {"apertura": "12:00", "cierre": "17:00"},
        "acepta_delivery": True,
        "plataformas_delivery": ["Rappi", "PedidosYa"]
        # NO tiene: categorias, acepta_tarjeta_fisica
    },
    {
        "ruc": "10789012345",
        "nombre_comercio": "Farmacia San Pablo Express",
        "tipo": "farmacia",
        "propietario": "Carlos Mendoza Ríos",
        "distrito": "Los Olivos",
        "departamento": "Lima",
        "calificacion": 4.5,
        "yape_activo": True,
        "monto_mensual_soles": 12000.00,
        "productos_destacados": ["paracetamol", "ibuprofeno", "vitaminas"],
        "horario": {"apertura": "07:00", "cierre": "23:00"},
        "venta_con_receta": True,
        "codigo_digemid": "F-2023-00456",  # Campo único de farmacias
        "acepta_delivery": True
    },
    {
        "ruc": "10234567891",
        "nombre_comercio": "Taxi Express — Luis Tapia",
        "tipo": "taxi",
        "propietario": "Luis Tapia Salcedo",
        "distrito": "Callao",
        "departamento": "Lima",
        "calificacion": 4.0,
        "yape_activo": True,
        "monto_mensual_soles": 3200.00,
        "vehiculo": {                        # Objeto único de taxis
            "placa": "ABC-123",
            "modelo": "Toyota Yaris 2022",
            "capacidad": 4
        },
        "zonas_cobertura": ["Callao", "Bellavista", "La Perla", "Miraflores"],
        "acepta_delivery": False
    },
    {
        "ruc": "20987654321",
        "nombre_comercio": "Distribuidora Norte SAC",
        "tipo": "empresa",
        "representante_legal": "Patricia Luna Torres",
        "distrito": "Independencia",
        "departamento": "Lima",
        "calificacion": 3.9,
        "yape_activo": True,
        "monto_mensual_soles": 85000.00,
        "num_empleados": 45,
        "sectores": ["abarrotes", "limpieza", "bebidas"],
        "clientes_mayoristas": 230,
        "horario": {"apertura": "08:00", "cierre": "18:00"},
        "acepta_delivery": True,
        "zonas_despacho": ["Lima Norte", "Lima Centro"]
    }
]

resultado = comerciantes.insert_many(lista_comerciantes)
print(f"✅ {len(resultado.inserted_ids)} comerciantes insertados en Atlas")
for i, id_ in enumerate(resultado.inserted_ids):
    print(f"   {lista_comerciantes[i]['tipo'].upper()}: {id_}")
```

---

**PASO 3 — Queries con filtros (3.2 — 1.5 pts):**

```python
# ============================================================
# CONSULTAS CON OPERADORES MONGODB
# ============================================================

print("="*55)
print("CONSULTA 1: Comerciantes premium (calificación > 4.3 y activos)")
premium = list(comerciantes.find(
    {"calificacion": {"$gt": 4.3}, "yape_activo": True},
    {"nombre_comercio": 1, "tipo": 1, "calificacion": 1, "_id": 0}
).sort("calificacion", -1))
for c in premium:
    print(f"  ★ {c['nombre_comercio']} ({c['tipo']}) — {c['calificacion']}")

print()
print("CONSULTA 2: Comercios con delivery en Lima que facturan > S/10,000/mes")
alto_valor = list(comerciantes.find(
    {
        "acepta_delivery": True,
        "departamento": "Lima",
        "monto_mensual_soles": {"$gt": 10000}
    },
    {"nombre_comercio": 1, "monto_mensual_soles": 1, "distrito": 1, "_id": 0}
))
for c in alto_valor:
    print(f"  → {c['nombre_comercio']} ({c['distrito']}): S/{c['monto_mensual_soles']:,.0f}/mes")

print()
print("CONSULTA 3: Bodegas O farmacias (operador $in)")
bodegas_farmacias = list(comerciantes.find(
    {"tipo": {"$in": ["bodega", "farmacia"]}},
    {"nombre_comercio": 1, "tipo": 1, "_id": 0}
))
for c in bodegas_farmacias:
    print(f"  → [{c['tipo']}] {c['nombre_comercio']}")
```

---

**PASO 4 — Aggregation Pipeline (3.3 — 1.5 pts):**

```python
# ============================================================
# ▶ TU TURNO: Completa el pipeline de facturación por tipo
# Objetivo: reporte para el equipo comercial de Yape
# ============================================================

pipeline_reporte = [
    # Paso 1: Solo comerciantes activos en Lima
    {"$match": {"yape_activo": ___, "departamento": ___}},
    
    # Paso 2: Agrupar por tipo de comercio
    {"$group": {
        "_id": "$tipo",
        "total_comercios":     {"$sum": ___},
        "facturacion_total":   {"$sum": ___},
        "calificacion_prom":   {"$avg": ___},
        "con_delivery":        {"$sum": {"$cond": ["$acepta_delivery", 1, 0]}}
    }},
    
    # Paso 3: Ordenar por facturación total descendente
    {"$sort": {"facturacion_total": ___}},
    
    # Paso 4: Formatear la salida
    {"$project": {
        "tipo_comercio":    "$_id",
        "total_comercios":  1,
        "facturacion_total": 1,
        "calificacion_prom": {"$round": ["$calificacion_prom", 1]},
        "con_delivery":     1,
        "_id": 0
    }}
]

print("📊 REPORTE COMERCIAL YAPE — FACTURACIÓN POR TIPO:")
print(f"{'TIPO':<20} {'COMERCIOS':>9} {'FACTURACIÓN/MES':>16} {'RATING':>7} {'C/DELIVERY':>11}")
print("-" * 67)
for r in comerciantes.aggregate(pipeline_reporte):
    print(f"{r['tipo_comercio']:<20} {r['total_comercios']:>9} "
          f"S/{r['facturacion_total']:>13,.0f} {r['calificacion_prom']:>7} "
          f"{r['con_delivery']:>11}")
```

*Pistas para los `___`:*
- *`yape_activo: ___` → `True`*
- *`departamento: ___` → `"Lima"`*
- *`$sum: ___` para contar → `1`*
- *`$sum: ___` para sumar → `"$monto_mensual_soles"`*
- *`$avg: ___` → `"$calificacion"`*
- *`$sort: ___` → `-1` (descendente)*

---

**Entregable Parte C:**
- Screenshot de Atlas UI → Browse Collections mostrando los documentos insertados
- Screenshot del output del pipeline ejecutado en Colab/local
- En el video: mostrar Atlas Dashboard + explicar por qué el esquema flexible de MongoDB es adecuado vs. SQL para este caso
RESPUESTA: la aplicacion esta en el git repositorio co le comparti arriba esta el enlace y esta usted como colaborador.
---

## PARTE D — DOCKER DESKTOP (3 puntos)
### *MongoDB local en contenedor — evidencia en video*

---

### PREGUNTA 4 — Contenerizar MongoDB con Docker Desktop (3 puntos)

**Contexto:** El equipo de desarrollo de Yape necesita un entorno local de pruebas idéntico al de Atlas. Docker permite crear ese entorno en segundos sin instalar MongoDB directamente.

**Prerrequisito:** Docker Desktop instalado y corriendo (ícono de ballena en la barra de tareas).

---

**PASO 1 — Levantar MongoDB en contenedor (4.1 — 1 pt):**

Ejecuta estos comandos en tu terminal (CMD, PowerShell o Terminal de Mac):

```bash
# 1. Descargar la imagen oficial de MongoDB
docker pull mongo:7.0

# 2. Levantar el contenedor con MongoDB
docker run -d \
  --name yape-mongo-local \
  -p 27017:27017 \
  -e MONGO_INITDB_ROOT_USERNAME=admin \
  -e MONGO_INITDB_ROOT_PASSWORD=yape2026 \
  mongo:7.0

# 3. Verificar que el contenedor está corriendo
docker ps

# Salida esperada:
# CONTAINER ID   IMAGE      COMMAND                  STATUS        PORTS                      NAMES
# abc123def456   mongo:7.0  "docker-entrypoint.s…"  Up 5 seconds  0.0.0.0:27017->27017/tcp   yape-mongo-local
```

**Verifica en Docker Desktop:** La pestaña "Containers" debe mostrar `yape-mongo-local` en estado **Running** (ícono verde).

---

**PASO 2 — Conectar Python al MongoDB local (4.2 — 1 pt):**

```python
# ============================================================
# CONECTAR A MONGODB EN DOCKER (localhost, no Atlas)
# ============================================================
from pymongo import MongoClient

# Conexión al contenedor Docker (diferente al Atlas)
client_docker = MongoClient(
    "mongodb://admin:yape2026@localhost:27017/",
    authSource="admin"
)

db_local = client_docker["yape_local"]
col_local = db_local["comerciantes_test"]

# Insertar el mismo comerciante del Paso 2 de Atlas
col_local.insert_one({
    "nombre_comercio": "Bodega Test Docker",
    "tipo": "bodega",
    "distrito": "Lima",
    "monto_mensual_soles": 1500.00,
    "yape_activo": True,
    "entorno": "docker_local"   # ← Campo que indica que es entorno local
})

# Verificar
doc = col_local.find_one({"nombre_comercio": "Bodega Test Docker"})
print("✅ Documento guardado en MongoDB Docker:")
print(f"   Nombre:   {doc['nombre_comercio']}")
print(f"   Entorno:  {doc['entorno']}")
print(f"   ID:       {doc['_id']}")

# Mostrar todos los documentos en la colección
print(f"\nTotal documentos en Docker: {col_local.count_documents({})}")
```

---

**PASO 3 — Diferencia entre Docker y Atlas (4.3 — 1 pt):**

Responde en el espacio de abajo (3-5 líneas):

```
a) ¿Cuándo usarías MongoDB en Docker en lugar de MongoDB Atlas para el equipo de Yape?
RESPUESTA: 
Usaría Docker para desarrollo local, pruebas rápidas, trabajo sin depender de internet y validación de código antes de enviarlo a un entorno cloud. Es útil cuando el equipo necesita un ambiente repetible sin instalar MongoDB directamente.

b) ¿Qué ventaja tiene Atlas M0 sobre el contenedor Docker para el contexto universitario?
RESPUESTA: 
En el contexto universitario, MongoDB Atlas M0 resulta más práctico porque permite acceder a la base de datos desde cualquier computadora con Internet, sin necesidad de instalar ni configurar un servidor local. Además, los datos permanecen disponibles en la nube y se pueden revisar fácilmente desde su interfaz web, lo que facilita las prácticas y las demostraciones. En cambio, con Docker es necesario tener Docker Desktop instalado y el contenedor en ejecución para poder acceder a la base de datos.

c) ¿Qué sucede con los datos del contenedor Docker si ejecutas `docker stop yape-mongo-local` y 
   luego `docker rm yape-mongo-local`? ¿Y con los datos de Atlas?
RESPUESTA: 
Con docker stop el contenedor se detiene pero conserva datos mientras exista el contenedor. Con docker rm se elimina el contenedor y, si no se configuró un volumen persistente, se pierden los datos. En Atlas los datos permanecen en la nube hasta que se elimine la base, colección o cluster.

```

**Comandos para detener y limpiar el contenedor al terminar:**

```bash
docker stop yape-mongo-local
docker rm yape-mongo-local
```

---

**Entregable Parte D:**
- Screenshot de Docker Desktop mostrando el contenedor `yape-mongo-local` en estado **Running**
- Screenshot del output de Python conectando al contenedor
- En el video: mostrar Docker Desktop → Containers → Logs del contenedor

---

## PARTE E — VIDEO DE SUSTENTACIÓN (2 puntos)

---

### PREGUNTA 5 — Demostración en Video (2 puntos)

**Duración:** 5 a 8 minutos
**Herramienta sugerida:** Loom (loom.com — gratuito), OBS Studio (gratuito), o grabador de pantalla de Windows/Mac.

**Estructura obligatoria del video:**

| Segmento | Tiempo | Qué mostrar |
|----------|--------|-------------|
| **1. Presentación** | 20 seg | Di tu nombre, código y tema del examen |
| **2. Arquitectura** | 1 min | Explica la tabla de P1.1 — justifica 2 decisiones tecnológicas con tus propias palabras |
| **3. Databricks** | 2 min | Muestra el notebook ejecutado, el dashboard generado, explica qué hace Bronze→Silver→Gold |
| **4. MongoDB Atlas** | 2 min | Abre Atlas UI → Browse Collections → muestra los 5 documentos → muestra el output del pipeline |
| **5. Docker Desktop** | 1 min | Muestra Docker Desktop con el contenedor corriendo → el output de Python conectando |
| **6. Uso de IA** | 30 seg | Menciona qué partes te ayudó IA a resolver y qué tuviste que modificar tú |

**Enlace del video:** `https://www.loom.com/share/114d199177b442a9a3e2b9e9c60c8d59`

---

## ENTREGABLES Y FORMA DE ENTREGA

### Estructura del PR en GitHub:

```
semana_04/Soluciones/TuNombre_TuCodigo/
│
├── P1_arquitectura.md          ← Tabla P1.1 + respuestas P1.2 y P1.3
│
├── P2_databricks_yape.ipynb    ← Notebook exportado desde Databricks (o .py)
│   o P2_databricks_yape.py
│
├── P3_mongodb_atlas.py         ← Código Python completo de las 4 partes de P3
│
├── P4_docker.py                ← Código Python del Paso 2 de Docker
│
├── screenshots/
│   ├── databricks_celda1.png   ← Output de cada celda ejecutada
│   ├── databricks_celda2.png
│   ├── databricks_celda3.png
│   ├── databricks_dashboard.png
│   ├── atlas_collections.png   ← Browse Collections en Atlas UI
│   ├── atlas_pipeline_output.png
│   └── docker_desktop.png      ← Contenedor en estado Running
│
└── README.md                   ← Enlace al video + descripción de lo implementado
```
RESPUESTA:

Yo cree una estructura mas comoda para mi .
semana_04/Soluciones/Jesus_Tolentino/
│
├── P1 Arquitectura
│      P1_arquitectura.md
│
├── P2 Databricks
│      P2_databricks_yape.ipynb
│
├── P3 MongoDB Atlas
│      config.py
│      comerciantes.py
│      consultas.py
│      pipeline.py
│      P3_mongodb_atlas.py
│      requirements.txt
│
├── P4_Docker
│      P4_docker.py
│      requirements.txt
│
├── screenshots
│      atlas_collections.png
│      atlas_pipeline_output.png
│      docker_desktop.png
│      databricks_celda1.png
│      databricks_celda2.png
│      databricks_celda3.png
│      databricks_dashboard.png
│      docker_desktop2.png
│      Driver_MongoDB.png
│      Prueba_de_autoria.png
│      conexion_mongoDB.png
│
└── README.md

**Rama del PR:** `semana04-solucion-TuNombre`
**Base:** `main`
**Descripción del PR:** Incluir el enlace al video en la descripción del PR.

---

## RÚBRICA DE CALIFICACIÓN

### RUBRICA — Evaluación Parcial Big Data DD283

| **DOCENTE** | Mg. Rubén Quispe Llacctarimay |
|-------------|-------------------------------|
| **Evaluación** | Parcial — Semanas 1 a 4 |
| **Herramientas** | Databricks Community · MongoDB Atlas M0 · Docker Desktop |
| **IA** | Permitida como asistente — se evalúa implementación y comprensión |

---

| ÍTEM | DESCRIPCIÓN | 100% del puntaje | 50% del puntaje | 0% |  PTS |
|------|-------------|-----------------|----------------|-----|------|
| **P1.1 — Arquitectura** | Tabla con 6 componentes, tecnología correcta y justificación | 6/6 correctos con justificación técnica específica del caso Yape | 3-5 correctos o justificaciones genéricas | < 3 correctos | **2** |
| **P1.2 — CAP Theorem** | 2 componentes con combinación correcta y explicación de sacrificio | Ambos correctos con explicación del sacrificio vinculada al caso | 1 correcto o explicación sin caso | Ambos incorrectos | **1** |
| **P1.3 — NewSQL** | 3 preguntas: limitación Oracle, por qué no MongoDB, mecanismo técnico | Raft/Paxos mencionado + limitación correcta + problema ACID de MongoDB | 2/3 correctos | 0-1 correctos | **1** |
| **P2 — Databricks: celdas 2 y 3** | Silver y Gold completados con `___` reemplazados correctamente | Output de ambas celdas visible con datos correctos en screenshot | Solo Silver correcta o Gold con errores menores | Sin output o celdas sin completar | **4** |
| **P2 — Databricks: dashboard** | Celda 4 ejecutada, gráfico generado y visible en screenshot | Gráfico con datos reales (no vacío) guardado en /FileStore | Gráfico incompleto (un solo panel) | Sin gráfico | **2** |
| **P3.1 — Atlas: inserción** | 5 documentos con estructura flexible visible en Atlas UI | 5 documentos insertados, screenshot de Atlas Browse Collections | 3-4 documentos o sin screenshot de Atlas | Sin inserción en Atlas real |  **2** |
| **P3.2 — Atlas: queries** | 3 consultas ejecutadas con output visible | Las 3 consultas con resultado correcto | 2/3 consultas correctas | Sin queries o resultados vacíos | **1.5** |
| **P3.3 — Atlas: pipeline** | Pipeline completado con los `___` reemplazados, tabla de facturación impresa | Output visible con columnas correctas y datos coherentes | Pipeline sin completar pero ejecutado con errores menores | Sin pipeline ejecutado | **1.5** |
| **P4.1 — Docker: contenedor** | `docker run` exitoso, Docker Desktop mostrando Running | Screenshot de Docker Desktop con contenedor verde | Screenshot sin estado Running claro | Sin evidencia de Docker | **1** |
| **P4.2 — Docker: Python** | Código ejecutado, documento insertado, output impreso | Output visible con nombre e ID del documento | Código correcto pero sin output | Sin conexión a Docker | **1** |
| **P4.3 — Docker: análisis** | 3 preguntas respondidas con argumentos técnicos (persistencia, casos de uso) | 2/3 con argumento técnico | Solo 1 con argumento | Sin respuesta o respuestas de 1 línea sin técnica | **1** |
| **P5 — Video** | Cubre los 6 segmentos, muestra todo funcionando, explica uso de IA | 5-6 segmentos cubiertos, demostraciones claras | 3-4 segmentos, demostraciones con cortes o sin explicación | < 3 segmentos o sin demostración real en software | **2** |
| | | | | **SUMA TOTAL** | **20** |

---

### Escala de calificación

| Puntaje | Nivel | Descripción |
|---------|-------|-------------|
| 18 – 20 | AD — Logro destacado | Implementación completa, explicación fluida, adaptaciones propias al código |
| 14 – 17 | A — Logro esperado | Implementación funcional en las 3 herramientas, comprensión demostrada en video |
| 11 – 13 | B — En proceso | Implementación parcial (2 de 3 herramientas), explicación con vacíos conceptuales |
| 0 – 10 | C — En inicio | No puede demostrar implementación o el video no corresponde al trabajo presentado |

---

### Criterio anti-copia para el video

El video es el principal mecanismo de verificación. Un estudiante que copió el código pero lo ejecutó en su máquina y puede explicarlo verbalmente **aprueba**. Un estudiante con código propio que no puede responder preguntas básicas sobre lo que implementó **puede ser evaluado con preguntas adicionales**.

*Si el video muestra capturas de pantalla de otra persona (distintas resoluciones, nombre de usuario diferente, fecha inconsistente), el examen será anulado.*

---

*Big Data DD283 | Universidad Autónoma del Perú | Evaluación Parcial | Semana 4 | 2026-1*
*Mg. Rubén Quispe Llacctarimay | Entrega: 48 horas | Puntaje: 20 pts*
