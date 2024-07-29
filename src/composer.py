import tkinter.messagebox as mb
from src.files import *

# Gera a composição de k-mers de uma sequência (SHOTGUN)
def gerar_composicao_kmer(sequencia, k):
    fita = []
    for i in range(len(sequencia) - k + 1):
        kmer = sequencia[i:i+k]
        fita.append(kmer)
    fita.sort()
    return fita

# Converte uma lista de k-mers em texto separado por vírgulas
def transformar_kmer_texto(composicao):
    mers = ", ".join(composicao).replace(" ","").replace("[","").replace("]","").replace("'","")
    return mers

# Gera e salva a composição k-mers
def mainComposer(sequencia, k, arquivo_entrada):
    arquivo_saida = 'composicao_kmers.txt'
    if arquivo_entrada == "" and sequencia == "":
        mb.showerror("Não foi informado sequencia nem arquivo. Tente novamente")
        return
    elif arquivo_entrada != "":
        arquivo = Arquivo(arquivo_entrada)
        try:
            sequencia = arquivo.abreArquivo()
        except:
            mb.showerror(f'Arquivo {arquivo.arquivo} não encontrado. Tente novamente')
            return
    if k != "":
        try:
            k = int(k)
        except:
            mb.showerror('Insira um valor inteiro positivo para k')
            return
        if k > 0:
            composicao = gerar_composicao_kmer(sequencia, k)
            composicao = transformar_kmer_texto(composicao)
        else:
            mb.showerror("Insira um valor inteiro positivo para k")
            return
    else:
        mb.showerror("k não pode estar vazio")
        return
    saida = Arquivo(arquivo_saida)
    saida.escreveArquivo(composicao)
    mb.showinfo('SUCESSO',f"Composição de k-mers salva em {arquivo_saida}")