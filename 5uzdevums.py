"""
Uzrakstiet programmu Python, lai aprēķinātu cilindra virsmas tilpumu un laukumu. 
Piezīme: Cilindrs ir viena no visvienkāršākajām izliektajām ģeometriskajām 
formām, virsma, ko veido punkti fiksētā attālumā no noteiktās taisnes, 
cilindra ass.
"""
"""
augstums=float(input("Ievadi augstumu!"))

tilpums_V=3.14*(augstums)
laukums=3.14*2

print("Cilindra tilpums ir:",tilpums_V)
print("Cilindra laukums ir:",laukums)
"""
"""Kļūdu labojums:"""

augstums=float(input("Ievadi augstumu!"))
radiuss=float(input("Ievadi rādiusu!"))

V_tilpums=3.14*radiuss*augstums
laukums=3.14*2*augstums

print("Cilindra tilpums ir: ",V_tilpums)
print("Cilindra laukums ir: ",laukums)
"""Izlaboju matemātiskās kļūdas"""