# GUÍA DE TRABAJO — SEMANA 1
## Big Data (DD283) | Universidad Autónoma del Perú

**Nombre(s)**: Tolentino Vargas Jesus Antonio    
**Grupo de proyecto**: 02 
**Fecha de entrega**: Antes de la sesión de la Semana 2  
**Modalidad**: Individual  
**Puntaje**: 20 puntos (2 puntos por pregunta)

---

> **Instrucciones**: Responde cada pregunta con tus propias palabras. No copies y pegues definiciones de internet — el objetivo es que construyas TU comprensión del tema. Se valorará la conexión con ejemplos reales de tu entorno laboral.

---

## PARTE 1: CONCEPTOS FUNDAMENTALES DE BIG DATA (10 preguntas)

### Pregunta 1
Define Big Data con tus propias palabras. ¿Cuál es la diferencia fundamental entre Big Data y una base de datos tradicional como SQL Server o MySQL que probablemente usas en tu empresa?

_Respuesta_:  
```
Big Data es el conjunto de tecnologías, metodologías y prácticas diseñadas para capturar, 
almacenar, procesar y analizar volúmenes de datos que superan la capacidad de las herramientas 
tradicionales. 

La diferencia fundamental con una base de datos tradicional como SQL Server o MySQL es:

- Escala: SQL Server está pensado para millones de registros en tablas estructuradas. 
  Big Data maneja billones de registros de todo tipo (texto, imágenes, audio, logs).

- Estructura: En SQL todo debe caber en tablas con columnas fijas (esquema rígido). 
  Big Data puede trabajar con datos sin estructura definida (schema-on-read).

- Procesamiento: SQL Server procesa en un solo servidor. Big Data distribuye el trabajo 
  en decenas o cientos de máquinas en paralelo (clústeres).

- Velocidad de ingesta: MySQL no está diseñado para recibir millones de eventos por segundo 
  en tiempo real. Big Data usa herramientas como Kafka o Spark Streaming para eso.

En mi trabajo actual en COEZ PERÚ, usamos registros estructurados de producción (partidas, 
avances, metrados) que perfectamente caben en una base SQL. Pero si quisiéramos cruzar esos 
datos con imágenes de obra, reportes PDF, logs de acceso biométrico y datos climáticos en 
tiempo real, ahí ya necesitaríamos una arquitectura Big Data.
```

---

### Pregunta 2
Explica las **5 V's del Big Data** con un ejemplo de tu propia empresa o de una empresa peruana que conozcas. Completa la siguiente tabla:

| V | Definición con tus palabras | Ejemplo de tu empresa/empresa conocida |
|---|---------------------------|---------------------------------------|
| Volumen |Cantidad masiva de datos generados que supera la capacidad de almacenamiento y procesamiento tradicional | Claro Perú genera millones de registros de llamadas, SMS y datos móviles por día de sus más de 10 millones de clientes|
| Velocidad | Rapidez con la que los datos se generan, procesan y necesitan estar disponibles|En Claro, cada transacción de recarga o consumo de datos debe registrarse en tiempo real para el control de saldo del cliente |
| Variedad | Diversidad de formatos y fuentes de datos: estructurados, semiestructurados y no estructurados| Claro maneja CDRs (registros de llamadas en CSV), contratos en PDF, grabaciones de llamadas al call center, tickets de atención en JSON y publicaciones en redes sociales|
| Veracidad |Confiabilidad y calidad de los datos; no todos los datos capturados son correctos o completos | En Claro, un cliente puede figurar con dirección desactualizada o doble registro; datos incorrectos llevan a campañas de retención mal dirigidas|
| Valor |Capacidad de extraer información útil y accionable de los datos para tomar decisiones de negocio |Claro puede predecir qué clientes tienen alta probabilidad de cancelar su plan y ofrecerles una promoción antes de que se vayan, reduciendo el churn |

---

