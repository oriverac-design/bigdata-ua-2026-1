# S3 — LABORATORIO EN CASA: MongoDB Atlas + Python
## Big Data DD283 | Universidad Autónoma del Perú | 2026-1
### Semana 3: Implementación NoSQL con MongoDB Atlas — Análisis de Empresas SUNAT

---

| Campo | Detalle |
|-------|---------|
| **Nombre del estudiante** | ______________________________________________ |
| **Código** | ______________________________________________ |
| **Fecha de entrega** | ______________________________________________ |
| **Duración estimada** | 2 horas |
| **Modalidad** | Individual (pareja con autorización) |
| **Entrega** | Screenshot del Atlas + Notebook (.ipynb) con resultados |

---

## OBJETIVO DEL LABORATORIO

Implementar una base de datos NoSQL en MongoDB Atlas con datos empresariales reales de SUNAT (simulados), usando Python (pymongo) para insertar, consultar y agregar datos. Comparar el enfoque NoSQL con el modelo relacional equivalente.

## COMPETENCIA QUE DESARROLLA

Implementa una base de datos NoSQL de manera eficiente con integridad, sin sesgar la estructura de los datos según el caso de negocio.

---

## SOFTWARE Y HERRAMIENTAS REQUERIDAS

| Herramienta | Versión | Link | Costo |
|-------------|---------|------|-------|
| **MongoDB Atlas** | M0 Free Tier | mongodb.com/atlas | Gratis permanente |
| **MongoDB Compass** | 1.40+ | mongodb.com/try/download/compass | Gratis |
| **Google Colab** | — | colab.research.google.com | Gratis |
| **Python** | 3.10+ | (preinstalado en Colab) | Gratis |
| **pymongo** | 4.6+ | pip install pymongo | Gratis |

### CONFIGURACIÓN INICIAL DE MONGODB ATLAS (15 min — hacer UNA vez)

**Paso 1 — Crear cuenta:**
```
1. Ir a: mongodb.com/atlas → "Try Free"
2. Registrarse con Google Account (lo más rápido)
3. Empresa: "Universidad Autónoma del Perú"
4. Goal: "Learn MongoDB"
```

**Paso 2 — Crear cluster M0 (gratuito):**
```
1. Clic "Create" (en la pantalla de "Deploy a cluster")
2. Tier: M0 (Free, Shared) — NO cambiar a M2/M5 (son de pago)
3. Cloud Provider: AWS | Region: South America (São Paulo)
4. Cluster Name: "BigDataUA-[TuApellido]"
5. Clic "Create Deployment"
```

**Paso 3 — Crear usuario de base de datos:**
```
En la pantalla "Security Quickstart":
1. Username: bigdata_user
2. Password: BigData2026!  (o genera uno automático y guárdalo)
3. Clic "Create User"
```

**Paso 4 — Configurar acceso de red:**
```
1. "Add My Current IP Address" (si estás en casa)
   O bien: "Allow Access from Anywhere" (IP: 0.0.0.0/0)
   para que Colab también pueda conectarse
2. Clic "Finish and Close"
```

**Paso 5 — Obtener connection string:**
```
1. En tu cluster → Clic "Connect"
2. "Drivers" → Python 3.12+
3. Copiar el string: 
   mongodb+srv://bigdata_user:<password>@bigdataua-apellido.xxxxx.mongodb.net/
4. Reemplazar <password> con tu contraseña
5. GUARDAR ESTE STRING — lo necesitas en el laboratorio
```

**Verificación de entorno listo:**
```python
# En Google Colab — ejecuta esto:
!pip install pymongo -q
from pymongo import MongoClient
client = MongoClient("TU_CONNECTION_STRING_AQUÍ")
print(client.list_database_names())
# Si ves: ['admin', 'local'] → ¡Conexión exitosa!
```

**Alternativa si no puedes acceder a Atlas:** Usar MongoDB en memoria con `mongomock`:
```python
!pip install mongomock pymongo -q
import mongomock
client = mongomock.MongoClient()
# Funciona igual que pymongo para el laboratorio (sin cloud)
```

