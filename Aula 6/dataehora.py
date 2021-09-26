import datetime
'''
print( datetime.datetime.now())
'''
'''
data_atual = datetime.now()
print(data_atual.strftime('%d%m%y%H%M%S'))

'''

from datetime import datetime

dh = datetime.now()
dh = dh.strftime('%H:%M:%S %d/%m/%Y')

print(dh)