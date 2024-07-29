class Node:
    def __init__(self, nome):
        self.nome = nome
        self.qtdPrefixo = 0
        self.qtdSufixo = 0
        self.diferenca = 0
        self.sufixos = []
    
    def aumentaQtdPrefixos(self):
        self.qtdPrefixo += 1
        self.diferenca = self.qtdPrefixo - self.qtdSufixo

    def aumentaQtdSufixos(self):
        self.qtdSufixo += 1
        self.diferenca = self.qtdPrefixo - self.qtdSufixo

    def adicionaSufixo(self, sufixo):
        self.sufixos.append(sufixo)