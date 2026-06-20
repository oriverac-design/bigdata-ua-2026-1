# LABORATORIO — SEMANA 1
## Análisis de Datos con Python + Identificación de Tipos de Datos
### Big Data (DD283) | Universidad Autónoma del Perú

**Nombre(s)**: Lindo Barrientos Jhonn Viequier  
**Grupo**: Grupo 01  
**Duración estimada**: 90 minutos  
**Modalidad**: Individual (en casa, en tu laptop)  
**Entrega**: Subir notebook .ipynb a GitHub Classroom antes de Semana 2

---

## OBJETIVO DEL LABORATORIO

Al completar este laboratorio serás capaz de:
- Cargar y explorar diferentes tipos de datos con Python
- Identificar las características de Big Data en datos reales
- Calcular métricas de volumen y velocidad de datos
- Crear tu primer notebook de análisis de datos

---

## REQUISITOS PREVIOS

**Opción A (recomendada)**: Usar Google Colab — no requiere instalación
- Ir a: https://colab.research.google.com/
- Crear nuevo notebook
- ¡Listo para trabajar!

**Opción B**: Usar Jupyter Notebook local
- Instalar Anaconda: https://www.anaconda.com/download
- Abrir Anaconda Navigator → Jupyter Notebook
- Crear nuevo notebook Python 3

---

## PARTE 1: CONFIGURACIÓN DEL ENTORNO (10 minutos)

### Paso 1.1: Instalar e importar librerías

Crea una celda nueva en tu notebook y ejecuta:

```python
# Instalar librerías (solo en Colab o si no están instaladas)
# !pip install pandas matplotlib seaborn requests

# Importar librerías
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json
import os
from datetime import datetime

# Verificar versiones
print(f"Pandas version: {pd.__version__}")
print(f"Python version: {os.sys.version}")
print("¡Entorno listo!")
```

**Captura de pantalla requerida**: Toma screenshot del output con las versiones instaladas.

---

## PARTE 2: DATOS ESTRUCTURADOS (20 minutos)

### Paso 2.1: Cargar datos reales de una empresa peruana

Vamos a trabajar con datos públicos del BCRP (Banco Central de Reserva del Perú).

```python
# Crear un dataset simulado de transacciones de una empresa peruana
# (basado en patrones reales del mercado peruano)

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Crear dataset de transacciones
np.random.seed(42)
n_transacciones = 10000

fechas = pd.date_range(start='2024-01-01', end='2024-12-31', periods=n_transacciones)
departamentos = ['Lima', 'Arequipa', 'Cusco', 'Trujillo', 'Piura', 'Chiclayo', 'Iquitos', 'Huancayo']
categorias = ['Alimentos', 'Electrodomésticos', 'Ropa', 'Farmacia', 'Tecnología', 'Deportes']

transacciones = pd.DataFrame({
    'id_transaccion': range(1, n_transacciones + 1),
    'fecha': fechas,
    'cliente_id': np.random.randint(1000, 9999, n_transacciones),
    'departamento': np.random.choice(departamentos, n_transacciones, 
                                     p=[0.45, 0.12, 0.10, 0.09, 0.08, 0.07, 0.05, 0.04]),
    'categoria': np.random.choice(categorias, n_transacciones),
    'monto_soles': np.round(np.random.exponential(150, n_transacciones) + 20, 2),
    'metodo_pago': np.random.choice(['Yape', 'Plin', 'Tarjeta', 'Efectivo', 'BIM'], 
                                     n_transacciones, p=[0.30, 0.20, 0.25, 0.20, 0.05]),
    'es_fraude': np.random.choice([0, 1], n_transacciones, p=[0.98, 0.02])
})

print(f"Dataset creado con {len(transacciones):,} registros")
print(f"Columnas: {list(transacciones.columns)}")
print(f"\nPrimeras 5 filas:")
transacciones.head()
```

### Paso 2.2: Explorar los datos

```python
# Exploración básica
print("=== INFORMACIÓN GENERAL DEL DATASET ===")
print(f"\nTamaño del dataset: {transacciones.shape}")
print(f"Filas: {transacciones.shape[0]:,}")
print(f"Columnas: {transacciones.shape[1]}")

print("\n=== TIPOS DE DATOS POR COLUMNA ===")
print(transacciones.dtypes)

print("\n=== ESTADÍSTICAS DESCRIPTIVAS ===")
print(transacciones.describe())

print("\n=== VALORES NULOS ===")
print(transacciones.isnull().sum())
```

