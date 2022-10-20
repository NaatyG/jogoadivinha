print('********************************')
print('Bem vindo ao jogo de adivinhação')
print('********************************')

numero_secreto = 42
total_tentativas = 3

print('Eu pensei em um número entre 1 e 100. Tente adivinha-lo!')
print('Quer tentar em qual nível de dificuldade?')
print('(1) Fácil  (2) Médio  (3) Difícil')
nivel = int(input("Defina seu nível: "))

if(nivel == 1):
    total_tentativas = 15
elif(nivel == 2):
    total_tentativas = 10
else:
    total_tentativas = 5

for rodada in range(1,total_tentativas + 1):
    print('Tentativa {} de {}'.format(rodada, total_tentativas))
    chute = int(input('Digite seu número: '))
    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if(chute < 1 or chute > 100):
        print('Por favor, apenas números entre 1 e 100')
        continue

    if(acertou):
        print('Parabéns, você acertou!')
        break

    else:
        if(menor):
            print('Lamento, você errou! Seu chute foi menor que o número secreto')
        elif(maior):
            print('Lamento, você errou! Seu chute foi maior que o número secreto')
    


print('FIM DO JOGO')