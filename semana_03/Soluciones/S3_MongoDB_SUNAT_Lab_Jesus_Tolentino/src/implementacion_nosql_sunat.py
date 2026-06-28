"""
S3 Big Data DD283 — Laboratorio MongoDB SUNAT Simulado
Autor: Jesús Antonio Tolentino Vargas

Uso:
1. Con MongoDB Atlas: coloca tu connection string en CONNECTION_STRING.
2. Sin Atlas: deja CONNECTION_STRING vacío y se usará mongomock en memoria.
"""

from datetime import datetime
import random
import time
import sqlite3
import pandas as pd

CONNECTION_STRING = ""


def obtener_cliente():
    if CONNECTION_STRING.strip():
        from pymongo import MongoClient
        client = MongoClient(CONNECTION_STRING)
        client.admin.command("ping")
        print("Conexión exitosa a MongoDB Atlas")
        return client
    import mongomock
    print("Usando mongomock como alternativa local en memoria")
    return mongomock.MongoClient()


def insertar_empresas_base(empresas):
    empresas.delete_many({})

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
        "facturacion_anual": {"2022": 650000, "2023": 850000, "2024": 1200000},
        "productos_servicios": ["Software ERP", "Consultoría TI", "Soporte"],
        "certificaciones": ["ISO 9001", "CMMI Level 3"],
        "contacto": {
            "email": "contacto@tecandina.com",
            "telefono": "01-4567890",
            "web": "www.tecandina.com"
        },
        "exporta": False
    }

    empresa_agricola = {
        "ruc": "20987654321",
        "razon_social": "Agroindustrias del Sur EIRL",
        "departamento": "Arequipa",
        "sector": "Agroindustria",
        "estado": "ACTIVO",
        "num_empleados": 120,
        "facturacion_anual": {"2023": 2800000, "2024": 3200000},
        "cultivos_principales": ["Páprika", "Cebolla amarilla", "Ajo"],
        "hectareas_certificadas": 450,
        "certificaciones_organicas": ["USDA Organic", "BIO Suisse"],
        "mercados_exportacion": ["Estados Unidos", "Países Bajos", "España"],
        "exporta": True,
        "volumen_exportacion_tn": 1200
    }

    empresas.insert_one(empresa_tech)
    empresas.insert_one(empresa_agricola)

    print("Empresas base insertadas")
    for emp in empresas.find():
        print(f"RUC: {emp['ruc']} | {emp['razon_social']} | Campos: {len(emp.keys())}")


def generar_dataset(empresas):
    random.seed(42)
    departamentos = ["Lima", "Arequipa", "La Libertad", "Piura", "Cusco",
                        "Junin", "Puno", "Ancash", "Loreto", "Cajamarca", "Moquegua"]
    sectores = ["Tecnología", "Comercio", "Manufactura", "Construcción",
                "Agroindustria", "Minería", "Servicios", "Transporte", "Salud", "Educación"]
    regimenes = ["Régimen General", "MYPE Tributario", "NRUS", "Régimen Especial"]
    estados = ["ACTIVO", "ACTIVO", "ACTIVO", "SUSPENDIDO", "BAJA"]

    empresas.delete_many({"ruc": {"$regex": "^SYNTHETIC"}})

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
            "fecha_registro": datetime(random.randint(2000, 2023), random.randint(1, 12), random.randint(1, 28))
        }
        dataset_empresas.append(empresa)

    resultado = empresas.insert_many(dataset_empresas)
    print(f"Insertadas {len(resultado.inserted_ids)} empresas sintéticas")
    return dataset_empresas


def consultas_basicas(empresas):
    print("\nCONSULTAS BÁSICAS")
    lista1 = list(empresas.find({"estado": "ACTIVO", "departamento": "Lima"}))
    print(f"Empresas activas en Lima: {len(lista1)}")

    print("\nTop 5 empresas por empleados (>50):")
    query2 = empresas.find(
        {"num_empleados": {"$gt": 50}},
        {"razon_social": 1, "num_empleados": 1, "_id": 0}
    ).sort("num_empleados", -1).limit(5)
    for e in query2:
        print(f"{e['razon_social']}: {e['num_empleados']} empleados")

    total_exportadoras = empresas.count_documents({
        "exporta": True,
        "sector": {"$in": ["Agroindustria", "Manufactura", "Minería"]}
    })
    print(f"\nEmpresas exportadoras en sectores productivos: {total_exportadoras}")

    print("\nEmpresas con facturación 2024 > S/1M:")
    query4 = empresas.find(
        {"facturacion_anual.2024": {"$gt": 1000000}},
        {"razon_social": 1, "facturacion_anual.2024": 1, "_id": 0}
    )
    for e in list(query4)[:5]:
        print(f"{e['razon_social']}: S/{e['facturacion_anual']['2024']:,}")


