#Múltiplos de 13

#Minha versao
x = int(input())
y = int(input())

contador = 0

while 1:
    if x <= y:
        while 1:
            if x > y:
                break
            else:
                if x % 13 != 0:
                    contador += x
            x+=1
    else:
        while 1:
            if y > x:
                break
            else:
                if y % 13 != 0:
                    contador += y
            y+=1
    break

print(contador)

#GPT

x = int(input())
y = int(input())

# Garantir que x seja o menor e y seja o maior
if x > y:
    x, y = y, x

contador = 0

for i in range(x, y + 1):
    if i % 13 != 0:
        contador += i

print(contador)
