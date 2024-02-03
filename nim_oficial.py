def partida():
    n = int(input('Quantas peças? '))
    m = int(input('Limite de peças por jogada? '))
    print(' ')
    if n % (m + 1) == 0:
        print('Voce começa!\n') 
        while n > 0:
            c = usuario_escolhe_jogada(n,m)
            n = n - c
            if c > 1:
                print(f'Voce tirou {c} peças.')
            else:
                print('Voce tirou uma peça.')
            if n > 1:
                print(f'Agora restam {n} peças no tabuleiro.\n')
            else:
                print('Agora resta apenas um peça no tabuleiro.\n')
                
            d = computador_escolhe_jogada(n,m)
            n = n - d
            if d > 1:
                print(f'Computador tirou {d} peças')
            else:
                print('Computador tirou uma peça')
            if n > 1:
                print(f'Agora restam {n} peças no tabuleiro.\n')
            elif n == 1:
                print('Agora resta apenas um peça no tabuleiro.\n')
        print('Fim do jogo! O computador ganhou!\n')
    
    else:
        print('Computador começa!\n')
        while n > 0:
            d = computador_escolhe_jogada(n,m)
            n = n - d
            if d > 1:
                print(f'Computador tirou {d} peças')
            else:
                print('Computador tirou uma peça')
            if n > 1:
                print(f'Agora restam {n} peças no tabuleiro.\n')
            elif n == 1:
                print('Agora resta apenas um peça no tabuleiro.\n')
            
            if n > 0:
                c = usuario_escolhe_jogada(n,m)
                n = n - c
                if c > 1:
                    print(f'Voce tirou {c} peças.')
                else:
                    print('Voce tirou uma peça.')
                if n > 1:
                    print(f'Agora restam {n} peças no tabuleiro.\n')
                elif n == 1:
                    print('Agora resta apenas um peça no tabuleiro.\n')
        print('Fim do jogo! O computador ganhou!\n')
            
def computador_escolhe_jogada(n,m):
    b = 1
    while b <= m:
        if (n - b) % (m + 1) == 0:
            return b
        else:
            b = b + 1
    return m

    
        
def usuario_escolhe_jogada(n,m):
  a = int(input('Quantas peças você vai tirar? '))
  while a > m or a == 0:
    print('Oops! Jogada inválida! Tente de novo.\n')
    a = int(input('Quantas peças você vai tirar? '))
    print(' ')
  return a




print('Bem-vindo ao jogo do NIM! Escolha:\n')
print('1 - Para jogar uma partida isolada')
print('2 - Para jogar um campeonato\n')
escolha = int(input())
while escolha != 1 and escolha != 2:
    print('Oops! Escolha inválida! Tente de novo.\n')
    escolha = int(input())
if escolha == 1:
    print('Voce escolheu uma partida isolada!\n')
    partida()
else:
    print('Voce escolheu um campeonato!\n')
    k = 1
    while k <= 3:
        print(f'**** Rodada {k} ****\n')
        partida()
        k = k + 1
    print('**** Final do campeonato! ****\n')
    print('Placar: Você 0 X 3 Computador')
