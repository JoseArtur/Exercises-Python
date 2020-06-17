num=int(input('Digite um numero inteiro: '))
esc=int(input('Escolha uma Base Numerica para Conversação:  \n [1] Binario \n [2] Octal \n [3] Hexadecimal   \n  '))
if esc==1:
  print (bin(num)[2:])
elif esc==2:
  print(oct(num)[2:])
elif esc==3:
  print(hex(num)[2:])
else:
  print('Tente Novamente')