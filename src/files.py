class Arquivo:
    def __init__(self, arquivo):
        self.arquivo = arquivo
        self.dados = None
        self.kmer = None
    
    #Lê arquivo de sequencias k-mers e retorna uma lista deles
    def abreArquivoSequencias(self):
        with open(self.arquivo, 'r', encoding='utf-8') as f:
            dados = f.read()
            sequencias = self.quebraEmLista(dados)
            sequencias.sort()
        return sequencias
    
    #Lê arquivo de entrada/saida
    def abreArquivo(self):
        with open(self.arquivo, 'r', encoding='utf-8') as f:
            dados = f.read()
        return dados
    
    #Obtem as sequências de entrada, trata e quebra em uma lista.
    def quebraEmLista(self, dados):
        sequencias = dados.replace(' ', '').replace('\n', '').split(',')
        self.kmer = len(sequencias[0])
        if sequencias[-1]:
            return sequencias
        else:
            return sequencias[:-1]
    
    #Salva os dados no arquivo desejado.
    def escreveArquivo(self, dados):
        with open(self.arquivo, 'w', encoding='utf-8') as f:
            f.write(dados)