
import zipfile
import os

ZIP_FILE = "skingrow-ai-site.zip"
OUTPUT_DIR = "."

if not os.path.exists(ZIP_FILE):
    raise FileNotFoundError(f"Не найден архив: {ZIP_FILE}")

with zipfile.ZipFile(ZIP_FILE, "r") as archive:
    archive.extractall(OUTPUT_DIR)

print("SkinGrow AI успешно распакован!")
print("Главный файл: skingrow-ai-package/index.html")
