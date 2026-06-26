# S3 — GUÍA DE TRABAJO DEL ESTUDIANTE
## Big Data DD283 | Universidad Autónoma del Perú | 2026-1
### Semana 3: Hadoop Mejoras + Sistemas NoSQL: Clasificación e Implementación

---

| Campo | Detalle |
|-------|---------|
| **Nombre del estudiante** | Javier Flores Condeña|
| **Código** | ______________________________________________ |
| **Sección** | Grupo 1 |
| **Fecha** |24/06/2026|
| **Tiempo estimado** | 90 minutos |
| **Puntaje total** | 100 puntos |

---

### INSTRUCCIONES GENERALES

- Lee cada enunciado con atención antes de responder.
- Esta guía evalúa los temas de la Semana 3: YARN, Hive, Impala, Ambari, NoSQL y el Teorema CAP.
- Tiempo recomendado: 90 minutos.
- Las secciones van de menor a mayor dificultad.
- En preguntas abiertas: responde en oraciones completas con argumentos técnicos.
- No hay respuestas en este documento — responde en el espacio indicado o en el documento que indique el docente.

---

## SECCIÓN A — PREGUNTAS DE OPCIÓN MÚLTIPLE (20 puntos | 2 pts c/u)

*Marca con X la alternativa correcta. Solo una es válida.*

---

**1.** ¿Cuál fue el problema principal del JobTracker en Hadoop 1.x que motivó la creación de YARN?

a) El JobTracker no soportaba el lenguaje Python para escribir jobs MapReduce  
b) El JobTracker mezclaba la gestión de recursos del clúster con la coordinación de jobs, convirtiéndose en cuello de botella y punto único de fallo  
c) El JobTracker solo podía gestionar un job MapReduce a la vez en todo el clúster  
d) El JobTracker no tenía interfaz gráfica para monitorear el estado de los nodos  

*Respuesta: b)*

---


**2.** Apache Hive traduce las consultas HiveQL en ¿qué tipo de trabajos distribuidos para ejecutarlas sobre HDFS?

a) Consultas SQL directas que corren en tiempo real sobre los DataNodes  
b) Jobs de Python que se distribuyen entre los DataNodes vía SSH  
c) Jobs MapReduce (o Tez/Spark en versiones modernas) que procesan los archivos de HDFS en paralelo  
d) Procedimientos almacenados en Java que se ejecutan en el NameNode  

*Respuesta: c)*

---

**3.** ¿Qué diferencia fundamental existe entre Apache Hive y Apache Impala en cuanto a su arquitectura de ejecución de consultas?

a) Hive usa SQL estándar e Impala usa un lenguaje de scripting propio llamado Pig Latin  
b) Hive compila las consultas en jobs MapReduce (alta latencia); Impala ejecuta SQL directamente en HDFS sin MapReduce (baja latencia, segundos)  
c) Hive solo funciona con datos estructurados, mientras Impala soporta JSON y XML  
d) Hive es de pago (Cloudera) e Impala es la versión gratuita open source  

*Respuesta: a)*

---

**4.** Apache Ambari fue diseñado principalmente para:

a) Almacenar datos no estructurados de forma distribuida en el ecosistema Hadoop  
b) Ejecutar consultas SQL interactivas sobre archivos en HDFS sin usar MapReduce  
c) Gestionar, monitorear e instalar componentes del ecosistema Hadoop desde una interfaz web centralizada  
d) Transferir datos de bases de datos relacionales a HDFS mediante conexiones JDBC  

*Respuesta: c)*

---

**5.** Según el Teorema CAP (Brewer, 2000), un sistema distribuido NO puede garantizar simultáneamente las tres propiedades. Si una empresa de telecomunicaciones necesita que el sistema de facturación nunca muestre montos incorrectos (aunque el sistema esté temporalmente no disponible), ¿qué combinación CAP debe elegir?

a) AP — Disponibilidad y Tolerancia a Particiones  
b) CA — Consistencia y Disponibilidad  
c) CP — Consistencia y Tolerancia a Particiones  
d) CAP — Las tres simultáneamente mediante replicación síncrona  

*Respuesta: c)*

---

**6.** ¿Cuál es la diferencia entre el modelo ACID y el modelo BASE en bases de datos?

