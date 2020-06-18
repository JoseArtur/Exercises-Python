nome=str(input('Digite seu Primeiro Nome: '))
Nome=nome.capitalize().strip()
print('-*'*20)
print('Seja Bem Vindo ao Simulador  \nDe Aceitação em um Empréstimo Bancario, \n{}!'.format(Nome))
print('-*'*20)
valori=float(input('Qual o valor do imovel de seu interesse?: \nR$ '))
print('-*'*20)

sal=float(input('Qual o seu salario ou renda mensal?: \nR$ '))
print('-*'*20)

anos=int(input('Em quantos anos você quer pagar?:  \n'))
print('-*'*20)

prest=valori/(anos*12)
if prest<0.3*sal and prest*12*anos==valori :
  print('Para pagar o valor de R${}, você deve pagar uma prestação mensal de R${:.2f} por {} anos'.format(valori, prest, anos))
elif prest<0.3*sal and prest*12*anos!=valori:
  print('Caro {}, você inseriu uma quantidade acima do possivel Anos, o maximo para os valores inseridos é de {}'.format(Nome, (valori/sal)/12))
else:
  print('Seu salario de R${} ainda não é suficiente para seu objetivo, o recomendavel é R${:.2f}'.format(sal, prest *10/3))
