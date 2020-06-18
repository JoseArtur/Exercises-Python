import random
ranu= random.randrange(0,5)
unu=int(input('Digite um numero de 0 a 5: '))
if unu==ranu:
  print('VOCE VENCEU')
else:
  print('A MAQUINA ESCOLHEU {}, TENTE NOVAMENTE'.format(ranu))