### Pregunta 3
¿Por qué una empresa como BCP (Banco de Crédito del Perú) NO podría usar solo una base de datos Oracle tradicional para procesar todos sus datos de transacciones en tiempo real? Menciona al menos 3 razones técnicas y 1 razón de negocio.

_Respuesta_:  
```
El BCP tiene más de 11 millones de clientes y procesa millones de transacciones diarias 
(pagos, transferencias, retiros, compras con tarjeta). Una base de datos Oracle tradicional 
no sería suficiente por las siguientes razones:

RAZONES TÉCNICAS:

1. Límite de escalabilidad vertical: Oracle escala agregando más RAM o CPU a un solo servidor 
   (escalamiento vertical), pero este tiene un techo físico y económico. Big Data escala 
   horizontalmente agregando más nodos al clúster, sin límite práctico.

2. Procesamiento batch vs. tiempo real: Oracle está optimizado para consultas transaccionales 
   (OLTP) o analíticas (OLAP) en lotes. Detectar fraude en una transacción con tarjeta 
   requiere procesar el evento en milisegundos mientras ocurre, lo que requiere herramientas 
   como Apache Kafka + Spark Streaming.

3. Variedad de datos no soportada: Las transacciones bancarias modernas incluyen metadatos 
   de geolocalización, fotos de vouchers, audios de banca telefónica y logs de aplicación 
   móvil. Oracle no está diseñado para almacenar y procesar eficientemente este tipo de 
   datos no estructurados a escala.

RAZÓN DE NEGOCIO:

4. Costo y tiempo de respuesta al mercado: Mantener un único Oracle empresarial de alta 
   disponibilidad capaz de soportar millones de transacciones simultáneas costaría decenas 
   de millones de dólares en licencias y hardware. Una arquitectura Big Data en la nube 
   (AWS, Azure) permite pagar solo por lo que se usa y escalar en minutos durante picos 
   como campañas de Cyber Wow o pago de CTS, manteniendo la competitividad del banco.
```

---

### Pregunta 4
Clasifica los siguientes tipos de datos como **Estructurado**, **Semi-estructurado** o **No estructurado**. Justifica tu respuesta:

| Dato | Clasificación | Justificación |
|------|-------------|--------------|
| Un archivo Excel con ventas mensuales | Estructurado|Tiene filas y columnas definidas, esquema fijo, cada celda corresponde a un campo específico |
| Un tweet sobre el precio del dólar |Semi-Estructurado|Tiene campos definidos (autor, fecha, texto, hashtags) pero el contenido del texto es libre y variable |
| Una foto del ticket de compra en Metro |No estructurado |Es una imagen binaria sin campos predefinidos; requiere OCR para extraer información |
| Un archivo JSON de la API de SUNAT | Semi-estructurado|Tiene jerarquía y etiquetas definidas (claves JSON) pero no sigue un esquema de tabla relacional |
| Un audio de una llamada al call center de Claro | No estructurado| Es un archivo de audio sin estructura predefinida; requiere procesamiento de voz (STT) para extraer datos|
| Un archivo CSV de exportaciones del BCRP |Estructurado|Filas y columnas con separador definido, esquema fijo y campos predecibles |
| Un video de seguridad de un supermercado |No Estructurado |Flujo continuo de imágenes binarias sin metadatos de contenido; requiere visión computacional para analizarlo |
| Un log de errores de un servidor web |Semi - Estructurado| Tiene un patrón repetitivo (fecha, nivel, mensaje) pero el campo de mensaje es texto libre y variable |

---

### Pregunta 5
¿Qué es un **clúster** en el contexto de Big Data? ¿Cuál es la diferencia entre un sistema de **memoria compartida** y un sistema de **memoria distribuida**? Usa un diagrama o esquema para explicarlo.

