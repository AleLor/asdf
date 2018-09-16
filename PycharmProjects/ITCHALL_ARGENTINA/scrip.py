adn = "A"
n = 20
orden = {ord('A'): 'AL', ord('L'): 'PACA', ord('P'): 'CP', ord('C'): 'PC'}
for x in range(n):
    adn = adn.translate(orden)

print(adn)