---

## PARTE 1 — EXPLORACIÓN: Conectar y Explorar MongoDB (30 min)

### 1.1 — Conectar a Atlas y crear la base de datos

```python
# ============================================================
# CELDA 1: Instalar e importar pymongo
# ============================================================
!pip install pymongo dnspython -q

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import json
from datetime import datetime
import pprint

# REEMPLAZA CON TU CONNECTION STRING DE ATLAS:
CONNECTION_STRING = "mongodb+srv://bigdata_user:BigData2026!@bigdataua-tuapellido.xxxxx.mongodb.net/"

# Conectar
client = MongoClient(CONNECTION_STRING)

# Verificar conexión
try:
    client.admin.command('ping')
    print("✅ Conexión exitosa a MongoDB Atlas!")
    print(f"   Databases disponibles: {client.list_database_names()}")
except ConnectionFailure:
    print("❌ No se pudo conectar. Verifica:")
    print("   1. El connection string es correcto")
    print("   2. La IP está en la whitelist de Atlas")
    print("   3. El usuario y contraseña son correctos")

# Crear/acceder a la base de datos del laboratorio
db = client["bigdata_s3_sunat"]
print(f"\n📁 Base de datos: {db.name}")
```

---

### 1.2 — Insertar documentos y explorar el modelo

```python
# ============================================================
# CELDA 2: Crear colección y explorar el modelo de datos NoSQL
# ============================================================

# Seleccionar la colección (se crea automáticamente al insertar)
empresas = db["empresas"]

# Insertar UNA empresa con estructura rica (documento 1)
empresa_tech = {
    "ruc": "20123456789",
    "razon_social": "Tecnología Andina SAC",
    "tipo_empresa": "SOCIEDAD ANONIMA CERRADA",
    "departamento": "Lima",
    "distrito": "Miraflores",
    "sector": "Tecnología",
    "regimen_tributario": "Régimen General",
    "estado": "ACTIVO",
    "fecha_registro_sunat": datetime(2018, 3, 15),
    "num_empleados": 45,
    "facturacion_anual": {          # Objeto anidado (no existe en SQL tablas planas)
        "2022": 650000,
        "2023": 850000,
        "2024": 1200000
    },
    "productos_servicios": ["Software ERP", "Consultoría TI", "Soporte"],
    "certificaciones": ["ISO 9001", "CMMI Level 3"],
    "contacto": {
        "email": "contacto@tecandina.com",
        "telefono": "01-4567890",
        "web": "www.tecandina.com"
    },
    "exporta": False
}

resultado = empresas.insert_one(empresa_tech)
print(f"✅ Empresa insertada con ID: {resultado.inserted_id}")
print(f"   Tipo del ID: {type(resultado.inserted_id)}")
print()

# Insertar empresa con ESTRUCTURA DIFERENTE (aquí está la magia del NoSQL)
empresa_agricola = {
    "ruc": "20987654321",
    "razon_social": "Agroindustrias del Sur EIRL",
    "departamento": "Arequipa",
    "sector": "Agroindustria",
    "estado": "ACTIVO",
    "num_empleados": 120,
    "facturacion_anual": {"2023": 2800000, "2024": 3200000},
    # Campos específicos de agroindustria (no existen en empresa tech):
    "cultivos_principales": ["Páprika", "Cebolla amarilla", "Ajo"],
    "hectareas_certificadas": 450,
    "certificaciones_organicas": ["USDA Organic", "BIO Suisse"],
    "mercados_exportacion": ["Estados Unidos", "Países Bajos", "España"],
    "exporta": True,
    "volumen_exportacion_tn": 1200
    # NO TIENE: "productos_servicios", "contacto.web", "certificaciones" TI
    # ← En SQL, estas columnas existirían pero con NULL. En MongoDB: simplemente no están
}

resultado2 = empresas.insert_one(empresa_agricola)
print(f"✅ Empresa agroindustrial insertada con ID: {resultado2.inserted_id}")

# Recuperar y mostrar ambos documentos
print("\n📄 DOCUMENTOS EN LA COLECCIÓN:")
for emp in empresas.find():
    print(f"\n  RUC: {emp['ruc']} | {emp['razon_social']}")
    print(f"  Campos: {list(emp.keys())}")
    print(f"  Total campos: {len(emp.keys())}")
```

