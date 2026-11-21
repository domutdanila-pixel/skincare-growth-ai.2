
import zipfile
import os

ZIP_FILE = "skingrow-ai.zip"
OUTPUT_DIR = "."

if not os.path.isfile(ZIP_FILE):
    raise FileNotFoundError(
        f"Архив {ZIP_FILE} не найден в корне репозитория!"
    )

with zipfile.ZipFile(ZIP_FILE, "r") as archive:
    archive.extractall(OUTPUT_DIR)

print("SkinGrow AI: архив успешно распакован!")