### Paso 2.3: Calcular métricas de Big Data

```python
# Calcular las 5 V's para este dataset

# VOLUMEN
tamaño_bytes = transacciones.memory_usage(deep=True).sum()
print("=== ANÁLISIS DE VOLUMEN ===")
print(f"Registros: {len(transacciones):,}")
print(f"Tamaño en memoria: {tamaño_bytes / 1024:.1f} KB")
print(f"Si escalamos a 100 millones de registros: {tamaño_bytes * 10000 / 1024**3:.1f} GB")

# VELOCIDAD (simulada)
print("\n=== ANÁLISIS DE VELOCIDAD ===")
trans_por_dia = transacciones.groupby(transacciones['fecha'].dt.date).size()
print(f"Promedio de transacciones por día: {trans_por_dia.mean():.0f}")
print(f"Máximo de transacciones en un día: {trans_por_dia.max()}")
print(f"Mínimo de transacciones en un día: {trans_por_dia.min()}")

# VERACIDAD (detección de fraude)
print("\n=== ANÁLISIS DE VERACIDAD ===")
print(f"Transacciones normales: {(transacciones['es_fraude']==0).sum():,}")
print(f"Transacciones sospechosas (fraude): {(transacciones['es_fraude']==1).sum():,}")
print(f"Tasa de fraude: {transacciones['es_fraude'].mean()*100:.2f}%")
```

### Paso 2.4: Visualización básica

```python
# Crear visualizaciones
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Análisis de Transacciones - Empresa Retail Peruana', fontsize=14, fontweight='bold')

# Gráfico 1: Distribución por departamento
trans_x_dept = transacciones['departamento'].value_counts()
axes[0, 0].bar(trans_x_dept.index, trans_x_dept.values, color='steelblue')
axes[0, 0].set_title('Transacciones por Departamento')
axes[0, 0].set_xlabel('Departamento')
axes[0, 0].set_ylabel('Número de Transacciones')
axes[0, 0].tick_params(axis='x', rotation=45)

# Gráfico 2: Métodos de pago
metodo_pago = transacciones['metodo_pago'].value_counts()
axes[0, 1].pie(metodo_pago.values, labels=metodo_pago.index, autopct='%1.1f%%', startangle=90)
axes[0, 1].set_title('Distribución de Métodos de Pago')

# Gráfico 3: Ventas por categoría
ventas_categoria = transacciones.groupby('categoria')['monto_soles'].sum().sort_values(ascending=True)
axes[1, 0].barh(ventas_categoria.index, ventas_categoria.values, color='coral')
axes[1, 0].set_title('Ventas Totales por Categoría (S/.)')
axes[1, 0].set_xlabel('Monto Total (S/.)')

# Gráfico 4: Tendencia de ventas en el tiempo
ventas_mes = transacciones.groupby(transacciones['fecha'].dt.month)['monto_soles'].sum()
axes[1, 1].plot(ventas_mes.index, ventas_mes.values, marker='o', color='green', linewidth=2)
axes[1, 1].set_title('Tendencia de Ventas por Mes')
axes[1, 1].set_xlabel('Mes')
axes[1, 1].set_ylabel('Ventas Totales (S/.)')
axes[1, 1].set_xticks(range(1, 13))
axes[1, 1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('analisis_transacciones.png', dpi=150, bbox_inches='tight')
plt.show()
print("¡Gráfico guardado como 'analisis_transacciones.png'!")
```

---

## PARTE 3: DATOS SEMI-ESTRUCTURADOS — JSON (15 minutos)

### Paso 3.1: Trabajar con datos JSON (tipo API)

