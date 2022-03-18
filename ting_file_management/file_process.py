import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for index in range(len(instance)):
        if instance.search(index)["nome_do_arquivo"] == path_file:
            return None
    path_file_content = txt_importer(path_file)
    processed_content = {}
    processed_content["nome_do_arquivo"] = path_file
    processed_content["qtd_linhas"] = len(path_file_content)
    processed_content["linhas_do_arquivo"] = path_file_content
    instance.enqueue(processed_content)
    return sys.stdout.write(str(processed_content))


def remove(instance):
    if len(instance) == 0:
        return sys.stdout.write("Não há elementos\n")
    removed_file_name = instance.dequeue()['nome_do_arquivo']
    return sys.stdout.write(
        f"Arquivo {removed_file_name} removido com sucesso\n"
        )


def file_metadata(instance, position):
    try:
        return sys.stdout.write(str(instance.search(position)))
    except IndexError:
        return sys.stderr.write("Posição inválida\n")
