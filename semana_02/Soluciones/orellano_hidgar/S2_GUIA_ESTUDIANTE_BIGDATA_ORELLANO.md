# S2 - GUIA DE TRABAJO DEL ESTUDIANTE - RESUELTA
## Big Data DD283 | Universidad Autonoma del Peru | 2026-1
### Semana 2: Computacion en la Nube para Big Data - Hadoop, HDFS, MapReduce, HBase

---

| Campo | Detalle |
|-------|---------|
| **Nombre del estudiante** | Hidgar Orellano Huerta |
| **Codigo de estudiante** | 2221892872 |
| **Seccion** | 6 |
| **Fecha** | 20/06/2026 |
| **Tiempo estimado** | 1.5 horas |
| **Puntaje total** | 100 puntos |

---

## SECCION A - PREGUNTAS DE OPCION MULTIPLE (20 puntos | 2 pts cada una)

*Marca con una X la alternativa correcta. Solo una respuesta es valida.*

---

**1.** ¿Cual es la funcion principal del NameNode en HDFS?

a) Almacenar los bloques de datos distribuidos en el cluster  
b) Procesar las tareas MapReduce asignadas a cada nodo  
c) **[X] Mantener el indice (metadatos) de donde se encuentran los bloques de datos**  
d) Gestionar las conexiones de red entre los DataNodes  

---

**2.** ¿Cual es el tamano de bloque predeterminado en HDFS (Apache Hadoop 3.x)?

a) 4 KB  
b) 64 MB  
c) **[X] 128 MB**  
d) 1 GB  

---

**3.** En el modelo MapReduce, ¿cual es la funcion de la fase "Shuffle and Sort"?

a) Escribir los resultados finales en HDFS  
b) **[X] Agrupar todos los pares clave-valor con la misma clave y enviarlos al mismo Reducer**  
c) Distribuir el archivo de entrada entre los DataNodes del cluster  
d) Comprimir los datos antes de enviarlos a los nodos trabajadores  

---

**4.** ¿Que componente de Hadoop se encarga de gestionar los recursos (CPU, RAM) del cluster y asignarlos a los trabajos que se ejecutan?

a) HDFS  
b) HBase  
c) **[X] YARN**  
d) ZooKeeper  

---

**5.** Una empresa quiere consultar el saldo de un cliente bancario en menos de 50 milisegundos, buscando por numero de DNI. ¿Que tecnologia del ecosistema Hadoop es mas adecuada para este caso?

a) HDFS - porque distribuye los datos en multiples nodos  
b) **[X] HBase - porque permite acceso aleatorio en tiempo real por Row Key**  
c) MapReduce - porque procesa datos en paralelo eficientemente  
d) Hive - porque permite consultas similares a SQL  

---

**6.** ¿Que diferencia fundamental existe entre Cloud Computing y Fog Computing?

a) Cloud usa servidores fisicos y Fog usa servidores virtuales  
b) **[X] Fog procesa los datos cerca de donde se generan (borde de la red), mientras Cloud centraliza el procesamiento en data centers remotos**  
c) Cloud es gratuito y Fog es de pago  
d) Fog solo funciona con datos estructurados, mientras Cloud procesa cualquier tipo  

---

**7.** Si un archivo de 400 MB se almacena en HDFS con tamano de bloque de 128 MB y factor de replicacion 3, ¿cuantos bloques fisicos (copias) se almacenan en total en el cluster?

a) 3  
b) 4  
c) 9  
d) **[X] 12**  

**Sustento:** 400 MB se dividen en 4 bloques logicos (128 + 128 + 128 + 16 MB). Con factor de replicacion 3, se almacenan 4 x 3 = 12 bloques fisicos.

---

**8.** ¿Cual es la principal limitacion de Hadoop MapReduce frente a Apache Spark?

a) MapReduce no puede procesar archivos de mas de 1 GB  
b) MapReduce requiere que los datos esten estructurados en formato CSV  
c) **[X] MapReduce escribe resultados intermedios en disco entre fases, haciendolo mas lento que Spark (que procesa en RAM)**  
d) MapReduce no soporta el lenguaje Python para programar los jobs  

