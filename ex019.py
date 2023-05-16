import random
nome = input("digite o primeiro nome que vai para o sorteio ? ")
nome2 = input("digite o segundo nome que vai para o sorteio ? ")
nome3 = input("digite o terceiro nome que vai para o sorteio ? ")
nome4 = input("digite o quarto nome que vai para o sorteio ? ")
nomes = nome,nome2,nome3,nome4
print(" entre {}, {}, {} e {} o sorteado sortudo foi {}".format(nome,nome2,nome3,nome4, random.choice(nomes)))

