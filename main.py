import string
import json

with open("fisier.txt", "r") as fisier:
    string_citit = fisier.read()

print(string_citit)
print()

cuvinte = [word.strip(string.punctuation) for word in string_citit.split()]
print(cuvinte)
print()

aparitii = {cuvant: cuvinte.count(cuvant) for cuvant in cuvinte}

print(aparitii)
#print(len(string_citit), len(aparitii.items()))
print()

frecventa_aparitie = {key: value for (key, value) in aparitii.items() if value/len(string_citit) <= 0.01}

#frecventa_aparitie = {filter(lambda (key, value): value/len(string_citit) <= 0.01, aparitii.items()}
'''
frecventa_aparitie = {}

for (key, value) in aparitii.items():
  if value/len(string_citit) <= 0.01:
    frecventa_aparitie[key] = value
'''
print(frecventa_aparitie)
#print(len(frecventa_aparitie))
print()

with open('data.json', 'w') as f:
  json.dump(frecventa_aparitie, f, indent = 4)

