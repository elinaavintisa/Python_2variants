"""
    Funkcija akrs akceptē trīs argumentus - skaiļus viens, divi un trīs, 
    aprēķina to kvadrātu starpību un atgriež to.
    Pārbaudiet funkcijas darbību ar dažādiem argumentiem, 
    parādot skaitli ar četriem simboliem aiz komata.

    Argumenti:
        viens {int vai float} -- pirmais skaitlis
        divi {int vai float} -- otrais skaitlis
        tris {int vai float} -- trešais skaitlis
    Atgriež:
        int vai float -- argumentu summa
 """
"""
import math
import decimal

def akrs(a, b, c):
   kvadrats=float(pow(a,2)+pow(b,2)+pow(c,2))
   return kvadrats
print('%.2f'% akrs(2, 3, 4))
"""
"""Kļudu labojums:"""
import math
import decimal

def akrs(a, b, c):
  kvadrats=float(pow(a,2)+pow(b,2)+pow(c,2))
  return kvadrats

print("%.4f" % akrs(2, 3, 4)) 
""" 2f vietā ieliku 4f, jo uzdevumā tiek prasīti 4 cipari aiz komata."""
