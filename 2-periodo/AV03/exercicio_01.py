from defs_ex01.Q1_liste_input import liste_input
from defs_ex01.Q2_liste_ordem_crescente import liste_ordem_crescente

#1 - Crie um programa que solicite ao usuário que digite uma string (input) e liste todos os jogos que contém a mesma.
search = input("Título: ")
liste_input(search)

#2 - Liste os jogos cadastrados pelo título em ordem crescente
liste_ordem_crescente()

#3 - Liste jogos que contém "k" no título ou no subtítulo
liste_input('k')
