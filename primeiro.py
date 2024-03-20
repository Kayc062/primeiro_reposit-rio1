import random
from time import sleep
while True:
    tentativas = 10
    aleatorio = random.randrange(0, 100)
    print('Bem vindo ao jogo de adivinhação de números')
    print('Tente adivinhar o número de 0 a 100. Você tem 10 tentativas.')
    while tentativas > 0:
        num = int(input('Digite seu palpite: '))
        print('PROCESSANDO....')
        sleep(2)   
        if aleatorio > num:
            print('Mais... Tente outra vez.')
        elif aleatorio < num:
            print('Menos... Tente outra vez.')
        else:
            print('Parabéns! Você acertou com {} tentativas.'.format(11 - tentativas))
            break  
        tentativas -= 1
    if tentativas == 0:
        print('Número máximo de tentativas atingido. O número correto era {}.'.format(aleatorio))
    jogar_novamente = input('Deseja jogar novamente? (s/n): ')
    if jogar_novamente.lower() != 's':
        print('Obrigado por jogar. Até mais!')
        break