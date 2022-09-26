from pathlib import Path

working_directory = Path.cwd()
files = [file for file in working_directory if file.is_file()]
# print(working_directory)
# print(files)
