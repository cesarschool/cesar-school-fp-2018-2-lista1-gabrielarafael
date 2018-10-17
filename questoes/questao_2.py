## QUESTÃO 2 ##
# Escreva um programa que converta uma temperatura digitada em °C (graus celsius) 
# para °F (graus fahrenheit). 
##


##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    tempCelsius = int(input("Digite a temperatura em Celsius"))

    tempFahrenheit = tempCelsius * 9/5 + 32

    print("a temperatura em fahrenheit é {} graus".format(tempFahrenheit))
    



if __name__ == '__main__':
    main()
