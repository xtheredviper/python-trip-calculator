destino = input("Olá, seja bem-vindo! Qual é o destino da sua viagem?")
distancia = float(input("Qual é a distância do seu destino?"))
consumo_medio_carro = float(input("Qual é o consumo médio do seu carro (km/l)?"))    
custo_atual_combustivel = float(input("Qual é o custo atual do combustível por litro?"))    
custo_total_combustivel = (distancia / consumo_medio_carro) * custo_atual_combustivel
print(f"Para sua viagem rumo a {destino}, você gastará aproximadamente R$ {custo_total_combustivel:.2f} em combustível.")