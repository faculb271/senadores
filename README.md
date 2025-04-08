# Proyecto: Senadores
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Pandas](https://img.shields.io/badge/Pandas-1.3%2B-orange)
![lxml](https://img.shields.io/badge/lxml-4.6%2B-green)
![cURL](https://img.shields.io/badge/cURL-7.75%2B-lightgrey)
![Last Commit](https://img.shields.io/github/last-commit/faculb271/senadores)

## Descripción

El proyecto Senadores es una herramienta que automatiza la obtención, limpieza y transformación de datos relacionados con los senadores y sus asignaciones administrativas. Este sistema incluye un crawler para descargar datos en formato JSON desde una fuente externa, un módulo de limpieza para estructurar los datos y la generación de archivos CSV y Excel listos para su análisis.


## Características

Crawler: Descarga automáticamente un archivo JSON desde una página web.

Procesamiento de Datos: Limpia y transforma los datos en un formato tabular.

Exportación: Genera archivos en formato CSV y Excel con las columnas requeridas.

Registro de Logs: Registra eventos 
importantes y errores durante la ejecucion

```
python crawler.py
```

El crawler descargará el archivo JSON y lo guardará en la ubicación especificada en la configuración.

# Funcionamiento del Crawler

Para utilizar el Crawler, hacemos lo siguiente

```
python crawler.py
```

El crawler descargará el archivo JSON y lo guardará en la ubicación especificada en la configuración.

### Flujo de Trabajo: 

1. **Descarga la página HTML** desde la URL base.

2. **Busca la URL del JSON** en el contenido HTML usando _find_json_url.
3. **Construye la URL completa** del JSON usando _build_full_url.
4. **Descarga el JSON** desde la URL completa.

5. **Guarda el JSON** en el archivo especificado usando _save_content.

### Log de Actividades
El crawler mantiene un registro de las actividades y posibles errores en un archivo de log configurado en config.py.

## Cleaning de Datos 

El segundo paso es limpiar los datos que nos da el JSON para obtenerlos en CSV o en formato Excel, por lo tanto ejecutamos el archivo cleaning.py
```
python cleaning.py
```
Esto lo que hara es cambiarle el nombre a las columnas y nos traera lo siguiente

**file_number**: Número de legajo.

**name**: Nombre del senador.

**last_name**: Apellido del senador.

**category**: Categoría administrativa.

**employment_type**: Tipo de empleo.

**assigned_to**: Destino asignado.

## Contribuciones

Si deseas contribuir a este proyecto, siéntete libre de abrir un "pull request" con mejoras o nuevas funcionalidades.