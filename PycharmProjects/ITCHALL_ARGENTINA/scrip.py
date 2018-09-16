def alpaca(n):
    adn = "A"
    orden = {ord('A'): 'AL', ord('L'): 'PACA', ord('P'): 'CP', ord('C'): 'PC'}
    for x in range(n):
        adn = adn.translate(orden)
    print("Cadena completa:",adn)
    print("Cantidad de ALPACA:", adn.count("ALPACA"))