---

**9.** En un modelo de servicio cloud, ¿cual corresponde a "Platform as a Service" (PaaS) en el contexto de Big Data?

a) Comprar servidores fisicos para el data center propio de la empresa  
b) Usar Amazon EC2 para instalar y configurar Hadoop manualmente  
c) **[X] Usar Amazon EMR o Google Dataproc, donde el proveedor gestiona el cluster y tu solo ejecutas los jobs**  
d) Usar Databricks con notebooks donde todo esta configurado y solo escribes codigo  

---

**10.** Un DataNode en un cluster Hadoop con factor de replicacion 3 falla repentinamente. ¿Cual es el comportamiento esperado del sistema?

a) Todo el cluster cae hasta que el DataNode sea reparado  
b) Se pierden permanentemente todos los bloques que estaban en ese DataNode  
c) **[X] El NameNode detecta el fallo, redirige las solicitudes a los otros nodos con copias, y comienza a re-replicar los bloques para restaurar el factor 3**  
d) El sistema suspende todos los jobs en ejecucion hasta recuperar el nodo  

---

## SECCION B - COMPLETAR Y RELACIONAR (20 puntos)

### B1. Completa los espacios en blanco (10 puntos | 2 pts cada uno)

**11.** En HDFS, el nodo que almacena el directorio/indice de donde estan los bloques se llama **NameNode**, mientras que los nodos que guardan fisicamente los bloques de datos se llaman **DataNodes**.

**12.** El modelo de programacion **MapReduce** divide el procesamiento en dos fases: una fase de transformacion local (MAP) que emite pares **clave-valor**, y una fase de agregacion (REDUCE) que consolida los resultados por clave.

**13.** La virtualizacion que permite ejecutar multiples sistemas operativos sobre un mismo hardware fisico usa una capa de software llamada **hipervisor**.

**14.** HBase organiza los datos en tablas donde cada fila tiene un identificador unico llamado **Row Key**, que es el unico indice nativo disponible para busquedas rapidas.

**15.** En Fog Computing, el procesamiento ocurre en el **borde** de la red (cerca de los dispositivos), reduciendo la **latencia** de comunicacion con el data center central.

---

### B2. Relacionar columnas (10 puntos | 1 pt cada par correcto)

Relaciona cada concepto (columna izquierda) con su descripcion correcta (columna derecha). Escribe la letra correspondiente.

| N° | Concepto | Letra | Descripcion |
|----|----------|-------|-------------|
| 1 | YARN | **E** | Gestor de recursos del cluster Hadoop que asigna CPU/RAM a los trabajos |
| 2 | ZooKeeper | **C** | Framework de coordinacion y sincronizacion distribuida en el ecosistema Hadoop |
| 3 | HBase | **A** | Base de datos NoSQL distribuida sobre HDFS para acceso aleatorio en tiempo real |
| 4 | Sqoop | **B** | Herramienta para importar/exportar datos entre RDBMS y HDFS |
| 5 | Hive | **D** | Motor de consultas SQL sobre datos en HDFS (similar a un data warehouse) |
| 6 | Kafka | **F** | Plataforma de streaming de eventos y mensajeria distribuida en tiempo real |
| 7 | Spark | **G** | Motor de procesamiento en memoria, sucesor de MapReduce, mas rapido |
| 8 | Docker | **H** | Tecnologia de contenedores para desplegar clusters Hadoop aislados |
| 9 | NameNode | **I** | Nodo maestro de HDFS que almacena los metadatos del sistema de archivos |
| 10 | DataNode | **J** | Nodo trabajador de HDFS que almacena fisicamente los bloques de datos |

---

## SECCION C - ANALISIS Y REFLEXION (30 puntos)

*Responde con oraciones completas. Extension sugerida: 3-5 lineas por pregunta.*

---

**16. (8 puntos)** El MINSA desea implementar un sistema para analizar los reportes de emergencias en todos los hospitales de Lima en tiempo real (cada hospital envia datos cada 30 segundos) y tambien quiere hacer analisis historicos de los ultimos 5 anos para identificar patrones estacionales de enfermedades.

