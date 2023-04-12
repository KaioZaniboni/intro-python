# > ESTRUTURAS CONDICIONAIS

idade = 20

if idade >= 18:
    print("Voce é maior de idade")
else:
    print("Voce é menor de idade")


"""
  Imagine que voce queria imprimir "Aprovada(o)",
  caso o estudante tenha uma média superior ou
  igual a 7, e "Reprovado", caso a média seja
  inferior a 7.
"""

"""
media = float(input("Infrome a média do estudante: "))

if media >= 7:
    print("Voce foi aprovada(o)!")
elif media >= 5:
    print("Recuperação")
else:
    print("Voce foi reprovada(o)!")
"""

media = 10
presenca = 100

if media >= 7 and presenca >= 70:
    print("Aprovado!")
else:
    print("Reprovado")