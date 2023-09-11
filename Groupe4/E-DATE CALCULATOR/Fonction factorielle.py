from math import *


"""def factorielle(n):
   if n == 0:
      return 1
   else:
      F = 1
      for k in range(2,n+1):
         F = F * k
      return F
   
n = int(input("Entrez votre nombre: \n"))
print(f"Son factorielle est {factorielle(n)}")"""

def pow(n,m):
   resultat = n**m
   return resultat


n = int(input("Entrez votre nombre: \n"))
m = int(input("Entrez votre exposant: \n"))

print(f" {n}  à la puissance {m} est {pow(n,m)}")