a) ¿Que tipo de procesamiento requiere cada necesidad (batch o streaming)?  
b) ¿Que componentes del ecosistema Hadoop/Cloud recomendarias para cada caso?  
c) Justifica por que elegiste esos componentes y no otros.

**Respuesta:**

a) El monitoreo de reportes enviados cada 30 segundos requiere **procesamiento streaming**, porque se necesita analizar informacion casi en tiempo real. El analisis de los ultimos 5 anos requiere **procesamiento batch**, porque se trabaja con datos historicos acumulados para encontrar patrones estacionales.

b) Para streaming recomendaria **Kafka** para recibir eventos desde hospitales, **Spark Structured Streaming** para procesarlos y **HBase** o una base NoSQL para consultar estados recientes por hospital, distrito o tipo de emergencia. Para historico recomendaria **HDFS/S3** como data lake, archivos **Parquet** y procesamiento con **Spark** o consultas con **Hive**.

c) Elijo Kafka y Spark Streaming porque MapReduce no esta disenado para latencias de segundos. Para el historico uso HDFS/S3 y Spark porque permiten almacenar y procesar grandes volumenes de datos con menor costo y mejor escalabilidad que una base transaccional tradicional.

---

**17. (8 puntos)** Compara el concepto de "localidad de datos" en Hadoop con el modelo cliente-servidor tradicional donde los datos viajan de la base de datos al servidor de aplicaciones para ser procesados.

a) ¿Que problema resuelve la "localidad de datos" en Hadoop?  
b) ¿Por que este principio es especialmente importante cuando los archivos tienen tamanos de 1 TB o mas?  
c) ¿Este principio sigue siendo valido en entornos cloud donde el almacenamiento (S3) y el computo (EC2) estan separados?

**Respuesta:**

a) La localidad de datos resuelve el problema de mover grandes volumenes por la red. En Hadoop se procura llevar el procesamiento al nodo donde estan los bloques, en vez de mover todos los datos hacia un servidor central.

b) Es importante con archivos de 1 TB o mas porque moverlos por red consume ancho de banda, aumenta tiempos de espera y puede saturar el cluster. Procesar localmente permite que cada nodo trabaje su parte y solo se intercambien resultados intermedios.

c) En cloud el principio cambia, pero sigue siendo valido. Si S3 y EC2 estan separados, conviene ubicarlos en la misma region, usar formatos eficientes como Parquet, particionar datos y evitar lecturas innecesarias para reducir latencia y costo.

---

**18. (6 puntos) - Mini caso de analisis:**

*La cadena Tottus Peru genera 2 millones de boletas de venta al dia en sus 80 tiendas. Cada boleta tiene: tienda, hora, lista de productos comprados, monto total, metodo de pago. Al final del mes, el gerente de analytics quiere saber: ¿que combinaciones de productos se compran juntas con mayor frecuencia (analisis de canasta)? El archivo mensual tiene 60 millones de filas y 25 GB.*

a) ¿Usarias HDFS o una base de datos relacional (SQL) para almacenar estos 25 GB? Justifica.  
b) Describe en pseudocodigo los pasos del algoritmo MapReduce para encontrar las 10 combinaciones de productos mas frecuentes.

**Respuesta:**

a) Usaria **HDFS o almacenamiento de objetos tipo data lake** porque el objetivo es analitico y puede crecer con el tiempo. Una base SQL podria guardar 25 GB, pero el analisis de combinaciones sobre 60 millones de filas escala mejor con procesamiento distribuido como Spark o MapReduce.

b) Pseudocodigo:

```text
MAP(linea_boleta):
    productos = extraer_lista_productos(linea_boleta)
    productos = ordenar_y_quitar_duplicados(productos)
    para cada par (p1, p2) en combinaciones(productos, 2):
        emitir((p1, p2), 1)

COMBINER(opcional):
    para cada par local:
        emitir(par, suma_local)

SHUFFLE_AND_SORT:
    agrupar todos los valores por la misma combinacion de productos

REDUCE(par, lista_conteos):
    total = suma(lista_conteos)
    emitir(par, total)

JOB_FINAL:
    ordenar por total descendente
    devolver las 10 combinaciones con mayor frecuencia
```

