n = int(input("Informe um numero inteiro: "))


for i in range (1, n + 1):
  
  if n <= 100 or n >= 1000:
    print("Valor inválido!\ninforme uma numero entre 100 e 1000")
    n = int(input())
  
  elif i % 4 == 0:
    print('PIN')
  else:
    contador_pin = 0
    for pin in str(i):
      
      if pin == '4':
        contador_pin += 1
    
    if contador_pin > 0:
      print('PIN')
    
    else:
        print(i)