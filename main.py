# '''
# Az ELDÖNTÉS esetében azt vizsgáljuk,
# hogy szerepel-e egy bizonyos tulajdonságú elem az adatsorban (itt a listában).

# A program azt vizsgálja, hogy van-e hárommal osztható szám a listában.
# '''
# lista = [2, 5, 4, 8, 9, 11, 10, 12]

# talalat = []
# index = 0
# while index < len(lista):
#     if lista[index] % 3 == 0:
#         talalat.append(lista[index])
#     index = index + 1

# print(f'Van a listában hárommal osztható szám. Az indexük: {talalat}')

'''
A SZÉLSŐÉRTÉK MEGHATÁROZÁSA esetében azt vizsgáljuk, hogy melyik a legkisebb, 
illetve a legnagyobb érték az adatsorban (itt a listában).
'''
lista = [12, 5, 4, 8, 9, 11, 10, 12, 6]

legkisebb = lista[0]
legnagyobb = lista[0]
for szam in lista:
        if szam < legkisebb:
            legkisebb = szam
        if szam > legnagyobb:
            legnagyobb = szam

print(f'A legkisebb szám a listában: {legkisebb}')
print(f'A legnagyobb szám a listában: {legnagyobb}')