---

**19. (8 puntos)** Explica por que el "Single Point of Failure" del NameNode fue el mayor problema de Hadoop 1.x y como lo resolvio Hadoop 2.x con la arquitectura de Alta Disponibilidad (HA). ¿Que implicaciones tiene este problema para el diseno de sistemas criticos de produccion?

**Respuesta:**

En Hadoop 1.x el NameNode era un punto unico de falla porque concentraba los metadatos de HDFS. Si el NameNode fallaba, los DataNodes aun podian tener los bloques fisicos, pero el cluster no podia ubicar archivos ni atender operaciones normales del sistema de archivos.

Hadoop 2.x resolvio este problema con Alta Disponibilidad (HA), usando un NameNode activo y otro standby sincronizado mediante JournalNodes y coordinacion con ZooKeeper. Si el activo falla, el standby puede asumir el rol y continuar el servicio con menor interrupcion.

Para sistemas criticos esto implica que no se debe depender de un unico componente central. Se requieren redundancia, failover automatico, monitoreo, copias de seguridad y pruebas de recuperacion para asegurar continuidad operativa.

---

## SECCION D - PREGUNTAS AVANZADAS Y DE CASO (30 puntos)

---

**20. Caso profesional real (15 puntos)**

*Eres el arquitecto de datos de la empresa Civa (empresa de transporte interprovincial en Peru). Civa opera 1,200 buses en 300 rutas. Cada bus tiene un dispositivo GPS que envia posicion, velocidad y estado del motor cada 15 segundos. Adicionalmente, cada bus tiene camaras de seguridad que graban continuamente (video comprimido: 2 GB/hora). La empresa quiere:*

*1. Monitorear en tiempo real la posicion de todos los buses para informar a los pasajeros*  
*2. Detectar conduccion peligrosa (frenadas bruscas, exceso de velocidad) automaticamente*  
*3. Analizar historicamente los datos de los ultimos 2 anos para optimizar rutas*  
*4. Almacenar los videos para revision en caso de incidentes (se conservan 30 dias)*

*Volumen de datos estimado: 1,200 buses x 4 datos GPS/min x 1,440 min/dia = 6.9 millones de registros GPS/dia. Videos: 1,200 buses x 2 GB/hora x 16 horas/dia = 38,400 GB (38.4 TB) de video al dia.*

Responde:

a) ¿Que componentes del ecosistema Hadoop/Cloud usarias para cada uno de los 4 requerimientos? Crea una tabla con: Requerimiento | Tecnologia | Justificacion (5 puntos)

**Respuesta a):**

| Requerimiento | Tecnologia | Justificacion |
|---------------|------------|---------------|
| 1. Monitorear posicion en tiempo real | Kafka + Spark Structured Streaming + API/dashboard | Kafka recibe eventos GPS continuamente y Spark procesa ubicaciones con baja latencia para mostrar posicion actual. |
| 2. Detectar conduccion peligrosa | Spark Structured Streaming/Flink + reglas o modelo ML + HBase/Redis | Permite evaluar velocidad, frenadas y patrones recientes por bus casi en tiempo real. |
| 3. Analizar historico de 2 anos | S3/MinIO o HDFS + Parquet + Spark/Hive | El historico requiere almacenamiento barato, escalable y analisis batch distribuido. |
| 4. Almacenar videos 30 dias | S3/MinIO con politicas de ciclo de vida | Los videos son archivos grandes no estructurados; conviene almacenamiento de objetos con retencion automatica. |

b) Para los datos GPS, ¿usarias HBase o HDFS? ¿Por que depende del caso de uso? Explica con un ejemplo concreto de cada caso de uso de GPS. (5 puntos)

**Respuesta b):**

Depende del caso. Para consultar la ultima ubicacion de un bus especifico usaria **HBase**, con una Row Key como `bus_id + timestamp`, porque permite acceso rapido por clave. Para analizar dos anos de rutas, velocidades promedio o patrones de retraso usaria **HDFS/S3 con Parquet**, porque es mas eficiente para escanear grandes volumenes y hacer agregaciones historicas con Spark.

