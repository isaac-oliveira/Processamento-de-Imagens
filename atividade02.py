import Arquivo
import Matriz

def gerarHistograma():
    histograma = []
    for i in range(0, 256):
        histograma.append(0)
    return histograma


def pegarDadosHistograma(matriz, l, a):
    histograma = gerarHistograma()
    for i in range(0, a):
        for j in range(0, l):
            tom = matriz[i][j]
            histograma[tom] += 1
    return histograma


def pj(histograma, total):
    aux = [x / total for x in histograma]
    return aux


def sk(histograma):
    aux = [x for x in histograma]
    for i in range(1, 256):
        aux[i] = aux[i] + aux[i-1]

    return aux


def gk(histograma):
    aux = []
    for i in histograma:
        aux.append(round((i * 255)))
    return aux

def equalizar(matriz, l, a):
    histograma = pegarDadosHistograma(matriz, largura, altura)
    histograma = pj(histograma, largura * altura)
    histograma = sk(histograma)
    histograma = gk(histograma)

    return paraMatriz(histograma, matriz, largura, altura)

def paraMatriz(histograma, matriz, l, a):
    aux = Matriz.gerarMatriz(l, a)
    for i in range(0, a):
        for j in range(0, l):
            tom = matriz[i][j]
            aux[i][j] = histograma[tom]

    return aux


caminho = input('Digite o caminho do arquivo: ')
arquivo = Arquivo.lerAquivo(caminho)
matriz, largura, altura = Matriz.transformarEmMatriz(arquivo)

matriz = equalizar(matriz, largura, altura)

ppm = Matriz.formatoPPM(matriz, largura, altura)
nome = input('Salvar como: ')
Arquivo.salvarArquivo(nome, ppm)
