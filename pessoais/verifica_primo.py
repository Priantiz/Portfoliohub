def numero_suspeito():
    numero = int(input('digite um numero suspeito'))
    if numero <= 1:
        print('o numero não é primo')
        return
    for ct in range(2, numero, 1):
        if numero % ct == 0:
            print('o numero não é primo')
            return
    print('o numero é primo')
    return

numero_suspeito()
