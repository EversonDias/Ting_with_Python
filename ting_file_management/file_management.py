import os
import sys


def txt_importer(path_file):
    file_name, file_ext = os.path.splitext(path_file)
    if file_ext != ".txt":
        print("Formato inválido", file=sys.stderr)
    else:
        if os.path.exists(path_file):
            with open(path_file, 'r') as file:
                lines = file.readlines()
                data = []
                for line in lines:
                    data.append(line.replace('\n', ''))
                return data
        else:
            print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
