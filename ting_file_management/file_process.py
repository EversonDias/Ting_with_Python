import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    file = txt_importer(path_file)
    for index in range(len(instance)):
        if path_file in instance.search(index)["nome_do_arquivo"]:
            return None
    data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file),
        "linhas_do_arquivo": file
    }
    instance.enqueue(data)
    print(data)


def remove(instance):
    if len(instance) == 0:
        return print("Não há elementos")
    name = instance.dequeue()["nome_do_arquivo"]
    print(f"Arquivo {name} removido com sucesso")


def file_metadata(instance, position):
    if position >= len(instance) or position < 0:
        return print("Posição inválida", file=sys.stderr)
    print(instance.search(position))
