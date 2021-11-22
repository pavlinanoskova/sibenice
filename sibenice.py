from ai_slovo import vyber_slova
from ai_slovo import vychozi_stav
from tah import tah

print("Vítej ve hře ŠIBENICE!")
slovo = (vyber_slova())
pole = vychozi_stav(slovo)
print(slovo)
print(pole)

print(tah(slovo, pole))
