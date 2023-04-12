# > DISCIONÁRIOS

# Criando discionários

discionario = {}
discionario = dict()

discionario = {"nome": "Kaio", "idade": 31, "altura": 1.90}
print(discionario)
print(discionario["idade"])


# Adicionando elementos em um discionário

discionario["programador"] = True
print(discionario)
discionario["altura"] = 2
print(discionario)


# Iterando sobre um discionário

for chave in discionario:
    print(chave, discionario[chave])


# Testando a existência de uma chave

print("peso" in discionario)
print("altura" in discionario)