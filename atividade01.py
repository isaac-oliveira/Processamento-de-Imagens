import Matriz
import Arquivo
# Efeitos


def negativo(matriz, l, a):
    aux = Matriz.gerarMatriz(l, a)
    for i in range(0, a):
        for j in range(0, l):
            aux[i][j] = abs(matriz[i][j] - 255)
    return aux


def limiarizacao(matriz, l, a):
    nivel = int(input('Digite o nível de limiarização: '))
    aux = Matriz.gerarMatriz(l, a)
    for i in range(0, a):
        for j in range(0, l):
            tom = matriz[i][j]
            aux[i][j] = 255 if tom > nivel else 0
    return aux


def mostrarOpcoes():
    print('Escolha uma opção: \n  1 - Negativo\n  2 - Limiarização')


def opcoes(opcao, matriz, l, a):
    index = opcao - 1
    return [negativo, limiarizacao][index](matriz, l, a)


caminho = input('Digite o caminho do arquivo: ')
arquivo = Arquivo.lerAquivo(caminho)
matriz, largura, altura = Matriz.transformarEmMatriz(arquivo)
mostrarOpcoes()
opcao = int(input('Digite uma opção: '))
matriz = opcoes(opcao, matriz, largura, altura)
ppm = Matriz.formatoPPM(matriz, largura, altura)
nome = input('Salvar como: ')
Arquivo.salvarArquivo(nome, ppm)
