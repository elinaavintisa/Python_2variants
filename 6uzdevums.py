"""
Uzrakstiet programmu Python, lai pārbaudītu, 
vai vairākiem ievadītajiem mainīgajiem ir vienāda vērtība.
"""
"""
a = 30
b = 40
c = 50

# method 1
if a == 10 or b == 10 or c == 10:
  print("True")
else:
  print("False")  

# method 2
if 10 in (a, b, c):
  print("True")
else:
  print("False")  

# method 3
if 10 in {a, b, c}:
  print("True")
else:
  print("False")
"""
"""Kļūdu labojums:"""

a=float(input("Ievadi pirmo skaitli: "))
b=float(input("Ievadi otro skaitli: "))
c=float(input("Ievadi trešo skaitli: "))

if a==b==c:
    print("Skaitļu vērtība ir vienāda!")

else:
    print("Skaitļu bērtība nav vienāda!")

"""Pamainīju formulu"""