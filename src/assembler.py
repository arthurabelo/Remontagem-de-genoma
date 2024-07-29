import copy
import tkinter.messagebox as mb
from src.node import *
from src.files import *
from src.grafo import *
from src.visualizador import *

#Quebra as sequencias em K-mers menores, retornando o prefixo e o sufixo
def quebraEmKmer(sequencia, k):
    k-=1
    sequenciaQuebrada = []
    for indice in range(len(sequencia) - k+1):
        sequenciaQuebrada.append(sequencia[indice:k+indice])
    #Prefixo, Sufixo
    return sequenciaQuebrada[0], sequenciaQuebrada[1]

#Concatena o mer atual à fita.
def adicionaFita(fita, mer):
    fita+=mer[-1]
    return fita

#Controi o grafo adicionando os vértices e as arestas do grafo.
def montaGrafo(grafo, sequencias, k):
    for sequencia in sequencias.dados:
        prefixo, sufixo = quebraEmKmer(sequencia, k)
        noPrefixo, noSufixo = Node(prefixo), Node(sufixo)
        #Adicionando o prefixo como vértice no grafo.
        if grafo.adicionaNoGrafo(noPrefixo.nome, noPrefixo):
            #O nó foi prefixo mais uma vez, aumenta a quantidade
            noPrefixo.aumentaQtdPrefixos()
            #O sufixo é adicionado à lista de sufixos do nó prefixo
            noPrefixo.adicionaSufixo(noSufixo.nome)
        #Caso ele já exista no grafo.
        else:
            #Adiciona o sufixo na lista de sufixos do nó.
            grafo.grafo[noPrefixo.nome].adicionaSufixo(noSufixo.nome)
            #O nó foi prefixo mais uma vez, aumenta a quantidade
            grafo.grafo[noPrefixo.nome].aumentaQtdPrefixos()
        #Adiciona o sufixo como vértice no grafo
        if grafo.adicionaNoGrafo(noSufixo.nome, noSufixo):
            #O nó foi sufixo mais uma vez.
            noSufixo.aumentaQtdSufixos()
        #Caso o sufixo já esteja no grafo.
        else:
            #Aumenta a quantidade de vezes que o Nó foi sufixo.
            grafo.grafo[noSufixo.nome].aumentaQtdSufixos()

#Busca o vértice inicial e o vértice final do caminho Euleriano comparando o parâmetro diferenca.
def defineInicioFim(grafo):
    #Vértice inicial e vértice final.
    inicial, final = None, None
    for item in list(grafo.grafo.keys()):
        # OBS: Para cada nó, a quantidade de arestas que chegam é a mesma que sai, exceto para o nó inicial e final
        if grafo.grafo[item].diferenca > 0: # 1
            inicial = grafo.grafo[item]
        elif grafo.grafo[item].diferenca < 0: # -1
            final = grafo.grafo[item]            
    return inicial, final

#Reconstrói o caminho Euleriano
def reconstrucao(grafoFinal, k):
    fita = ''
    fitaUm, fitaAuxiliar, fitaDois = '', '', ''
    # Define o início e o fim do caminho Euleriano
    inicial, final = defineInicioFim(grafoFinal)
    # Verifica se é possível percorrer um caminho Euleriano
    if inicial is None or final is None:
        mb.showinfo('INFO', 'Não é possível percorrer um caminho Euleriano!')
        return False
    # Inicia a construção da fita com o nome do vértice inicial
    fita += inicial.nome
    proximo = inicial
    # Continua percorrendo o grafo até que todos os vértices sejam visitados
    while grafoFinal.grafo:
        try:
            # Verifica se o vértice atual tem sufixos para explorar
            if grafoFinal.grafo[proximo.nome].sufixos:
                # Seleciona e remove o próximo sufixo da lista do vértice atual
                sufixoAtual = grafoFinal.grafo[proximo.nome].sufixos.pop(0)
                # Atualiza o próximo vértice a ser visitado
                proximo = grafoFinal.grafo[sufixoAtual]
                # Adiciona o sufixo atual à fita
                fita = adicionaFita(fita, sufixoAtual)
                #Se após a remoção a lista de sufixos ficar vazia.
                if len(grafoFinal.grafo[proximo.nome].sufixos) == 0:
                    #Remove o vértice do grafo.
                    grafoFinal.removeDoGrafo(proximo.nome)
                #Se não existir chave no grafo que coincida com o sufixo atual
                if grafoFinal.pesquisaChave(proximo.nome) == False:
                    fitaAuxiliar = fita
                    fita = fitaUm+fitaAuxiliar+fitaDois
                    #Percorre a fita que já foi criada
                    for base in range(0,len(fita)-1):
                        #Percorre cada mer
                        merAtual = fita[base:base+k]
                        #Se esse mer da fita for vértice do grafo.
                        if grafoFinal.pesquisaChave(merAtual) == True:
                            #Se a lista de sufixos desse vértice não for vazia.
                            if len(grafoFinal.grafo[merAtual].sufixos) != 0:
                                #O próximo que antes era nulo, será esse vértice.
                                proximo = grafoFinal.grafo[merAtual]
                                #A primeira parte da fita será do inicio da fita até o mer encontrado.
                                fitaUm = fita[0:base+k]
                                #A segunda parte da fita será do mer encontrado até o fim da fita.
                                fitaDois = fita[base+k:len(fita)]
                                #A fita é reiniciada.
                                fita = ""
                                break
            else:
                    #Remove o vértice do grafo.
                    grafoFinal.removeDoGrafo(proximo.nome)
        except KeyError:
            #Programa finalizado.
            break
    return fita

def mainAssembler():
    nome_arquivo_entrada = 'composicao_kmers.txt'
    arquivo_saida = 'ArthurCarvalho.txt' # No PDF da atividade pediu como saída um arquivo com o primeiro e último nome
    arquivo_saida_2 = 'output.txt' # Na atividade do SIGAA pediu output.txt como saída
    sequencias = Arquivo(nome_arquivo_entrada)
    sequencias.dados = sequencias.abreArquivoSequencias()
    k = sequencias.kmer
    saida = Arquivo(arquivo_saida) # PDF
    saida2 = Arquivo(arquivo_saida_2) # SIGAA
    grafo = Grafo()
    montaGrafo(grafo, sequencias, k)
    inicial, final = defineInicioFim(grafo)
    grafo_copia = copy.deepcopy(grafo)
    if k is not None:
        fita = reconstrucao(grafo_copia,k-1)
    if fita != False:
        saida.escreveArquivo(fita)
        saida2.escreveArquivo(fita) # SIGAA
        mb.showinfo('SUCESSO',f"Genoma remontado salvo em {arquivo_saida}")