_Respuesta_:  
```
Un CLÚSTER en Big Data es un conjunto de computadoras (nodos) interconectadas que trabajan 
en conjunto como si fueran un solo sistema. Cada nodo aporta su CPU, RAM y almacenamiento 
al pool total. El objetivo es dividir el trabajo de procesamiento y almacenamiento entre 
todos los nodos para manejar datos a escala que un solo servidor no podría.

MEMORIA COMPARTIDA vs. MEMORIA DISTRIBUIDA:

┌─────────────────────────────────────────────────────────────┐
│              MEMORIA COMPARTIDA                             │
│                                                             │
│   CPU 1 ──┐                                                 │
│   CPU 2 ──┼──► [ RAM COMPARTIDA ] ◄── Todos acceden        │
│   CPU 3 ──┘       (un solo pool)       al mismo espacio     │
│                                                             │
│   Ejemplo: Un servidor de 64 núcleos con 512 GB de RAM      │
│   Limitación: El hardware tiene un techo físico (y de $)    │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│              MEMORIA DISTRIBUIDA                            │
│                                                             │
│   [ Nodo 1: CPU + RAM propia ] ──┐                          │
│   [ Nodo 2: CPU + RAM propia ] ──┼──► Red de comunicación   │
│   [ Nodo 3: CPU + RAM propia ] ──┘    (Ethernet/InfiniBand) │
│                                                             │
│   Cada nodo tiene su propia memoria, no la comparte         │
│   Se comunican enviando mensajes por la red                  │
│   Ejemplo: Clúster Hadoop con 50 nodos commodity            │
│   Ventaja: Escala agregando más nodos sin límite práctico   │
└─────────────────────────────────────────────────────────────┘

Big Data usa principalmente memoria distribuida porque permite escalar horizontalmente 
a bajo costo usando servidores estándar (commodity hardware).
```

---

### Pregunta 6
Investiga y responde: ¿Qué empresa latinoamericana (puede ser peruana) ha implementado Big Data de manera exitosa? Describe:
- El problema que tenían
- La solución Big Data que implementaron
- Los resultados que obtuvieron

_Fuente consultada (URL o libro)_: https://aws.amazon.com/es/solutions/case-studies/mercadolibre/

_Respuesta_:  
```
EMPRESA: MercadoLibre (operaciones en Perú y toda Latinoamérica)

PROBLEMA:
MercadoLibre es el marketplace más grande de Latinoamérica, con operaciones en 18 países 
incluido Perú. Su principal problema era la detección de fraude en transacciones de 
MercadoPago en tiempo real. Con millones de transacciones diarias, el sistema tradicional 
no podía evaluar el riesgo de cada pago en milisegundos sin frenar la experiencia del 
usuario. Adicionalmente, necesitaban personalizar las recomendaciones de productos para 
cada uno de sus más de 100 millones de usuarios activos.

SOLUCIÓN BIG DATA:
MercadoLibre implementó una arquitectura Big Data sobre AWS que incluye:
- Apache Kafka para ingesta de eventos de transacciones en tiempo real
- Amazon EMR (Elastic MapReduce con Spark) para procesamiento distribuido
- Modelos de Machine Learning entrenados sobre histórico de transacciones para 
  scoring de fraude en tiempo real (menos de 500ms por transacción)
- Data Lake en Amazon S3 para almacenar todos los eventos de navegación, 
  compra y pago de los usuarios
- Amazon Redshift como Data Warehouse para análisis de negocio

RESULTADOS:
- Reducción del fraude en un 30% manteniendo la tasa de aprobación de pagos
- Tiempo de evaluación de riesgo por transacción menor a 500 milisegundos
- Recomendaciones personalizadas que incrementaron el CTR (click-through rate) 
  de productos recomendados en más de 20%
- Capacidad de procesar picos de hasta 50,000 transacciones por segundo durante 
  eventos como Cyber Monday sin degradación del servicio

Este caso es relevante para el contexto peruano porque MercadoLibre opera 
activamente en Perú y sus soluciones de fraude protegen también a los 
compradores y vendedores peruanos.
```

---

### Pregunta 7
Explica la diferencia entre **Data Lake** y **Data Warehouse**. ¿En qué situación usarías cada uno? Da un ejemplo de negocio para cada caso.

