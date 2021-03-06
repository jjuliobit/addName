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
    try:
     if remova == 'nome':
      lista['nome'].remove(a)
      print('Foi removido com sucesso.')
     if remova == 'idade':
      str(lista['idade'])
      lista['idade'].remove(a)
      print('Foi removido com sucesso.')
    except TypeError as e:
        print(f'Erro: {e}')
    

def remover_tudo(a):
    lista.clear()
    print()
    print('Removido com sucesso...')
    ver_lista()
    return a

def editar(i):
    if edita == 'nome':
     lista['nome'] = i
     print('Editado nome com sucesso.')
    if edita == 'idade':
     lista['idade'] = i
     print('Editado idade com sucesso.')
     


def ver_lista():
    if not lista == []:
     print()
     print('========== LISTA ==========')
     for ls in lista.items():
      print(ls)
    else:
     print('========== LISTAS VAZIAS ==========')
     print(f'{lista}')


while True:
    user = input('Digite:\n add, remove, remove all, editar e lista: ')
    if user == 'add':
        ad_nome = input('Qual é seu nome?\n -> ')
        add(ad_nome)
        ad_idade = input('Qual é sua idade?\n -> ')
        add_idade(ad_idade)
    if user == 'editar':
        edita = input('digite nome ou idade que deseja editar? ')
        if edita == 'nome':
         edite_nome = input('Digite um nome novo.\n -> ')
         editar(edite_nome)
        if edita == 'idade':
         edite_idade = input('Digite uma idade nova.\n -> ')
         editar(edite_idade)
    if user == 'remove':
        remova = input('Deseja remover o nome ou idade? ')
        if remova == 'nome':
         remova_nome = input('Qual nome deseja excluir?  ')
         remover(remova_nome)
        if remova == 'idade':
         remova_idade = input('Qual idade deseja excluir?  ')
         remover(remova_idade)
    if user == 'remove all':
        remova_all = input('Certeza que quer remover tudo? Digite\n (s) ou (n) -> ')
        if remova_all != 's':
          print('Não foi removidos.')
        else:
            remover_tudo(remova_all)
    if user == 'lista':
        ver_lista()
