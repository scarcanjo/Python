import os
arquivo1 = open("dados1.txt",'w', encoding='utf-8')
print(os.path.abspath(arquivo1.name))

arquivo1.write("Oi")

print(os.path.relpath(arquivo1.name)) #printar nome do arquivo
print(arquivo1)
arquivo1.close() #fecha o arquivo