| | Data Lake | Data Warehouse |
|--|----------|---------------|
| Definición |Repositorio centralizado que almacena datos en su formato original (raw), sin transformar, de cualquier tipo y fuente|Repositorio optimizado para análisis, donde los datos ya fueron limpiados, transformados y estructurados en esquemas predefinidos|
| Tipo de datos |Estructurados, semi-estructurados y no estructurados (imágenes, logs, JSON, CSV, audio, video)|Principalmente estructurados, organizados en tablas relacionales con esquema fijo|
| Cuándo usarlo |Cuando se necesita almacenar grandes volúmenes de datos sin saber aún cómo se van a usar, o para exploración y ciencia de datos|Cuando se necesitan reportes y dashboards con consultas repetitivas, rápidas y predecibles sobre datos ya conocidos|
| Ejemplo de negocio |Claro Perú guarda en un Data Lake todos los logs de red, grabaciones de llamadas, tickets de soporte y eventos de app en bruto para que los data scientists los exploren|El área financiera de Claro consulta el Data Warehouse para generar el reporte mensual de ingresos por tipo de plan, ya procesado y limpio|
| Herramienta típica |Amazon S3 + Apache Hadoop, Azure Data Lake Storage, Google Cloud Storage|Amazon Redshift, Google BigQuery, Snowflake, Azure Synaps|

---

### Pregunta 8
¿Qué son los **requisitos de un sistema Big Data**? Identifica y explica los 5 requisitos principales que debe cumplir una arquitectura Big Data robusta. Para cada uno, menciona qué pasa si ese requisito NO se cumple.

_Respuesta_:  
```
Los requisitos de un sistema Big Data son las características mínimas que debe cumplir 
la arquitectura para manejar datos masivos de manera confiable y útil para el negocio.

1. ESCALABILIDAD
   Definición: El sistema debe poder crecer (más datos, más usuarios, más velocidad) 
   agregando recursos sin rediseñar la arquitectura.
   Si NO se cumple: El sistema colapsa en picos de demanda (como pagos de fin de mes 
   en una telco) y hay que migrarlo completo cuando se queda pequeño.

2. TOLERANCIA A FALLOS (Fault Tolerance)
   Definición: Si un nodo del clúster falla, el sistema debe continuar operando 
   sin pérdida de datos ni interrupción del servicio.
   Si NO se cumple: Una falla de hardware en un servidor detiene todo el procesamiento 
   y se pierden datos críticos que ya llegaron al sistema.

3. PROCESAMIENTO EN TIEMPO REAL (Baja latencia)
   Definición: Capacidad de procesar y responder a eventos casi en el instante 
   en que ocurren (milisegundos a segundos).
   Si NO se cumple: La detección de fraude bancario que tarda 10 minutos en vez de 
   500ms es inútil; la transacción fraudulenta ya se aprobó.

4. CONSISTENCIA Y CALIDAD DE DATOS
   Definición: Los datos almacenados y procesados deben ser confiables, sin duplicados 
   ni corrupción, y coherentes entre todos los nodos del clúster.
   Si NO se cumple: Los reportes generan cifras contradictorias según qué nodo 
   responde la consulta, y las decisiones de negocio se basan en datos incorrectos.

5. SEGURIDAD Y GOBERNANZA
   Definición: Control de quién accede a qué datos, cifrado en tránsito y en reposo, 
   y cumplimiento de normativas de privacidad (como la Ley 29733 en Perú).
   Si NO se cumple: Datos personales de clientes quedan expuestos, generando multas 
   regulatorias y pérdida de confianza de los usuarios.
```

---

