"""
# exemplos de variaveis numericas
numero1 = 29 # numerica inteira
idade = 35 # num int
preco = 10.5 # num float


# exemplos de variaveis string
nomeCompleto = "Jose Alves"
tituloDaPage = "**** Restaurante Panela velha"
simbolo "£æ↓→"
# exemplo variavel boleana (true/false)
casado = True
solteiro = False
funcionario = True


datanasc = input("Em que ano você nasceu? ") # lembre-se que dados coletados sao do tipo string caso vc queira fazer calculos numericos
idade = 2021 - int(datanasc)
print("Sua idade é " + str(idade) + " anos.")
if idade < 18:
	print ("Você é menor de idade ")
else: 
	print("Você é maior de idade ")
	"""
nomecompleto = input("Qual é o seu nome completo ? ")
if "Araujo" in nomecompleto:
	print("Você é da familia Araujo ")
	print(" Legal!")
else: 
	print("Não conheço sua familia ")
	print ("Puxa vida!")
	