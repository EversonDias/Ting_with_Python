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


def file_process(path_file, list):
    file_name, file_ext = os.path.splitext(path_file)
    name = file_name.split('/')[-1]
    file = txt_importer(path_file)
    isRepeated = False
    for index in range(len(list)):
        if name in list.search(index)["nome_do_arquivo"]:
            isRepeated = True
    data = {}
    if not isRepeated:
        data["nome_do_arquivo"] = name
        data["qtd_linhas"] = len(file)
        data["linhas_do_arquivo"] = file
        list.enqueue(data)
        print(data, file=sys.stderr)
