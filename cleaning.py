import pandas as pd
import config
import log

log = log.Log().get_logger(config.LOG_FILE_LIMPIEZA)

file = "senadores.json"
df = pd.read_json(file)
rows = pd.DataFrame(df["table"]["rows"])

try:
    rows["file_number"] = rows["LEGAJO"].fillna("")  # Extraer LEGAJO
    rows[["last_name", "name"]] = rows["APELLIDO Y NOMBRE"].str.split(", ", expand=True).fillna("")  # Separar apellido y nombre
    rows["category"] = rows["CATEGORIA"].fillna("").str.strip()  # Extraer CATEGORIA
    rows["employment_type"] = rows["PLANTA"].fillna("").str.strip()  # Extraer PLANTA
    rows["assigned_to"] = rows["DESTINO"].fillna("").str.strip()  # Extraer DESTINO

    processed_df = rows[["file_number", "name", "last_name", "category", "employment_type", "assigned_to"]]
    log.info("Perfectamente procesado")
except Exception as e:
    log.error(f"Hubo un error con {e}")

try:
    processed_df.to_csv("senadores.csv", index=False, encoding="utf-8")
    processed_df.to_excel("senadores.xlsx", index=False, engine="openpyxl")
    log.info("Se procesaron y guardaron los datos correctamente.")
except Exception as e:
    log.error(f"Hubo un problema durante el procesamiento: {e}")

