# S2 — GUÍA DE TRABAJO DEL ESTUDIANTE
## Big Data DD283 | Universidad Autónoma del Perú | 2026-1
### Semana 2: Computación en la Nube para Big Data — Hadoop, HDFS, MapReduce, HBase

---

| Campo | Detalle |
|-------|---------|
| **Nombre del estudiante** | TOLENTINO VARGAS JESUS ANTONIO |
| **Sección** | SECCION 06 |
| **Fecha** | 18/06/2026 |
| **Tiempo estimado** | 1.5 horas |
| **Puntaje total** | 100 puntos |

---

### INSTRUCCIONES

- Lee cada pregunta con atención antes de responder.
- Esta guía evalúa los temas vistos en la sesión de la Semana 2.
- Tiempo recomendado: 90 minutos.
- **No incluyas respuestas en este documento** — responde en papel o en el documento que te indique el docente.
- Las preguntas van de menor a mayor dificultad. Completa en orden.
- Para las preguntas de código, puedes escribir pseudocódigo si no recuerdas la sintaxis exacta.

---

## SECCIÓN A — PREGUNTAS DE OPCIÓN MÚLTIPLE (20 puntos | 2 pts cada una)

*Marca con una X la alternativa correcta. Solo una respuesta es válida.*

---

**1.** ¿Cuál es la función principal del NameNode en HDFS?

a) Almacenar los bloques de datos distribuidos en el clúster  
b) Procesar las tareas MapReduce asignadas a cada nodo  
c) Mantener el índice (metadatos) de dónde se encuentran los bloques de datos[x]
d) Gestionar las conexiones de red entre los DataNodes  

RESPUESTA: c) 

---

**2.** ¿Cuál es el tamaño de bloque predeterminado en HDFS (Apache Hadoop 3.x)?

a) 4 KB  
b) 64 MB  
c) 128 MB[x] 
d) 1 GB  
RESPUESTA: c) 
---

**3.** En el modelo MapReduce, ¿cuál es la función de la fase "Shuffle and Sort"?

a) Escribir los resultados finales en HDFS  
b) Agrupar todos los pares clave-valor con la misma clave y enviarlos al mismo Reducer[x]  
c) Distribuir el archivo de entrada entre los DataNodes del clúster  
d) Comprimir los datos antes de enviarlos a los nodos trabajadores  
RESPUESTA: b)
---

**4.** ¿Qué componente de Hadoop se encarga de gestionar los recursos (CPU, RAM) del clúster y asignarlos a los trabajos que se ejecutan?

a) HDFS  
b) HBase  
c) YARN[x]  
d) ZooKeeper 

RESPUESTA: c)
---

**5.** Una empresa quiere consultar el saldo de un cliente bancario en menos de 50 milisegundos, buscando por número de DNI. ¿Qué tecnología del ecosistema Hadoop es más adecuada para este caso?

a) HDFS — porque distribuye los datos en múltiples nodos  
b) HBase — porque permite acceso aleatorio en tiempo real por Row Key[x]  
c) MapReduce — porque procesa datos en paralelo eficientemente  
d) Hive — porque permite consultas similares a SQL  
RESPUESTA: b)
---

**6.** ¿Qué diferencia fundamental existe entre Cloud Computing y Fog Computing?

a) Cloud usa servidores físicos y Fog usa servidores virtuales  
b) Fog procesa los datos cerca de donde se generan (borde de la red), mientras Cloud centraliza el procesamiento en data centers remotos[x]  
c) Cloud es gratuito y Fog es de pago  
d) Fog solo funciona con datos estructurados, mientras Cloud procesa cualquier tipo  
RESPUESTA: b)
---

**7.** Si un archivo de 400 MB se almacena en HDFS con tamaño de bloque de 128 MB y factor de replicación 3, ¿cuántos bloques físicos (copias) se almacenan en total en el clúster?

a) 3  
b) 4  
c) 9  
d) 12[x] 
RESPUESTA: d)
---

**8.** ¿Cuál es la principal limitación de Hadoop MapReduce frente a Apache Spark?

