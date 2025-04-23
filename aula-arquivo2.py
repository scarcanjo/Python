import os
#fechar e verificar status do arquivo:

arquivo1 = open('dados1.txt')

print(arquivo1.closed)

arquivo1.close()

print(arquivo1.closed)

#Verificar caminho do arquivo

print(os.path.realpath('dados1.txt'))
print(os.path.abspath('dados1.txt'))