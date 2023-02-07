def investigacao():
    res1 = int(input('Telefonou para a vítima? 1 = sim ou 0 = não: '))
    res2 = int(input('Esteve no local do crime? 1 = sim ou 0 = não: '))
    res3 = int(input('Mora perto da vítima? 1 = sim ou 0 = não: '))
    res4 = int(input('Devia para a vítima? 1 = sim ou 0 = não: '))
    res5 = int(input('Já trabalhou com a vítima? 1 = sim ou 0 = não: '))

    soma_respostas = res1 + res2 + res3 + res4 + res5 

    if soma_respostas < 2:
        print("\nInocente!")
    elif soma_respostas == 2:
        print("\nSuspeita!")
    elif 3 <= soma_respostas <= 4:
        print("\nCúmplice!")
    elif soma_respostas == 5:
        print("\nAssassino!")
    else:
        print('\nResposta Inválida! \nTente Novamente!\n')
        investigacao()
investigacao() 