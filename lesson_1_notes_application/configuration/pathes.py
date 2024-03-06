# Пути к файлам

from pathlib import Path

dir_path = Path(__file__).parents[1]
NOTE_FILE_PATH = Path(dir_path,'note_direction.csv')
