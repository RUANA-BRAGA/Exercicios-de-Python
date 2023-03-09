Tempo_servico = int(input("Digite o tempo de serviço: ").strip())
Valor_bonus = float(input("Digite o valor do bonus por ano trabalhado: ").strip())
Calc_bonus = Tempo_servico*Valor_bonus
print(f"O valor da bonificaçao por ano trabalhado sera de {Calc_bonus:.2f} reais")