a) ACID usa SQL y BASE usa Python; son lenguajes de consulta distintos  
b) ACID garantiza consistencia estricta en transacciones (apropiado para bancos); BASE acepta consistencia eventual a favor de alta disponibilidad (apropiado para redes sociales)  
c) ACID solo funciona en bases de datos locales; BASE solo funciona en bases de datos distribuidas en la nube  
d) ACID es el modelo de NoSQL y BASE es el modelo relacional tradicional  

*Respuesta: b)*

---

**7.** Una empresa de streaming de música necesita almacenar el perfil de 50 millones de usuarios donde cada usuario puede tener atributos completamente diferentes (algunos tienen listas de reproducción, otros favoritos, otros historial de podcasts, con esquemas variables). ¿Qué tipo de base de datos NoSQL es más adecuada?

a) Key-Value (Redis) — porque permite acceso ultrarápido por clave de usuario  
b) Document (MongoDB) — porque cada documento puede tener estructura diferente sin esquema fijo  
c) Column-family (Cassandra) — porque está optimizada para escrituras masivas en tiempo real  
d) Graph (Neo4j) — porque permite modelar las relaciones entre usuarios y canciones  

*Respuesta: b)*

---

**8.** ¿Cuál es la principal ventaja de Apache Cassandra frente a MongoDB para almacenar el historial de llamadas de una operadora con 2,000 millones de registros al año?

a) Cassandra tiene una interfaz SQL más intuitiva que MongoDB para analistas de negocio  
b) Cassandra permite esquemas más flexibles que MongoDB para datos con atributos variables  
c) Cassandra está optimizada para escrituras masivas y continuas con acceso predecible por partition key + timestamp, sin punto único de fallo  
d) Cassandra soporta transacciones ACID completas, mientras MongoDB solo tiene consistencia eventual  

*Respuesta: c)*

---

**9.** Sqoop es una herramienta del ecosistema Hadoop diseñada para:

a) Monitorear la salud de los DataNodes y alertar cuando alguno falla  
b) Ejecutar consultas SQL interactivas sobre datos almacenados en HDFS  
c) Transferir datos en batch entre bases de datos relacionales (Oracle, MySQL) y HDFS en ambas direcciones  
d) Gestionar la seguridad y autenticación de usuarios en el clúster Hadoop  

*Respuesta: c)*

---

**10.** Una startup peruana lanza una app de redes sociales. Al inicio tienen 10,000 usuarios. Proyectan 5 millones en 12 meses. El perfil de cada usuario incluye fotos, listas de amigos, publicaciones con diferentes formatos (texto, imagen, video, encuesta). ¿Qué argumento técnico justifica usar MongoDB en lugar de PostgreSQL desde el inicio?

a) MongoDB es más rápido en todas las operaciones, incluyendo transacciones financieras, sin importar el volumen  
b) MongoDB permite escalar horizontalmente con sharding automático y soporta esquemas flexibles que se adaptan a los distintos tipos de contenido sin costosas migraciones de esquema  
c) PostgreSQL no soporta datos de tipo JSON, por lo que no puede almacenar publicaciones de redes sociales  
d) MongoDB incluye un motor de búsqueda de texto completo que PostgreSQL no tiene en ninguna versión  

*Respuesta: b)*

---

## SECCIÓN B — COMPLETAR Y RELACIONAR (20 puntos)

### B1. Completa los espacios en blanco (10 puntos | 2 pts c/u)

**11.** En la arquitectura YARN, el componente _ResourceManager_ gestiona los recursos del clúster (CPU, RAM) a nivel global, mientras que el _ApplicationMaster_ coordina la ejecución de cada aplicación individual en los nodos del clúster.

**12.** El Teorema CAP establece que un sistema distribuido solo puede garantizar dos de tres propiedades simultáneamente: _Consistencia_ (todos los nodos ven los mismos datos), _Disponibilidad__ (el sistema siempre responde), y Tolerancia a Particiones (el sistema funciona aunque la red falle).

**13.** En MongoDB, los datos se organizan en _colecciones_ (equivalente a una tabla SQL), que contienen _documentos_ (equivalente a filas) en formato JSON/BSON, donde cada uno puede tener una estructura diferente.

