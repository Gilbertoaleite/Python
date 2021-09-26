'''
Para rodar esse script
você deve instalar o modulo
vpython primeiro, com o comando:

pip install vpython

NOTA: Essa linha de comando
deve ser digitada no Prompt do
Windows em modo Administrador
'''

# carrega o módulo vpython e em seguida
# chama as funções vpython.sphere() e vpython.vector()
# as quais estão dentro do módulo vpython:
import vpython
vpython.sphere(radius=1.5,color=vpython.vector(1,0,0))


# outra forma de carregar o módulo a qual
# permite chamar as funcões diretamente.
# chama a funcões sphere() e vector(),
# as quais vieram do módulo vpython:
from vpython import *
sphere(radius=1.5,color=vector(1,0,0))
