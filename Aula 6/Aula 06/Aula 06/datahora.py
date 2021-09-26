# exemplo de uso do modulo datetime
# (que já vem instalado junto com Python)
# importa o módulo:
import datetime

# imprime a data e hora diretamente
# chamando a funcao de dentro do módulo
print( datetime.datetime.now() )

# carrega a data e hora na variável dh
# e depois imprime conventendo dh para string
# com o comando str()
dh = datetime.datetime.now()
print("Data e hora atual: " + str(dh) )


