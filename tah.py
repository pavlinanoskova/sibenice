
def tah(slovo, pole):
    tah = input("Hádej písmeno: ")
    index = 0
    for char in slovo:

        if char == tah:
            pole = pole[:index] + tah + pole[index+1:]

        index = index + 1
    return pole

