## QUESTÃO 4 ##
# Escreva um programa que pergunte a quantidade de km percorridos por um carro 
# alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi 
# alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e 
# R$ 0,15 por km rodado.

##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    print("questao 4")
    dias = int(input("Quantos dias passou com o carro alugado?\n"))
    km = float(input("Qual o número de km rodados como o carro?\n"))

    ValorTotal = dias*60 + km*0.15

    print("O valor total do aluguel foi de R$ ", ValorTotal)

    
if __name__ == '__main__':
    main()
