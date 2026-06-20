# Lab Semana 1 — Big Data DD283
**Estudiante**: Jhonn Viequier Lindo Barrientos  
**Fecha**: Junio 2026  
**Empresa del proyecto**: Telecomunicaciones B2B (proyecto de grupo: g1-churn-telecom-b2b)

## ¿Qué aprendí?
Aprendí a diferenciar en la práctica los tres tipos de datos del Big Data: estructurados (un DataFrame de transacciones con esquema fijo), semi-estructurados (un JSON tipo API que tuve que aplanar a tabla) y no estructurados (comentarios de texto libre que clasifiqué por sentimiento). También comprobé cómo calcular las V's directamente sobre los datos: medí el volumen en memoria y lo proyecté a 100 millones de registros, calculé la velocidad como transacciones por día, y la veracidad mediante la tasa de fraude. Por último, entendí que diseñar una arquitectura Big Data consiste en conectar de forma coherente la ingesta, el almacenamiento, el procesamiento y la visualización según el tipo de dato y el caso de uso.

## ¿Qué fue lo más difícil?
Lo más difícil fue trabajar con el JSON anidado de la Parte 3, porque tuve que recorrer estructuras dentro de estructuras (el campo "contacto" y la lista "compras") y manejar los valores nulos para convertir todo a una tabla plana sin perder información. Manejar los valores `null` y las listas vacías al pasar de JSON a DataFrame requirió cuidado para no romper los cálculos de totales.

## ¿Cómo aplica en mi empresa actual?
En COEZ PERÚ, donde trabajo como Ingeniero de Producción, manejo a diario datos estructurados (metrados y avances de partidas en Excel), semi-estructurados (correos y formatos de submittal) y no estructurados (fotografías de obra y PDFs de planos). Este laboratorio me mostró que podría centralizar todo ese flujo fragmentado en una arquitectura tipo Data Lake para tener control de producción en tiempo real, en lugar de las planillas manuales y desconectadas que usamos hoy. Además, el ejercicio de detección de fraude y predicción conecta directamente con el proyecto de mi grupo sobre predicción de fuga de clientes (churn) en telecomunicaciones.
