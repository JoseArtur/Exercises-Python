ano=int(input('Digite um ano para descobrir se é Bissexto: '))
if ((ano%100)%4==0 and ano%100!=0) or (ano%400==0):
  print('ESSE É UM ANO BISSEXTO')
else:
  print('ESSE NAO É UM ANO BISSEXTO')