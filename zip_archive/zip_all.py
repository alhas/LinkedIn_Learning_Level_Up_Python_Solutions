import os
from zipfile import ZipFile


def zip_all(file_path: str, extensions: tuple[str], outputfile: str) -> None:
    with ZipFile(outputfile, 'w') as zfile:
        def scan_dir(file_path):
            with os.scandir(file_path) as it:
                for entry in it:
                    if entry.name.endswith(extensions) and entry.is_file():
                        zfile.write(entry)
                    elif entry.is_dir():
                        zfile.write(entry)
                        scan_dir(entry.path)
        scan_dir(file_path)


zip_all('./merge_csv', ('.csv', '.py'), './zip_archive/merge_csv.zip')