a) MapReduce no puede procesar archivos de más de 1 GB  
b) MapReduce requiere que los datos estén estructurados en formato CSV  
c) MapReduce escribe resultados intermedios en disco entre fases, haciéndolo más lento que Spark (que procesa en RAM)[x]
d) MapReduce no soporta el lenguaje Python para programar los jobs  
RESPUESTA: c)
---

**9.** En un modelo de servicio cloud, ¿cuál corresponde a "Platform as a Service" (PaaS) en el contexto de Big Data?

a) Comprar servidores físicos para el data center propio de la empresa  
b) Usar Amazon EC2 para instalar y configurar Hadoop manualmente  
c) Usar Amazon EMR o Google Dataproc, donde el proveedor gestiona el clúster y tú solo ejecutas los jobs[x] 
d) Usar Databricks con notebooks donde todo está configurado y solo escribes código  
RESPUESTA: c)
---

**10.** Un DataNode en un clúster Hadoop con factor de replicación 3 falla repentinamente. ¿Cuál es el comportamiento esperado del sistema?

a) Todo el clúster cae hasta que el DataNode sea reparado  
b) Se pierden permanentemente todos los bloques que estaban en ese DataNode  
c) El NameNode detecta el fallo, redirige las solicitudes a los otros nodos con copias, y comienza a re-replicar los bloques para restaurar el factor 3[x] 
d) El sistema suspende todos los jobs en ejecución hasta recuperar el nodo  
RESPUESTA: c)
---

## SECCIÓN B — COMPLETAR Y RELACIONAR (20 puntos)

### B1. Completa los espacios en blanco (10 puntos | 2 pts cada uno)

**11.** En HDFS, el nodo que almacena el directorio/índice de dónde están los bloques se llama **NameNode**, mientras que los nodos que guardan físicamente los bloques de datos se llaman **DataNodes**.

**12.** El modelo de programación **MapReduce** divide el procesamiento en dos fases: una fase de transformación local (MAP) que emite pares **clave-valor (key-value)**, y una fase de agregación (REDUCE) que consolida los resultados por clave.

**13.** La virtualización que permite ejecutar múltiples sistemas operativos sobre un mismo hardware físico usa una capa de software llamada **Hipervisor**.

**14.** HBase organiza los datos en tablas donde cada fila tiene un identificador único llamado **Row Key**, que es el único índice nativo disponible para búsquedas rápidas.

**15.** En Fog Computing, el procesamiento ocurre en el **borde (edge)** de la red (cerca de los dispositivos), reduciendo la **latencia** de comunicación con el data center central.

---

### B2. Relacionar columnas (10 puntos | 1 pt cada par correcto)

Relaciona cada concepto (columna izquierda) con su descripción correcta (columna derecha). Escribe la letra correspondiente.

| N° | Concepto | | Letra | Descripción |
|----|----------|-|-------|-------------|
| 1 | YARN |E | A | Base de datos NoSQL distribuida sobre HDFS para acceso aleatorio en tiempo real |
| 2 | ZooKeeper |C | B | Herramienta para importar/exportar datos entre RDBMS y HDFS |
| 3 | HBase |A | C | Framework de coordinación y sincronización distribuida en el ecosistema Hadoop |
| 4 | Sqoop |B | D | Motor de consultas SQL sobre datos en HDFS (similar a un data warehouse) |
| 5 | Hive |D | E | Gestor de recursos del clúster Hadoop que asigna CPU/RAM a los trabajos |
| 6 | Kafka |F | F | Plataforma de streaming de eventos y mensajería distribuida en tiempo real |
| 7 | Spark |G | G | Motor de procesamiento en memoria, sucesor de MapReduce, 100x más rápido |
| 8 | Docker |H | H | Tecnología de contenedores para desplegar clústeres Hadoop aislados |
| 9 | NameNode |I | I | Nodo maestro de HDFS que almacena los metadatos del sistema de archivos |
| 10 | DataNode |J | J | Nodo trabajador de HDFS que almacena físicamente los bloques de datos |

