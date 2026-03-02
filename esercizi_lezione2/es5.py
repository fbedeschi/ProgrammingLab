def verifica_primo(numero):
    i = 2
    primo = True
    while i<numero:
        if numero%i == 0:
            primo = False
        i+=1
    return primo

    

num = input("inserire un numero: ")
num = int(num)
prim = verifica_primo(num)
if prim:
    print("il numero è primo")
else:
    print("il numero non è primo")
