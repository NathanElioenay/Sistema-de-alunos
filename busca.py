def buscar_aluno(lista):
    while True: 
        nome = input('Buscar Aluno: ').strip().title()
        if not nome.replace(' ', '').isalpha():
            print('\033[0;31mError: Digite apenas letras!\033[m')
            continue

        for contato in lista:
            if contato['nome'] == nome:
                return contato

        print('Aluno não encontrado!')
        return None
