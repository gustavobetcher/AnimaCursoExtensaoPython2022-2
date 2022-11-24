print("Início da aula 3 (09/11)")

contador = 1

# Exibir de 1 até 10
while(contador <= 10):
  print(contador)
  contador = contador+1


# Laço for (python for = for each)
fruta = "morango"
print(fruta)

fruta1 = "morango"
fruta2 = "laranja"
fruta3 = "pêra"

#Lista
frutas = ["morango", "laranja", "pêra"]


#mostra todas
print(frutas)
#quero exibir apenas a terceira
print(frutas[2])

#Exibir quantas frutas tem na minha lista?
#Lenght = tamanho
print(len(frutas))

#Incluir uma fruta nova
frutas.append("manga")

print(len(frutas))
print(frutas)

print(frutas[0])
print(frutas[1])
print(frutas[2])
print(frutas[3])

print("Exemplo das frutas com while..")
frutas.append("uva")

i=0
while(i<len(frutas)):
  print(frutas[i])
  i = i + 1

print("Exemplo das frutas com FOR")
for fruta in frutas:
  print(fruta)