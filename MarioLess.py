n = 8

for linhas in range(1, n + 1):
    for blocos in range(1, n + 1):
        if blocos > n - linhas:
            print("#", end="")
        else:
            print(" ", end="")
        
    print()