---

## SECCIÓN C — ANÁLISIS Y REFLEXIÓN (30 puntos)

*Responde con oraciones completas. Extensión sugerida: 3-5 líneas por pregunta.*

---

**16. (8 puntos)** El MINSA desea implementar un sistema para analizar los reportes de emergencias en todos los hospitales de Lima en tiempo real (cada hospital envía datos cada 30 segundos) y también quiere hacer análisis históricos de los últimos 5 años para identificar patrones estacionales de enfermedades.

a) ¿Qué tipo de procesamiento requiere cada necesidad (batch o streaming)?

Los reportes que envían los hospitales cada 30 segundos necesitan un procesamiento streaming, ya que la información debe analizarse prácticamente en tiempo real para detectar emergencias o cambios importantes de forma inmediata.

En cambio, el análisis de los datos acumulados durante los últimos cinco años corresponde a un procesamiento batch, porque se trabaja con información histórica para identificar tendencias y patrones sin que sea necesario obtener resultados al instante.
 
b) ¿Qué componentes del ecosistema Hadoop/Cloud recomendarías para cada caso?

Para el procesamiento en tiempo real utilizaría Apache Kafka para recibir continuamente los datos enviados por los hospitales y Apache Spark Streaming para analizarlos a medida que llegan. Los resultados podrían mostrarse en un dashboard para que el personal de salud monitoree la situación en tiempo real.

Para el análisis histórico emplearía HDFS o un Data Lake para almacenar toda la información generada durante los cinco años, y Apache Spark o Apache Hive para ejecutar consultas y generar reportes sobre grandes volúmenes de datos de forma eficiente.
  
c) Justifica por qué elegiste esos componentes y no otros.

Kafka y Spark Streaming son una buena combinación para este caso porque permiten recibir y procesar la información apenas llega desde los hospitales. Esto hace posible detectar situaciones críticas casi en tiempo real y apoyar la toma de decisiones de forma rápida. En cambio, para analizar la información acumulada de los últimos cinco años es más conveniente utilizar HDFS junto con Spark o Hive, ya que están diseñados para procesar grandes volúmenes de datos de manera eficiente. De esta forma se utiliza la herramienta adecuada para cada necesidad.

---

**17. (8 puntos)** Compara el concepto de "localidad de datos" en Hadoop con el modelo cliente-servidor tradicional donde los datos viajan de la base de datos al servidor de aplicaciones para ser procesados.

a) ¿Qué problema resuelve la "localidad de datos" en Hadoop?

La localidad de datos busca reducir el tráfico en la red. En lugar de mover archivos muy grandes hacia el servidor donde se ejecuta el programa, Hadoop envía el procesamiento al nodo donde ya están almacenados los datos. Esto hace que el trabajo sea mucho más rápido y aprovecha mejor los recursos del clúster.
  
b) ¿Por qué este principio es especialmente importante cuando los archivos tienen tamaños de 1 TB o más?

Cuando los archivos tienen tamaños de 1 TB o más, copiarlos de un servidor a otro puede tomar bastante tiempo y consumir mucho ancho de banda. Al procesar los datos directamente en el nodo donde se encuentran almacenados, solo se envían los resultados finales, que normalmente son mucho más pequeños.
  
c) ¿Este principio sigue siendo válido en entornos cloud donde el almacenamiento (S3) y el cómputo (EC2) están separados?

En los servicios cloud el almacenamiento y el procesamiento suelen estar separados, por lo que parte de la información sí debe viajar por la red. Sin embargo, este impacto se reduce gracias a la infraestructura de alta velocidad del proveedor y al uso de formatos optimizados como Parquet. Aunque el concepto cambia un poco respecto a Hadoop tradicional, el objetivo sigue siendo minimizar el movimiento innecesario de datos.

---

**18. (6 puntos) — Mini caso de análisis:**