### Pregunta 9
La empresa en la que trabajas actualmente, ¿tiene algún problema de datos que podría resolverse con Big Data? Describe:
- El problema o necesidad
- Qué tipo de datos implicaría (V's del Big Data)
- Una propuesta inicial de solución (aunque sea básica)

*(Si no puedes compartir información de tu empresa por confidencialidad, usa una empresa pública del sector)*

_Respuesta_:  
```
Trabajo en COEZ PERÚ E.I.R.L., empresa subcontratista ejecutando instalaciones eléctricas, 
mecánicas y civiles en el proyecto de construcción I.E. N° 159 Glorioso 10 de Octubre 
(proyecto PRONIED/MINEDU con contratista principal CCECC).

PROBLEMA O NECESIDAD:
El control de producción en obra se hace actualmente de manera manual y fragmentada: 
avances físicos en planillas Excel, comunicaciones técnicas en correo, fotografías de 
obra sin catalogar, reportes de SSOMA en formatos distintos, y registros de ingreso de 
personal en papel o sistemas desconectados. No existe visibilidad en tiempo real del 
avance vs. lo planificado, ni alertas tempranas cuando una partida se desvía del 
cronograma. Con 488 partidas en 4 activos simultáneos, la coordinación manual genera 
retrasos en la toma de decisiones.

TIPO DE DATOS (V's DEL BIG DATA):
- Volumen: Registros diarios de avance de 488 partidas × 4 activos × duración del proyecto
- Variedad: Datos estructurados (metrados Excel), semi-estructurados (correos técnicos, 
  JSON de API), no estructurados (fotos de obra, PDFs de submittals, planos DWG)
- Velocidad: Registros de asistencia biométrica en tiempo real, alertas de SSOMA inmediatas
- Veracidad: Datos de avance reportados por distintos maestros de obra con criterios distintos
- Valor: Predecir partidas en riesgo de atraso antes de que impacten la ruta crítica

PROPUESTA INICIAL DE SOLUCIÓN:
1. Data Lake en la nube (Azure o AWS) para centralizar todos los tipos de datos del proyecto
2. Pipeline de ingesta automática desde el sistema de control de asistencia biométrica 
   y desde las planillas de avance diario
3. Dashboard en Power BI conectado al Data Lake para visualización en tiempo real del 
   avance vs. programado por partida, activo y semana
4. Modelo predictivo básico (regresión) que identifique partidas con tendencia de atraso 
   con 3 días de anticipación para activar alertas al Ingeniero Residente
```

---

### Pregunta 10
**Análisis crítico**: Lee el siguiente caso y responde las preguntas:

> "Una empresa de telecomunicaciones en Perú tiene 8 millones de clientes. Cada cliente genera en promedio 500 registros de datos al día (llamadas, SMS, datos móviles, pagos). La empresa quiere predecir qué clientes cancelarán su contrato en los próximos 30 días para ofrecerles retención proactiva."

**a)** ¿Cuántos registros se generan por día? ¿Por año?  
**b)** ¿Qué tipo de datos están involucrados?  
**c)** ¿Cuáles de las 5 V's son más relevantes en este caso?  
**d)** ¿Qué tecnologías Big Data necesitarían para resolver este problema?  
**e)** ¿Qué impacto ético podría tener esta solución? (pista: privacidad de datos)

