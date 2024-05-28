def resumo():
    mensagem = "Marie Skłodowska-Curie, nascida Maria Salomea Skłodowska, foi uma física e química polonesa naturalizada francesa, que conduziu pesquisas pioneiras sobre radioatividade."
    return mensagem


def doutorado():
    mensagem = "Recebeu seu doutorado em março de 1895 e fez sua tese de doutorado em raios urânicos."
    return mensagem


def contribuicoes():
    mensagem = "Por meio de sua tese de doutorado, ela conseguiu provar que o óxido de urânio é um mineral capaz de eliminar a radiação armazenada nos átomos. Com isso, descobriu ainda a radioatividade. Além disso, juntamente com Pierre Curie, ela descobriu dois novos elementos químicos: Polônio e Rádio."
    return mensagem


def artigos():
    mensagem = "Die Radioaktivität - 1911\nTreatise on Radioactivity-1910\n Pierre Currie-1923\n Entre outros..."
    return mensagem


def citacoes():
    mensagem = "'Nada na vida deve ser temido, somente compreendido. Agora é hora de compreender mais para temer menos.'\n 'Um cientista no seu laboratório não é apenas um técnico: é, também, um menino colocado à frente de fenômenos naturais que impressionam como se de um conto de fadas se tratassem!'
    return mensagem


def sair():
    mensagem = "\nObrigado pela leitura!"
    return mensagem


def erro():
    mensagem = "\nOpção inválida!"
    return mensagem


print("\nBoa noite! Você está aprendendo sobre Marie Curie!\n")

continuar = True
while continuar == True:

    opcao = int(
        input(
"""
\nDigite o número correspondente ao menu que você deseja acessar:
1 - Resumo
2 - Doutorado
3 - Contribuições
4 - Principais Artigos
5 - Citações
6 - Sair\n
"""
        )
    )

    if opcao == 1:
        print("1 - Resumo")
        mensagem = resumo()

    elif opcao == 2:
        print("2 - Doutorado")
        mensagem = doutorado()

    elif opcao == 3:
        print("3 - Contribuições")
        mensagem = contribuicoes()

    elif opcao == 4:
        print("4 - Principais Artigos")
        mensagem = artigos()

    elif opcao == 5:
        print("5 - Citações")
        mensagem = citacoes()

    elif opcao == 6:
        mensagem = sair()
        continuar = False

    else:
        mensagem = erro()

    print(mensagem)
