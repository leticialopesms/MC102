n = int(input())                                    #Número de salas do mapa.
 
lista_salas = []
for i in range(n):
    salas = input().split()                         #Lista de salas existentes no mapa.
    salas = list(map(int, salas[1:n+1]))
    lista_salas.append(salas)
 
quantidade_itens = int(input())                     #Número de itens no mapa.
 
itens_em_salas = [0] * n
for j in range(quantidade_itens):
    numero_sala, nome_item = input().split()        #Lista de itens a serem distribuídos no mapa.
    numero_sala = int(numero_sala)
    sala_e_item = [numero_sala, nome_item]
    itens_em_salas.pop(numero_sala)
    itens_em_salas.insert(numero_sala, sala_e_item)
 
numero_sala_clone = int(input())                    #Sala onde o clone está.
 
numero_sala_bot = int(input())                      #Sala inicial do bot.
 
tamanho_inventario = int(input())                   #Tamanho do inventário.
inventario = []
 
trajeto = list(map(int, input().split()))           #Salas por onde o bot vai passar.
 
 
 
class Mapa:
    '''Define a classe Mapa.
    Armazena o número de salas.'''
 
    def __init__(self, sala):
        self._sala = sala
 
    def entra_em_sala(self):
        '''Indica para qual sala o jogador deve se mover.'''
        sala_atual = trajeto[0]
        print("Mover para sala", sala_atual)
        trajeto.pop(0)
        return sala_atual
 
 
class Sala:
    '''Define a classe Sala.
    Determina a condição da sala onde o bot está a cada rodada.'''
 
    def __init__(self, sala_oponente):
        self.sala_oponente = sala_oponente
 
    def igual_sala_oponente(self, sala_oponente):
        '''Verifica se a sala do bot é igual, ou não, à sala do clone.'''
        if numero_sala_bot == sala_oponente:
            return True
 
    def sala_vazia(self):
        '''Verifica se há item na sala.
        Se houver, indica o item.'''
        if sala_e_item == 0:
            return True
        else:
            global nome_item
            nome_item = sala_e_item[1]
            return False
 
 
class Item:
    '''Define a classe Item.
    Estabelece métodos para executar as ações que o bot deve fazer com cada item.'''
 
    def __init__(self, item, sala_do_item):
        self.item = item
        self.sala_do_item = sala_do_item
 
    def pegar(self, sala_do_item):
        '''Pega e remove o item da sala.'''
        print("Pegar", self.item)
        if len(inventario) < tamanho_inventario:
            global itens_em_salas
            itens_em_salas[sala_do_item] = 0
 
    def adicionar(self, item):
        '''Adiciona item ao inventário'''
        if len(inventario) < tamanho_inventario:
            print(self.item, "adicionado ao inventário")
            inventario.append(item)
        else:
            print("Inventário cheio!")
 
 
 
print('''Bem-vindo as Aventuras de Sarah 2.0
      Sarah acorda no saguão do antigo castelo de sua família, 
      ela tem a oportunidade única de derrotar o seu clone maligno
      que se apoderou do reino. Para isso ela deve encontrar o baú
      da sua família que contém a espada mágica que apenas a verdadeira
      herdeira pode utilizar.
      Na sala onde está Sarah vê várias portas. Qual é a sua próxima ação?''')
 
print("DEBUG - O clone está na sala:", numero_sala_clone)
 
for k in range(len(trajeto) + 1):
 
    sala_bot = Sala(numero_sala_clone)
 
    if not sala_bot.igual_sala_oponente(numero_sala_clone):
        sala_e_item = itens_em_salas[int(numero_sala_bot)]
        if sala_bot.sala_vazia():
            print('''Você está na sala de número''', numero_sala_bot,'''e dela você pode ir para as salas''', lista_salas[int(numero_sala_bot)])
        else:
            print('''Você está na sala de número''', numero_sala_bot,
                  '''ela contém um baú com''', nome_item, 
                  '''e dela você pode ir para as salas''', 
                  lista_salas[int(numero_sala_bot)])
            item = Item(nome_item, numero_sala_bot)
            item.pegar(numero_sala_bot)
            item.adicionar(nome_item)
 
            if "poção" in inventario:
                print('''Você pegou a poção da morte e virou pó instantaneamente.
                      Tente novamente...''')
                break
 
        castelo = Mapa(lista_salas)
 
        sala_bot = castelo.entra_em_sala()
        numero_sala_bot = int(sala_bot)
    else:
        if "espada" in inventario:
            print('''Você derrotou o clone maligno com a espada mágica!
                  Com a Sarah no reino o mundo pode voltar ao equilíbrio.
                  PARABÉNS!''')
        else:
            print('''Infelizmente você encontrou o clone sem a espada das
                  fadas e foi derrotado. Tente novamente...''')
        break