**14.** Apache _Pig_ traduce un lenguaje de scripting llamado "Pig Latin" en jobs MapReduce, mientras que Apache _Hive_ traduce consultas en un dialecto SQL propio (HiveQL) en jobs MapReduce o Spark.

**15.** La herramienta _Sqoop_ (SQL-to-Hadoop) permite importar datos de una base de datos MySQL a HDFS de forma paralela usando múltiples conexiones JDBC simultáneas.

---

### B2. Relacionar columnas (10 puntos | 1 pt c/par correcto)

Relaciona cada tecnología/concepto (columna A) con su descripción correcta (columna B):

| N° | Columna A | Letra | Columna B |
|----|-----------|-------|-----------|
| 1 | Redis |D| A | Motor SQL interactivo de Cloudera que ejecuta consultas directamente sobre HDFS sin MapReduce |
| 2 | Apache Cassandra | E | B | Base de datos de grafos optimizada para navegar relaciones complejas en milisegundos |
| 3 | Impala | A | C | Herramienta de gestión de clúster Hadoop con interfaz web (instala, monitorea, configura servicios) |
| 4 | Neo4j | B | D | Base de datos Key-Value en memoria con latencia < 1ms, usada para caché de sesiones |
| 5 | Ambari | C | E | Base de datos columnar distribuida sin maestro (ring), optimizada para escrituras masivas |
| 6 | Dremel | F | F | Tecnología de Google que inspira los formatos de almacenamiento columnar y BigQuery |
| 7 | Apache Drill | G | G | Motor SQL schema-free que consulta HDFS, MongoDB, S3 y otros sin esquema previo |
| 8 | MongoDB | H | H | Base de datos NoSQL documental con esquema flexible (BSON/JSON), más usada mundialmente |
| 9 | Tez | I | I | Framework de procesamiento DAG que reemplaza MapReduce como motor de ejecución de Hive |
| 10 | Flume | J | J | Herramienta de ingesta de logs/eventos en streaming hacia HDFS o Kafka |

---

## SECCIÓN C — ANÁLISIS Y REFLEXIÓN (30 puntos)

*Responde con oraciones completas y argumentos técnicos. Extensión: 3-5 líneas por pregunta.*

---

**16. (8 puntos)** El Ministerio de Salud (MINSA) del Perú quiere modernizar su sistema de información para el programa de Vigilancia Epidemiológica. El sistema debe:
- Almacenar reportes de casos de enfermedades de 8,000 establecimientos de salud a nivel nacional
- Cada reporte tiene campos variables (dengue tiene campos de serotipos; COVID tenía campos de variante; hepatitis tiene campos de cronología de vacunas)
- Permitir consultas como "¿cuántos casos de dengue hubo en Loreto en la semana 23?"
- Responder en menos de 2 segundos para el dashboard del epidemiólogo

a) ¿Qué tipo de base de datos NoSQL recomendarías para almacenar los reportes? Justifica con al menos 2 razones técnicas relacionadas al caso.

*Recomendaría MongoDB porque permite almacenar documentos con estructuras variables para diferentes enfermedades. Además, ofrece flexibilidad de esquema y escalabilidad horizontal para manejar información proveniente de miles de establecimientos de salud.*

b) ¿Qué componente del ecosistema Hadoop usarías para las consultas analíticas del dashboard? ¿Hive, Impala/Spark SQL, o HBase? Justifica.

*Utilizaría Impala o Spark SQL porque proporcionan consultas analíticas de baja latencia y tiempos de respuesta cercanos al tiempo real, ideales para realizar dashboards ejecutivos.*

---

**17. (8 puntos)** Compara el paradigma ACID de las bases de datos relacionales con el paradigma BASE de las bases de datos NoSQL. Luego responde:

a) ¿En qué tipo de aplicaciones es OBLIGATORIO usar ACID y por qué? 

*En sistemas bancarios, financieros, pagos electrónicos y contabilidad, porque cualquier inconsistencia puede generar pérdidas económicas o errores críticos.*
 
b) ¿En qué tipo de aplicaciones es ACEPTABLE y BENEFICIOSO usar BASE y por qué?  

