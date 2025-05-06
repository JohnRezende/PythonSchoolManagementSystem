# João Victor Alves de Rezende
# Análise e Desenvolvimento de Sistemas
# Sistema de Gerenciamento de uma escola hipotética

import json  # Importando biblioteca para persistência de dados
import time  # Importando biblioteca para utilizar função .sleep para navegar entre os menus

# Arquivos de persistência para cada "classe" (não utilizei classes)
arquivo_estudante = "estudantes.json"
arquivo_professor = "professores.json"
arquivo_disciplina = "disciplinas.json"
arquivo_turma = "turmas.json"
arquivo_matricula = "matriculas.json"

# Campos (lista de tuplas) para cada tipo de dado
campos_estudante = [("codigo", int), ("nome", str), ("CPF", str)]
campos_professor = [("codigo", int), ("nome", str), ("CPF", str)]
campos_disciplina = [("codigo", int), ("nome", str)]
campos_turma = [("codigo", int), ("codigo_professor", int),
                ("codigo_disciplina", int)]
campos_matricula = [("codigo_turma", int), ("codigo_estudante", int)]

# Criação de funções


def main_menu():  # Função para mostrar menu principal
    print('\n===== MENU PRINCIPAL =====')
    print('(1) Gerenciar estudantes')
    print('(2) Gerenciar professores')
    print('(3) Gerenciar disciplinas')
    print('(4) Gerenciar turmas')
    print('(5) Gerenciar matrículas')
    print('(9) Sair')


def sub_menu():  # Função para mostrar menu secundário
    print('\n- - - MENU DE OPERAÇÕES - - -')
    print('(1) Incluir')
    print('(2) Listar')
    print('(3) Atualizar')
    print('(4) Excluir')
    print('(9) Voltar ao menu principal\n')


def ler_arquivo(nome_arquivo):  # Função ler arquivo json
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except:
        return []


def salvar_arquivo(lista, nome_arquivo):  # Função para salvar em arquivo json
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        json.dump(lista, arquivo, ensure_ascii=False, indent=4)


def input_campos(campos):  # Função para criar dicionário para inserir dados
    dados = {}
    for campo, tipo in campos:
        while True:
            try:
                valor = input(f"Digite {campo.replace('_', ' ')}: ")
                dados[campo] = tipo(valor)
                break
            except:
                print(f"Valor inválido para {campo}. Tente novamente.")
    return dados


def incluir(campos, nome_arquivo, validar_codigo=False):  # Função para incluir registros
    print('==== INCLUSÃO ====')
    lista = ler_arquivo(nome_arquivo)
    novo = input_campos(campos)

    if validar_codigo:  # Verifica se já esxiste o código digitado
        for item in lista:
            if item["codigo"] == novo["codigo"]:
                print("Código já existe. Inclusão cancelada.")
                return
    if nome_arquivo == arquivo_turma:  # Verifica se já existe o professor e disciplina digitados
        if not existe_codigo(arquivo_professor, novo['codigo_professor']) or not existe_codigo(arquivo_disciplina, novo['codigo_disciplina']):
            print("Professor ou disciplina não existe. Inclusão cancelada.")
            return
    if nome_arquivo == arquivo_matricula:  # Verifica se a turma e o estudante digitados já existem
        if not existe_codigo(arquivo_turma, novo['codigo_turma']) or not existe_codigo(arquivo_estudante, novo['codigo_estudante']):
            print("Turma ou estudante não existe. Inclusão cancelada.")
            return

    lista.append(novo)
    salvar_arquivo(lista, nome_arquivo)


def listar(nome_arquivo):  # Função para listar registros
    print('==== LISTAGEM ====')
    lista = ler_arquivo(nome_arquivo)
    if not lista:
        print('Nenhum registro encontrado.')
    for item in lista:
        print(item)


def atualizar(campos, nome_arquivo):  # Função para atualizar registros
    print('==== ATUALIZAR ====')
    lista = ler_arquivo(nome_arquivo)
    try:
        cod = int(input('Digite o código do registro a atualizar: '))
    except:
        print("Código inválido.")
        return

    for i, item in enumerate(lista):
        if item["codigo"] == cod:
            print(f"Registro atual: {item}")
            atualizado = input_campos(campos)
            lista[i] = atualizado
            salvar_arquivo(lista, nome_arquivo)
            print("Registro atualizado com sucesso.")
            return
    print("Registro não encontrado.")


def excluir(nome_arquivo):  # Função para excluir registros
    print('==== EXCLUIR ====')
    lista = ler_arquivo(nome_arquivo)
    try:
        cod = int(input('Digite o código do registro a excluir: '))
    except:
        print("Código inválido.")
        return

    for item in lista:
        if item["codigo"] == cod:
            lista.remove(item)
            salvar_arquivo(lista, nome_arquivo)
            print("Registro excluído.")
            return
    print("Registro não encontrado.")


def existe_codigo(nome_arquivo, codigo):  # Função para evitar duplicações de registro
    lista = ler_arquivo(nome_arquivo)
    for item in lista:
        if item['codigo'] == codigo:
            return True
    return False


# Função para processar escolha do menu secundário
def processar_menu_secundario(campos, nome_arquivo, validar_codigo=False):
    while True:
        sub_menu()
        opcao = input('Escolha uma opção: ')
        if opcao == '1':
            incluir(campos, nome_arquivo, validar_codigo)
        elif opcao == '2':
            listar(nome_arquivo)
        elif opcao == '3':
            atualizar(campos, nome_arquivo)
        elif opcao == '4':
            excluir(nome_arquivo)
        elif opcao == '9':
            break
        else:
            print('Opção inválida.')
        time.sleep(1.5)


# Loop principal
while True:
    main_menu()
    escolha = input('Informe a opção desejada: ')
    if escolha == '1':
        processar_menu_secundario(campos_estudante, arquivo_estudante)
    elif escolha == '2':
        processar_menu_secundario(campos_professor, arquivo_professor)
    elif escolha == '3':
        processar_menu_secundario(campos_disciplina, arquivo_disciplina)
    elif escolha == '4':
        processar_menu_secundario(
            campos_turma, arquivo_turma, validar_codigo=True)
    elif escolha == '5':
        processar_menu_secundario(
            campos_matricula, arquivo_matricula, validar_codigo=False)
    elif escolha == '9':
        print('Saindo do sistema...')
        break
    else:
        print('Opção inválida. Tente novamente.')
    time.sleep(1.5)

print('----- VOCÊ SAIU DO SISTEMA -----')
