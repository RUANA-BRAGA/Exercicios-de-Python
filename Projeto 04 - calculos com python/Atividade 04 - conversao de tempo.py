Minutos = int(input("Digite os minutos: ").strip())
Conversao = Minutos//60 
resto_hora = Minutos%60
print(f"{Minutos} minutos convertido em horas equivale á {Conversao} hora(s) e {resto_hora} minuto(s)")