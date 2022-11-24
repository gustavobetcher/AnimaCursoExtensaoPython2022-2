# comando input(): = permite o user digitar
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

print(f"Boa noite, seu nome é {nome}")
print("Sua idade é {}".format(idade))

#Dobro da idade
dobro = idade * 2
print("O dobro da idade informada é {}".format(dobro))

# If e Else
if idade >= 18:
  print("Você é maior de idade, ótimo! Já pode beber ou dirigir")
else:
  print("Você é menor de idade")

genero = input("Informe o gênero M=Masculino, F=Feminino, O=Outros: ")
if idade >= 18 and genero == "M":
  print("... e você também precisa/precisou prestar o serviço militar obrigatório")