*En redes sociales, plataformas multimedia y aplicaciones masivas donde es más importante mantener disponibilidad que consistencia inmediata.*

c) ¿Existe algún sistema de bases de datos que combine ambos paradigmas? ¿Cuál es su nombre y cómo lo logra?

*Sí. Google Spanner, CockroachDB y MongoDB ofrecen mecanismos que combinan escalabilidad distribuida y propiedades ACID.*

---

**18. (6 puntos) — Mini caso de análisis:**

*La plataforma de e-commerce "CompraYa Perú" tiene estos componentes en su sistema:*
- *Catálogo: 2 millones de productos con atributos variables (electrónicos tienen voltaje, ropa tiene talla, alimentos tienen fecha de vencimiento)*
- *Carrito de compras: almacena el carrito activo de 200K usuarios simultáneos (expira en 2 horas si no compran)*
- *Órdenes de compra: cada orden debe debitarse exactamente una vez de la cuenta del usuario (si el pago falla, no debe cobrarse)*
- *Historial de navegación: registra cada producto visto por cada usuario (50M eventos/día para recomendaciones)*

a) Para cada componente, identifica el tipo de base de datos más adecuado (SQL, MongoDB, Redis, Cassandra) y justifica brevemente cada elección.

| Componente | Tecnología | Justificación |
|------------|------------|---------------|
| Catálogo | MongoDB | Esquema flexible |
| Carrito | Redis | Acceso rápido y expiración automática |
| Órdenes | SQL | Transacciones ACID |
| Historial | Cassandra | Escrituras masivas |

b) ¿Es correcto usar UNA SOLA base de datos para todo el sistema? Argumenta si la arquitectura polilíngüe (polyglot persistence) es mejor o peor aquí.

*No es recomendable utilizar una sola base de datos. La estrategia Polyglot Persistence permite optimizar cada componente utilizando la tecnología más adecuada para sus necesidades específicas.*

---

**19. (8 puntos)** Explica por qué Apache Pig (2008) fue un paso importante en la evolución del ecosistema Hadoop, y luego explica por qué la industria lo abandonó en favor de Apache Spark (2014). ¿Qué característica de Pig sobrevivió en Spark? ¿Qué limitación eliminó Spark?

*Apache Pig fue importante porque permitió simplificar la programación de procesos distribuidos mediante Pig Latin. Posteriormente fue reemplazado por Apache Spark debido a su mayor velocidad gracias al procesamiento en memoria. Spark conservó la abstracción de la complejidad distribuida y eliminó la alta latencia de MapReduce.*

---

## SECCIÓN D — PREGUNTAS AVANZADAS Y DE CASO (30 puntos)

---

**20. Caso profesional real (15 puntos)**

*Eres el Data Architect de Interbank. El banco tiene 3.5 millones de clientes con las siguientes necesidades de datos:*

*Sistema 1 — Core bancario (transacciones):* 5 millones de transacciones diarias (depósitos, retiros, transferencias). Cada transacción debe procesarse exactamente una vez. Si el sistema falla a mitad de una transferencia, el dinero no puede perderse ni duplicarse.

*Sistema 2 — App móvil (perfil del cliente):* Cuando el cliente abre la app, ve su saldo, últimas 5 transacciones y ofertas personalizadas. El tiempo de carga aceptable es 300ms. En días de pago (quincena, fin de mes), hay 800K logins simultáneos.

*Sistema 3 — Motor de recomendaciones:* El banco quiere mostrar "Productos que te pueden interesar" basado en el perfil financiero del cliente. El modelo necesita analizar historial de 5 años de transacciones de 3.5M clientes (75TB de datos) cada semana para re-entrenar el modelo.

*Sistema 4 — Detección de redes de fraude:* Algunos clientes crean redes de cuentas para mover dinero ilícito. El banco necesita detectar cuando una transacción forma parte de un ciclo: A → B → C → A en menos de 5 minutos.

Responde:

a) Para cada sistema (1, 2, 3, 4), ¿qué tecnología de almacenamiento/procesamiento utilizarías? Crea una tabla con: Sistema | Tecnología | Tipo (SQL/NoSQL/qué tipo) | Justificación técnica específica (3 líneas por sistema) (8 puntos)