**Pregunta de reflexión 1.1:**
> ¿Cuántos campos tiene el documento de la empresa de tecnología vs. la empresa agroindustrial? ¿Qué pasaría en una base de datos SQL si la empresa agroindustrial no tiene `contacto.web` — cómo quedaría esa columna?
>
> Escribe tu respuesta como comentario en el notebook.

*La empresa de tecnologia tiene 16 campos y las empresa agroindustria tiene 14 campos*

*Si la empresa agroindustrial no tiene la información de contacto.web, una base de datos relacional (SQL) manejará la situación así: la columna permanecerá fija en la estructura de la tabla por obligación, y la celda de este registro se guardará con un valor NULL. Esto ocurre porque el modelo SQL exige un esquema estricto y uniforme para todas sus filas.*


---

### 1.3 — Insertar dataset masivo de empresas

```python
# ============================================================
# CELDA 3: Insertar 100 empresas para análisis
# ============================================================
import random

# Limpiar colección de inserciones previas de este dataset
empresas.delete_many({"ruc": {"$regex": "^SYNTHETIC"}})

departamentos = ["Lima", "Arequipa", "La Libertad", "Piura", "Cusco", 
                 "Junin", "Puno", "Ancash", "Loreto", "Cajamarca", "Moquegua"]
sectores = ["Tecnología", "Comercio", "Manufactura", "Construcción", 
            "Agroindustria", "Minería", "Servicios", "Transporte", "Salud", "Educación"]
regimenes = ["Régimen General", "MYPE Tributario", "NRUS", "Régimen Especial"]
estados = ["ACTIVO", "ACTIVO", "ACTIVO", "SUSPENDIDO", "BAJA"]  # 60% activos

dataset_empresas = []
for i in range(100):
    dep = random.choice(departamentos)
    sector = random.choice(sectores)
    empleados = random.randint(1, 500)
    
    empresa = {
        "ruc": f"SYNTHETIC{i:06d}",
        "razon_social": f"Empresa {sector} {dep} {i:03d} SAC",
        "departamento": dep,
        "sector": sector,
        "regimen_tributario": random.choice(regimenes),
        "estado": random.choice(estados),
        "num_empleados": empleados,
        "facturacion_anual": {
            "2022": random.randint(50000, 5000000),
            "2023": random.randint(50000, 5000000),
            "2024": random.randint(50000, 5000000)
        },
        "exporta": random.choice([True, False]),
        "fecha_registro": datetime(random.randint(2000, 2023), 
                                   random.randint(1, 12), 
                                   random.randint(1, 28))
    }
    dataset_empresas.append(empresa)

# Insert masivo (insert_many es mucho más eficiente que 100 inserts individuales)
resultado = empresas.insert_many(dataset_empresas)
print(f"✅ Insertadas {len(resultado.inserted_ids)} empresas")
print(f"   Total documentos en colección: {empresas.count_documents({})}")
```

**Pregunta de reflexión 1.2:**
> ¿Por qué `insert_many()` es más eficiente que llamar `insert_one()` 100 veces en un bucle? Pista: piensa en el overhead de red entre tu código y el servidor de MongoDB en São Paulo.

*Es que hacer 100 insert_one en un bucle es un dolor de cabeza por la distancia con el servidor de São Paulo. Como la latencia (el ping) de Perú allá es de unos 100ms, cada inserción individual tiene que viajar, registrarse y volver. Terminas perdiendo como 10 segundos solo esperando en la red! Con insert_many(), el código mete los 100 documentos en una sola "caja", hace un único viaje de ida y vuelta, y listo: se procesa todo en menos de un segundo*

---

## PARTE 2 — APLICACIÓN: Consultas y Aggregation Pipeline (60 min)

