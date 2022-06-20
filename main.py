lista ={
    'nome': [], 
    'idade': [],
}


def add(a):
    if ad_nome in lista['nome']:
        print(f'O nome já existe na lista. ({ad_nome.upper()})')
    else: 
     print(f'Adicionado o nome: ({ad_nome.upper()}) na lista com sucesso.') 
     lista['nome'].append(a)

def add_idade(a):
    if ad_idade in lista['idade']:
     print(f'A idade já existe na lista. ({ad_idade})')
    else:
     print(f'Adicionado a idade: ({ad_idade}) na lista com sucesso.')
     lista['idade'].append(a)


def remover(a):
    if not lista in lista['nome']:
     lista['nome'].remove(a)
    return a

def remover_tudo(a):
    lista.clear()
    print()
    print('Removido com sucesso...')
    ver_lista()
    return a

def ver_lista():
    if not lista == []:
     print()
     print('========== LISTA ==========')
     for nomes in lista.items():
        print(nomes)
    else:
        print('========== LISTAS VAZIAS ==========')
        print({lista})


while True:
    user = input('Digite\n add, remove, remove all, lista: ')
    if user == 'add':
        ad_nome = input('Qual é seu nome?\n -> ')
        add(ad_nome)
        ad_idade = input('Qual é sua idade?\n -> ')
        add_idade(ad_idade)
    if user == 'remove':
        remova = input('Deseja remover o nome ou idade? ')
        remover(remova)
    if user == 'remove all':
        remova_all = input('Certeza que quer remover tudo? Digite\n (s) ou (n) -> ')
        if remova_all != 's':
          print('Não foi removidos.')
        else:
            remover_tudo(remova_all)
    if user == 'lista':
        ver_lista()
