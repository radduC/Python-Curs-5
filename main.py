import string

with open("fisier.txt", "r") as fisier:
    string_citit = fisier.read()

print(string_citit)

cuvinte = [word.strip(string.punctuation) for word in string_citit.split()]
print(cuvinte)

aparitii = {cuvant: cuvinte.count(cuvant) for cuvant in cuvinte}

print(aparitii)
