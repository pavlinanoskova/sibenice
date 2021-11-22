from random import randrange
def vyber_slova():
    index = randrange(3)
    seznam = ["polevka", "rizek", "dort"]
    slovo = seznam[index]
    return slovo

def vychozi_stav(slovo):
    pole = (len(slovo) * "_")
    return pole