### 2.1 — Consultas básicas (equivalentes a SQL WHERE)

```python
# ============================================================
# CELDA 4: Consultas MongoDB vs. equivalente SQL
# ============================================================

print("=" * 60)
print("CONSULTAS MONGODB — con equivalente SQL comentado")
print("=" * 60)

# CONSULTA 1: Empresas activas de Lima
# SQL: SELECT * FROM empresas WHERE estado='ACTIVO' AND departamento='Lima'
query1 = empresas.find(
    {"estado": "ACTIVO", "departamento": "Lima"}
)
lista1 = list(query1)
print(f"\n1. Empresas activas en Lima: {len(lista1)}")

# CONSULTA 2: Empresas con más de 50 empleados
# SQL: SELECT razon_social, num_empleados FROM empresas WHERE num_empleados > 50
query2 = empresas.find(
    {"num_empleados": {"$gt": 50}},           # $gt = greater than
    {"razon_social": 1, "num_empleados": 1, "_id": 0}  # Proyección (SELECT columnas)
).sort("num_empleados", -1).limit(5)          # ORDER BY DESC LIMIT 5

print(f"\n2. Top 5 empresas por empleados (>50):")
for e in query2:
    print(f"   {e['razon_social']}: {e['num_empleados']} empleados")

# CONSULTA 3: Empresas exportadoras en sectores productivos
# SQL: SELECT * FROM empresas WHERE exporta=TRUE AND sector IN ('Agroindustria','Manufactura','Minería')
query3 = empresas.find({
    "exporta": True,
    "sector": {"$in": ["Agroindustria", "Manufactura", "Minería"]}  # $in = IN (...)
})
print(f"\n3. Empresas exportadoras en sectores productivos: {empresas.count_documents({'exporta': True, 'sector': {'$in': ['Agroindustria', 'Manufactura', 'Minería']}})}")

# CONSULTA 4: Empresas con facturación 2024 mayor a 1 millón (campo anidado)
# SQL: SELECT * FROM empresas e JOIN facturacion f ON e.id=f.empresa_id WHERE f.año=2024 AND f.monto > 1000000
# ← En SQL necesitas JOIN. En MongoDB accedes directo con notación punto:
query4 = empresas.find(
    {"facturacion_anual.2024": {"$gt": 1000000}},
    {"razon_social": 1, "facturacion_anual.2024": 1, "_id": 0}
)
print(f"\n4. Empresas con facturación 2024 > S/1M:")
for e in list(query4)[:5]:
    print(f"   {e['razon_social']}: S/{e['facturacion_anual']['2024']:,}")
```

---

### 2.2 — Aggregation Pipeline (equivalente a GROUP BY + funciones de agregación)

