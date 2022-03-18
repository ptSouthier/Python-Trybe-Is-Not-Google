def exists_word(word, instance):
    search_result = list()
    for index in range(len(instance)):
        curr_file = instance.search(index)
        search_data = {}
        search_data["palavra"] = word
        search_data["arquivo"] = curr_file["nome_do_arquivo"]
        search_data["ocorrencias"] = list()
        for line_index in range(curr_file["qtd_linhas"]):
            if word in curr_file["linhas_do_arquivo"][line_index].split(" "):
                search_data["ocorrencias"].append({"linha": line_index})
    #     line_words = curr_file["linhas_do_arquivo"][line_index].split(" ")
    #     for curr_word in line_words:
    #         if curr_word == word:
    #             search_data["ocorrencias"].append({"linha": line_index})
        if len(search_data["ocorrencias"]) > 0:
            search_result.append(search_data)
    return search_result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