_Respuesta_:  
```
a) VOLUMEN DE REGISTROS:
   Por día:  8,000,000 clientes × 500 registros = 4,000,000,000 (4 mil millones de registros/día)
   Por año:  4,000,000,000 × 365 = 1,460,000,000,000 (1.46 billones de registros/año)
   
   Asumiendo ~200 bytes por registro:
   Por día:  4B × 200B = ~800 GB/día
   Por año:  ~292 TB/año
   Esto confirma que es imposible manejarlo con una base de datos tradicional.

b) TIPO DE DATOS INVOLUCRADOS:
   - Estructurados: CDRs de llamadas (fecha, duración, destino, costo), registros de 
     pagos (monto, fecha, canal), consumo de datos en MB por día
   - Semi-estructurados: Tickets de atención al cliente en JSON, interacciones con 
     app móvil en logs, respuestas a encuestas NPS
   - No estructurados: Grabaciones de llamadas al call center, mensajes de chat 
     con agentes virtuales, historial de navegación web

c) V's MÁS RELEVANTES:
   - VOLUMEN: 4 mil millones de registros diarios hacen imposible el procesamiento 
     en un sistema tradicional
   - VELOCIDAD: Los patrones de uso cambian hora a hora; el modelo debe actualizarse 
     frecuentemente para ser predictivo y no reactivo
   - VARIEDAD: Los datos vienen de múltiples sistemas (red, billing, CRM, app) 
     en formatos distintos que deben integrarse
   - VALOR: Es la V más importante para el negocio; sin extraer valor (predicción 
     de churn) los datos son solo costo de almacenamiento

d) TECNOLOGÍAS BIG DATA NECESARIAS:
   - Ingesta: Apache Kafka (streaming de eventos en tiempo real)
   - Almacenamiento: Data Lake en Amazon S3 o Azure Data Lake
   - Procesamiento batch: Apache Spark con PySpark para entrenar modelos
   - Procesamiento streaming: Spark Streaming para scoring en tiempo real
   - Machine Learning: MLlib (Spark) o scikit-learn para modelo de clasificación 
     de churn (Random Forest, XGBoost)
   - Orquestación: Apache Airflow para automatizar pipelines
   - Visualización: Power BI o Tableau para dashboards de retención
   - Nuestro proyecto del grupo (g1-churn-telecom-b2b) trabaja exactamente este caso

e) IMPACTO ÉTICO:
   - Privacidad de datos: Analizar el comportamiento detallado de 8 millones de 
     personas implica procesar datos personales sensibles. En Perú, la Ley N° 29733 
     (Ley de Protección de Datos Personales) exige consentimiento informado para 
     el tratamiento de datos con fines de perfilamiento comercial.
   - Discriminación algorítmica: Si el modelo aprende que ciertos segmentos 
     socioeconómicos tienen mayor churn, podría llevar a ofrecer mejores promociones 
     solo a clientes de mayor valor, generando inequidad en el servicio.
   - Transparencia: Los clientes identificados como "en riesgo de churn" no saben 
     que están siendo perfilados; esto genera una asimetría de información.
   - Uso secundario de datos: Los datos recolectados para facturación se usan para 
     predicción de comportamiento, lo cual puede no estar contemplado en los 
     términos y condiciones originales del contrato.
```

---

## PARTE 2: REFLEXIÓN Y CONEXIÓN CON TU PROYECTO (2 preguntas adicionales)

### Pregunta 11 — Tu Proyecto
Describe brevemente el proyecto Big Data que tu grupo ha elegido:
- Nombre del proyecto
- Empresa o sector al que aplica
- Problema que resuelve
- ¿Cuáles de las 5 V's están presentes en los datos del proyecto?

_Respuesta_:  
```
NOMBRE DEL PROYECTO: g1-churn-telecom-b2b
Repositorio: https://github.com/RubenCarty/bigdata-g1-churn-telecom-b2b

EMPRESA O SECTOR:
El proyecto aplica al sector de telecomunicaciones, específicamente al segmento B2B 
(Business to Business), es decir, empresas clientes de una operadora de telecomunicaciones. 
El contexto es una empresa telco que presta servicios de conectividad, telefonía y datos 
a clientes corporativos.

PROBLEMA QUE RESUELVE:
El proyecto busca predecir la fuga de clientes empresariales (churn) en el sector 
telecomunicaciones. A diferencia del churn B2C (clientes individuales), los clientes 
B2B tienen contratos más grandes y su pérdida impacta significativamente los ingresos 
de la empresa. La solución propone un modelo de Machine Learning que identifique, con 
anticipación suficiente, qué clientes corporativos tienen alta probabilidad de no renovar 
su contrato, permitiendo a la fuerza comercial intervenir de manera proactiva.

V's DEL BIG DATA PRESENTES EN EL PROYECTO:

- VOLUMEN: Histórico de transacciones, consumos, pagos e interacciones de miles de 
  clientes empresariales durante meses o años de relación comercial

- VARIEDAD: Datos estructurados de facturación y contratos, semi-estructurados de 
  tickets de soporte técnico, y potencialmente no estructurados de comunicaciones 
  con el account manager

- VERACIDAD: Crítica en este proyecto; datos de consumo mal registrados o clientes 
  duplicados en el CRM generarían un modelo de predicción poco confiable

- VALOR: El valor de negocio es claro y cuantificable: retener un cliente B2B puede 
  equivaler a cientos de miles de soles en ingresos anuales por contrato
```

