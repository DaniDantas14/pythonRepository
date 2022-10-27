lista_festa = ["bolo","salada","balões","letreiro_feliz_aniversario","refrigerante"]

lista_festa_supermercado = []

for item in lista_festa:
    if len(item) > 6:
        lista_festa_supermercado.append(item)

print(f"Lista do Supermercado: \n {lista_festa_supermercado}")

print("\nItens para comprar:")
for i in range(len(lista_festa)-3,len(lista_festa)):
    print(f"{lista_festa[i]}")