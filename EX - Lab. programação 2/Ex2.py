valor_produto = float(input("Informe o valor do seu produto: "))

desconto = valor_produto * 15/100

valor_com_desconto = valor_produto - desconto

print("Valor total: {:.2f}".format(valor_com_desconto))
print("(Valor integral: {:.2f} - Desconto: {:.2f})".format(valor_produto, desconto))