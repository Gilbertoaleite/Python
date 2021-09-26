# importa o módulo meumodulo.py e
# chama as funções bd() e bn()
# especificando o nome do módulo
import meumodulo
meumodulo.bd("Richard")
meumodulo.bn("Pedro")


# outro jeito de importar módulo
# o qual permite acessar as funções
# diretamente, ou seja, sem especificar
# nome do modulo antes da função
from meumodulo import *
bd("Paulo")
bn("Maria")