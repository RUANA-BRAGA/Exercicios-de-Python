preco = float(input("Qual o preço do produto? ").strip())
calc_desconto = float((preco*0.10))
Valor_descontado = float(preco - calc_desconto)
print(f"O produto de valor {preco} terá com desconto valor de {Valor_descontado:.2f} reais")