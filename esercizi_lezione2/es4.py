def conta(parola,lettera):
    numero_occorrenze=0
    for i in parola:
        if i==lettera:
            numero_occorrenze+=1
    return numero_occorrenze

par =input("inserire una parola ")
lett = input("inserire una lettera ") 

print(f"il numero di occorenze è {conta(par,lett)}")