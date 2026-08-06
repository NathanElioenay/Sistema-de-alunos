import aluno, notas, media, titulos, arquivos
from time import sleep
alunos = []
arquivo = 'turma.json'
if arquivos.arquivo_existe(arquivo):
    alunos = arquivos.ler_arquivo(arquivo)
else:
    arquivos.criar_arquivo(arquivo)
    alunos = []

while True:
    print('''
1 - Cadastrar Aluno
2 - Lançar Nota
3 - Calcular Média
4 - Aprovado/Reprovado
5 - Ranking
6 - Dados do aluno
0 - Fechar Programa
''')
    try:
        escolha = int(input('Escolha uma opção:'))
        if escolha not in  [1,2,3,4,5,6,0]:
            continue

        if escolha == 1:
            titulos.titulo('CADASTRO DE ALUNOS')
            aluno.cadastrar_aluno(alunos)
            arquivos.salvar_arquivo(arquivo, alunos)
        elif escolha == 2:
            titulos.titulo('LANÇAMENTO DE NOTAS')
            notas.lancar_nota(alunos)
            arquivos.salvar_arquivo(arquivo, alunos)
        elif escolha == 3:
            titulos.titulo('MÉDIA DO ALUNO')
            media.media_aluno(alunos)
        elif escolha == 4:
            titulos.titulo('APROVADO/REPROVADO')
            media.aprovado_reprovado(alunos)
        elif escolha == 5:
            titulos.titulo('RANKING DE ALUNOS')
            notas.ranking(alunos)
        elif escolha == 6:
            aluno.dado_aluno(alunos)
        elif escolha == 0:
            print('Finalizando...')
            sleep(1)
            print('Alterações e cadastros foram armazenados.')
            sleep(1)
            break
    except ValueError:
        print('\033[0;31mError: Opção inválida, Tente novamente!\033[m')
print('Volte sempre!!!')