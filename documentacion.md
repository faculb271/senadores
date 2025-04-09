# Segundo Crawler

Tags: Documentacion

```python
def __init__(self): # Constructor
    self.url = config.BASE_URL
    self.output = config.FILE
    self.__log = log.Log().get_logger(config.LOG_FILE)
```

- **self.url**: URL base de la página web desde donde se descargará el JSON.
- **self.output**: Ruta del archivo donde se guardará el JSON descargado.
- **self.__log**: Configura un logger para registrar eventos y errores.

```python
def _build_full_url(self, relative_url):
    """Construye una URL completa a partir de una URL relativa."""
    if relative_url.startswith('http'):
        return relative_url
        
    if relative_url.startswith('/'):
        parsed_url = urllib.parse.urlparse(self.url)
        base_domain = f"{parsed_url.scheme}://{parsed_url.netloc}"
        return urllib.parse.urljoin(base_domain, relative_url)
    else:
        return urllib.parse.urljoin(self.url, relative_url)
```

 

- **Cómo funciona**:
    - Si la URL ya es absoluta (`http`), la devuelve tal cual.
    - Si es relativa (`/`), combina el dominio base con la URL relativa.
    - Si no tiene `/`, asume que es relativa y la combina con la URL base.

```python
def _find_json_url(self, html_content):
    """Encuentra la URL del JSON en el contenido HTML."""
    try:
        tree = html.fromstring(html_content)
        json_links = tree.xpath('//div[@class="datosAbiertosDiv"]//a[contains(@href, "ExportarListadoAgentes/json")]')
        return json_links[0].get('href')
    except Exception as e:
        self.__log.error(f"Algo falla con {e}")
```

- **Cómo funciona**:
    - Convierte el contenido HTML en un árbol DOM.
    - Usa una expresión XPath para buscar enlaces (`<a>`) que contengan `"ExportarListadoAgentes/json"`.
    - Devuelve el atributo `href` del primer enlace encontrado.
- **Manejo de errores**: Si algo falla, registra el error en el log.

```python
def _save_content(self, content, output_path):
    """Guarda el contenido en un archivo, eliminando etiquetas <pre> si están presentes."""
    try:
        decoded_content = content.decode('utf-8')
        if decoded_content.startswith('<pre>') and decoded_content.endswith('</pre>'):
            decoded_content = decoded_content[5:-6]

        os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(decoded_content)
    except (IOError, OSError, UnicodeDecodeError) as e:
        self.__log.error(f"Error al guardar el archivo: {e}")
```

- **Cómo funciona**:
    - Decodifica el contenido binario a texto.
    - Si el contenido comienza con `<pre>` y termina con `</pre>`, elimina estas etiquetas.
    - Crea el directorio de destino si no existe.
    - Escribe el contenido limpio en el archivo.

```python
def run(self):
    """Descarga el archivo JSON desde la página web."""
    try:
        self.__log.info(f"Obteniendo página desde: {self.url}")
        response = requests.get(self.url)
        
        json_href = self._find_json_url(response.content)
        
        json_full_url = self._build_full_url(json_href)
        self.__log.info(f"Se encontró el JSON en: {json_full_url}")
        
        # Descargar el JSON
        json_response = requests.get(json_full_url)
        self.__log.info(f"JSON descargado exitosamente en: {self.output}")
        
    except requests.exceptions.RequestException as e:
        self.__log.error(f"Error de conexión: {e}")
    except Exception as e:
        self.__log.error(f"Error inesperado: {e}")
```

- **Propósito**: Orquesta todo el proceso de descarga del JSON.
- **Pasos**:
    1. **Descarga la página HTML** desde la URL base.
    2. **Busca la URL del JSON** en el contenido HTML usando _find_json_url.
    3. **Construye la URL completa** del JSON usando _build_full_url.
    4. **Descarga el JSON** desde la URL completa.
    5. **Guarda el JSON** en el archivo especificado usando _save_content.
- **Manejo de errores**:
    - Registra errores de conexión o HTTP.
    - Maneja excepciones generales.