# Sistema Escolar em Python

##  Sobre o projeto

Este projeto foi desenvolvido com o objetivo de praticar os conceitos fundamentais de Python por meio da criação de um sistema escolar executado no terminal.

O sistema permite cadastrar alunos, lançar notas, calcular médias, verificar a situação do aluno e gerar um ranking baseado no desempenho.

Os dados são armazenados em um arquivo JSON, permitindo que as informações permaneçam salvas entre as execuções do programa.

---

##  Funcionalidades

* Cadastro de alunos
* Busca de alunos pelo nome
* Lançamento de notas
* Cálculo da média
* Verificação da situação do aluno

  * Aprovado
  * Recuperação
  * Reprovado
* Ranking de alunos por média
* Consulta dos dados de um aluno
* Persistência dos dados utilizando JSON

---

##  Tecnologias utilizadas

* Python 3
* Módulos da biblioteca padrão:

  * `json`
  * `os`
  * `datetime`

---

##  Estrutura do projeto

```text
sistema_escolar/
│
├── sistema.py          # Programa principal
├── aluno.py            # Cadastro e consulta de alunos
├── busca.py            # Busca de alunos
├── notas.py            # Lançamento de notas e ranking
├── media.py            # Média e situação do aluno
├── arquivos.py         # Leitura e gravação do JSON
├── titulos.py          # Impressão de títulos
├── turma.json          # Banco de dados em JSON
└── README.md
```

---

##  Como executar

1. Clone este repositório:

```bash
git clone <https://github.com/NathanElioenay/Sistema-de-alunos.git>
```

2. Entre na pasta do projeto:

```bash
cd sistema-de-alunos
```

3. Execute o programa:

```bash
python sistema.py
```

---

##  Menu do sistema

```text
1 - Cadastrar Aluno
2 - Lançar Nota
3 - Calcular Média
4 - Aprovado/Reprovado
5 - Ranking
6 - Dados do aluno
0 - Fechar Programa
```

---

##  Objetivo do projeto

Este projeto foi desenvolvido como prática de programação em Python, com foco nos seguintes conceitos:

* Estruturas de decisão
* Estruturas de repetição
* Listas
* Dicionários
* Funções
* Modularização
* Manipulação de arquivos JSON
* Tratamento de exceções
* Organização de projetos

---

##  Aprendizados

Durante o desenvolvimento foram praticados conceitos importantes, como:

* Separação do código em módulos.
* Persistência de dados utilizando arquivos JSON.
* Manipulação de listas e dicionários.
* Busca e atualização de informações.
* Organização do código para facilitar manutenção e reutilização.

---

##  Autor

Projeto desenvolvido por **NathanElioenay** como parte dos estudos em Python.