```python
# ============================================================
# CELDA 5: Aggregation Pipeline — el corazón analítico de MongoDB
# Equivalente al GROUP BY + SUM/AVG/COUNT de SQL
# ============================================================

print("\n" + "=" * 60)
print("AGGREGATION PIPELINE — Análisis de empresas por sector")
print("=" * 60)

# Pipeline 1: Empresas activas por sector con métricas
# SQL equivalente:
# SELECT sector, COUNT(*) as total, AVG(num_empleados) as prom_emp,
#        SUM(facturacion_anual_2024) as total_facturacion
# FROM empresas WHERE estado='ACTIVO'
# GROUP BY sector ORDER BY total DESC

pipeline_sector = [
    # Etapa 1: Filtrar solo empresas activas (como WHERE)
    {"$match": {"estado": "ACTIVO"}},
    
    # Etapa 2: Agrupar por sector y calcular métricas (como GROUP BY + funciones)
    {"$group": {
        "_id": "$sector",                                    # GROUP BY sector
        "total_empresas": {"$sum": 1},                      # COUNT(*)
        "empleados_promedio": {"$avg": "$num_empleados"},   # AVG(num_empleados)
        "facturacion_total_2024": {"$sum": "$facturacion_anual.2024"},  # SUM(fact_2024)
        "empresas_exportadoras": {"$sum": {"$cond": ["$exporta", 1, 0]}} # COUNT WHERE exporta=True
    }},
    
    # Etapa 3: Agregar campo calculado (como SELECT campo_calculado)
    {"$addFields": {
        "pct_exportadoras": {
            "$round": [
                {"$multiply": [
                    {"$divide": ["$empresas_exportadoras", "$total_empresas"]}, 
                    100
                ]}, 1
            ]
        }
    }},
    
    # Etapa 4: Ordenar por total de empresas descendente
    {"$sort": {"total_empresas": -1}},
    
    # Etapa 5: Limitar a top 8 sectores
    {"$limit": 8},
    
    # Etapa 6: Reformatear para presentación
    {"$project": {
        "sector": "$_id",
        "total_empresas": 1,
        "empleados_promedio": {"$round": ["$empleados_promedio", 0]},
        "facturacion_total_2024": 1,
        "pct_exportadoras": 1,
        "_id": 0
    }}
]

resultados = list(empresas.aggregate(pipeline_sector))

print(f"\n{'SECTOR':<20} {'TOTAL':>8} {'EMP.PROM':>10} {'FACTURAC.2024':>15} {'%EXPORT':>8}")
print("-" * 70)
for r in resultados:
    print(f"{r['sector']:<20} {r['total_empresas']:>8} {int(r['empleados_promedio']):>10} "
          f"S/{r['facturacion_total_2024']:>13,.0f} {r['pct_exportadoras']:>7.1f}%")
```

---

### 2.3 — Tu turno: Implementar análisis por departamento

```python
# ============================================================
# CELDA 6: TU IMPLEMENTACIÓN — Análisis por departamento
# ============================================================

# TAREA: Implementa un Aggregation Pipeline que calcule:
# Por cada departamento:
# 1. Total de empresas
# 2. Total de empleados
# 3. Facturación promedio 2024
# 4. Régimen tributario más común (hint: necesitas $push y luego procesar)
# 5. Solo para empresas ACTIVAS

# ESTRUCTURA BASE (completa los ___):
pipeline_departamento = [
    # Filtro: solo empresas activas
    {"$match": {"estado": ___}},
    
    # Agrupar por departamento
    {"$group": {
        "_id": "$departamento",
        "total_empresas": {"$sum": ___},
        "total_empleados": {"$sum": "$num_empleados"},
        "facturacion_promedio_2024": {"$avg": ___},
        "regimenes": {"$push": "$regimen_tributario"}  # Lista de regímenes
    }},
    
    # Ordenar por total de empleados
    {"$sort": {"total_empleados": ___}},  # -1 = descendente
    
    # Top 5
    {"$limit": 5}
]

resultados_dep = list(empresas.aggregate(pipeline_departamento))

print("TOP 5 DEPARTAMENTOS POR EMPLEADOS:")
for r in resultados_dep:
    print(f"  {r['_id']}: {r['total_empresas']} empresas | "
          f"{r['total_empleados']} empleados | "
          f"Fact.prom: S/{r['facturacion_promedio_2024']:,.0f}")

# PUNTO DE VERIFICACIÓN 2.3:
# Si Lima aparece primero con más empleados → tu código está correcto
# Lima tiene 35% de las empresas en Perú según estadísticas reales
```

---

### 2.4 — Crear índices y comparar rendimiento

```python
# ============================================================
# CELDA 7: Índices en MongoDB — la clave del rendimiento
# ============================================================
import time

# SIN ÍNDICE: consulta de empresas por sector
start = time.time()
for _ in range(100):  # 100 consultas para medir
    list(empresas.find({"sector": "Tecnología"}))
tiempo_sin_indice = (time.time() - start) / 100 * 1000
print(f"Sin índice (100 consultas): {tiempo_sin_indice:.2f} ms promedio")

# CREAR ÍNDICE en el campo sector
empresas.create_index("sector")
print("\nÍndice creado en campo 'sector'")

# CON ÍNDICE: misma consulta
start = time.time()
for _ in range(100):
    list(empresas.find({"sector": "Tecnología"}))
tiempo_con_indice = (time.time() - start) / 100 * 1000
print(f"Con índice (100 consultas): {tiempo_con_indice:.2f} ms promedio")
print(f"Mejora: {tiempo_sin_indice/tiempo_con_indice:.1f}x más rápido")

# Ver todos los índices de la colección
print(f"\nÍndices en la colección 'empresas':")
for idx in empresas.list_indexes():
    print(f"  - {idx['name']}: {idx['key']}")
```

