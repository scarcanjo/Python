import os
arquivo = open('dados1.txt', 'w', encoding='utf-8')

print("Dados do arquivo:")
print("Nome:",arquivo.name)
print("Modo:",arquivo.mode)
print("O arquivo está fechado?",arquivo.closed)

arquivo.write = ("Olá Mundo!")

arquivo.close()
print("O arquivo está fechado agora?",arquivo.closed)

print("Caminho relativo:", os.path.realpath("dados1.txt"))
print("Caminho caminho absoluto:", os.path.abspath("dados1.txt"))
exit()