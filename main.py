nome = input("Digite seu nome:")
idade = int(input("Digite sua idade:"))
altura = float(input("Digite sua altura:"))
peso = float(input("Digite seu peso:"))

op=int(input("Estado Civil:\n 1.Casado \n 2.Solteiro \n"))

if op==1.:
    print("Casado")
else:
    print ("Solteiro")

eu=[nome,idade,altura,peso,op]
print (eu)

print("Nome : ", eu[0])
print("Idade : ", eu[1], " anos")
print("Altura: ", eu[2], "m")
print("Peso : ", eu[3], "kg")
print("Casado: ", eu[4])