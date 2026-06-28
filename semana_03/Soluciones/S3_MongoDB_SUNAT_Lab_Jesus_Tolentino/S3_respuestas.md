# S3 — Big Data DD283 — Semana 3
## Laboratorio MongoDB Atlas con datos SUNAT simulados

**Estudiante:** Jesús Antonio Tolentino Vargas  
**Curso:** Big Data DD283  
**Tema:** Hadoop Mejoras + Sistemas NoSQL: Clasificación e Implementación  

---

## Respuestas de reflexión

### Pregunta de reflexión 1.1

El documento de la empresa de tecnología tiene más campos porque incluye información como `tipo_empresa`, `distrito`, `regimen_tributario`, `fecha_registro_sunat`, `productos_servicios`, `certificaciones` y un objeto `contacto` con email, teléfono y web. La empresa agroindustrial tiene una estructura diferente, con campos propios como `cultivos_principales`, `hectareas_certificadas`, `certificaciones_organicas`, `mercados_exportacion` y `volumen_exportacion_tn`.

En una base de datos SQL tradicional, si la empresa agroindustrial no tuviera `contacto.web`, esa columna tendría que existir igual en la tabla y quedaría con valor `NULL`. En MongoDB no es necesario crear ese campo si no aplica al documento, lo que evita columnas vacías y permite un modelo más flexible.

---

### Pregunta de reflexión 1.2

`insert_many()` es más eficiente que ejecutar `insert_one()` cien veces porque reduce el número de viajes de red entre el programa y el servidor MongoDB. Si el clúster está en São Paulo y el código se ejecuta desde Colab o una PC local, cada operación individual agrega latencia de red. Con `insert_many()` se envía el lote completo en una sola operación, reduciendo overhead y mejorando el rendimiento.

---

### Pregunta de análisis 2.4

Con 100 documentos la diferencia entre consultar con índice y sin índice puede ser pequeña porque MongoDB puede recorrer todos los registros rápidamente. Sin embargo, con 1 millón de documentos la diferencia sería mucho mayor, ya que sin índice tendría que hacer un escaneo completo de la colección. Con índice, MongoDB puede ubicar los documentos de forma directa usando una estructura tipo **B-tree**, similar a la idea de acceso rápido por clave como ocurre con Row Key en HBase.

---

### Pregunta 3.1 — Relación Aggregation Pipeline con MapReduce

En MongoDB, la fase `$match` se parece a la etapa **Map** porque filtra y selecciona los documentos relevantes que serán procesados. La fase `$group` se parece a la etapa **Reduce**, porque agrupa los documentos por una clave y calcula métricas como conteo, suma o promedio.

Por ejemplo, en el análisis por sector, `$match` selecciona solo las empresas activas y `$group` agrupa por `sector` para calcular el total de empresas, promedio de empleados y facturación total. Esta lógica es equivalente a MapReduce, pero expresada mediante un pipeline declarativo.

---

### Pregunta 3.2 — Conexión con proyecto grupal

En un proyecto grupal de gestión empresarial o comercial, almacenaría en MongoDB los datos que tienen estructura variable, como perfiles de clientes, catálogos de productos, reportes, formularios o documentos con campos personalizados. El campo equivalente a `_id` podría ser el RUC, código de cliente, número de expediente o identificador único del registro.

Sí tendría sentido usar Aggregation Pipeline cuando el análisis sea puntual y esté sobre una colección de tamaño moderado, por ejemplo totales por categoría, conteos por estado o promedios por zona. Para análisis masivos con muchos archivos históricos o grandes volúmenes, PySpark sería más adecuado.

---

## Celda 6 completada — Análisis por departamento

```python
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
```

---

## Comparación SQL vs MongoDB

En SQL, los datos anidados como la facturación anual requieren normalizarse en tablas separadas. Por ejemplo, una tabla `empresas_sql` y otra tabla `facturacion_sql`, relacionadas mediante una clave foránea. Para obtener la facturación por sector se necesita hacer un `JOIN`.

En MongoDB, la facturación puede estar embebida dentro del mismo documento de la empresa como un objeto anidado. Esto permite consultar directamente `facturacion_anual.2024` sin usar `JOIN`, simplificando el modelo cuando los datos pertenecen naturalmente al mismo objeto de negocio.

---

## Conclusión

MongoDB es adecuado para este laboratorio porque permite representar empresas con estructuras diferentes sin forzar un esquema rígido. Además, mediante consultas, proyecciones, índices y Aggregation Pipeline, permite realizar análisis similares a SQL, pero trabajando directamente con documentos flexibles en formato BSON/JSON.