**Pregunta de análisis 2.4:**
> Con 100 documentos la diferencia de velocidad con/sin índice es pequeña. ¿Por qué con 1 millón de documentos la diferencia sería dramática? 

Es como buscar una receta en un libro: sin índice, tienes que pasar y leer las 1 millón de páginas una por una hasta encontrarla. Con el índice, simplemente miras la sección ordenada alfabéticamente y vas directo a la página exacta. Pasar de revisar un millón de hojas a mirar solo una es lo que hace que la base de datos no se sature y responda al instante.

¿Qué estructura de datos usa MongoDB internamente para sus índices (similar a HBase Row Key)?

MongoDB utiliza internamente la estructura de Árboles B+ (B-Trees) mediante su motor WiredTiger, organizando los valores indexados de forma jerárquica para búsquedas ultrarrápidas. Cada nodo hoja almacena el valor ordenado junto a un puntero que apunta a la ubicación física del documento en el disco. A diferencia de HBase, que ordena los datos físicamente según su Row Key, MongoDB genera los índices como estructuras secundarias e independientes. Esto te permite tener múltiples índices sobre distintos campos de una misma colección sin alterar cómo se guardan los datos originales.

---

## PARTE 3 — DESAFÍO (30 min)

### 3.1 — Comparación SQL vs. NoSQL: el mismo análisis en dos modelos

Para el desafío, vas a implementar el mismo análisis en SQL (usando SQLite de Python) y en MongoDB, y comparar la complejidad del código.

```python
# ============================================================
# CELDA 8: El mismo análisis en SQL y en MongoDB
# ¿Cuál es más simple para este caso?
# ============================================================
import sqlite3
import pandas as pd

# ---- PARTE A: SQL con SQLite ----
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# En SQL, los datos anidados (facturacion_anual) requieren tabla separada
cursor.executescript("""
    CREATE TABLE empresas_sql (
        id INTEGER PRIMARY KEY,
        ruc TEXT,
        razon_social TEXT,
        departamento TEXT,
        sector TEXT,
        num_empleados INTEGER,
        exporta INTEGER
    );
    
    CREATE TABLE facturacion_sql (
        id INTEGER PRIMARY KEY,
        empresa_id INTEGER,
        anio INTEGER,
        monto REAL,
        FOREIGN KEY (empresa_id) REFERENCES empresas_sql(id)
    );
""")

# Insertar datos (simplificado: solo 10 empresas de ejemplo)
for i, emp in enumerate(dataset_empresas[:10]):
    cursor.execute("INSERT INTO empresas_sql VALUES (?,?,?,?,?,?,?)",
                   (i, emp['ruc'], emp['razon_social'], emp['departamento'],
                    emp['sector'], emp['num_empleados'], int(emp['exporta'])))
    for anio, monto in emp['facturacion_anual'].items():
        cursor.execute("INSERT INTO facturacion_sql VALUES (?,?,?,?)",
                       (None, i, int(anio), monto))
conn.commit()

# Consulta SQL: facturación 2024 por sector (requiere JOIN)
query_sql = """
    SELECT e.sector, 
           COUNT(e.id) as total_empresas,
           SUM(f.monto) as facturacion_total
    FROM empresas_sql e
    JOIN facturacion_sql f ON e.id = f.empresa_id
    WHERE f.anio = 2024
    GROUP BY e.sector
    ORDER BY facturacion_total DESC
"""
df_sql = pd.read_sql_query(query_sql, conn)
print("RESULTADO SQL (con JOIN):")
print(df_sql.to_string())

# ---- PARTE B: MongoDB (acceso directo, sin JOIN) ----
pipeline_nosql = [
    {"$group": {
        "_id": "$sector",
        "total_empresas": {"$sum": 1},
        "facturacion_total": {"$sum": "$facturacion_anual.2024"}
    }},
    {"$sort": {"facturacion_total": -1}}
]
resultados_nosql = list(empresas.aggregate(pipeline_nosql))
print("\nRESULTADO MongoDB (sin JOIN, acceso directo a campo anidado):")
for r in resultados_nosql[:5]:
    print(f"  {r['_id']}: {r['total_empresas']} empresas, S/{r['facturacion_total']:,.0f}")

# Pregunta de reflexión:
print("\n¿Qué fue más simple para datos anidados: SQL o MongoDB?")
```

