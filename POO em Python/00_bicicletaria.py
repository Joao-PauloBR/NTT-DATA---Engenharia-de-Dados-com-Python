class Bicicleta:
    # Método construtor
    def __init__(self, cor, marca, ano, valor, marcha): # Inicializador dos atributos da classe
        self.cor = cor
        self.marca = marca
        self.ano = ano
        self.valor = valor
        self.marcha = 1

    def buzinar(self):
        print("Plim Plim...")

    def parar(self):
        print("Parando a bicicleta...")
        print("Bicicleta parada!")

    def correr(self):
        print("Vrum...")

    def get_cor(self):
        return self.cor
    # Aqui serve para você entender que o Python precisa que seja passado o self, mas não necessariamente precisa se chamar self.
#    def trocar_marcha(numero_marcha):
#        print(numero_marcha)
#        print("Marcha trocada...")
    def trocar_marcha(self, numero_marcha):
        print("Trocando marcha...")
        
        def _trocar_marcha():
            if numero_marcha > self.marcha:
                print("Marcha trocada.")
            else:
                print("Não foi possível trocar de marcha.")


    def __str__(self):
        return f"Bicicleta: cor={self.cor}, marca={self.marca}, ano={self.ano}, valor={self.valor}" # Jeito mais indicado de fazer (em comparação com o print)

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}" # Método mais indicado, pois está automatizado.

bici_01 = Bicicleta("Preta", "Caloi", 2020, 1200)
bici_01.buzinar()
bici_01.correr()
bici_01.parar()



print(bici_01.cor, bici_01.marca, bici_01.ano, bici_01.valor) # Jeito menos indicado de fazer. Tente utilizar a função

bici_02 = Bicicleta("Vermelha", "Monark", 2022, 1900)
bici_02.buzinar() # É a mesma coisa que: Bicicleta.buzinar(bici_02)
print(bici_02.get_cor()) # Acessa o atributo cor, mas não é a melhor forma
print(bici_02.cor) # Jeito mais indicado de acessar o atributo em Python

bici_02.trocar_marcha()