```python
# Simular respuesta de una API (similar a la API de Reniec o SUNAT)
# Este es el tipo de dato semi-estructurado más común en sistemas modernos

datos_clientes_json = """
[
    {
        "id": "CLI-001",
        "nombres": "Juan Carlos",
        "apellidos": "Quispe Mamani",
        "dni": "45678901",
        "contacto": {
            "email": "jquispe@empresa.com",
            "telefono": "987654321",
            "distrito": "San Miguel"
        },
        "compras": [150.50, 320.00, 89.90],
        "fecha_registro": "2023-01-15",
        "activo": true,
        "etiquetas": ["premium", "fiel", "digital"]
    },
    {
        "id": "CLI-002", 
        "nombres": "Maria Elena",
        "apellidos": "Torres Flores",
        "dni": "56789012",
        "contacto": {
            "email": "matorres@gmail.com",
            "telefono": null,
            "distrito": "Miraflores"
        },
        "compras": [500.00, 1200.50],
        "fecha_registro": "2023-03-22",
        "activo": true,
        "etiquetas": ["vip", "presencial"]
    },
    {
        "id": "CLI-003",
        "nombres": "Roberto",
        "apellidos": "Mendoza García", 
        "dni": "67890123",
        "contacto": {
            "email": null,
            "telefono": "976543210",
            "distrito": "Callao"
        },
        "compras": [],
        "fecha_registro": "2024-01-05",
        "activo": false,
        "etiquetas": ["nuevo", "inactivo"]
    }
]
"""

# Parsear JSON
clientes = json.loads(datos_clientes_json)
print(f"Número de clientes: {len(clientes)}")
print(f"\nEstructura del primer cliente:")
print(json.dumps(clientes[0], indent=2, ensure_ascii=False))
```

### Paso 3.2: Análisis del JSON

```python
# Convertir JSON a DataFrame para análisis
datos_tabulares = []
for cliente in clientes:
    datos_tabulares.append({
        'id': cliente['id'],
        'nombre_completo': f"{cliente['nombres']} {cliente['apellidos']}",
        'dni': cliente['dni'],
        'distrito': cliente['contacto']['distrito'],
        'tiene_email': cliente['contacto']['email'] is not None,
        'tiene_telefono': cliente['contacto']['telefono'] is not None,
        'total_compras': sum(cliente['compras']),
        'num_compras': len(cliente['compras']),
        'activo': cliente['activo'],
        'es_premium': 'premium' in cliente['etiquetas'] or 'vip' in cliente['etiquetas']
    })

df_clientes = pd.DataFrame(datos_tabulares)
print("=== CLIENTES CONVERTIDOS DE JSON A TABLA ===")
print(df_clientes.to_string(index=False))

print("\n=== RESUMEN DE COMPLETITUD DE DATOS ===")
print(f"Clientes con email: {df_clientes['tiene_email'].sum()}/{len(df_clientes)}")
print(f"Clientes con teléfono: {df_clientes['tiene_telefono'].sum()}/{len(df_clientes)}")
print(f"Clientes activos: {df_clientes['activo'].sum()}/{len(df_clientes)}")
print(f"Clientes premium/VIP: {df_clientes['es_premium'].sum()}/{len(df_clientes)}")
```

---

## PARTE 4: DATOS NO ESTRUCTURADOS — TEXTO (15 minutos)

### Paso 4.1: Análisis de texto (comentarios de clientes)

```python
# Simular comentarios de clientes en redes sociales sobre una empresa peruana
comentarios_clientes = [
    "Excelente servicio en Plaza Vea de San Miguel, muy rápido el pago con Yape!",
    "Pésima atención, esperé 30 minutos para ser atendido, nunca más voy a Tottus de La Molina",
    "El producto llegó a tiempo pero la caja estaba dañada. Regular la experiencia",
    "Super bueno el envío express de Ripley, llegó en 2 horas a Miraflores",
    "Me cobraron de más y cuando reclamé me tardaron 1 semana en devolver el dinero",
    "El área de electrónica tiene todo, encontré el celular que buscaba a buen precio",
    "App del supermercado se cae constantemente, muy mala experiencia digital",
    "Calidad del producto excelente pero precio alto comparado con Metro",
    "Personal muy amable y capacitado para asesorar sobre productos",
    "Compré en línea y el producto era diferente a la foto, decepcionante"
]

print("=== ANÁLISIS DE DATOS NO ESTRUCTURADOS (TEXTO) ===")
print(f"Total de comentarios: {len(comentarios_clientes)}")

# Análisis básico sin librerías especializadas
palabras_positivas = ['excelente', 'super', 'bueno', 'rápido', 'amable', 'calidad']
palabras_negativas = ['pésima', 'mala', 'dañada', 'tardaron', 'decepcionante', 'se cae']

resultados = []
for i, comentario in enumerate(comentarios_clientes, 1):
    texto_lower = comentario.lower()
    score_pos = sum(1 for p in palabras_positivas if p in texto_lower)
    score_neg = sum(1 for p in palabras_negativas if p in texto_lower)
    
    if score_pos > score_neg:
        sentimiento = "POSITIVO"
    elif score_neg > score_pos:
        sentimiento = "NEGATIVO"
    else:
        sentimiento = "NEUTRO"
    
    num_palabras = len(comentario.split())
    resultados.append({
        'id': i,
        'sentimiento': sentimiento,
        'num_palabras': num_palabras,
        'comentario': comentario[:50] + "..."
    })
    
df_sentimientos = pd.DataFrame(resultados)
print("\n=== RESULTADOS DE ANÁLISIS DE SENTIMIENTO ===")
print(df_sentimientos.to_string(index=False))

print("\n=== RESUMEN ===")
print(df_sentimientos['sentimiento'].value_counts())
```

