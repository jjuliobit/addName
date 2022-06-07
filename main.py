from ast import Index


lista = []

def add(a):
    lista.append(a)
    return


def excluir(e):
    lista.remove(e)
    return

def limpar(a):
    lista.clear()
    return a
    

def ver_lista(u):
    if lista == []:
        print('==========Lista vazias===========')
    else:
        print('==========Você está na lista==========')
        print(lista)
    return u 


while True:
 user = input('digite adicionar , apagar, apagar tudo ou lista: ')
 if user == 'adicionar':
     ad = input('qual nome que deseja adicionar? ')
     add(ad)
 elif user == 'apagar':
      d = input('qual nome que deseja apagar, ou deseja tudo digite apagar tudo? ')
      excluir(d)
 elif user == 'apagar tudo':
     cl = input('ceterza que quer apagar tudo?\n digite (s) ou (n): ')
     limpar(cl)
 elif user == 'lista':
      ver_lista(user)
   
     
