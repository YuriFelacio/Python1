"""a = 5
print(type(a))
b = "mari"
print(type(b))
c = 8.5
print(type(c))
d = ()
print(type(d))
e = []
print(type(e))
f = {}
print(type(f))
g = 5+1j
print(type(g))
h = False
print(type(h))
print(type(i))


#tipos de print()
nome = "andré"
idade = "catorze"
print("Olá mr goofy (",nome,") você tem", idade, "anos")
print("Olá mr goofy (" + nome + ") você tem " + idade + " anos")
print("Olá mr goofy ({}) você tem {} anos".format(nome, idade))
print(f"Olá mr goofy ({nome}) você tem {idade} anos ")


#caixa de entrada de dados
n1 = input("Digite seu nome? ")
n2 = input("Digite seu nome? ")
n3 = input("Digite seu nome? ")

print("os nomes são:",n1,",",n2,"e",n3)
print(f"os nomes são: \n {n1} \n {n2} \n e {n3} \n")

dia = 10
mes = 2
ano = 2023

print("João estava andando na padaria", end=", ")
print("porque estava com fome", end=".\n")
print(dia,mes,ano, sep="/")


#criação de listas
nomes = ["Matheus","Marcelo","Barack","Obama","JOEBIDEN"]
print(nomes[4])
nomes[2] = "1"
print(nomes)


#criação de tuplas
carros =("gol","uno","obama","celta","palio")
print(carros[0])
print(carros)
#carros[0] = "mercedes" #error
                                               
#criação de dicionário
peso = {"amanda":55.6,"joao": 70.6, "artur": 55.6}
print(peso)

v1 = int(input("Digite algo: "))
v2 = int(input("Digite algo: "))

print(valor.isnumeric())
print(valor.istitle())
print(valor.isalpha())
print(valor.isalnum())
print(valor.isupper())
print(valor.islower())
print(valor.isdigit())
print(valor.isspace())
print(v1)
type(v1)
print(f"a soma dos valores {v1} e {v2} resulta na soma {v1 + v2}")

result = (2*10)/5**2+(125/5)
print(result)

a = 2371//3
b = 2372561/3
c = 237%5
print(a,b,c, a+b+c)
print(round(b))
print(f"{b: .2f}")

d = 4**2
print(d)
e = pow(4,3)
print(e)

a = input("Digite seu nome: ")
b = "Joaquim"
print(f"Seja bem vindo {a:10}")
print(f"Seja bem vindo {a:<10}")
print(f"Seja bem vindo {a:>10} e {b}")
print(f"Seja bem vindo {a:^10} e {b}")
print(f"Seja bem vindo {a:-^10}")
"""