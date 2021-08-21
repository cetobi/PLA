def somaImposto(taxaImposto, custo):
    imposto = float(taxaImposto)
    preco = float(custo)

    imposto /= 100
    taxa = imposto * preco
    precoImposto = preco + taxa

    return precoImposto

taxaImposto = input("Porcentagem do Imposto: ")
custo = input("Custo do produto: ")
preco = somaImposto(taxaImposto, custo)
print("O preço do produto com imposto ficou: " + str(preco))