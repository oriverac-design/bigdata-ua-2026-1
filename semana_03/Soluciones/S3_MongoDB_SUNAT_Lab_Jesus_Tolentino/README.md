# S3 — Laboratorio MongoDB SUNAT Simulado

Este proyecto contiene la implementación del laboratorio de Semana 3 del curso Big Data DD283.

## Archivos

- `notebook/S3_MongoDB_SUNAT_Lab.ipynb`: notebook completo para Google Colab.
- `src/implementacion_nosql_sunat.py`: versión ejecutable en Python local.
- `S3_respuestas.md`: respuestas listas para copiar al Markdown.
- `requirements.txt`: dependencias del proyecto.
- `screenshots/`: carpeta para colocar evidencias de Atlas.

## Ejecución en Colab

1. Subir el notebook a Google Colab.
2. Reemplazar `CONNECTION_STRING` por el string real de MongoDB Atlas.
3. Ejecutar todas las celdas.
4. Tomar captura de MongoDB Atlas con la colección `empresas`, un documento expandido y los índices.

## Ejecución local

```bash
pip install -r requirements.txt
python src/implementacion_nosql_sunat.py
```

Si `CONNECTION_STRING` está vacío, el script usa `mongomock` como alternativa en memoria.
