import string
import json

#Exercitiul 1

with open("fisier.txt", "r") as fisier:
    string_citit = fisier.read()

print('string_citit: \n')
print(string_citit)
print()

cuvinte = [word.strip(string.punctuation) for word in string_citit.split()]

print('cuvinte: \n')
print(cuvinte)
print()
print('numar cuvinte: ', len(cuvinte))
print()

aparitii = {cuvant: cuvinte.count(cuvant) for cuvant in cuvinte}

print('aparitie cuvinte: \n')
print(aparitii)
#print(len(string_citit), len(aparitii.items()))
print()


#Exercitiul 2

frecventa_aparitie = {key: value for (key, value) in aparitii.items() if value/len(cuvinte) <= 0.01}

#frecventa_aparitie = {filter(lambda (key, value): value/len(string_citit) <= 0.01, aparitii.items()}
'''
frecventa_aparitie = {}

for (key, value) in aparitii.items():
  if value/len(cuvinte) <= 0.01:
    frecventa_aparitie[key] = value
'''
print('frecventa_aparitie sub 1% raportat la numarul de cuvinte: \n')
print(frecventa_aparitie)
#print(len(frecventa_aparitie))
print()

with open('data.json', 'w') as f:
  json.dump(frecventa_aparitie, f, indent = 4)


#Exercitiul 3

with open('data.json') as f:
  data = json.load(f)

print('data = \n')
print(data)
print()

#sorted_data = sorted(data.items(), key = lambda kv:(kv[1], kv[0]))
#sortam top 6, pentru ca top 10 le cuprinde cam pe toate...
sorted_data = {k: v for k, v in sorted(data.items(), key = lambda item: item[1]) if v < 6}

print('sorted_data (top 6 cuvinte): \n')
print(sorted_data)
print()