---

## PARTE 5: ARQUITECTURA BIG DATA — DISEÑO (20 minutos)

### Paso 5.1: Diseñar la arquitectura para tu empresa

**Instrucción**: Basándote en los datos que has analizado en este laboratorio, diseña la arquitectura Big Data para una empresa retail peruana que quiere:
1. Analizar transacciones en tiempo real
2. Predecir fraudes
3. Recomendar productos personalizados
4. Analizar comentarios de redes sociales

Completa el siguiente template en tu notebook:

```python
# TEMPLATE DE ARQUITECTURA BIG DATA
# Completa los campos marcados con [TU RESPUESTA]

arquitectura = {
    "empresa": "Supermercados [Tu empresa elegida]",
    "problema_principal": "[Describe el problema de negocio]",
    
    "fuentes_de_datos": {
        "estructuradas": ["[ej: Base de datos de ventas POS]", "[...]"],
        "semi_estructuradas": ["[ej: API de pagos Yape]", "[...]"],
        "no_estructuradas": ["[ej: Videos de cámaras de seguridad]", "[...]"]
    },
    
    "estimacion_volumen": {
        "registros_por_dia": "[Tu cálculo]",
        "tamaño_estimado_por_año": "[Tu cálculo en GB/TB]"
    },
    
    "tecnologias_propuestas": {
        "ingesta": "[Herramienta para capturar datos en tiempo real]",
        "almacenamiento": "[Herramienta para guardar los datos]",
        "procesamiento": "[Herramienta para procesar/analizar]",
        "visualizacion": "[Herramienta para presentar resultados]"
    },
    
    "casos_uso_principales": [
        "[Caso 1: ej Detección de fraude en tiempo real]",
        "[Caso 2: ...]",
        "[Caso 3: ...]"
    ]
}

import json
print(json.dumps(arquitectura, indent=2, ensure_ascii=False))
```

---

## ENTREGABLES DEL LABORATORIO

Sube a tu repositorio GitHub los siguientes archivos:

- [ ] `lab_s1_tipos_datos.ipynb` — El notebook completo con todas las partes ejecutadas
- [ ] `analisis_transacciones.png` — El gráfico generado en Parte 2
- [ ] `README.md` — Incluye: Tu nombre, que aprendiste, qué fue lo más difícil

**Formato del README.md**:
```markdown
# Lab Semana 1 — Big Data DD283
**Estudiante**: Tu Nombre  
**Fecha**: 
**Empresa del proyecto**: 

## ¿Qué aprendí?
[Tu reflexión — mínimo 3 oraciones]

## ¿Qué fue lo más difícil?
[Tu reflexión]

## ¿Cómo aplica en mi empresa actual?
[Tu reflexión — mínimo 2 oraciones]
```

---

## CRITERIOS DE EVALUACIÓN DEL LABORATORIO

| Criterio | Puntos |
|---------|--------|
| Notebook ejecutado sin errores (todas las celdas) | 30 |
| Análisis correcto de datos estructurados (Parte 2) | 20 |
| Análisis correcto de datos JSON (Parte 3) | 15 |
| Análisis de texto completado (Parte 4) | 15 |
| Arquitectura diseñada con lógica coherente (Parte 5) | 15 |
| README con reflexión genuina | 5 |
| **TOTAL** | **100** |

---

## AYUDA Y RECURSOS

**Si tienes un error en Python**:
1. Copia el mensaje de error en Google
2. Busca en Stack Overflow
3. Pregunta en el foro del curso explicando: qué intentas hacer, qué error recibes

**Recursos útiles**:
- Pandas documentation: https://pandas.pydata.org/docs/
- Matplotlib gallery: https://matplotlib.org/stable/gallery/
- Google Colab shortcuts: Ctrl+Enter (ejecutar celda), Shift+Enter (ejecutar y bajar)

---

*Recuerda: El error es parte del aprendizaje. Si ves un error rojo, es una oportunidad de aprender a debuggear — una habilidad fundamental de un Ingeniero de Datos.*
