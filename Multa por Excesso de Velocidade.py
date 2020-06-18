velo=float(input('Velocidade do Carro: '))
if velo>80:
  print('VOCE ESTA ACIMA DA VELOCIDADE PERMITIDA\n O preço da sua multa é de R${}'.format((velo-80)*7))
else:
  print('Sua Velocidade esta dentro do permitido, Continue!!!')