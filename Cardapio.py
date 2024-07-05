"""
Cardápio:

Código | Especificação | Preço
   1    Cachorro-Quente R$  4.00
   2    X-Salada        R$  4.50    
   3    X-Bacon         R$  5.00
   4    Torrada Simples R$  2.00
   5    Refrigerante    R$  1.50
   
"""

x = input().split()

total = 0

for valor in x:
    if valor == '1':
        total += 4
    
    elif valor == '2':
        total += 4.5
    
    elif valor == '3':
        total += 5
    
    elif valor == '4':
        total += 2
    
    else:
        total += 1.5

print("Total: R$ {:.2f}".format(total))
