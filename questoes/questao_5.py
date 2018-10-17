## QUESTÃO 5 ##
# Escreva um programa para calcular a redução do tempo de vida de um fumante. 
# Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. 
# Considere que um fumante perde 10 minutos de vida a cada cigarro, calcule 
# quantos dias de vida um fumante perderá. Exiba o total em dias. 
##


##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    minutosDia = 1440
    minutosCigarro = 10
    diasAno = 365

    cigarrosDia = int(input("quantos cigarros você fuma por dia? "))
    anosFumando = int(input("há quantos anos você fuma? "))
    
    diasFumando = anosFumando * diasAno
    totalCigarros = cigarrosDia * diasFumando
    diasPerdidos = totalCigarros * minutosCigarro // minutosDia

    print("Você perdeu {} dias de vida".format(diasPerdidos))


    
if __name__ == '__main__':
    main()
