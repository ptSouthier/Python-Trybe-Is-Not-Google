import sys


def txt_importer(path_file):
    path_extension = (path_file.split("."))[1]
    if path_extension != "txt":
        sys.stderr.write("Formato inválido\n")
    try:
        file = open(path_file, "r")
    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
    else:
        content = file.read()
        return content.split("\n")
