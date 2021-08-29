n=0
somme = 0
for n in range(1,100, n++):
    print("Avant le calcul",n,somme)
    somme = n + somme
    n+=1
    print("apres le calcul",n,somme)
print(n , somme)
