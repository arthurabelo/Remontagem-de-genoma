# Remontagem de Genoma

Este projeto implementa uma aplicação para remontagem de genomas utilizando a técnica de Shotgun, que divide a composição em k-mers. A aplicação possui uma interface gráfica desenvolvida com Tkinter que permite ao usuário desmontar e remontar composições, além de visualizar grafos de k-mers.

## Funcionalidades

1. **Desmontar Composição (Composer)**:
   - Permite ao usuário inserir manualmente uma sequência ou carregar a partir de um arquivo (Neste exemplo: "ArthurCarvalho.txt" ou "output.txt").
   - Gera a composição de k-mers da sequência fornecida e salva no arquivo composicao_kmers.txt

2. **Remontar Composição (Assembler)**:
   - Lê a composição de k-mers a partir de um arquivo (composicao_kmers.txt).
   - Reconstrói a sequência original e salva em arquivos de saída (Neste exemplo: "ArthurCarvalho.txt" ou "output.txt").

3. **Exibir Grafo**:
   - Gera e exibe o grafo de k-mers a partir de uma sequência fornecida (Neste exemplo: "ArthurCarvalho.txt").

## Como Usar

### Requisitos

- Python 3.x
- Tkinter

### Executando a Aplicação

1. Clone o repositório:
    ```gh repo clone arthurabelo/Remontagem-de-genoma
    ```

2. Execute o arquivo `main.py`:
    ```python main.py
    ```

### Interface Gráfica

1. **Desmontar Composição (Composer)**:
   - Clique no botão `Desmontar composição (composer)`.
   - Informe o nome do arquivo de entrada (opcional) e o tamanho do k-mer (obrigatório).
   - Clique em `Abrir arquivo` para gerar a composição de k-mers.
   - Caso tenha preenchido apenas o tamanho do k-mer, será solicitado que digite a sequência de DNA manualmente e clique em enviar ou, se preferir, clique em Gerar sequência para gerar uma sequência aleatória. Informe a quantidade de bases desejada e clique em Gerar sequência.
   - Será gerada uma sequência aleatória que será armazenada na forma de composição no arquivo `composicao_kmers.txt`.
   - Caso deseje obter a sequência de DNA gerada, clique no botão Voltar e aperte em `Remontar Composição (Assembler)`

2. **Remontar Composição (Assembler)**:
   - Clique no botão `Remontar composição (assembler)`.
   - A sequência será remontada a partir do arquivo `composicao_kmers.txt` e salva nos arquivos `ArthurCarvalho.txt` e `output.txt`.

3. **Exibir Grafo**:
   - Clique no botão "Exibir grafo".
   - Informe o tamanho do k-mer e visualize o grafo gerado a partir do arquivo `ArthurCarvalho.txt`

### Arquivos de Entrada e Saída

- **Entrada**:
  - `composicao_kmers.txt`: Arquivo contendo a composição de k-mers.
  - `ArthurCarvalho.txt`: Arquivo opcional para entrada manual.

- **Saída**:
  - `ArthurCarvalho.txt`: Arquivo de saída com a sequência remontada.
  - `output.txt`: Arquivo de saída com a sequência remontada.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).