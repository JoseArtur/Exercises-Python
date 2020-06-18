from random import sample
print('-'*40)
print( 'SORTEIO DE ORDEM DE 4 NOMES \nINSIRA ABAIXO OS 4 NOMES: ')
a1=input('PRIMEIRO NOME: ')
a2=input('SEGUNDO NOME: ')
a3=input('TERCEIRO NOME: ')
a4=input("QUARTO NOME: ")
lista=sample([a1,a2,a3,a4],4)
print('ESSA É A ORDEM:',lista)