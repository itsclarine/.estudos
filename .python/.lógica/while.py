# aprendendo laços de repetições

# enquanto:
# enquanto expressão (faça)
#  bloco 
# fimEnquanto

# =======contar de 0 - 10 =======
contador = 0
while contador <= 10:
  print(contador)
  contador = contador + 1
print('fim da contagem')
print('====================')

# ======contar de 10-0 =======
contador = 10
while contador >= 0:
  print(contador)
  contador = contador - 1
print('fim da contagem')
print('====================')

# =====contar de 10 em 10 começando no 0 =======
contador = 0
while contador <= 100:
  print(contador)
  contador = contador + 10
print('fim da contagem')
print('====================')

# =====ir ate onde o usuario quiser =======
contador_ = int(input('digite um valor para inicar a contagem:'))
print(contador_)
contador = int(input('digite um valor para finalizar a contagem: '))
print(contador)

while contador_ <= contador:
  print(contador_)
  contador_ = contador_ +1
print('fim da contagem')
print('====================') 