---

### 3.2 — Pregunta de reflexión final

Responde en el notebook como texto (celda de texto en Colab):

**Pregunta 3.1:**
> En este laboratorio implementaste un Aggregation Pipeline de MongoDB. ¿En qué fase específica del pipeline puedes ver la equivalencia con las fases MAP y REDUCE de Hadoop MapReduce? Describe la analogía con un ejemplo de tu análisis.

**Pregunta 3.2 — Conexión con tu proyecto grupal:**
> ¿Qué datos de tu proyecto grupal (Grupos 1-7) almacenarías en MongoDB en lugar de en una tabla SQL? ¿Qué campo sería el equivalente al "_id" o clave de acceso principal? ¿Tendría sentido usar el Aggregation Pipeline de MongoDB en lugar de PySpark para algún análisis específico de tu proyecto?

---

## ENTREGABLES

1. **Screenshot de MongoDB Atlas** mostrando:
   - La colección `empresas` con el total de documentos visibles
   - Un documento expandido mostrando el objeto anidado `facturacion_anual`
   - Los índices creados en la colección

2. **Notebook Google Colab** (.ipynb) con:
   - Todas las celdas ejecutadas sin errores
   - Respuestas a las preguntas de reflexión como celdas de texto
   - La celda 6 completada (análisis por departamento)
   - Comparación SQL vs. MongoDB de la Parte 3

3. **Link del notebook** (File → Share → "Anyone with the link can view")

---

## RÚBRICA DE EVALUACIÓN

| Criterio | Excelente (4) | Suficiente (2-3) | Mínimo (1) | Cero (0) |
|----------|--------------|-----------------|------------|---------|
| Conexión a Atlas (15%) | Atlas M0 activo, connection exitosa, screenshot | Mongomock como alternativa | Error de conexión pero evidencia de intento | No intentó |
| Parte 1: Inserción (20%) | 100+ docs insertados, 2 estructuras diferentes mostradas | Dataset insertado sin análisis de estructura | Solo 1 documento insertado | No ejecutó Part 1 |
| Parte 2: Aggregation (35%) | Pipeline completo + Celda 6 implementada + índices | Pipeline del docente ejecutado sin Celda 6 propia | Solo consultas básicas (find) | No implementó pipeline |
| Parte 3: Desafío (20%) | Comparación SQL vs MongoDB + reflexiones escritas | Solo código, sin reflexiones | Intento parcial | No realizó Parte 3 |
| Calidad reflexiones (10%) | Respuestas conectan con proyecto grupal y conceptos de clase | Respuestas genéricas correctas | Respuestas muy breves | Sin respuestas |

---

## RECURSOS DE APOYO

- MongoDB Atlas Docs: https://www.mongodb.com/docs/atlas/
- pymongo Tutorial: https://pymongo.readthedocs.io/en/stable/tutorial.html
- Aggregation Pipeline: https://www.mongodb.com/docs/manual/core/aggregation-pipeline/
- MongoDB University (gratis): https://learn.mongodb.com/
- Video: "MongoDB Crash Course" (Traversy Media, YouTube, 30 min)

---

*Big Data DD283 | Universidad Autónoma del Perú | Semana 3 | 2026-1*
