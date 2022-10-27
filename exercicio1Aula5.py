lista_notas = [7.0,5.5,4.5]
lista_notas2 = [6.5,9.7,8.0,3.5]
lista_notas.append(10)
lista_notas.extend(lista_notas2)
lista_notas.insert(2,9.0)
lista_notas.insert(8,6.0)
lista_notas.append(0)
print(lista_notas)
lista_notas.pop()
print(lista_notas)

media = 0
maiorNota = 0
menorNota = 0 

media = sum(lista_notas)/len(lista_notas)
maiorNota = max(lista_notas)
menorNota = min(lista_notas)

print(media)
print(f"maior nota: {maiorNota:,.2f} ")
print(f"menor nota: {menorNota:,.2f} ")
print(f"média final das notas: {media:,.2f} ")
    