*La cadena Tottus Perú genera 2 millones de boletas de venta al día en sus 80 tiendas. Cada boleta tiene: tienda, hora, lista de productos comprados, monto total, método de pago. Al final del mes, el gerente de analytics quiere saber: ¿qué combinaciones de productos se compran juntas con mayor frecuencia (análisis de canasta)? El archivo mensual tiene 60 millones de filas y 25 GB.*

a) ¿Usarías HDFS o una base de datos relacional (SQL) para almacenar estos 25 GB? Justifica.

En este caso utilizaría HDFS porque el objetivo es analizar una gran cantidad de información de manera periódica. Los 25 GB mensuales y los millones de registros pueden procesarse de forma distribuida utilizando Spark o MapReduce. Una base de datos relacional sería más adecuada para operaciones transaccionales, pero no para este tipo de análisis masivo.
  
b) Describe en pseudocódigo los pasos del algoritmo MapReduce para encontrar las 10 combinaciones de productos más frecuentes.

<b>// FASE MAP
map(clave, boleta):
    productos = boleta.lista_de_productos
    // generar todos los pares de productos comprados juntos
    para cada par (A, B) en combinaciones(productos, 2):
        par_ordenado = ordenar(A, B)   // (Leche, Pan) = (Pan, Leche)
        emitir(par_ordenado, 1)

// FASE SHUFFLE AND SORT (automática)
// agrupa todos los "1" de cada par de productos igual

// FASE REDUCE
reduce(par_producto, lista_de_unos):
    total = suma(lista_de_unos)
    emitir(par_producto, total)

// PASO FINAL (ordenar y tomar top 10)
ordenar todos los pares por total descendente
devolver los primeros 10 pares</b>

---

**19. (8 puntos)** Explica por qué el "Single Point of Failure" del NameNode fue el mayor problema de Hadoop 1.x y cómo lo resolvió Hadoop 2.x con la arquitectura de Alta Disponibilidad (HA). 

En Hadoop 1.x existía un único NameNode encargado de administrar todos los metadatos del sistema de archivos. Si ese servidor fallaba, el clúster dejaba de funcionar porque ya no era posible saber dónde estaban almacenados los bloques de datos, aunque estos siguieran existiendo en los DataNodes.

Hadoop 2 solucionó este problema incorporando Alta Disponibilidad (HA), donde existen dos NameNodes: uno activo y otro en espera. Ambos permanecen sincronizados y, si el principal presenta una falla, el secundario asume el control automáticamente. Esto permite mantener el servicio disponible sin afectar el funcionamiento del clúster.


¿Qué implicaciones tiene este problema para el diseño de sistemas críticos de producción?


Este caso demuestra la importancia de evitar puntos únicos de fallo en sistemas críticos. En ambientes de producción siempre es recomendable implementar mecanismos de redundancia y recuperación automática para garantizar la continuidad del servicio.

---

## SECCIÓN D — PREGUNTAS AVANZADAS Y DE CASO (30 puntos)

---

**20. Caso profesional real (15 puntos)**

*Eres el arquitecto de datos de la empresa Civa (empresa de transporte interprovincial en Perú). Civa opera 1,200 buses en 300 rutas. Cada bus tiene un dispositivo GPS que envía posición, velocidad y estado del motor cada 15 segundos. Adicionalmente, cada bus tiene cámaras de seguridad que graban continuamente (video comprimido: 2 GB/hora). La empresa quiere:*

*1. Monitorear en tiempo real la posición de todos los buses para informar a los pasajeros*  
*2. Detectar conducción peligrosa (frenadas bruscas, exceso de velocidad) automáticamente*  
*3. Analizar históricamente los datos de los últimos 2 años para optimizar rutas*  
*4. Almacenar los videos para revisión en caso de incidentes (se conservan 30 días)*

*Volumen de datos estimado: 1,200 buses × 4 datos GPS/min × 1,440 min/día = 6.9 millones de registros GPS/día. Videos: 1,200 buses × 2 GB/hora × 16 horas/día = 38,400 GB (38.4 TB) de video al día.*

Responde:

a) ¿Qué componentes del ecosistema Hadoop/Cloud usarías para cada uno de los 4 requerimientos? Crea una tabla con: Requerimiento | Tecnología | Justificación (5 puntos)


| Requerimiento                                               | Tecnología                             | Justificación                                                                                                                                                                                                                                                                                                                                                   |
| :---------------------------------------------------------- | :------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1. Monitoreo en tiempo real de la posición de los buses** | **Apache Kafka + Spark Streaming**     | Los dispositivos GPS generan información constantemente, por lo que se necesita una plataforma capaz de recibir y procesar esos datos casi al instante. Kafka permite manejar el flujo continuo de eventos y Spark Streaming analiza la información en tiempo real para actualizar la ubicación de cada bus.                                                    |
| **2. Detectar conducción peligrosa**                        | **Spark Streaming + Machine Learning** | Para identificar excesos de velocidad o frenadas bruscas es necesario analizar cada evento conforme ocurre. Spark Streaming permite aplicar reglas de negocio o modelos de Machine Learning para detectar comportamientos anómalos y generar alertas en pocos segundos.                                                                                         |
| **3. Análisis histórico de dos años para optimizar rutas**  | **HDFS + Apache Spark + Hive**         | El análisis histórico trabaja con millones de registros acumulados, por lo que resulta más eficiente almacenarlos en HDFS y procesarlos con Spark. Hive facilita la consulta de esos datos mediante un lenguaje similar a SQL para generar reportes y apoyar la toma de decisiones.                                                                             |
| **4. Almacenamiento de videos por 30 días**                 | **Amazon S3 o MinIO**                  | Debido al gran volumen de videos que se genera diariamente, un almacenamiento de objetos es la alternativa más conveniente. Este tipo de solución ofrece mayor capacidad de crecimiento, menor costo por almacenamiento y permite administrar fácilmente el ciclo de vida de los archivos, eliminándolos automáticamente cuando cumplen el tiempo de retención. |


b) Para los datos GPS, ¿usarías HBase o HDFS? ¿Por qué depende del caso de uso? Explica con un ejemplo concreto de cada caso de uso de GPS. (5 puntos)

Depende del caso de uso:


Utilizaría HBase cuando sea necesario consultar rápidamente la información de un bus específico, por ejemplo conocer su ubicación actual para informar a un pasajero. Como HBase permite búsquedas por Row Key, la respuesta se obtiene en muy poco tiempo.

En cambio, utilizaría HDFS cuando el objetivo sea analizar millones de registros históricos para identificar patrones, retrasos o proponer mejoras en las rutas. En este escenario resulta más eficiente procesar toda la información mediante Spark.

Lo más recomendable es combinar ambas tecnologías: HBase para las consultas en tiempo real y HDFS para el análisis histórico.

En la práctica se usan ambos: HBase para el acceso en vivo y HDFS para el histórico.

c) ¿Los videos irían a HDFS, HBase o a un almacenamiento de objetos (S3/MinIO)? Justifica considerando el volumen (38 TB/día × 30 días = 1.15 PB). (5 puntos)

Los videos los almacenaría en un sistema de almacenamiento de objetos como Amazon S3 o MinIO. Este tipo de plataformas está diseñado para manejar archivos grandes de forma económica y escalable.

Guardar más de un petabyte de videos en HDFS implicaría un consumo muy alto de almacenamiento debido a la replicación, mientras que HBase tampoco está pensado para almacenar archivos multimedia de gran tamaño. Además, el almacenamiento de objetos permite administrar políticas de retención y eliminar automáticamente los videos cuando cumplen el tiempo definido.

**-El object storage está diseñado para archivos grandes e inmutables (como videos) a un costo por TB mucho menor.  
-HDFS sufriría con tantos archivos grandes porque sobrecargaría la memoria del NameNode con metadatos, y mantener réplicas de 1.15 PB sería carísimo.  
-HBase está pensado para registros pequeños con acceso aleatorio, no para blobs de video de 2 GB/hora.  
-S3/MinIO permite políticas de retención automática (borrar a los 30 días) y escala virtualmente sin límite.**