def pipeline_sector(empresas):
    print("\nAGGREGATION PIPELINE POR SECTOR")
    pipeline_sector = [
        {"$match": {"estado": "ACTIVO"}},
        {"$group": {
            "_id": "$sector",
            "total_empresas": {"$sum": 1},
            "empleados_promedio": {"$avg": "$num_empleados"},
            "facturacion_total_2024": {"$sum": "$facturacion_anual.2024"},
            "empresas_exportadoras": {"$sum": {"$cond": ["$exporta", 1, 0]}}
        }},
        {"$addFields": {
            "pct_exportadoras": {
                "$round": [
                    {"$multiply": [{"$divide": ["$empresas_exportadoras", "$total_empresas"]}, 100]},
                    1
                ]
            }
        }},
        {"$sort": {"total_empresas": -1}},
        {"$limit": 8},
        {"$project": {
            "sector": "$_id",
            "total_empresas": 1,
            "empleados_promedio": {"$round": ["$empleados_promedio", 0]},
            "facturacion_total_2024": 1,
            "pct_exportadoras": 1,
            "_id": 0
        }}
    ]
    for r in list(empresas.aggregate(pipeline_sector)):
        print(r)


def pipeline_departamento(empresas):
    print("\nTOP 5 DEPARTAMENTOS POR EMPLEADOS")
    pipeline_departamento = [
        {"$match": {"estado": "ACTIVO"}},
        {"$group": {
            "_id": "$departamento",
            "total_empresas": {"$sum": 1},
            "total_empleados": {"$sum": "$num_empleados"},
            "facturacion_promedio_2024": {"$avg": "$facturacion_anual.2024"},
            "regimenes": {"$push": "$regimen_tributario"}
        }},
        {"$sort": {"total_empleados": -1}},
        {"$limit": 5}
    ]
    for r in list(empresas.aggregate(pipeline_departamento)):
        print(f"{r['_id']}: {r['total_empresas']} empresas | {r['total_empleados']} empleados | Fact.prom: S/{r['facturacion_promedio_2024']:,.0f}")


def indices(empresas):
    print("\nÍNDICES")
    start = time.time()
    for _ in range(100):
        list(empresas.find({"sector": "Tecnología"}))
    tiempo_sin_indice = (time.time() - start) / 100 * 1000
    print(f"Sin índice: {tiempo_sin_indice:.2f} ms promedio")
    empresas.create_index("sector")
    print("Índice creado en campo sector")
    start = time.time()
    for _ in range(100):
        list(empresas.find({"sector": "Tecnología"}))
    tiempo_con_indice = (time.time() - start) / 100 * 1000
    print(f"Con índice: {tiempo_con_indice:.2f} ms promedio")
    for idx in empresas.list_indexes():
        print(f"- {idx['name']}: {idx['key']}")


def comparacion_sql_mongodb(dataset_empresas, empresas):
    print("\nCOMPARACIÓN SQL VS MONGODB")
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
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
    for i, emp in enumerate(dataset_empresas[:10]):
        cursor.execute("INSERT INTO empresas_sql VALUES (?,?,?,?,?,?,?)",
                        (i, emp["ruc"], emp["razon_social"], emp["departamento"],
                        emp["sector"], emp["num_empleados"], int(emp["exporta"])))
        for anio, monto in emp["facturacion_anual"].items():
            cursor.execute("INSERT INTO facturacion_sql VALUES (?,?,?,?)", (None, i, int(anio), monto))
    conn.commit()
    query_sql = """
        SELECT e.sector, COUNT(e.id) as total_empresas, SUM(f.monto) as facturacion_total
        FROM empresas_sql e
        JOIN facturacion_sql f ON e.id = f.empresa_id
        WHERE f.anio = 2024
        GROUP BY e.sector
        ORDER BY facturacion_total DESC
    """
    df_sql = pd.read_sql_query(query_sql, conn)
    print("Resultado SQL:")
    print(df_sql.to_string(index=False))
    pipeline_nosql = [
        {"$group": {"_id": "$sector", "total_empresas": {"$sum": 1}, "facturacion_total": {"$sum": "$facturacion_anual.2024"}}},
        {"$sort": {"facturacion_total": -1}}
    ]
    print("\nResultado MongoDB:")
    for r in list(empresas.aggregate(pipeline_nosql))[:5]:
        print(f"{r['_id']}: {r['total_empresas']} empresas, S/{r['facturacion_total']:,.0f}")


def main():
    client = obtener_cliente()
    db = client["bigdata_s3_sunat"]
    empresas = db["empresas"]
    insertar_empresas_base(empresas)
    dataset_empresas = generar_dataset(empresas)
    consultas_basicas(empresas)
    pipeline_sector(empresas)
    pipeline_departamento(empresas)
    indices(empresas)
    comparacion_sql_mongodb(dataset_empresas, empresas)
    print("\nLaboratorio finalizado correctamente")


if __name__ == "__main__":
    main()
