from tkinter import *

import random
from src.composer import mainComposer
from src.assembler import mainAssembler
from src.visualizador import VisualizadorGrafoKmers
from src.files import *

class App(Tk):
    def __init__(self):
        super().__init__()
        self.title('Remontagem de Genoma')
        self.geometry('350x200')
        self.criar_widgets()

    def criar_widgets(self):
        self.label = Label(self, text="Selecione uma opção:")
        self.label.pack()

        self.button_composer = Button(self, text="Desmontar composição (composer)", command=self.open_input_file)
        self.button_composer.pack()

        self.button_assembler = Button(self, text="Remontar composição (assembler)", command=mainAssembler)
        self.button_assembler.pack()
        
        self.button_visualizar = Button(self, text="Exibir grafo", command=self.exibir_menu_grafo)
        self.button_visualizar.pack()

        self.button_back = Button(self, text="Voltar", command=self.restart_app)
        self.button_back.pack(side=BOTTOM, anchor=SE)

    # Chama outra janela para definir o tamanho do k-mer
    def exibir_menu_grafo(self):        
        self.label.pack_forget()
        self.button_composer.pack_forget()
        self.button_assembler.pack_forget()
        self.button_visualizar.pack_forget()

        self.k_label = Label(self, text="Digite o tamanho do K-mer: *") # Obrigatório
        self.k_label.pack()
        
        self.k_entry = Entry(self)
        self.k_entry.pack()
        
        self.button_open = Button(self, text="Exibir grafo", command=lambda: self.exibir_grafo(self.k_entry.get()))
        self.button_open.config(state=DISABLED)

        def enable_button(e):
            if self.k_entry.get():
                self.button_open.config(state=NORMAL)
            else:
                self.button_open.config(state=DISABLED)

        self.k_entry.bind("<KeyRelease>", enable_button)
        self.button_open.pack()

        self.observacao_label = Label(self, text="OBS: O campo K-mer é obrigatório")
        self.observacao_label.pack()
        
    # Exibe o grafo a partir do arquivo com a sequência
    def exibir_grafo(self, kmer):
        kmer = int(kmer)
        fita = Arquivo('ArthurCarvalho.txt')
        fita = fita.abreArquivo()
        visualizador = VisualizadorGrafoKmers(fita)
        visualizador.visualizar_grafo(kmer)

    # Chama outra janela para inserir nome do arquivo e o valor de k
    def open_input_file(self):
        self.label.pack_forget()
        self.button_composer.pack_forget()
        self.button_assembler.pack_forget()
        self.button_visualizar.pack_forget()

        self.input_label = Label(self, text="Informe o nome do arquivo input: (ArthurCarvalho.txt)") # Opcional. Deixar vazio para entrada manual ou gerar sequência
        self.input_label.pack()

        self.input_entry = Entry(self)
        self.input_entry.pack()
        
        self.k_label = Label(self, text="Digite o tamanho do K-mer: *") # Obrigatório
        self.k_label.pack()

        self.k_entry = Entry(self)
        self.k_entry.pack()

        self.button_open = Button(self, text="Abrir arquivo", command=lambda: self.manualComposer(self.input_entry.get(), self.k_entry.get()))
        self.button_open.config(state=DISABLED)

        def enable_button(e):
            if self.k_entry.get():
                self.button_open.config(state=NORMAL)
            else:
                self.button_open.config(state=DISABLED)

        self.k_entry.bind("<KeyRelease>", enable_button)
        self.button_open.pack()

        self.observacao_label = Label(self, text="OBS: Deixe o nome do arquivo vazio para entrada manual.\nO campo K-mer é obrigatório")
        self.observacao_label.pack()

    # Exibe janela para entrada da sequência manualmente
    def manualComposer(self, arquivo_entrada, kmer):
        self.input_label.pack_forget()
        self.input_entry.pack_forget()
        self.button_open.pack_forget()
        self.k_label.pack_forget()
        self.k_entry.pack_forget()
        self.observacao_label.pack_forget()

        if arquivo_entrada == "":
            self.sequencia_label = Label(self, text="Digite a sequência de DNA:")
            self.sequencia_label.pack()

            self.sequencia_entry = Entry(self)
            self.sequencia_entry.pack()

            self.button_send_composer = Button(self, text="Enviar", command=lambda: mainComposer(self.sequencia_entry.get(), kmer, arquivo_entrada))
            self.button_send_composer.pack()

            self.button_send_generator = Button(self, text="Gerar sequência", command=lambda: self.gerarGenoma(kmer))
            self.button_send_generator.pack()

        else:
            mainComposer('', kmer, arquivo_entrada)

    # Exibe janela para definir quantidade de bases do genoma a ser gerado. Será usado o valor de k informado anteriormente
    def gerarGenoma(self, k):
        self.sequencia_label.pack_forget()
        self.sequencia_entry.pack_forget()
        self.button_send_composer.pack_forget()
        self.button_send_generator.pack_forget()

        self.qtd_bases_label = Label(self, text="Digite a quantidade de bases:")
        self.qtd_bases_label.pack()

        self.qtd_bases_entry = Entry(self)
        self.qtd_bases_entry.pack()

        self.button_send_gerarSequencia = Button(self, text="Gerar sequência", command=lambda: self.gerarSequencia(self.qtd_bases_entry.get(), k))
        self.button_send_gerarSequencia.pack()

    # Gera um genoma aleatório com base na quantidade de bases e valor k informados
    def gerarSequencia(self, quantidade, k):
        k = int(k)
        quantidade = int(quantidade)
        dna = []
        letras = "ACGT"
        genoma = ""
        if(k <= quantidade):
            for _ in range(quantidade):
                num_aleatorio = random.randint(4,1000000)
                letra_atual = letras[num_aleatorio % 4]
                dna.append(letra_atual)
            genoma = "".join(dna)
            mainComposer(genoma, k, "") # Chama o composer para a sequência gerada, que irá quebrá-lo em k-mers
            return True
        else:
            return False

    # Reinicia a aplicação ao clicar em voltar
    def restart_app(self):
        self.destroy()  # Destrói a janela atual
        self.__init__()  # Recria a instância da classe App

if __name__ == "__main__":
    app = App()
    app.mainloop()

