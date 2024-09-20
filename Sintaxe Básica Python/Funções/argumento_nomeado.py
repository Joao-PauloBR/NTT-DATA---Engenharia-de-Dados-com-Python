def salvar_carro(marca, modelo, ano, placa):
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

salvar_carro("Fiat", "Palio", 1999, "ABC-1234") # É fácil confundir e passar valores nos campos errados
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234") # Melhor
salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"})
