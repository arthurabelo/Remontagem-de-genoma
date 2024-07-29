# Exibição gráfica da composição

import os
import matplotlib.pyplot as plt
import networkx as nx

class VisualizadorGrafoKmers:
    def __init__(self, fita):
        self.fita = fita

    def kmers(self, seq,k):
        kmers =[]
        if(k > len(seq)):
            return kmers
        for i in range(len(seq) - k + 1):
            kmers.append(seq[i:i+k])

        return kmers

    def DeBruijnGrafo(self, mers, k):
        #Passo 1 : pegar todos k-mers da fita
        k_mers = []
        temp = []
        for i in mers:
            temp = self.kmers(i,k)
            k_mers.extend(temp)

        #Passo 2 : pegar nós de prefixos e sufixos k-1-mer conectados por edges
        edges = {}
        for i in k_mers:
            edges[i] = [i[0:k-1],i[1:]]

        G = nx.DiGraph()

        #Passo 3: Adiciona os nós e arestas ao grafo visual
        for i in edges:
            G.add_edge(edges[i][0], edges[i][1])

        # Calcula o tamanho do grafo para ajustes dinâmicos
        graph_size = len(G.nodes())
        node_size_adjusted = max(300, 700 / max(1, graph_size / 5))  # Ajusta o tamanho dos nós
        font_size_adjusted = max(10, 12 / max(1, graph_size / 10))  # Ajusta o tamanho da fonte
        
        # Define limites máximos para largura e altura para evitar excesso de uso de memória
        max_fig_width = 100
        max_fig_height = 100

        fig_width = min(max(6, graph_size * 10), max_fig_width)  # Aumenta width de acordo com que o grafo aumenta, com limite máximo
        fig_height = min(max(6, graph_size * 10), max_fig_height)  # Aumenta height de acordo com que o grafo aumenta, com limite máximo
        plt.figure(figsize=(fig_width, fig_height)) # Define o tamanho da figura
        plt.subplots_adjust(left=0, bottom=0, right=1, top=1)  # Ajusta os parâmetros do subplot

        # Desenha o grafo com ajustes dinâmicos
        pos = nx.spring_layout(G)
        nx.draw_networkx(G, pos, with_labels=True, node_size=node_size_adjusted, font_size=font_size_adjusted)

        # Converte as edges em tuplas, cria um dict e desenha os edges
        for i in edges:
            edges[i] = tuple(edges[i])
        graphNodes = dict(zip(edges.values(), edges.keys()))
        nx.draw_networkx_edge_labels(G, pos, edge_labels=graphNodes, bbox=None, alpha=0.5)

        # Salva o grafo
        if not os.path.exists('imagens'):
            os.makedirs('imagens')
        plt.savefig("imagens/DeBruijnGraph_{}_{}-K{}.png".format(self.fita[:3], self.fita[-3:], k))
        plt.show()

    def visualizar_grafo(self, k):
        listafita = []
        listafita.append(self.fita)
        self.DeBruijnGrafo(listafita, k)