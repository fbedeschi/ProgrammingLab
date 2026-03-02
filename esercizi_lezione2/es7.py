def fattoriale(num):
    if num==1:
        return 1
    else :
        return num * fattoriale(num-1)
    
num = int(input("inserire un numero: "))
print(f"il fattoriale di {num} è {fattoriale(num)}")