c) ¿Los videos irian a HDFS, HBase o a un almacenamiento de objetos (S3/MinIO)? Justifica considerando el volumen (38 TB/dia x 30 dias = 1.15 PB). (5 puntos)

**Respuesta c):**

Los videos irian a **almacenamiento de objetos como S3 o MinIO**. El volumen aproximado de 1.15 PB en 30 dias requiere almacenamiento economico, escalable y con politicas de retencion. HBase no es adecuado para videos porque esta pensado para registros por fila/columna, no para archivos binarios enormes. HDFS podria almacenarlos, pero seria menos flexible para retencion, acceso desde aplicaciones y control de costos.

---

**21. Pregunta de diseno (8 puntos)**

*"¿Como implementarias un sistema de deteccion de fraude bancario en tiempo real usando componentes del ecosistema Hadoop/Cloud? El sistema debe analizar 10,000 transacciones por segundo y emitir una alerta en menos de 2 segundos si detecta un patron sospechoso."*

Describe:
- La arquitectura de componentes (que tecnologia en cada capa)
- Como fluyen los datos desde la transaccion hasta la alerta
- Por que el procesamiento batch tradicional (MapReduce) NO seria suficiente para este caso
- Que herramienta reemplazaria a MapReduce en este escenario

**Respuesta:**

Implementaria una arquitectura con **Kafka** como capa de ingestion de eventos, **Spark Structured Streaming** o **Apache Flink** como motor de procesamiento en tiempo real, una base de baja latencia como **HBase/Redis/Cassandra** para consultar historial reciente del cliente, y un servicio de alertas que notifique al sistema antifraude o bloquee temporalmente la operacion.

El flujo seria: la transaccion se genera en banca movil, POS o web; se publica como evento en Kafka; Spark/Flink consume el evento, aplica reglas y modelos de riesgo, consulta informacion historica o reciente del cliente, calcula un score y emite una alerta si supera el umbral. Luego la alerta se envia a un sistema operacional y el evento se guarda en un data lake para auditoria y entrenamiento posterior.

MapReduce batch no seria suficiente porque procesa por lotes y escribe resultados intermedios en disco, lo que no permite responder en menos de 2 segundos. En este escenario lo reemplazaria **Spark Structured Streaming** o **Apache Flink**, porque trabajan con flujos continuos y baja latencia.

---

**22. Pensamiento critico (7 puntos)**

*"¿Que pasaria si una empresa decide usar HBase para TODO su almacenamiento Big Data - tanto para analisis historico de 5 anos (petabytes) como para consultas en tiempo real - en lugar de usar HDFS para el historico y HBase para el tiempo real?"*

Analiza:
- ¿Es tecnicamente posible?
- ¿Cuales serian los problemas de rendimiento, costo y escalabilidad?
- ¿Cual seria el riesgo de este diseno en produccion?
- ¿Que evidencia de la sesion de clase apoya tu respuesta?

**Respuesta:**

Es tecnicamente posible guardar grandes volumenes en HBase, pero no seria una buena decision para todos los casos. HBase es fuerte para consultas rapidas por Row Key, pero no es la mejor herramienta para analisis historico masivo de petabytes, donde se requieren escaneos amplios, agregaciones y formatos optimizados para analitica.

Los problemas serian mayor costo operativo, complejidad de administracion, necesidad de disenar Row Keys cuidadosamente, riesgo de hotspots, compactaciones pesadas y bajo rendimiento en consultas historicas comparado con Parquet sobre HDFS/S3. Tambien podria afectar las consultas en tiempo real si la misma plataforma recibe cargas batch muy pesadas.

El riesgo en produccion seria crear una arquitectura monolitica dificil de escalar y optimizar. La evidencia de la sesion muestra que cada componente cumple un rol distinto: **HDFS/S3** para almacenamiento historico masivo, **Spark/Hive** para analitica distribuida y **HBase** para acceso aleatorio en tiempo real.

---

*Big Data DD283 | Universidad Autonoma del Peru | Semana 2 | 2026-1*
