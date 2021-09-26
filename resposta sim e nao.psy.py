#!/usr/bin/env python3

from random import randrange

questions = {
	'a': 'Palmeiras tem mundial?',
	'b': 'Corinthians tem mundial?'
}

answer1 = [
	'Não tem copinha e nem mundial',
	'Não tem copinha e nem mundial'  
	
	]

answer2 = [
	'Sim, o Corinthians tem mundial',
	'Sim, o Corinthians tem mundial',
	
	]

def main():
	while True:
		qst = input('Entre com a pergunta: ')
		if qst == questions['a']:
			print('\n\tO resultado é:  %s\n' %answer1[randrange(len(answer1))])
		elif qst == questions['b']:
			print('\n\tO resultado é:  %s\n' %answer2[randrange(len(answer2))])
		else:
			print('\n\tDesculpe, não entendi...\n')

if __name__ == '__main__':
	main() 
