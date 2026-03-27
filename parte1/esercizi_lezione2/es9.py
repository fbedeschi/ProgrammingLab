def conta_vocali(parola) :
    cont = 0
    vocali = ["a","e","i","o","u"]
    for i in parola:
        if i in vocali:
            cont +=1
    return cont
par = input("inserire un parola: ")
print(f"il numero di vocali in {par} è {conta_vocali(par)}")