---

### Pregunta 12 — Arquitectura inicial
Dibuja (a mano o usando draw.io) una arquitectura inicial **muy básica** de cómo crees que debería funcionar tu proyecto. Incluye: fuentes de datos, almacenamiento, procesamiento y visualización.

*(Adjunta la imagen o el link de draw.io)*

_Link o descripción de tu diagrama_:  
```
ARQUITECTURA INICIAL — PROYECTO g1-churn-telecom-b2b

┌─────────────────────────────────────────────────────────────────────┐
│                        FUENTES DE DATOS                             │
│                                                                     │
│  [CRM Corporativo]  [Sistema de Billing]  [Tickets de Soporte]      │
│  (contratos, seg-   (facturas, pagos,     (incidencias, reclamos,   │
│   mento, industria)  consumos mensuales)   tiempo de resolución)    │
└────────────────────────────┬────────────────────────────────────────┘
                             │ ETL / Ingesta
                             ▼
┌─────────────────────────────────────────────────────────────────────┐
│                     ALMACENAMIENTO                                  │
│                                                                     │
│              [ DATA LAKE — Datos crudos (CSV/JSON) ]                │
│              Almacena dataset histórico de clientes B2B             │
└────────────────────────────┬────────────────────────────────────────┘
                             │ Limpieza y transformación
                             ▼
┌─────────────────────────────────────────────────────────────────────┐
│                     PROCESAMIENTO                                   │
│                                                                     │
│   [Python + Pandas]  →  Limpieza, feature engineering, EDA          │
│   [Scikit-learn / PySpark ML]  →  Modelo de clasificación churn     │
│   (Jupyter Notebooks en /notebooks del repositorio)                 │
└────────────────────────────┬────────────────────────────────────────┘
                             │ Resultados y predicciones
                             ▼
┌─────────────────────────────────────────────────────────────────────┐
│                     VISUALIZACIÓN Y ACCIÓN                          │
│                                                                     │
│   [Dashboard Power BI / Matplotlib]  →  Score de churn por cliente  │
│   [Alerta comercial]  →  Lista de clientes en riesgo alto           │
│                          para intervención proactiva del equipo     │
└─────────────────────────────────────────────────────────────────────┘

Herramientas principales del proyecto:
- Lenguaje: Python 3.x
- Librerías: pandas, scikit-learn, matplotlib, seaborn
- Entorno: Jupyter Notebooks
- Repositorio: GitHub (fork-based workflow, rama main)
- Dataset: Histórico de clientes B2B de telecomunicaciones (Kaggle o simulado)
```

---

## CRITERIOS DE EVALUACIÓN

| Criterio | Puntos |
|---------|--------|
| Responde todas las preguntas (no deja en blanco) | 4 |
| Usa sus propias palabras, no copia de internet | 4 |
| Da ejemplos reales de su entorno laboral | 4 |
| Las definiciones son técnicamente correctas | 4 |
| Respuestas de reflexión (P9, P11, P12) muestran pensamiento propio | 4 |
| **TOTAL** | **20** |

---

> **Recuerda**: La nota EC (10% del total) se basa en tu dominio conceptual. Esta guía de trabajo es el mejor preparativo. Si puedes responder estas 12 preguntas con seguridad, el examen EC no debería sorprenderte.

---

*Entrega: Subir al repositorio de GitHub Classroom o al foro de la plataforma virtual antes de la Semana 2*
