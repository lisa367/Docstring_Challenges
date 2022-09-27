from pathlib import Path
import shutil

working_directory = Path.cwd()
files = [file for file in working_directory.iterdir() if file.is_file()]
directories = [directory for directory in working_directory.iterdir() if directory.is_dir()]
# print(working_directory)
# print(files)
# print(directories)

for file in files:
    extension = file.split(".")[-1]
    # extension = file.suffix
    if extension in directories:
        pass
    else:
        new_dir = working_directory / extension
        new_dir.mkdir(exist_ok=True)
        # Déplacer le fichier dans le nouveau dossier
        shutil.move(file, new_dir)