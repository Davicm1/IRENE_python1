class Carro:
    def __init__(self, fabricante, modelo, ano, cor, valor):
        self.fabricante = fabricante
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.valor = valor

    def calcular_parcelas(self, quantidade_parcelas):
        if quantidade_parcelas <= 0:
            raise ValueError("A quantidade de parcelas deve ser maior que zero.")
        valor_parcela = self.valor / quantidade_parcelas
        return valor_parcela

# Exemplo de uso
def main():
    # Criando um carro
    fabricante = input("Digite o fabricante do carro: ")
    modelo = input("Digite o modelo do carro: ")
    ano = int(input("Digite o ano do carro: "))
    cor = input("Digite a cor do carro: ")
    valor = float(input("Digite o valor do carro: "))

    carro = Carro(fabricante, modelo, ano, cor, valor)

    # Solicitando a quantidade de parcelas
    quantidade_parcelas = int(input("Digite a quantidade de parcelas: "))
    
    try:
        valor_parcela = carro.calcular_parcelas(quantidade_parcelas)
        print(f"Valor de cada parcela: R$ {valor_parcela:.2f}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