---

**21. Pregunta de diseño (8 puntos)**

*"¿Cómo implementarías un sistema de detección de fraude bancario en tiempo real usando componentes del ecosistema Hadoop/Cloud? El sistema debe analizar 10,000 transacciones por segundo y emitir una alerta en menos de 2 segundos si detecta un patrón sospechoso."*

Describe:
- La arquitectura de componentes (qué tecnología en cada capa)
- Cómo fluyen los datos desde la transacción hasta la alerta
- Por qué el procesamiento batch tradicional (MapReduce) NO sería suficiente para este caso
- Qué herramienta reemplazaría a MapReduce en este escenario

Para este escenario implementaría una arquitectura basada en procesamiento en tiempo real.

Las transacciones ingresarían primero a Apache Kafka, que actuaría como plataforma de mensajería. Luego Spark Streaming consumiría esos eventos y evaluaría cada transacción aplicando reglas de negocio o un modelo de Machine Learning. Si fuera necesario consultar información del cliente, se accedería rápidamente a HBase, y finalmente, si se detecta una operación sospechosa, el sistema enviaría una alerta al área correspondiente.

No utilizaría MapReduce porque trabaja por lotes y necesita escribir resultados intermedios en disco, lo que incrementa considerablemente la latencia. En un sistema antifraude la respuesta debe generarse en pocos segundos, por lo que herramientas como Spark Streaming o Apache Flink resultan mucho más apropiadas.

---

**22. Pensamiento crítico (7 puntos)**

*"¿Qué pasaría si una empresa decide usar HBase para TODO su almacenamiento Big Data — tanto para análisis histórico de 5 años (petabytes) como para consultas en tiempo real — en lugar de usar HDFS para el histórico y HBase para el tiempo real?"*

Analiza:
- ¿Es técnicamente posible?

Sí, es posible almacenar toda la información en HBase, pero no sería la mejor decisión. Aunque HBase puede manejar grandes volúmenes de datos, fue diseñado principalmente para consultas rápidas sobre registros específicos y no para realizar análisis históricos de varios años.

- ¿Cuáles serían los problemas de rendimiento, costo y escalabilidad?

Problemas de rendimiento, costo y escalabilidad:


Rendimiento: Al utilizar HBase para almacenar datos históricos, las consultas analíticas serían más lentas, ya que este tipo de base de datos no está optimizada para recorrer grandes cantidades de información. En cambio, HDFS junto con Spark o Hive ofrece un mejor desempeño para este tipo de análisis.

Costo: Mantener petabytes de información en HBase implica un mayor consumo de memoria y recursos del clúster. Esto incrementa el costo de infraestructura y hace que el sistema sea menos eficiente para datos que solo se consultan de manera ocasional.

Escalabilidad: A medida que el volumen de información aumenta, también lo hacen las tareas de administración interna de HBase, como las compactaciones y el balanceo de regiones. Esto puede afectar el rendimiento general del sistema y dificultar su administración.

- ¿Cuál sería el riesgo de este diseño en producción?

El principal riesgo es utilizar una sola tecnología para resolver necesidades diferentes. El sistema terminaría consumiendo más recursos, aumentando los costos y reduciendo el rendimiento tanto de las consultas en tiempo real como de los análisis históricos. En lugar de aprovechar las ventajas de HBase, se estaría utilizando fuera del escenario para el que fue diseñado.

- ¿Qué evidencia de la sesión de clase apoya tu respuesta?

Durante la sesión vimos que cada componente del ecosistema Hadoop cumple una función específica. HDFS está orientado al almacenamiento distribuido y al procesamiento masivo de datos históricos, mientras que HBase está pensado para consultas rápidas sobre registros individuales. Por esa razón, una arquitectura que combine ambas tecnologías resulta más eficiente que intentar resolver todos los casos de uso únicamente con HBase.

---

*Big Data DD283 | Universidad Autónoma del Perú | Semana 2 | 2026-1*
*Guía de trabajo — NO incluye respuestas*
