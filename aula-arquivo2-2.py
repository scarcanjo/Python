import os
arquivo= open('dados1.txt','r')

read= arquivo.read()

print("Arquivo em unica string:",repr(read))

arquivo.close
arquivo= open('dados1.txt','r')

readline= arquivo.readline()
print("Arquivo com caracteres:",repr(readline))
readline2= arquivo.readline()
print("Arquivo com caracteres:",repr(readline2))
readline3= arquivo.readline()
print("Arquivo com caracteres:",repr(readline3))
readline4= arquivo.readline()
print("Arquivo com caracteres:",repr(readline4))

arquivo.close
arquivo= open('dados1.txt','r')

readlines= arquivo.readlines()
print("Arquivo por linhas:",repr(readlines))

arquivo.close