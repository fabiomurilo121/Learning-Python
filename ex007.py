vProduto = int(input("Informe o valor do produto: "))
vDesconto = int(input("Informe o desconto em %: "))

descon = vProduto * vDesconto
descon = descon // 100
result = vProduto - descon

print("O valor do produto era {} e ficou {} com os {}% de desconto".format(vProduto,result,vDesconto))