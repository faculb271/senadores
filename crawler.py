from curl_cffi import requests
import config
import log
from lxml import html

class FileJSON:
    def __init__(self):
        self.url = config.BASE_URL
        self.output = config.FILE
        self.__log = log.Log().get_logger(config.LOG_FILE)

    def download(self):
        try:
            response = requests.get(self.url)
            tree = html.fromstring(response.content)
            json_url = tree.xpath('//a[contains(@href, "json")]')
            if json_url:
                self.__log.info(f"Se encontro el JSON")
            else:
                self.__log.error(f"No se encontro el JSON")
        except requests.exceptions.RequestException as e:
            self.__log.error(f"Error al obtener la pagina HTML: {e}")

if __name__ == "__main__":
    file_json = FileJSON()
    file_json.download()