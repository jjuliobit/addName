lista = []


def add(a):
    if ad in lista:
        print('O nome já existe na lista.')
    else:
        print(f'Adicionado: {ad} na lista com sucesso.')
        lista.append(a)

def remover(a):
    lista.remove(a)
    return

def remover_tudo(a):
    lista.clear()
    return a

def ver_lista():
    if not lista == []:
     print('========== LISTA ==========')
     print(f'Listas: {lista}')
    else:
        print('========== LISTAS VAZIAS ==========')


while True:
    user = input('Digite\n add, remove, remove all, lista: ')
    if user == 'add':
        ad = input('Qual nome que deseja adicionar? ')
        add(ad)
    if user == 'remove':
        remova = input('qual nome que deseja remover? ')
        remover(remova)
    if user == 'remove all':
        remova_all = input('Certeza que quer remover tudo? Digite (s) ou (n)')
        if remova_all == 's':
            remover_tudo(remova_all)
    if user == 'lista':
        ver_lista()