| Sistema | Tecnología | Tipo | Justificación |
|----------|------------|------|---------------|
| Core Bancario | PostgreSQL u Oracle | SQL | Garantiza ACID y consistencia estricta |
| App Móvil | Redis + SQL | Mixto | Baja latencia para consultas frecuentes |
| Recomendaciones | Hadoop + Spark | Big Data | Procesamiento distribuido de 75 TB |
| Fraude | Neo4j | Grafo | Detección rápida de relaciones y ciclos |

b) Aplica el Teorema CAP a los Sistemas 1 y 2 específicamente. ¿Cuál combinación CAP debe tener cada uno y por qué? Da un ejemplo de qué pasaría si eligieras la combinación incorrecta. (4 puntos)

- Sistema 1: CP. Porque la consistencia es prioritaria.

- Sistema 2: AP. Porque la disponibilidad es prioritaria.

*Una elección incorrecta podría ocasionar saldos erróneos o indisponibilidad masiva de usuarios.*


c) En el Sistema 3 (recomendaciones), el equipo de ML propone usar un archivo CSV de 75 TB almacenado en el servidor local del equipo para entrenar el modelo semanalmente. ¿Qué argumentas tú como Data Architect en contra de esta propuesta? ¿Qué propones en su lugar? (3 puntos)

*Un archivo CSV de 75 TB en un servidor local no escala adecuadamente. Es preferible utilizar HDFS y Spark para distribuir el almacenamiento y procesamiento.*

---

**21. Pregunta de diseño (8 puntos)**

*"¿Cómo implementarías una base de datos NoSQL para el sistema de seguimiento de paquetes de Olva Courier Perú? El sistema debe: (a) registrar cada evento de cada paquete (recepción, en tránsito, en distribución, entregado) en tiempo real; (b) permitir al cliente consultar 'dónde está mi paquete' por número de guía en menos de 100ms; (c) guardar historial de los últimos 2 años (150M paquetes × 8 eventos = 1.2B eventos)."*

Diseña:
- El tipo de NoSQL elegido y justificación

*Tipo de NoSQL: Cassandra.*

- El modelo de datos (cómo organizarías los documentos/columnas/claves)

*Partition Key = número de guía.*

*Clustering Key = fecha/hora del evento.*

- La consulta que usarías para responder "¿dónde está el paquete #PE123456?"

SELECT * FROM paquetes WHERE guia='PE123456';

- Por qué esta solución es mejor que usar una tabla SQL con índices

*Porque la solución escala horizontalmente y soporta miles de millones de eventos con alta disponibilidad.*
---

**22. Pensamiento crítico (7 puntos)**

*"¿Qué pasaría si MongoDB Atlas (la plataforma cloud de MongoDB) tiene una caída de servicio de 2 horas durante el horario pico de tu aplicación? ¿Qué riesgos concretos implica depender de una sola base de datos NoSQL en la nube para una aplicación crítica como la app de Claro Perú?"*

Analiza:
- ¿Qué componentes de la app dejarían de funcionar?

*Una caída de MongoDB Atlas afectaría autenticación, perfiles de usuarios, consultas y operaciones críticas.*

- ¿Qué estrategias de resiliencia implementarías para mitigar el riesgo?

**Para mitigar riesgos se recomienda:**

    - Replicación multirregión.
    - Backups automáticos.
    - Failover automático.
    - Arquitectura multi-cloud cuando sea necesario.

- ¿Es mejor tener múltiples proveedores de NoSQL o un solo proveedor con alta disponibilidad configurada?

*En la mayoría de los casos es mejor contar con un único proveedor bien configurado con alta disponibilidad, ya que reduce la complejidad operativa y los costos. Sin embargo, para aplicaciones extremadamente críticas, una estrategia multi-cloud puede ofrecer mayor resiliencia frente a fallas masivas de un proveedor.*

- ¿Qué nivel de SLA (Service Level Agreement) deberías negociar con MongoDB Atlas?

*El SLA recomendado para una aplicación crítica es superior a 99.95%.*

---

*Big Data DD283 | Universidad Autónoma del Perú | Semana 3 | 2026-1*
*Guía de trabajo — NO incluye respuestas*
