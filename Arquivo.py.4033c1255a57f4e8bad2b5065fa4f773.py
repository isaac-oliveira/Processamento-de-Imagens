def lerAquivo(path):
    arquivo = []
    with open(path, 'r') as file:
        arquivo += [x for x in file]
        file.close()
    return arquivo


def salvarArquivo(nome, ppm):
    with open(nome + '.ppm', 'w+') as file:
        for linha in ppm:
            file.write(linha + '\n')
        file.close()