import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for i in range(len(instance)):
        if instance.search(i)["nome_do_arquivo"] == path_file:
            return None
    path_file_content = txt_importer(path_file)
    processed_content = {}
    processed_content["nome_do_arquivo"] = path_file
    processed_content["qtd_linhas"] = len(path_file_content)
    processed_content["linhas_do_arquivo"] = path_file_content
    instance.enqueue(processed_content)
    return sys.stdout.write(str(processed_content))


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
