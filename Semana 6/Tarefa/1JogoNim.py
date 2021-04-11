#n - numero de peças inicialmente no tabuleiro
#m - numero de peças que vao ser retiradas no maximo, sendo maior que 0
def computador_escolhe_jogada(n,m):
    jogadaValida = False
    tentativa = 1
    jogada = 1
    
    while(not jogadaValida) and (jogada <= m): 
        if(n - jogada)%(m + 1) == 0:
            jogadaValida = True #achou a jogada perfeita
        else:
            tentativa = tentativa + 1
            jogada = jogada + 1

    if not jogadaValida:
        jogada = m
    return jogada

def usuario_escolhe_jogada(n,m):
    jogadaValida = False
    
    while not jogadaValida:
        jogada = int(input("Quantas peças você vai tirar? "))
        print( n)
        if (jogada <= m) and (jogada > 0) and (jogada <= n):
            jogadaValida = True
        else:
            print("Oops! Jogada inválida! Tente de novo. ")
    return jogada

def campeonato():
    global uPlacar
    global cPlacar 
    cont = 0
    
    while cont < 3:
        print("")
        print("*** Rodada",cont+1,"***")
        print("")
        partida()
        cont = cont + 1
    print("")
    print("*** Final do campeonato! ***")
    print("Placar: Você",uPlacar,"X",cPlacar,"Computador")
        
def menu():
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print("")
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato")
    escolha = int(input(""))
    print("")
    if escolha == 1:
        print("Você escolheu uma partida isolada")
        print("")
        partida()
        
    elif escolha == 2:
        print("Você escolheu um campeonato")
        print("")
        campeonato()
    else:
        print("Escolha invalida")
        print("")
        menu()
    
def partida():
    global uPlacar
    global cPlacar 
    n = int(input("Quantas peças iniciais? "))
    m = int(input("Limite de peças por jogada? "))
    print("")

    pc = False
    if n % (m+1) != 0:
        pc = True
        print("O computador começa!")
        print("")
    else:
        print("Você começa!")
        print("")
        
    while n > 0:
        if pc == True:
            valorRemovido = computador_escolhe_jogada(n,m)
            n = n - valorRemovido
            print("O computador retirou",valorRemovido,"peças.")
            print("Agora restam",n,"peças no tabuleiro.")
            print("")
            vencedor = "Computador"
        if n > 0:
            valorRemovido = usuario_escolhe_jogada(n,m)
            n = n - valorRemovido
            print("Você retirou",valorRemovido,"peças.")
            print("Agora restam",n,"peças no tabuleiro.")
            print("")
            vencedor = "Você"
            pc = True
            
    print("Fim de jogo!O",vencedor,"ganhou!")
    if vencedor == "Computador":
        cPlacar = cPlacar + 1
    elif vencedor == "Você":
        uPlacar = uPlacar + 1
#main
uPlacar = 0
cPlacar = 0
menu()

